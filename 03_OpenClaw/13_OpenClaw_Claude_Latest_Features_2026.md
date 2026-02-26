---
tags:
  - openclaw
  - claude
  - remote-control
  - kakao
  - advanced
  - 2026
---

# OpenClaw + Claude 최신 기능 종합 가이드 (2026-02)
# Complete Guide: OpenClaw & Claude Latest Features

> **작성일**: 2026-02-26
> **환경**: Windows 11 + WSL2 Ubuntu / OpenClaw 2026.2.2-3
> **Author**: Bella (OZKIZ) + Claude (Opus 4.6)

---

## 목차

1. [전체 로드맵 (Step-by-Step)](#1-전체-로드맵)
2. [Claude Code Remote Control](#2-claude-code-remote-control)
3. [OpenClaw-Kakao (카카오톡 연동)](#3-openclaw-kakao-카카오톡-연동)
4. [OpenClaw 실전 고급 운영 팁](#4-openclaw-실전-고급-운영-팁)
5. [ClawDeck - 미션 컨트롤](#5-clawdeck---미션-컨트롤)
6. [Ollama 로컬 모델 연동](#6-ollama-로컬-모델-연동)
7. [실전 활용 시나리오](#7-실전-활용-시나리오)
8. [프롬프트 작성 가이드](#8-프롬프트-작성-가이드)
9. [설정 시 주의사항](#9-설정-시-주의사항)
10. [참고 자료](#10-참고-자료)

---

## 1. 전체 로드맵

### 추천 학습 & 적용 순서

```
Phase 1 (이번 주) ────────────────────────────────────
│ ✅ Step 1: Remote Control 설정 (30분)
│ ✅ Step 2: OpenClaw 모델 업그레이드 확인 (완료)
│ ✅ Step 3: Cron 자동화 2~3개 설정 (1시간)
│
Phase 2 (다음 주) ────────────────────────────────────
│ 🔲 Step 4: OpenClaw-Kakao 브릿지 설치 (2~3시간)
│ 🔲 Step 5: 멀티 에이전트 설정 (1시간)
│ 🔲 Step 6: Webhook 연동 (n8n/Make)
│
Phase 3 (2주 후~) ────────────────────────────────────
│ 🔲 Step 7: ClawDeck 대시보드 설치
│ 🔲 Step 8: Ollama 로컬 모델 (선택)
│ 🔲 Step 9: Custom Skill 개발
```

---

## 2. Claude Code Remote Control

### 2.1 이게 뭐야?

> 내 PC에서 돌아가는 Claude Code 세션을 **스마트폰/태블릿/다른 PC 브라우저**에서 원격 조작하는 기능

**핵심 포인트:**
- 로컬 환경(파일, MCP 서버, 프로젝트 설정)이 그대로 유지됨
- 클라우드가 아닌 **내 PC에서 실행** → 웹/모바일은 "리모컨" 역할만
- 네트워크 끊겨도 자동 재연결

### 2.2 요구 사항

| 항목 | 조건 |
|------|------|
| **구독** | Pro 또는 Max 플랜 (API 키 불가) |
| **인증** | `/login`으로 claude.ai 로그인 |
| **Claude Code 버전** | 2.1.52 이상 |
| **워크스페이스 신뢰** | 프로젝트 디렉토리에서 최소 1번 `claude` 실행 |

### 2.3 시작 방법

#### 방법 A: 새 세션으로 시작
```bash
# 프로젝트 디렉토리에서
claude remote-control
```
→ 세션 URL + QR 코드 표시됨

#### 방법 B: 기존 세션에서 전환
```
# Claude Code 세션 안에서
/remote-control    # 또는 /rc
```

#### 연결하기
1. **URL 직접 열기**: 터미널에 표시된 URL을 브라우저에서 열기
2. **QR 코드 스캔**: 스마트폰 Claude 앱으로 스캔
3. **claude.ai/code**: 세션 목록에서 선택 (초록 점 = 온라인)

### 2.4 유용한 옵션

```bash
# 상세 로그 보기
claude remote-control --verbose

# 샌드박싱 활성화 (보안 강화)
claude remote-control --sandbox

# 세션 이름 지정 후 원격 제어
/rename "마케팅 프로젝트 작업"
/rc
```

### 2.5 자동 활성화 설정

매번 `/rc` 치기 귀찮으면:
```
/config
→ "Enable Remote Control for all sessions" → true
```

### 2.6 보안 모델

| 보안 항목 | 설명 |
|-----------|------|
| 인바운드 포트 | 열지 않음 (아웃바운드 HTTPS만) |
| 통신 암호화 | TLS (Anthropic API 경유) |
| 인증 토큰 | 단기 수명, 용도별 분리 |
| 파일 접근 | 로컬에서만 처리 (클라우드 전송 안 함) |

### 2.7 Bella의 활용 시나리오

| 상황 | 활용법 |
|------|--------|
| **출근길/퇴근길** | 폰으로 코딩 진행 상황 확인 & 지시 |
| **회의 중** | PC에서 돌아가는 작업을 폰으로 모니터링 |
| **외출 시** | 고객 문의 관련 코드 수정을 원격으로 지시 |
| **카페 작업** | 집 PC의 프로젝트를 카페 노트북에서 이어서 |

### 2.8 제한사항

- 동시 원격 세션: **1개만** 가능
- 터미널 닫으면 세션 종료됨
- 네트워크 10분 이상 끊기면 타임아웃
- Team/Enterprise 플랜은 아직 미지원

---

## 3. OpenClaw-Kakao (카카오톡 연동)

### 3.1 아키텍처

```
┌─────────────────┐     ┌──────────────┐     ┌─────────────────┐
│  BlueStacks 5   │     │   Bridge     │     │  OpenClaw       │
│  KakaoTalk      │────▶│   Server     │────▶│  Gateway        │
│  + MessengerBotR│     │  (Node.js)   │     │  (Claude AI)    │
└─────────────────┘     │  포트: 8787  │     │  포트: 18789    │
                        └──────┬───────┘     └─────────────────┘
                        ┌──────┴──────┐
                        │ ADB Watcher │  ← 이미지 자동 감지
                        │  (Python)   │
                        └─────────────┘
```

### 3.2 작동 원리

**텍스트 메시지:**
```
사용자 카톡 전송 → MessengerBotR 감지 → Bridge → Gateway → Claude 응답 → 카톡 전달
```

**이미지 메시지:**
```
사용자 이미지 전송 → 카톡 자동저장 → ADB Watcher 감지 → Bridge → Claude Vision 분석 → 결과 전달
```

### 3.3 설치 전제 조건

| 항목 | 요구사항 |
|------|----------|
| Node.js | v18 이상 |
| Python | 3.8 이상 |
| BlueStacks | 5 (ADB 활성화) |
| MessengerBotR | Android 앱 |
| OpenClaw CLI | 설치 및 설정 완료 |
| 카카오톡 | **부계정** 사용 권장 |

### 3.4 설치 순서

#### Step 1: 저장소 클론
```bash
git clone https://github.com/tornado1014/openclaw-kakao.git
cd openclaw-kakao
```

#### Step 2: Bridge 서버 설치
```bash
cd bridge
npm install
cd ..
```

#### Step 3: ADB Watcher 설치 (이미지 분석용)
```bash
cd watcher
pip install -r requirements.txt
cd ..
```

#### Step 4: 환경 설정
```bash
cp .env.example .env
```

`.env` 파일 편집:
```env
# OpenClaw Gateway 정보 (openclaw gateway status에서 확인)
OPENCLAW_GATEWAY_URL=http://localhost:18789
OPENCLAW_GATEWAY_TOKEN=your-gateway-token

# (선택) 이미지 분석 폴백용 Gemini
GOOGLE_API_KEY=your-gemini-api-key
```

#### Step 5: 실행
```bash
# 1. OpenClaw Gateway 시작 (WSL)
openclaw gateway start

# 2. Bridge 서버 시작
cd bridge && npm start

# 3. ADB Watcher 시작 (이미지 지원)
cd watcher && python adb_watcher.py --auto-port
```

#### Step 6: MessengerBotR 설정
1. BlueStacks에서 MessengerBotR 앱 설치
2. `messenger-bot/bot-script.js` 내용을 MessengerBotR 에디터에 복사
3. 봇 활성화

### 3.5 사용 가능한 명령어

| 명령어 | 설명 |
|--------|------|
| `/ping` | 봇 상태 확인 |
| `/bridgeping` | Bridge 연결 확인 |
| `/status` | 시스템 전체 상태 |
| `/clear` | 대화 세션 리셋 |
| `/whoami` | 세션 키 확인 |
| `/help` | 도움말 |
| `/on` · `/off` | 봇 활성/비활성 |
| `/질문 <메시지>` | 그룹채팅에서 AI 질문 |

- **1:1 채팅**: 그냥 메시지 보내면 AI 응답
- **그룹 채팅**: `/질문` 접두사 필요

### 3.6 주의사항

> **반드시 카카오톡 부계정 사용!**
> - 본계정 사용 시 계정 정지 위험
> - BlueStacks에서 부계정으로 로그인
> - 본계정은 평소대로 폰에서 사용

| 주의사항 | 설명 |
|----------|------|
| 부계정 필수 | 자동화 봇 = 카카오톡 이용약관 위반 가능성 |
| BlueStacks ADB | ADB 디버깅 반드시 활성화 |
| Bridge 포트 | 8787 포트가 방화벽에 막히지 않도록 |
| 이미지 자동저장 | 카톡 설정에서 "사진 자동 다운로드" 활성화 필요 |
| Gateway 토큰 | `.env`에 정확한 토큰 입력 |

---

## 4. OpenClaw 실전 고급 운영 팁

### 4.1 Cron 자동화 (즉시 적용 가능)

#### 아침 브리핑 설정
```bash
openclaw cron add \
  --name "morning-briefing" \
  --schedule "0 8 * * *" \
  --message "오늘 일정, 중요 알림, 어제 미완료 작업을 정리해줘" \
  --session isolated
```

#### 퇴근 리포트
```bash
openclaw cron add \
  --name "daily-report" \
  --schedule "0 18 * * 1-5" \
  --message "오늘 완료한 업무와 내일 할 일을 정리해줘" \
  --session isolated
```

#### 주간 마케팅 분석
```bash
openclaw cron add \
  --name "weekly-marketing" \
  --schedule "0 9 * * 1" \
  --message "이번 주 소셜미디어 성과와 다음 주 콘텐츠 계획을 제안해줘" \
  --session isolated
```

#### 크론 관리 명령어
```bash
openclaw cron list          # 등록된 크론 목록
openclaw cron runs          # 실행 이력
openclaw cron edit <name>   # 수정
openclaw cron run --force <name>  # 즉시 실행
openclaw cron remove <name> # 삭제
```

**핵심**: `--session isolated`로 비용과 컨텍스트 분리!

### 4.2 Webhook 연동

`openclaw.json`에 웹훅 활성화:
```json
{
  "webhooks": {
    "enabled": true,
    "endpoints": ["/hooks/wake", "/hooks/agent"]
  }
}
```

#### 활용 예시
```bash
# 외부에서 에이전트 호출 (GitHub PR 리뷰 등)
curl -X POST http://localhost:18789/hooks/agent \
  -H "Content-Type: application/json" \
  -d '{"message": "새 PR을 리뷰해줘", "delivery": "telegram"}'
```

**n8n/Make 연동 아이디어:**
- GitHub PR → OpenClaw 코드 리뷰 → Slack 알림
- Gmail 중요 메일 → OpenClaw 요약 → Telegram 전달
- 고객 문의 접수 → OpenClaw 초안 작성 → 이메일 발송 대기

### 4.3 멀티 에이전트 시스템

역할별 에이전트를 분리하여 운영:

```json
{
  "agents": {
    "personal": {
      "model": { "primary": "anthropic/claude-sonnet-4-6" },
      "permissions": "full",
      "channels": ["whatsapp:+821097805690"]
    },
    "customer-service": {
      "model": { "primary": "anthropic/claude-sonnet-4-6" },
      "permissions": "restricted",
      "channels": ["kakao:customer-room"],
      "sandbox": true
    },
    "marketing": {
      "model": { "primary": "anthropic/claude-haiku-4-5" },
      "permissions": "read-only",
      "channels": ["telegram:marketing-group"]
    }
  }
}
```

| 에이전트 | 모델 | 역할 | 비용 |
|----------|------|------|------|
| personal | Sonnet 4.6 | 개인 비서 (전체 권한) | 중간 |
| customer | Sonnet 4.6 | 고객 응대 (제한 권한) | 중간 |
| marketing | Haiku 4.5 | 마케팅/요약 (읽기 전용) | 저렴 |

### 4.4 모델 역할 분리 전략

```
┌─────────────────────────────────────────────┐
│  복잡한 분석/코딩  →  Opus 4.6 (비쌈)      │
│  일반 대화/응대    →  Sonnet 4.6 (균형)     │
│  간단 분류/요약    →  Haiku 4.5 (저렴)      │
│  개인정보 민감     →  Ollama 로컬 (무료)     │
└─────────────────────────────────────────────┘
```

### 4.5 Workspace 파일 베스트 프랙티스

| 파일 | 용도 | 예시 |
|------|------|------|
| `AGENTS.md` | 핵심 행동 규칙, 안전 지침 | "고객에게 가격 할인 약속 금지" |
| `SOUL.md` | 성격, 커뮤니케이션 스타일 | "따뜻하고 전문적인 톤" |
| `MEMORY.md` | 장기 기억 (프로젝트, 선호도) | "Bella는 한/중/영 3개 국어 사용" |
| `HEARTBEAT.md` | 자동 체크리스트, 긴급도 분류 | "20분 무응답 시 이메일 발송" |

### 4.6 브라우저 자동화

```bash
# 경쟁사 가격 모니터링 크론
openclaw cron add \
  --name "price-monitor" \
  --schedule "0 10,16 * * *" \
  --message "다음 경쟁사 사이트의 메인 상품 가격을 확인하고 비교표 만들어줘: [URL 목록]" \
  --session isolated
```

### 4.7 보안 감사 (정기 실행 권장)

```bash
# 기본 보안 점검
openclaw security audit

# 심층 점검
openclaw security audit --deep

# 자동 수정
openclaw security audit --fix
```

---

## 5. ClawDeck - 미션 컨트롤

### 5.1 이게 뭐야?

> 여러 OpenClaw 에이전트를 **한 대시보드에서 관리/모니터링/오케스트레이션**하는 오픈소스 도구

### 5.2 핵심 기능

| 기능 | 설명 |
|------|------|
| **세션 추적** | 모든 에이전트 활동 기록 & 검색 |
| **실시간 모니터링** | 활성 에이전트 상태 라이브 대시보드 |
| **오케스트레이션** | 워크플로 정의, 에이전트간 작업 전달 |
| **로그 집계** | 분산 로그를 한 곳에서 검색 |

### 5.3 언제 필요한가?

- 에이전트 3개 이상 운영할 때
- 고객 응대 + 마케팅 + 개인 비서를 동시에 돌릴 때
- 팀원과 에이전트 관리를 공유할 때

### 5.4 설치

```bash
# GitHub: clawdeckio/clawdeck
git clone https://github.com/clawdeckio/clawdeck.git
cd clawdeck
npm install && npm start
```

→ Phase 3에서 에이전트가 늘어나면 도입 권장

---

## 6. Ollama 로컬 모델 연동

### 6.1 왜 필요한가?

| 상황 | Ollama 사용 이유 |
|------|-----------------|
| API 비용 절감 | 간단한 작업은 로컬 모델로 처리 |
| 개인정보 보호 | 민감한 데이터가 외부로 나가지 않음 |
| 오프라인 사용 | 인터넷 없이도 AI 사용 가능 |

### 6.2 권장 모델

| 모델 | 용도 | VRAM |
|------|------|------|
| `glm-4.7-flash` | 빠른 응답, 가벼운 작업 | ~25GB |
| `kimi-k2.5:cloud` | 클라우드 연동 | - |
| `minimax-m2.5:cloud` | 클라우드 연동 | - |

### 6.3 설정 방법

```bash
# 1. Ollama 설치 (WSL)
curl -fsSL https://ollama.com/install.sh | sh

# 2. 모델 다운로드
ollama pull glm-4.7-flash

# 3. OpenClaw에서 연동
openclaw configure --section model
# Provider: ollama 선택
# Model: glm-4.7-flash
```

`openclaw.json`에 추가:
```json
{
  "models": {
    "ollama/glm-4.7-flash": {
      "alias": "local",
      "endpoint": "http://localhost:11434"
    }
  }
}
```

> **참고**: Bella의 현재 환경(Windows 11 Home)에서는 VRAM이 부족할 수 있으므로, 클라우드 모델을 우선 사용하고 필요시 도입 검토

---

## 7. 실전 활용 시나리오

### 7.1 Bella의 업무별 활용 맵

```
┌────────────────────────────────────────────────────────┐
│                    Bella의 OpenClaw 생태계              │
├───────────┬───────────┬───────────┬────────────────────┤
│  WhatsApp │  KakaoTalk│ Telegram  │   Claude Code      │
│  (고객응대)│ (한국고객) │ (개인비서) │   (개발/프로젝트)   │
├───────────┴───────────┴───────────┴────────────────────┤
│              OpenClaw Gateway (Sonnet 4.6)              │
├────────────────────────────────────────────────────────┤
│    Cron 자동화  │  Webhook  │  MCP 서버  │  ClawDeck   │
└────────────────────────────────────────────────────────┘
```

### 7.2 시나리오별 설정

#### A. 회사 업무 (고객 응대)

**채널**: WhatsApp + KakaoTalk (부계정)
**에이전트**: customer-service

```markdown
# AGENTS.md (고객 응대 에이전트)

## 역할
- 이름: 貝拉 (Bella)
- 역할: 고객 응대 비서

## 규칙
1. 고객 언어에 맞춰 응답 (중국어/한국어/영어)
2. 가격 할인, 환불 약속 절대 금지
3. 복잡한 문의 → 20분 대기 → 이메일 정리 (bella@ozkiz.com)
4. 주인에게는 한국어+중국어 번역 제공

## 응답 톤
- 친절하고 전문적
- 이모지 적절히 사용
- 문제 해결 중심
```

#### B. 학교 (학습 보조)

**채널**: Telegram
**에이전트**: study-assistant

```markdown
# AGENTS.md (학습 보조 에이전트)

## 역할
- 과제 마감 리마인더
- 논문/자료 요약
- 학습 계획 수립 도우미

## 크론 설정
- 매일 아침 8시: 오늘 수업/과제 알림
- 매주 일요일 저녁: 다음 주 학습 계획 제안
```

**크론 설정:**
```bash
openclaw cron add \
  --name "school-reminder" \
  --schedule "0 8 * * 1-5" \
  --message "오늘 수업 일정과 마감 임박한 과제를 알려줘" \
  --session isolated
```

#### C. 마케팅 & 소셜 계정 운영

**채널**: Telegram
**에이전트**: marketing

```markdown
# AGENTS.md (마케팅 에이전트)

## 역할
- 소셜미디어 콘텐츠 아이디어 제안
- 해시태그 생성
- 게시물 초안 작성 (인스타/블로그)
- 트렌드 분석 (Brave Search 활용)

## 규칙
1. 브랜드 톤 유지 (OZKIZ 스타일)
2. 게시물은 반드시 초안으로 → 승인 후 게시
3. 주 3회 콘텐츠 계획 제안
```

**크론 설정:**
```bash
# 주 3회 콘텐츠 제안
openclaw cron add \
  --name "content-ideas" \
  --schedule "0 10 * * 1,3,5" \
  --message "이번 주 OZKIZ 인스타그램/블로그 콘텐츠 아이디어 3개를 제안해줘. 트렌드와 시즌을 고려해서." \
  --session isolated
```

#### D. 프로젝트 (Claude Smart Korea)

**채널**: Claude Code + Remote Control
**활용**:

```bash
# Remote Control로 프로젝트 작업
cd D:/AI_coding_project_all/Claude\ Smart\ Korea
claude remote-control --verbose
```

→ 집에서 시작한 코딩을 외출 시 폰으로 모니터링 & 지시

#### E. 일상 개인 비서

```bash
# 종합 아침 브리핑
openclaw cron add \
  --name "morning-all" \
  --schedule "0 7 30 * * *" \
  --message "오늘 날씨, 일정, 미완료 작업, 중요 알림을 한눈에 정리해줘" \
  --session isolated
```

---

## 8. 프롬프트 작성 가이드

### 8.1 OpenClaw 시스템 프롬프트 (SOUL.md)

```markdown
# SOUL.md - OpenClaw 성격 설정

## 기본 정보
- 이름: 貝拉 (Bella)
- 주인: Bella (OZKIZ)
- 언어: 한국어, 중국어, 영어 (상황에 맞게 전환)
- 시간대: Asia/Seoul (GMT+9)

## 성격
- 따뜻하고 전문적
- 이모지 적절히 사용 (과하지 않게)
- 간결하지만 필요한 정보는 빠뜨리지 않음
- 유머 센스 약간

## 커뮤니케이션 원칙
1. 고객에게는 항상 존댓말
2. 주인에게는 친근하게
3. 불확실한 정보는 "확인 후 알려드리겠습니다" 로 대응
4. 문제 발생 시 즉시 주인에게 알림
```

### 8.2 고객 응대 프롬프트 예시

```markdown
# AGENTS.md - 고객 응대 전문

## 응대 흐름
1. 인사 → 2. 요구 파악 → 3. 해결/안내 → 4. 마무리

## 자주 묻는 질문 템플릿

### 배송 문의
"안녕하세요! 주문 번호를 알려주시면 배송 상태를 확인해드릴게요 📦"

### 제품 문의
"해당 제품에 대해 안내해드릴게요! [제품 정보 제공]
추가 궁금하신 점이 있으시면 말씀해주세요 😊"

### 교환/반품
"교환/반품 관련 문의시군요.
자세한 내용은 담당자 확인 후 안내드리겠습니다.
(→ 주인에게 즉시 알림)"

## 절대 하지 말 것
- ❌ 가격 할인 약속
- ❌ 환불 승인
- ❌ 재고/입고 일정 확정
- ❌ 개인정보 요청
```

### 8.3 학습용 프롬프트

```markdown
# 학습 보조 에이전트 프롬프트

## 역할
당신은 학습 튜터입니다. 다음 원칙을 따라주세요:

1. **설명 방식**: 쉬운 비유 → 핵심 개념 → 예시 순서
2. **질문 유도**: 답을 바로 주지 말고 힌트를 먼저 제공
3. **요약**: 긴 자료는 핵심만 3줄로 먼저 요약
4. **언어**: 전공 용어는 한국어(영어 병기)
   예: "회귀분석(Regression Analysis)"
```

### 8.4 마케팅 콘텐츠 프롬프트

```markdown
# 마케팅 에이전트 프롬프트

## 브랜드 정보
- 브랜드: OZKIZ
- 타겟: [타겟 고객층]
- 톤: 세련되고 따뜻한

## 콘텐츠 작성 규칙
1. 인스타: 150자 이내 + 해시태그 10~15개
2. 블로그: 제목(클릭 유도) + 소제목 3~5개 + 본문
3. 모든 콘텐츠는 CTA(행동 유도) 포함
4. 시즌/트렌드 반영

## 출력 형식
```
📱 인스타 캡션:
[캡션 내용]

#해시태그1 #해시태그2 ...

📝 블로그 제목 후보 (3개):
1. ...
2. ...
3. ...
```
```

---

## 9. 설정 시 주의사항

### 9.1 보안 체크리스트

| # | 항목 | 중요도 | 상태 |
|---|------|--------|------|
| 1 | Gateway를 127.0.0.1에만 바인딩 | 🔴 필수 | ✅ |
| 2 | WhatsApp allowlist 설정 | 🔴 필수 | ✅ |
| 3 | API 키를 .env에만 저장 (git 제외) | 🔴 필수 | ✅ |
| 4 | 카카오톡은 부계정만 사용 | 🔴 필수 | 🔲 |
| 5 | `security audit` 주기적 실행 | 🟡 권장 | 🔲 |
| 6 | 민감 작업은 sandbox 모드 | 🟡 권장 | 🔲 |
| 7 | 고객 응대 에이전트 권한 제한 | 🟡 권장 | 🔲 |
| 8 | ClawDeck으로 활동 모니터링 | 🟢 선택 | 🔲 |

### 9.2 비용 관리 주의사항

| 실수 | 결과 | 예방법 |
|------|------|--------|
| 크론을 너무 자주 설정 | API 비용 폭증 | 최소 간격 1시간 |
| `--session isolated` 안 씀 | 컨텍스트 누적 → 토큰 낭비 | 항상 isolated 사용 |
| Opus 모델 남용 | 비용 10배 | 간단한 작업은 Haiku 사용 |
| 고객 대화 무한 루프 | 비용 폭증 | 최대 턴 수 제한 설정 |

### 9.3 Windows + WSL2 환경 주의사항

| 주의사항 | 설명 |
|----------|------|
| WSL 메모리 | `.wslconfig`에서 메모리 제한 설정 권장 |
| 포트 충돌 | Windows와 WSL 포트 포워딩 확인 |
| BlueStacks + WSL | 동시 실행 시 메모리 부족 가능 → 최소 16GB RAM 권장 |
| npm 경로 | Windows npm과 WSL npm 혼동 주의 (WSL 안에서만 실행) |
| 절전 모드 | 절전 시 Gateway 연결 끊김 → 절전 비활성화 또는 재연결 크론 설정 |

### 9.4 카카오톡 연동 특별 주의사항

> ⚠️ **카카오톡 자동화는 공식적으로 지원되지 않는 방식입니다**

| 위험 | 대처 |
|------|------|
| 계정 정지 | **반드시 부계정 사용** |
| BlueStacks 업데이트 | 자동 업데이트 끄기 (호환성 깨질 수 있음) |
| MessengerBotR 불안정 | 주기적 상태 확인 (`/ping`) |
| 이미지 감지 실패 | ADB Watcher 로그 확인 |

---

## 10. 참고 자료

### 공식 문서
- [OpenClaw 공식 문서](https://docs.openclaw.ai/)
- [Claude Code Remote Control 문서](https://code.claude.com/docs/en/remote-control)
- [OpenClaw GitHub](https://github.com/openclaw/openclaw)

### 카카오톡 연동
- [openclaw-kakao GitHub](https://github.com/tornado1014/openclaw-kakao)

### 커뮤니티 & 가이드
- [OpenClaw 200% 활용하기 - EffiFlow](https://jangwook.net/en/blog/en/openclaw-advanced-usage/)
- [ClawDeck: Mission Control](https://openclaws.io/blog/clawdeck-mission-control)
- [Claude Code Remote Control - Simon Willison](https://simonwillison.net/2026/Feb/25/claude-code-remote-control/)
- [Remote Control - VentureBeat](https://venturebeat.com/orchestration/anthropic-just-released-a-mobile-version-of-claude-code-called-remote)
- [OpenClaw - 나무위키](https://namu.wiki/w/OpenClaw)
- [Ollama + OpenClaw 연동 가이드](https://leejams.github.io/openclaw-ollama/)

### 기존 가이드 (이 폴더 내)
- [OpenClaw 완전 가이드](./11_OpenClaw_Complete_Guide.md)
- [OpenClaw 빠른 명령어](./OpenClaw_Quick_Commands.md)
- [OpenClaw 설정 로그](./OpenClaw_Setup_Log_2026-02-03.md)

---

## 업데이트 로그

| 날짜 | 내용 |
|------|------|
| 2026-02-26 | v1.0 초기 작성 - 전체 가이드 통합 |

---

*Made with Claude Opus 4.6 by Bella (OZKIZ)*
