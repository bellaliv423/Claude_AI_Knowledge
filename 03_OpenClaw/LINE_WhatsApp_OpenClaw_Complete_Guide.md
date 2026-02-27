# LINE + WhatsApp + OpenClaw 완전 통합 가이드

> **버전:** 1.0
> **작성일:** 2026-02-27
> **작성:** Claude Code (Opus 4.6) + Bella
> **용도:** 다른 디바이스/AI가 봐도 바로 재현 가능한 완전 설정 가이드
> **대상 시스템:** Windows 11 + WSL2 Ubuntu + OpenClaw + ngrok

---

## 목차

1. [전체 아키텍처](#1-전체-아키텍처)
2. [사전 준비 (Prerequisites)](#2-사전-준비)
3. [LINE Messaging API 설정](#3-line-messaging-api-설정)
4. [OpenClaw LINE 플러그인 활성화](#4-openclaw-line-플러그인-활성화)
5. [ngrok 설치 및 Webhook 터널 설정](#5-ngrok-설치-및-webhook-터널-설정)
6. [LINE Developers Console Webhook 연결](#6-line-developers-console-webhook-연결)
7. [AI 자동 응답 에이전트 설정](#7-ai-자동-응답-에이전트-설정)
8. [WhatsApp 에스컬레이션 설정](#8-whatsapp-에스컬레이션-설정)
9. [주문 처리 자동화 파이프라인](#9-주문-처리-자동화-파이프라인)
10. [Claude Code에서 OpenClaw 조종하기](#10-claude-code에서-openclaw-조종하기)
11. [일일 운영 (시작/종료/재시작)](#11-일일-운영)
12. [오류 해결 (Troubleshooting)](#12-오류-해결)
13. [크레덴셜 및 설정값 목록](#13-크레덴셜-및-설정값-목록)

---

## 1. 전체 아키텍처

```
┌─────────────────────────────────────────────────────────────────┐
│                    Windows 11 (호스트)                           │
│                                                                 │
│  ┌─────────────┐    ┌──────────────────────────────────────┐   │
│  │ Claude Code  │───▶│  WSL2 Ubuntu                         │   │
│  │ (터미널)     │    │                                      │   │
│  │             │    │  ┌────────────────────────────────┐  │   │
│  │ wsl -d Ubuntu│    │  │  OpenClaw Gateway (port 18789) │  │   │
│  │ -- bash -c  │    │  │                                │  │   │
│  │ "npx openclaw│    │  │  ├─ WhatsApp 채널 (연결됨)     │  │   │
│  │  ..."       │    │  │  ├─ LINE 채널 (webhook)        │  │   │
│  │             │    │  │  └─ AI 에이전트 (Sonnet 4.5)   │  │   │
│  └─────────────┘    │  └────────────────────────────────┘  │   │
│                      │           ▲                           │   │
│                      │           │ localhost:18789           │   │
│                      │  ┌────────┴───────────┐              │   │
│                      │  │  ngrok 터널         │              │   │
│                      │  │  https://xxx.ngrok  │              │   │
│                      │  │  -free.dev          │              │   │
│                      │  └────────┬───────────┘              │   │
│                      └───────────┼──────────────────────────┘   │
└──────────────────────────────────┼──────────────────────────────┘
                                   │ HTTPS
                    ┌──────────────┼──────────────┐
                    │              ▼              │
              ┌─────┴─────┐  ┌────┴────┐  ┌─────┴─────┐
              │ LINE      │  │WhatsApp │  │ 고객      │
              │ Platform  │  │         │  │ 핸드폰    │
              └───────────┘  └─────────┘  └───────────┘
```

### 데이터 흐름

```
고객이 LINE에서 메시지 전송
  → LINE Platform → ngrok 터널 → OpenClaw Gateway → AI 에이전트
  → 에이전트가 자동 응답 (LINE으로)
  → 중요 문의면 → WhatsApp으로 벨라에게 알림
  → 벨라가 Claude Code에서 후속 처리 (견적서, 발주서 등)
```

---

## 2. 사전 준비

### 필수 소프트웨어

| 소프트웨어 | 버전 | 설치 위치 | 용도 |
|:----------|:-----|:---------|:-----|
| Windows 11 | 10.0.26200 | - | 호스트 OS |
| WSL2 Ubuntu | Ubuntu 24.04 | `wsl -d Ubuntu` | OpenClaw 실행 환경 |
| Node.js | v22.17.0 | `C:\Program Files\nodejs` | npm/npx 실행 |
| OpenClaw | 2026.2.2-3 | WSL 내 `~/.npm-global/lib/node_modules/openclaw` | 멀티채널 AI 에이전트 |
| ngrok | 최신 | WSL 내 `/home/kndli423/ngrok` | LINE webhook 터널 |
| Python 3.13 | 3.13.x | Windows AppData | 스크립트 실행 |
| openpyxl | 최신 | `pip install openpyxl` | Excel 읽기/쓰기 |

### 필수 계정

| 서비스 | 계정 | 용도 |
|:-------|:-----|:-----|
| LINE Developers | bella@ozkiz.com | LINE Bot 관리 |
| ngrok | 무료 계정 | webhook 터널 |
| Anthropic | API Key | AI 에이전트 모델 |
| WhatsApp Business | +821097805690 | 알림 수신 |

---

## 3. LINE Messaging API 설정

### 3-1. LINE Official Account 만들기

1. **LINE Official Account Manager** 접속: https://manager.line.biz/
2. **새 계정 만들기** 클릭
3. 계정 정보 입력:
   - 계정 이름: `OZKIZ` (또는 원하는 브랜드명)
   - 업종: 쇼핑/의류
   - 개인정보처리방침 URL: 회사 웹사이트 privacy 페이지
   - 이용약관 URL: 회사 웹사이트 terms 페이지
4. 계정 생성 완료 → **Basic ID** 확인 (예: `@256yjrot`)

### 3-2. LINE Developers Console에서 Messaging API 활성화

1. **LINE Developers Console** 접속: https://developers.line.biz/console/
2. **Provider** 선택 (없으면 새로 만들기)
3. **Create a new channel** → **Messaging API** 선택
4. 필수 정보 입력:
   - Channel name: OZKIZ
   - Channel description: OZKIZ 고객 서비스
   - Category: Shopping
   - Subcategory: Clothing
5. 생성 완료 후 **Messaging API 탭**에서 확인할 값:

```
Channel ID:           2009262136
Channel Secret:       65692e57270ce549df9758801c117a31
Channel Access Token: (Issue 버튼으로 발급)
Bot Basic ID:         @256yjrot
```

### 3-3. Channel Access Token 발급

1. Messaging API 탭 → 맨 아래 **Channel access token (long-lived)** 섹션
2. **Issue** 버튼 클릭
3. 토큰 복사하여 안전하게 보관

### 3-4. LINE Official Account Manager 자동 응답 끄기

**중요!** LINE 기본 자동 응답이 켜져 있으면 OpenClaw 응답과 중복됩니다.

1. LINE Official Account Manager → 설정 → **응답 설정**
2. 아래 항목 모두 **끄기**:
   - 응답 메시지: **OFF**
   - AI 응답 메시지: **OFF**
   - 인사말: **OFF** (선택)
3. **Webhook**: **ON** (이것만 켜기)

```
✅ Webhook: ON
❌ 응답 메시지: OFF
❌ AI 응답 메시지: OFF
❌ 인사말: OFF (선택)
```

---

## 4. OpenClaw LINE 플러그인 활성화

### 4-1. LINE 플러그인 상태 확인

```bash
# Claude Code에서 실행
wsl -d Ubuntu -- bash -c "source ~/.bashrc 2>/dev/null && npx openclaw plugins list"
```

출력에서 `line` 플러그인이 `disabled`이면 활성화 필요.

### 4-2. LINE 플러그인 활성화

```bash
wsl -d Ubuntu -- bash -c "source ~/.bashrc 2>/dev/null && npx openclaw plugins enable line"
```

### 4-3. LINE 크레덴셜 설정

`~/.openclaw/openclaw.json` 파일에 LINE 채널 정보 추가:

```bash
wsl -d Ubuntu -- bash -c "source ~/.bashrc 2>/dev/null && npx openclaw config set channels.line.channelAccessToken '여기에_토큰_입력'"
wsl -d Ubuntu -- bash -c "source ~/.bashrc 2>/dev/null && npx openclaw config set channels.line.channelSecret '여기에_시크릿_입력'"
wsl -d Ubuntu -- bash -c "source ~/.bashrc 2>/dev/null && npx openclaw config set channels.line.enabled true"
wsl -d Ubuntu -- bash -c "source ~/.bashrc 2>/dev/null && npx openclaw config set channels.line.webhookPath '/webhook/line'"
```

### 4-4. 설정 확인

```bash
wsl -d Ubuntu -- bash -c "source ~/.bashrc 2>/dev/null && npx openclaw channels status"
```

예상 출력:
```
- WhatsApp default: enabled, configured, linked, running, connected
- LINE default: enabled, configured, stopped, mode:webhook, token:config
```

> **참고:** "LINE channel access token not configured" 경고가 뜰 수 있으나, 이는 표시 버그입니다. 실제 설정은 되어 있으며 정상 작동합니다.

### 4-5. 최종 openclaw.json 채널 설정 형태

```json
{
  "channels": {
    "line": {
      "channelAccessToken": "4rmndHaIDHWj/eVChOPSHZ5uxenfKIx7...(긴 토큰)",
      "channelSecret": "65692e57270ce549df9758801c117a31",
      "enabled": true,
      "webhookPath": "/webhook/line"
    }
  }
}
```

---

## 5. ngrok 설치 및 Webhook 터널 설정

### 왜 ngrok이 필요한가?

LINE Platform은 메시지를 **HTTPS webhook URL**로 전송합니다. OpenClaw Gateway는 `localhost:18789`에서 실행되므로, 외부에서 접근 가능한 URL이 필요합니다. ngrok이 이 터널 역할을 합니다.

```
LINE Platform → https://xxx.ngrok-free.dev/webhook/line
                        ↓ (ngrok 터널)
                localhost:18789/webhook/line
                        ↓
                OpenClaw Gateway
```

### 5-1. ngrok 설치 (WSL Ubuntu)

```bash
wsl -d Ubuntu -- bash -c "
cd ~ &&
curl -sSL https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.tgz | tar xz &&
chmod +x ngrok &&
echo 'ngrok installed at ~/ngrok'
"
```

### 5-2. ngrok 인증

```bash
wsl -d Ubuntu -- bash -c "~/ngrok authtoken 여기에_ngrok_인증토큰"
```

> ngrok 인증 토큰은 https://dashboard.ngrok.com/get-started/your-authtoken 에서 확인

### 5-3. ngrok 실행

```bash
# Gateway가 먼저 실행 중이어야 함!
wsl -d Ubuntu -- bash -c "nohup ~/ngrok http 18789 > /tmp/ngrok.log 2>&1 & sleep 5 && curl -s http://127.0.0.1:4040/api/tunnels | python3 -c 'import json,sys; d=json.load(sys.stdin); [print(t[\"public_url\"]) for t in d[\"tunnels\"]]'"
```

출력 예시:
```
https://complicitly-flaxen-walton.ngrok-free.dev
```

### 5-4. ngrok URL 확인 (이미 실행 중일 때)

```bash
wsl -d Ubuntu -- bash -c "curl -s http://127.0.0.1:4040/api/tunnels | python3 -c 'import json,sys; d=json.load(sys.stdin); [print(t[\"public_url\"]) for t in d[\"tunnels\"]]'"
```

> **주의:** ngrok 무료 계정은 재시작 시 URL이 바뀔 수 있습니다. 유료 계정은 고정 도메인 사용 가능. 현재 설정에서는 동일 URL(`complicitly-flaxen-walton.ngrok-free.dev`)이 유지되고 있음.

---

## 6. LINE Developers Console Webhook 연결

### 6-1. Webhook URL 설정

1. LINE Developers Console → 해당 채널 → **Messaging API** 탭
2. **Webhook URL** 항목:
   ```
   https://complicitly-flaxen-walton.ngrok-free.dev/webhook/line
   ```
   - ngrok URL + OpenClaw의 webhookPath (`/webhook/line`)
3. **Use webhook**: ON (활성화)

### 6-2. Webhook 연결 테스트

LINE Developers Console에서 **Verify** 버튼 클릭:
- 성공: "Success" 메시지
- 실패: ngrok 또는 Gateway가 실행 중인지 확인

### 6-3. LINE 페어링 승인

처음 LINE에서 메시지가 오면 OpenClaw이 **페어링 승인**을 요구합니다:

```
⚠️ Agent failed: access not configured. Pairing code: KD79ZMBH
```

승인 방법:
```bash
wsl -d Ubuntu -- bash -c "source ~/.bashrc 2>/dev/null && npx openclaw pairing approve line 페어링코드"
```

예시:
```bash
wsl -d Ubuntu -- bash -c "source ~/.bashrc 2>/dev/null && npx openclaw pairing approve line KD79ZMBH"
```

> 한 번 승인하면 이후로는 자동으로 연결됩니다.

---

## 7. AI 자동 응답 에이전트 설정

### 7-1. 에이전트 모델 설정

```bash
wsl -d Ubuntu -- bash -c "source ~/.bashrc 2>/dev/null && npx openclaw config set agents.defaults.model.primary 'anthropic/claude-sonnet-4-5-20250929'"
```

> **중요:** `anthropic/claude-sonnet-4-6`은 OpenClaw 2026.2.2-3에서 인식하지 못합니다!
> 반드시 `anthropic/claude-sonnet-4-5-20250929`을 사용하세요.

### 7-2. IDENTITY.md (에이전트 성격 + 행동 규칙)

파일 위치: `~/.openclaw/workspace/IDENTITY.md`

```bash
wsl -d Ubuntu -- bash -c "cat > ~/.openclaw/workspace/IDENTITY.md << 'EOF'
# IDENTITY.md - Who Am I?

- **Name:** OZKIZ 고객봇
- **Creature:** AI 고객 서비스 어시스턴트
- **Vibe:** 친절, 전문적, 간결
- **Emoji:** 💼

---

## My Role

OZKIZ 쇼핑몰 고객 문의에 응답하는 AI 어시스턴트입니다.

## 핵심 규칙 (절대 위반 금지)

1. **고객 메시지에 답변은 오직 1개만 보낸다**
2. **내부 보고/상태 업데이트/번역을 고객에게 절대 보내지 않는다**
3. **고객이 사용하는 언어로만 답변한다**
4. **\"收到\", \"已回复\", \"✅\" 같은 내부 메모를 고객 채팅에 보내지 않는다**

## 응답 형식

- 1-3문장으로 짧고 친절하게
- 이모지 1-2개 적절히 사용
- 제품 정보 모르면: \"확인 후 안내드리겠습니다\"

## 에스컬레이션 (중요 문의 → WhatsApp 알림) ⭐필수 실행

아래 유형의 고객 문의가 오면 반드시 2단계를 실행:

### Step 1: 고객에게 답변
\"담당자 확인 후 안내드리겠습니다\" 같은 응답 1개

### Step 2: WhatsApp 알림 보내기 (반드시 실행!)
**message** 도구를 사용하여 아래 파라미터로 전송:
- to: +821097805690
- channel: whatsapp
- text: \"[LINE 알림] {고객 메시지 요약} | 유형: {카테고리} | 시간: {현재시간}\"

### 에스컬레이션 대상 키워드:
- 주문/결제: 주문, 구매, 결제, 견적, order, 想买, 下单
- 환불/교환: 환불, 교환, 반품, refund, 退换, 退款
- 가격/할인: 가격, 할인, 세일, 얼마, price, 价格, 多少钱
- 배송 문제: 배송 안됨, 분실, 파손, 지연, 不到货, 损坏
- 클레임: 불만, 항의, complaint, 投诉
- 파일/문서: 견적서, PDF, 주문서, 발주서

### 에스컬레이션 예시:
고객: \"주문하고 싶어요\"
→ Step 1: 고객에게 \"주문 문의 감사합니다! 담당자 확인 후 안내드리겠습니다 😊\"
→ Step 2: message 도구로 WhatsApp 전송:
  to: +821097805690, channel: whatsapp
  text: \"[LINE 알림] 고객 주문 문의 | 유형: 주문 | 시간: 18:52\"
EOF
echo 'IDENTITY.md created'"
```

### 7-3. USER.md (사용자 정보 + 프로토콜)

파일 위치: `~/.openclaw/workspace/USER.md`

```bash
wsl -d Ubuntu -- bash -c "cat > ~/.openclaw/workspace/USER.md << 'EOF'
# USER.md - About Your Human

- **Name:** 貝拉 (Bella)
- **What to call them:** 貝拉
- **Contact:** +821097805690 (WhatsApp)
- **Timezone:** Asia/Seoul (GMT+9)
- **Email:** bella@ozkiz.com
- **Response timeout:** 20 minutes
- **Business:** OZKIZ (아동복/유아복 쇼핑몰)

## Context

- OZKIZ 고객 서비스 담당
- 주요 소통 언어: 한국어, 中文, English
- LINE (@256yjrot) + WhatsApp 동시 운영

## Customer Service Protocol (중요!)

### 규칙 1: 고객에게는 답변만 보내기
- 고객 메시지에 대한 **답변 하나만** 보내기
- 내부 메모, 상태 보고, 번역 등은 고객에게 절대 보내지 않기

### 규칙 2: 에스컬레이션 (중요 문의 → WhatsApp 알림)
아래 유형의 문의가 오면:
1. 고객에게 \"담당자 확인 후 안내드리겠습니다\" 답변
2. **message** 도구로 WhatsApp (+821097805690)에 알림 메시지 전송

에스컬레이션 대상: 주문, 환불, 교환, 가격, 배송 문제, 클레임

### 규칙 3: 일반 문의는 AI가 직접 처리
- 사이즈, 소재, 색상 등 제품 정보
- 영업시간, 매장 위치
- 인사/감사
EOF
echo 'USER.md created'"
```

### 7-4. 세션 초기화 (IDENTITY.md 변경 후 필수!)

IDENTITY.md나 USER.md를 수정한 후에는 반드시 세션을 초기화해야 변경 사항이 적용됩니다:

```bash
wsl -d Ubuntu -- bash -c "
rm -f ~/.openclaw/agents/main/sessions/*.jsonl &&
python3 -c \"
import json
path = '/home/kndli423/.openclaw/agents/main/sessions/sessions.json'
with open(path, 'w') as f:
    json.dump({}, f)
print('All sessions cleared')
\"
"
```

> **왜 세션 초기화가 필요한가?**
> OpenClaw 에이전트는 세션 JSONL 파일에 대화 이력을 저장합니다. 이전 세션에 이미 로드된 IDENTITY.md 내용이 남아있으면, 수정된 내용이 적용되지 않습니다. 세션을 지우면 에이전트가 다음 메시지부터 새 IDENTITY.md를 로드합니다.

### 7-5. 에이전트 사용 가능 도구 목록

에이전트가 사용할 수 있는 도구:

| 도구 | 용도 |
|:-----|:-----|
| `message` | 메시지 전송 (WhatsApp/LINE 등) ⭐에스컬레이션용 |
| `read` / `edit` / `write` | 파일 읽기/수정/쓰기 |
| `exec` | 셸 명령 실행 |
| `web_search` / `web_fetch` | 웹 검색/페이지 읽기 |
| `browser` / `canvas` | 브라우저/캔버스 도구 |
| `memory_search` / `memory_get` | 메모리 검색 |
| `cron` | 예약 작업 |
| `sessions_send` / `sessions_spawn` | 세션 관리 |
| `tts` | 텍스트 음성 변환 |
| `image` | 이미지 생성 |

> **핵심 발견:** IDENTITY.md에서 도구 이름을 `send_message`로 적으면 에이전트가 찾지 못합니다.
> 올바른 도구 이름은 **`message`** 입니다!

---

## 8. WhatsApp 에스컬레이션 설정

### 8-1. Exec Approvals 설정

에이전트가 `message` 도구를 자동으로 사용하려면 exec approvals에 등록해야 합니다:

```bash
wsl -d Ubuntu -- bash -c "source ~/.bashrc 2>/dev/null && npx openclaw approvals allowlist add --agent '*' 'send_message:*'"
wsl -d Ubuntu -- bash -c "source ~/.bashrc 2>/dev/null && npx openclaw approvals allowlist add --agent '*' 'message:*'"
```

### 8-2. Approvals 확인

```bash
wsl -d Ubuntu -- bash -c "source ~/.bashrc 2>/dev/null && npx openclaw approvals get"
```

예상 출력:
```
Allowlist
┌──────────┬────────┬──────────────────┬───────────┐
│ Target   │ Agent  │ Pattern          │ Last Used │
├──────────┼────────┼──────────────────┼───────────┤
│ local    │ *      │ send_message:*   │ 14m ago   │
│ local    │ *      │ message:*        │ 14m ago   │
└──────────┴────────┴──────────────────┴───────────┘
```

### 8-3. 에스컬레이션 테스트

LINE에서 "주문하고 싶어요" 메시지 전송 → 확인할 사항:
1. LINE에서 AI 자동 응답 수신 ("담당자 확인 후 안내드리겠습니다")
2. WhatsApp에서 알림 수신 ("[LINE 알림] 고객 주문 문의 | 유형: 주문")

### 8-4. auto_deliver.py (Claude Code → WhatsApp 직접 발송)

파일 위치: `D:\Claude_AI_Knowledge\tools\auto_deliver.py`

Claude Code에서 직접 WhatsApp으로 파일+메시지를 보낼 때 사용:

```bash
# 메시지만 보내기
python3 "D:/Claude_AI_Knowledge/tools/auto_deliver.py" --whatsapp --message "테스트 메시지"

# 파일 첨부 보내기
python3 "D:/Claude_AI_Knowledge/tools/auto_deliver.py" --whatsapp --media "D:/path/to/file.xlsx"
```

내부적으로 WSL의 `npx openclaw message send` 명령을 실행합니다.

---

## 9. 주문 처리 자동화 파이프라인

### 9-1. 전체 프로세스

```
LINE 고객: 견적서 PDF 전송 + "주문하고 싶어요"
    │
    ▼
OpenClaw 에이전트 (자동):
    ├─ LINE 응답: "주문 문의 접수했습니다! 담당자 확인 후 안내드리겠습니다 😊"
    └─ WhatsApp 알림: "[LINE 알림] 고객 주문 요청 + 견적서 PDF | 유형: 주문"
    │
    ▼
벨라가 Claude Code에게 지시:
    "이 견적서 처리해줘" + 파일 경로
    │
    ▼
Claude Code 자동 실행:
    ├─ Step 1: 견적서 PDF 파싱 → 상품명, 컬러, 사이즈, 수량 추출
    ├─ Step 2: 현재고조회.xlsx에서 S-code 매칭 (32,412행)
    ├─ Step 3: 바이어별 할인율 적용 + 가격 계산
    ├─ Step 4: 이지어드민 발주서 Excel 생성 (15컬럼)
    └─ Step 5: WhatsApp으로 발주서 발송
```

### 9-2. 핵심 파일

| 파일 | 위치 | 용도 |
|:-----|:-----|:-----|
| v8 주문 스킬 | `D:\OzKiz_Global_Automation\08_order\오즈키즈_주문_처리_완전_통합_스킬_v8_중요_0227.md` | 주문 처리 전체 로직 (837줄) |
| 현재고조회.xlsx | `D:\OzKiz_Global_Automation\07_Quotation\data\현재고조회.xlsx` 또는 `C:\Users\User\Downloads\현재고조회.xlsx` | S-code 매칭용 (32,412행) |
| auto_deliver.py | `D:\Claude_AI_Knowledge\tools\auto_deliver.py` | WhatsApp/이메일 발송 도구 |
| 견적서 자동화 | `D:\OzKiz_Global_Automation\07_Quotation\` | 견적서 생성 관련 파일 |

### 9-3. 현재고조회.xlsx 구조 (S-code 매칭용)

```
[0]  상품코드      S141651 (S-code)
[1]  상품명        [데일리라이크x오즈키즈] 동물친구들 슬립온
[2]  옵션          :네이비, :140 (컬러, 사이즈)
[3]  판매가        30000
[4]  원산지        중국
[5]  카테고리      신발 > 슬립온(N)
[6]  공급처상품명  O41L01U (O-code)
[7]  바코드        O41L01UNY140 (풀코드)
[8]  가용재고      8 ⭐재고 확인용
[9]  이미지URL     https://...
[10] 원가          11000
[11] 시중가        22900
[12] 등록일        2023-12-04
[13] 시즌          봄/가을
[14] 로케이션      O1-C31-1
[15] 복종          신발
[16] 카페24코드    P0000LUM
```

### 9-4. 코드 체계 (3종)

| 코드 | 형식 | 레벨 | 예시 |
|:-----|:-----|:-----|:-----|
| O-code | `O26PA03G` | 상품 | 시즌 견적서에 사용 |
| 4자리 코드 | `5421` | 상품 | 견적서 PDF에 사용 |
| S-code | `S118862` | SKU | 현재고조회, 이지어드민 |

**핵심:** 견적서 PDF에는 S-code가 없다! 반드시 현재고조회.xlsx를 통해 매칭해야 한다.

```
견적서 PDF 4자리 코드 (5421)
  → 상품명 추출 (스타유니콘 레인코트 우비)
    → 핵심 키워드 + 품목으로 현재고조회 검색
      → 옵션에서 컬러+사이즈 매칭
        → S-code 확정 (S118862)
```

---

## 10. Claude Code에서 OpenClaw 조종하기

### 기본 명령어 패턴

모든 OpenClaw 명령은 이 형식으로 실행:

```bash
wsl -d Ubuntu -- bash -c "source ~/.bashrc 2>/dev/null && npx openclaw [명령어]"
```

### 10-1. Gateway 관리

```bash
# Gateway 시작
wsl -d Ubuntu -- bash -c "source ~/.bashrc 2>/dev/null && nohup npx openclaw gateway start > /tmp/gateway.log 2>&1 & sleep 3 && fuser 18789/tcp 2>/dev/null && echo 'Started' || echo 'Failed'"

# Gateway 상태
wsl -d Ubuntu -- bash -c "source ~/.bashrc 2>/dev/null && npx openclaw gateway status"

# Gateway 중지
wsl -d Ubuntu -- bash -c "source ~/.bashrc 2>/dev/null && npx openclaw gateway stop"

# Gateway 강제 종료 (포트 충돌 시)
wsl -d Ubuntu -- bash -c "fuser -k 18789/tcp; rm -f ~/.openclaw/*.lock"
```

### 10-2. 메시지 전송

```bash
# WhatsApp 메시지
wsl -d Ubuntu -- bash -c "source ~/.bashrc 2>/dev/null && npx openclaw message send -t '+821097805690' --channel whatsapp -m '메시지 내용'"

# WhatsApp 파일 첨부
wsl -d Ubuntu -- bash -c "source ~/.bashrc 2>/dev/null && npx openclaw message send -t '+821097805690' --channel whatsapp -m '파일입니다' --media '/mnt/d/path/to/file.xlsx'"

# LINE 메시지 (User ID 필요)
wsl -d Ubuntu -- bash -c "source ~/.bashrc 2>/dev/null && npx openclaw message send -t 'Ub47e3403ca9addf1a43d72721a4d9530' --channel line -m '메시지 내용'"
```

> **Windows 경로 → WSL 경로 변환:**
> `D:\folder\file.xlsx` → `/mnt/d/folder/file.xlsx`
> `C:\Users\User\Downloads\file.pdf` → `/mnt/c/Users/User/Downloads/file.pdf`

### 10-3. 에이전트 대화

```bash
# 에이전트에게 작업 지시
wsl -d Ubuntu -- bash -c "source ~/.bashrc 2>/dev/null && npx openclaw agent --session-id my-task -m '작업 내용'"

# JSON 출력으로 결과 파싱
wsl -d Ubuntu -- bash -c "source ~/.bashrc 2>/dev/null && npx openclaw agent --session-id my-task --json -m '작업 내용'"

# 에이전트 응답을 채널로 전달
wsl -d Ubuntu -- bash -c "source ~/.bashrc 2>/dev/null && npx openclaw agent --session-id my-task --deliver --channel whatsapp -t '+821097805690' -m '작업 내용'"
```

### 10-4. 채널 상태

```bash
wsl -d Ubuntu -- bash -c "source ~/.bashrc 2>/dev/null && npx openclaw channels status"
```

### 10-5. 로그 확인

```bash
wsl -d Ubuntu -- bash -c "source ~/.bashrc 2>/dev/null && npx openclaw logs --limit 50 --plain"
```

---

## 11. 일일 운영

### 11-1. 아침 시작 순서

```bash
# 1. Gateway 시작
wsl -d Ubuntu -- bash -c "source ~/.bashrc 2>/dev/null && nohup npx openclaw gateway start > /tmp/gateway.log 2>&1 & sleep 3 && echo 'Gateway started'"

# 2. ngrok 시작
wsl -d Ubuntu -- bash -c "nohup ~/ngrok http 18789 > /tmp/ngrok.log 2>&1 & sleep 5 && curl -s http://127.0.0.1:4040/api/tunnels | python3 -c 'import json,sys; d=json.load(sys.stdin); [print(t[\"public_url\"]) for t in d[\"tunnels\"]]'"

# 3. 채널 상태 확인
wsl -d Ubuntu -- bash -c "source ~/.bashrc 2>/dev/null && npx openclaw channels status"

# 4. WhatsApp 테스트 메시지
wsl -d Ubuntu -- bash -c "source ~/.bashrc 2>/dev/null && npx openclaw message send -t '+821097805690' --channel whatsapp -m '[시스템] 오늘도 OZKIZ 고객봇 정상 가동!'"
```

### 11-2. 재부팅 후 복구

Windows 재부팅 후에는 WSL의 모든 프로세스가 종료됩니다. 위 "아침 시작 순서"를 다시 실행하세요.

> **ngrok URL이 바뀌었다면:**
> 1. 새 URL 확인 (ngrok API 또는 로그)
> 2. LINE Developers Console → Messaging API → Webhook URL 업데이트
> 3. Verify 버튼으로 확인
>
> **현재는 ngrok 유료 고정 도메인 사용 중이므로 URL 변경 없음.**

### 11-3. 종료 (선택)

```bash
# ngrok 종료
wsl -d Ubuntu -- bash -c "pkill ngrok"

# Gateway 종료
wsl -d Ubuntu -- bash -c "source ~/.bashrc 2>/dev/null && npx openclaw gateway stop"
```

---

## 12. 오류 해결 (Troubleshooting)

### 오류 1: "Unknown model: anthropic/claude-sonnet-4-6"

**원인:** OpenClaw 2026.2.2-3이 해당 모델명을 인식하지 못함
**해결:**
```bash
wsl -d Ubuntu -- bash -c "source ~/.bashrc 2>/dev/null && npx openclaw config set agents.defaults.model.primary 'anthropic/claude-sonnet-4-5-20250929'"
```

### 오류 2: 에이전트가 고객에게 여러 메시지 전송 (내부 보고 누출)

**증상:** 고객이 중국어 내부 보고 ("收到客户咨询", "已回复客户") 메시지를 받음
**원인:** IDENTITY.md에 단일 응답 규칙이 없었거나, 기존 세션에 이전 지시가 남아있음
**해결:**
1. IDENTITY.md에 "답변은 오직 1개만" 규칙 추가 (위 7-2 참조)
2. 모든 세션 초기화 (위 7-4 참조)
3. 세션 초기화 후에도 문제 지속되면, Gateway 재시작까지 수행

### 오류 3: "access not configured" + 페어링 코드

**증상:** 새 LINE 발신자가 메시지를 보내면 "access not configured. Pairing code: XXXXXXXX"
**해결:**
```bash
wsl -d Ubuntu -- bash -c "source ~/.bashrc 2>/dev/null && npx openclaw pairing approve line XXXXXXXX"
```

### 오류 4: Gateway 포트 충돌 ("port 18789 already in use")

**원인:** 이전 Gateway 프로세스가 제대로 종료되지 않음
**해결:**
```bash
wsl -d Ubuntu -- bash -c "fuser -k 18789/tcp 2>/dev/null; rm -f ~/.openclaw/*.lock; sleep 1 && nohup npx openclaw gateway start > /tmp/gateway.log 2>&1 &"
```

### 오류 5: "LINE channel access token not configured" 경고

**원인:** `npx openclaw channels status` 명령의 표시 버그
**실제 상태:** 설정은 정상. 메시지 수신/발신 정상 작동
**확인 방법:** `npx openclaw config get channels.line`으로 실제 설정 확인

### 오류 6: WhatsApp 에스컬레이션 안 됨

**원인 1:** IDENTITY.md에서 도구 이름이 `send_message`로 되어있음 (잘못된 이름)
**해결:** 도구 이름을 **`message`**로 변경 + 세션 초기화

**원인 2:** exec approvals에 `message:*` 패턴이 없음
**해결:**
```bash
wsl -d Ubuntu -- bash -c "source ~/.bashrc 2>/dev/null && npx openclaw approvals allowlist add --agent '*' 'message:*'"
```

**에이전트 사용 가능 도구 확인 방법:**
```bash
wsl -d Ubuntu -- bash -c "source ~/.bashrc 2>/dev/null && npx openclaw agent --session-id tool-check --json -m '사용 가능한 도구 목록 알려줘'" 2>&1 | python3 -c "import re,sys; tools=re.findall(r'\"name\":\s*\"([^\"]+)\"',sys.stdin.read()); print(list(dict.fromkeys(tools)))"
```

### 오류 7: ngrok "command not found"

**원인:** ngrok이 PATH에 없음
**해결:** 절대 경로 사용 `~/ngrok` 또는 `/home/kndli423/ngrok`

### 오류 8: auto_deliver.py 인코딩 오류 (cp949)

**원인:** subprocess.run()에서 Windows 기본 인코딩(cp949) 사용
**해결:** `encoding="utf-8", errors="replace"` 파라미터 추가
```python
result = subprocess.run(cmd, capture_output=True, text=True,
                       timeout=120, encoding="utf-8", errors="replace")
```

---

## 13. 크레덴셜 및 설정값 목록

> **보안 경고:** 이 섹션의 값은 실제 크레덴셜입니다. 절대 공개 저장소에 커밋하지 마세요!

### LINE

| 항목 | 값 |
|:-----|:---|
| Channel ID | `2009262136` |
| Channel Secret | `65692e57270ce549df9758801c117a31` |
| Channel Access Token | `4rmndHaIDHWj/eVChOPSHZ5uxenf...` (긴 토큰, openclaw.json에 저장됨) |
| Bot Basic ID | `@256yjrot` |
| Bot User ID | `Ub47e3403ca9addf1a43d72721a4d9530` |

### ngrok

| 항목 | 값 |
|:-----|:---|
| Auth Token | `3AFJQBoIBbE5yayxgLP2SU1zr3b_2WGjes56718vejNmHFKHr` |
| 현재 URL | `https://complicitly-flaxen-walton.ngrok-free.dev` |
| Webhook 전체 URL | `https://complicitly-flaxen-walton.ngrok-free.dev/webhook/line` |

### WhatsApp

| 항목 | 값 |
|:-----|:---|
| 벨라 번호 | `+821097805690` |

### OpenClaw

| 항목 | 값 |
|:-----|:---|
| Gateway 포트 | `18789` |
| 에이전트 모델 | `anthropic/claude-sonnet-4-5-20250929` |
| Workspace | `/home/kndli423/.openclaw/workspace/` |
| 설정 파일 | `/home/kndli423/.openclaw/openclaw.json` |
| 세션 디렉토리 | `/home/kndli423/.openclaw/agents/main/sessions/` |

### 파일 경로

| 파일 | 경로 |
|:-----|:-----|
| IDENTITY.md | `~/.openclaw/workspace/IDENTITY.md` (WSL) |
| USER.md | `~/.openclaw/workspace/USER.md` (WSL) |
| openclaw.json | `~/.openclaw/openclaw.json` (WSL) |
| auto_deliver.py | `D:\Claude_AI_Knowledge\tools\auto_deliver.py` (Windows) |
| v8 주문 스킬 | `D:\OzKiz_Global_Automation\08_order\오즈키즈_주문_처리_완전_통합_스킬_v8_중요_0227.md` |
| 현재고조회.xlsx | `D:\OzKiz_Global_Automation\07_Quotation\data\현재고조회.xlsx` |
| ngrok 바이너리 | `/home/kndli423/ngrok` (WSL) |

---

## 부록: 빠른 참조 카드

### 한 줄 명령어 모음

```bash
# 전체 시작 (Gateway + ngrok + 상태 확인)
wsl -d Ubuntu -- bash -c "source ~/.bashrc 2>/dev/null && nohup npx openclaw gateway start > /tmp/gw.log 2>&1 & sleep 3 && nohup ~/ngrok http 18789 > /tmp/ng.log 2>&1 & sleep 5 && npx openclaw channels status"

# WhatsApp 메시지 보내기
wsl -d Ubuntu -- bash -c "source ~/.bashrc 2>/dev/null && npx openclaw message send -t '+821097805690' --channel whatsapp -m '메시지'"

# LINE 메시지 보내기
wsl -d Ubuntu -- bash -c "source ~/.bashrc 2>/dev/null && npx openclaw message send -t 'Ub47e3403ca9addf1a43d72721a4d9530' --channel line -m '메시지'"

# 세션 초기화 (에이전트 리셋)
wsl -d Ubuntu -- bash -c "rm -f ~/.openclaw/agents/main/sessions/*.jsonl && echo '{}' > ~/.openclaw/agents/main/sessions/sessions.json"

# Gateway 강제 재시작
wsl -d Ubuntu -- bash -c "fuser -k 18789/tcp 2>/dev/null; rm -f ~/.openclaw/*.lock; sleep 1 && source ~/.bashrc 2>/dev/null && nohup npx openclaw gateway start > /tmp/gw.log 2>&1 &"

# ngrok URL 확인
wsl -d Ubuntu -- bash -c "curl -s http://127.0.0.1:4040/api/tunnels | python3 -c 'import json,sys; [print(t[\"public_url\"]) for t in json.load(sys.stdin)[\"tunnels\"]]'"

# 에이전트 도구 목록 확인
wsl -d Ubuntu -- bash -c "source ~/.bashrc 2>/dev/null && npx openclaw agent --session-id tools --json -m '도구 목록'" 2>&1 | python3 -c "import re,sys; print(list(dict.fromkeys(re.findall(r'\"name\":\s*\"([^\"]+)\"',sys.stdin.read()))))"
```

---

## 14. 바탕화면 원클릭 시작

### 14-1. 배치 파일 (이미 설치됨)

파일: `C:\Users\User\Desktop\OZKIZ_OpenClaw_Start.bat`

더블클릭하면 자동으로:
1. Gateway 시작 (port 18789)
2. ngrok 터널 시작
3. 채널 상태 확인
4. WhatsApp 테스트 메시지 발송

> 이 창을 닫아도 서비스는 계속 실행됩니다 (nohup으로 백그라운드 실행)

### 14-2. 새 디바이스에 배치 파일 만들기

바탕화면에 `OZKIZ_OpenClaw_Start.bat` 파일을 만들고 아래 내용 저장:

```batch
@echo off
chcp 65001 >nul
echo OZKIZ OpenClaw 전체 시작
wsl -d Ubuntu -- bash -c "fuser -k 18789/tcp 2>/dev/null; rm -f ~/.openclaw/*.lock 2>/dev/null; sleep 1 && source ~/.bashrc 2>/dev/null && nohup npx openclaw gateway start > /tmp/gw.log 2>&1 & sleep 4 && echo 'Gateway OK'"
wsl -d Ubuntu -- bash -c "pkill ngrok 2>/dev/null; sleep 1 && nohup /home/kndli423/ngrok http 18789 > /tmp/ng.log 2>&1 & sleep 5 && curl -s http://127.0.0.1:4040/api/tunnels | python3 -c \"import json,sys; [print('ngrok:', t['public_url']) for t in json.load(sys.stdin)['tunnels']]\" || echo 'ngrok FAILED'"
wsl -d Ubuntu -- bash -c "source ~/.bashrc 2>/dev/null && npx openclaw channels status"
wsl -d Ubuntu -- bash -c "source ~/.bashrc 2>/dev/null && npx openclaw message send -t '+821097805690' --channel whatsapp -m '[OZKIZ] 시스템 시작 완료!'"
pause
```

---

## 15. Claude Code에게 요청하는 프롬프트 모음

### 벨라가 Claude Code에게 이렇게 말하면 됩니다:

### 시스템 시작/종료

| 벨라가 하는 말 | Claude Code가 하는 일 |
|:-------------|:--------------------|
| "오픈클로 시작해줘" | Gateway + ngrok + 채널 상태 확인 + WhatsApp 테스트 |
| "오픈클로 상태 확인해줘" | `channels status` 실행, 모든 채널 연결 확인 |
| "오픈클로 재시작해줘" | Gateway 강제 종료 후 재시작 + ngrok 재시작 |
| "오픈클로 종료해줘" | Gateway + ngrok 종료 |
| "ngrok URL 뭐야?" | ngrok API에서 현재 터널 URL 조회 |

### 메시지 발송

| 벨라가 하는 말 | Claude Code가 하는 일 |
|:-------------|:--------------------|
| "왓츠앱으로 메시지 보내줘: [내용]" | WhatsApp 채널로 메시지 전송 |
| "라인으로 메시지 보내줘: [내용]" | LINE 채널로 메시지 전송 |
| "이 파일 왓츠앱으로 보내줘" | auto_deliver.py 또는 message send --media로 파일 전송 |
| "이 엑셀 왓츠앱으로 보내줘" | Excel 파일을 WhatsApp으로 첨부 전송 |

### 에이전트 관리

| 벨라가 하는 말 | Claude Code가 하는 일 |
|:-------------|:--------------------|
| "라인 에이전트 리셋해줘" | 세션 JSONL 파일 삭제 + sessions.json 초기화 |
| "IDENTITY.md 수정해줘: [내용]" | IDENTITY.md 업데이트 + 세션 초기화 |
| "에이전트 도구 목록 확인해줘" | agent --json 으로 도구 목록 조회 |
| "에이전트한테 [내용] 물어봐줘" | agent --session-id로 에이전트에게 메시지 전달 |
| "에이전트 로그 보여줘" | `openclaw logs --limit 50` 실행 |

### 주문 처리

| 벨라가 하는 말 | Claude Code가 하는 일 |
|:-------------|:--------------------|
| "TY #023 air 2/28" | v8 스킬 따라 Tiny You 주문 처리 → 이지어드민 Excel 생성 |
| "PAD #025 air 2/23" | PAD/TOEY 주문 처리 → 이지어드민 Excel 생성 |
| "이 견적서 처리해줘" + PDF 경로 | PDF 파싱 → S-code 매칭 → 이지어드민 발주서 생성 |
| "발주서 만들어줘" | 이지어드민 Excel (15컬럼) 생성 |
| "발주서 왓츠앱으로 보내줘" | 생성된 Excel을 WhatsApp으로 전송 |
| "현재고 확인해줘: [상품명]" | 현재고조회.xlsx에서 검색 → 재고 수량 응답 |

### 업무 자동화

| 벨라가 하는 말 | Claude Code가 하는 일 |
|:-------------|:--------------------|
| "오늘 LINE 문의 요약해줘" | 에이전트 세션 로그에서 오늘 대화 추출 → 요약 |
| "크론 등록해줘: 매일 9시 인사" | `openclaw cron add` 으로 예약 작업 등록 |
| "LINE 고객한테 [내용] 답장해줘" | LINE 채널로 특정 고객에게 메시지 전송 |

### 예시 대화

```
벨라: 오픈클로 시작해줘
Claude Code: Gateway 시작합니다...
  → Gateway OK (port 18789) ✅
  → ngrok OK: https://complicitly-flaxen-walton.ngrok-free.dev ✅
  → WhatsApp: connected ✅
  → LINE: webhook mode ✅
  → WhatsApp 테스트 메시지 발송 완료 ✅

벨라: 고객이 라인으로 견적서 보냈어. Downloads에 있을거야. 처리해줘
Claude Code: Downloads 폴더에서 견적서 PDF 찾겠습니다...
  → 견적서_20260227.pdf 발견
  → PDF 파싱 중... 상품 5개, 총 120개 수량
  → 현재고조회.xlsx에서 S-code 매칭 중...
  → 이지어드민 발주서 생성 완료: OZKIZ_발주서_20260227.xlsx
  → WhatsApp으로 발송할까요?

벨라: 응 보내줘
Claude Code: WhatsApp 발송 완료! ✅
  Message ID: 3EB0E1083702AEFBDB14F6
```

---

*이 문서는 2026-02-27 실제 설정 및 테스트 기록을 기반으로 작성되었습니다.*
*Claude Code (Opus 4.6) + Bella 공동 작업*
