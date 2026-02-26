---
tags:
  - openclaw
  - setup
  - wsl
  - whatsapp
  - guide
---

# OpenClaw (구 Moltbot/Clawdbot) 완벽 가이드
# OpenClaw Complete Guide - Personal AI Assistant

> **작성일 / Created**: 2026-02-03
> **업데이트 / Updated**: 2026-02-03
> **버전 / Version**: 1.0
> **Author**: Bella (OZKIZ) + Claude (Opus 4.5)

---

## 목차 / Table of Contents

1. [OpenClaw란?](#openclaw란)
2. [명칭 변천사](#명칭-변천사)
3. [Claude vs OpenClaw 비교](#claude-vs-openclaw-비교)
4. [설치 가이드 (Windows WSL2)](#설치-가이드-windows-wsl2)
5. [기본 실행 방법](#기본-실행-방법)
6. [채널 연결 (텔레그램)](#채널-연결-텔레그램)
7. [자동화 활용 아이디어](#자동화-활용-아이디어)
8. [보안 주의사항](#보안-주의사항)
9. [비용 관리](#비용-관리)
10. [실제 사용 후기 정리](#실제-사용-후기-정리)
11. [FAQ](#faq)
12. [참고 자료](#참고-자료)

---

## OpenClaw란?

**OpenClaw**는 내 PC/서버에서 실행되는 **실행형 AI 에이전트**입니다.

### 핵심 특징

| 특징 | 설명 |
|------|------|
| **자가 호스팅** | 내 환경에서 24/7 실행 |
| **메신저 통합** | WhatsApp, Telegram, Slack, Discord, iMessage 등 |
| **실제 작업 수행** | 파일 정리, 브라우저 제어, 크론 자동화 |
| **멀티 모델** | Claude, GPT, Gemini 등 다양한 모델 지원 |

### 한 문장 정의

> "웹에서 답만 받는 AI"가 아니라 "내 환경에서 실제로 일하는 AI 비서"

---

## 명칭 변천사

```
Clawdbot (2025) → Moltbot (2026.01) → Open Claw (2026.01.29~)
```

| 시기 | 명칭 | 변경 이유 |
|------|------|----------|
| 2025 | Clawdbot | 초기 명칭 (Claude 기반) |
| 2026.01 | Moltbot | Anthropic 상표권 이슈로 변경 |
| 2026.01.29~ | **Open Claw** | 커뮤니티 브랜딩 전략 |

**현재 공식 명칭**: Open Claw
**GitHub**: https://github.com/openclaw/openclaw

---

## Claude vs OpenClaw 비교

| 구분 | Claude (Web/API) | OpenClaw |
|------|------------------|----------|
| **실행 위치** | Anthropic 클라우드 | 내 PC/서버 (자가호스팅) |
| **사용 방식** | 질문 → 답변 | 메신저로 지시 → 실제 작업 |
| **24/7 운영** | 요청 기반 | 데몬/크론으로 상시 가동 |
| **파일 접근** | 제한적 | 로컬 파일시스템 직접 접근 |
| **보안 책임** | Anthropic | 사용자 직접 관리 |
| **비용** | 구독 또는 API | API 비용만 (호스팅은 별도) |

### 언제 OpenClaw를 선택?

- 24시간 돌아가는 개인 비서가 필요할 때
- 메신저로 업무 지시를 하고 싶을 때
- 파일/브라우저 자동화가 필요할 때
- 구독료 대신 API 비용만 내고 싶을 때

---

## 설치 가이드 (Windows WSL2)

### 전제 조건

| 항목 | 요구사항 |
|------|----------|
| OS | Windows 10/11 + WSL2 |
| Node.js | v22 이상 |
| WSL | Ubuntu 권장 |

### Step 1: WSL2 설치 확인

```bash
# PowerShell에서 실행
wsl --list --verbose
```

WSL2가 없으면:
```bash
wsl --install -d Ubuntu
```

### Step 2: WSL Ubuntu에서 Node.js 확인

```bash
# WSL Ubuntu 터미널에서
node -v   # v22 이상 필요
npm -v
```

### Step 3: OpenClaw 글로벌 설치

```bash
# WSL Ubuntu에서 실행
npm install -g openclaw@latest
```

### Step 4: 온보딩 실행

```bash
# 설치 마법사 실행
npx openclaw onboard --install-daemon
```

온보딩에서 설정하는 것들:
1. API 키 입력 (Claude/OpenAI)
2. 채널 연결 (Telegram 권장)
3. 보안 설정

### Step 5: 설치 확인

```bash
npx openclaw --version
# 2026.2.1 출력되면 성공!
```

---

## 기본 실행 방법

### Gateway 시작

```bash
# 게이트웨이 실행 (기본 포트: 18789)
npx openclaw gateway --port 18789 --verbose
```

### 메시지 보내기

```bash
# 테스트 메시지 전송
npx openclaw message send --to +821012345678 --message "Hello from OpenClaw"
```

### 에이전트 실행

```bash
# 단일 명령 실행
npx openclaw agent --message "오늘 할 일 정리해줘" --thinking high
```

### 상태 확인

```bash
# 헬스체크
npx openclaw doctor
```

---

## 채널 연결 (텔레그램)

텔레그램이 초보자에게 가장 쉬운 채널입니다.

### Step 1: BotFather에서 봇 생성

1. 텔레그램에서 `@BotFather` 검색
2. `/newbot` 입력
3. 봇 이름 설정
4. **토큰 복사** (sk-... 형태)

### Step 2: OpenClaw 설정

`~/.openclaw/openclaw.json`:
```json
{
  "channels": {
    "telegram": {
      "botToken": "123456:ABCDEF..."
    }
  }
}
```

### Step 3: 연결 테스트

1. 텔레그램에서 내 봇 찾기
2. `/start` 누르기
3. 메시지 보내기 → 응답 확인

---

## 자동화 활용 아이디어

### 초보자용 (안전한 자동화)

| 자동화 | 설명 | 난이도 |
|--------|------|--------|
| **아침 브리핑** | 일정 + 날씨 + 할 일 요약 | 쉬움 |
| **리마인더** | 운동, 약, 마감 알림 | 쉬움 |
| **뉴스 요약** | 관심 분야 뉴스 클리핑 | 쉬움 |
| **회의 체크리스트** | 10분 전 준비물 알림 | 쉬움 |

### 중급자용 (업무 자동화)

| 자동화 | 설명 | 난이도 |
|--------|------|--------|
| **이메일 분류** | 중요 메일만 알림 | 중간 |
| **문서 요약** | PDF/문서 자동 요약 | 중간 |
| **코드 리뷰** | PR 자동 분석 | 중간 |
| **파일 정리** | 다운로드 폴더 자동 분류 | 중간 |

### 고급자용 (비즈니스 자동화)

| 자동화 | 설명 | 난이도 |
|--------|------|--------|
| **고객 문의 처리** | WhatsApp Business 연동 | 어려움 |
| **서버 모니터링** | 장애 감지 + 알림 | 어려움 |
| **브라우저 자동화** | 폼 입력, 데이터 수집 | 어려움 |
| **워크플로 통합** | Gmail + 캘린더 + Notion | 어려움 |

### 크론 설정 예시

```bash
# 매일 아침 8시 브리핑
npx openclaw cron add \
  --name "morning-briefing" \
  --schedule "0 8 * * *" \
  --message "오늘 일정과 할 일을 정리해줘" \
  --session isolated
```

**중요**: `--session isolated` 옵션으로 비용과 컨텍스트 분리!

---

## 보안 주의사항

### 절대 하지 말 것 (3대 실수)

1. **대시보드 인터넷 노출**
   - 로컬(127.0.0.1)에서만 접근
   - 외부 필요시 VPN/Tailscale 사용

2. **메인 PC에서 중요 데이터와 함께 운영**
   - 전용 기기 또는 격리 환경 권장
   - 민감 정보가 없는 환경에서 시작

3. **DM 무제한 허용**
   - 승인/페어링 방식 사용
   - 화이트리스트로 제한

### 보안 점검 명령어

```bash
# 기본 보안 감사
npx openclaw security audit

# 상세 점검
npx openclaw security audit --deep

# 자동 수정
npx openclaw security audit --fix
```

### 권장 설정

```json
{
  "gateway": {
    "bind": "127.0.0.1",
    "auth": {
      "mode": "password"
    }
  },
  "channels": {
    "telegram": {
      "dmPolicy": "pairing"
    }
  }
}
```

---

## 비용 관리

### 비용 구조

| 항목 | 비용 |
|------|------|
| OpenClaw 자체 | 무료 (오픈소스) |
| 호스팅 (VPS) | 월 $5~$20 (선택) |
| **API 사용량** | 변동 (주요 비용) |

### 월 예상 비용

| 사용량 | 예상 비용 | 사용 패턴 |
|--------|----------|----------|
| 라이트 | $10~20 | 브리핑, 요약 중심 |
| 중간 | $30~50 | 업무 자동화 일부 |
| 헤비 | $100+ | 대량 자동 실행 |

### 비용 절감 팁

1. **Isolated 세션 사용**: 컨텍스트 누적 방지
2. **작은 모델 먼저**: 필요한 곳만 큰 모델
3. **크론 주기 조절**: 너무 자주 실행 X
4. **작업 완료 시 세션 리셋**

---

## 실제 사용 후기 정리

### 사례 1: Mac mini 24/7 개인 비서 (MacStories)

- **환경**: M4 Mac mini + Telegram + iMessage
- **자동화**: RSS 모니터링 → 쇼노트 생성 → Todoist 태스크 → Notion 회고
- **체감**: "개별 도구를 연결하는 수고가 줄어듦"

### 사례 2: 소규모 비즈니스 전체 자동화 (Vertu)

- **환경**: Mac mini + Gmail + WhatsApp Business + 스프레드시트
- **자동화**: 영업 문의 → Follow-up → 스케줄 관리 → 재고 체크
- **체감**: "항상 깨어 있는 직원을 둔 효과"

### 사례 3: 하루 만에 삭제한 후기 (Reddit)

- **이유**: 파일시스템 + 브라우저 접근이 너무 광범위해서 불안
- **교훈**: "권한과 격리 설계가 먼저", 로컬에서 최소 권한으로 시작

### 사례 4: 능동형 브리핑 (r/LocalLLM)

- **환경**: Cron + 웹훅 + 이메일 파서
- **자동화**: 아침마다 Slack DM으로 "어제 못 끝낸 작업, 오늘 마감, 미처리 이메일"
- **체감**: "팀 리드가 먼저 브리핑해주는 느낌"

---

## FAQ

### Q1: Windows에서 직접 실행 가능한가요?

**WSL2 권장**. Windows 네이티브는 bash 스크립트 호환 문제가 있습니다.

### Q2: 한국어 잘 되나요?

모델 성능에 따름. 시스템 프롬프트에 "한국어로 응답" 규칙 추가 권장.

### Q3: 카카오톡 연동은?

공식 지원 X. 텔레그램/Slack/Discord가 봇 생태계가 더 성숙함.

### Q4: 구독 서비스와 비교해서 저렴한가요?

| 구분 | 월 비용 |
|------|---------|
| ChatGPT Plus | ~$20 (고정) |
| Claude Pro | ~$20 (고정) |
| OpenClaw | $5~50 (변동, 사용량 기반) |

라이트 사용자라면 OpenClaw가 더 저렴.

### Q5: 보안이 걱정됩니다

- 로컬에서만 시작
- `security audit` 정기 실행
- 전용 기기/격리 환경 권장

---

## 참고 자료

### 공식
- [OpenClaw GitHub](https://github.com/openclaw/openclaw)
- [공식 문서](https://docs.openclaw.ai)
- [Discord 커뮤니티](https://discord.gg/openclaw)

### 관련 문서
- [05_Structured_Outputs_Guide.md](./05_Structured_Outputs_Guide.md)
- [06_Memory_Context_Guide.md](./06_Memory_Context_Guide.md)

### 후기/사례
- [MacStories 리뷰](https://www.macstories.net)
- [Reddit r/artificial](https://reddit.com/r/artificial)
- [Reddit r/LocalLLM](https://reddit.com/r/LocalLLM)

---

## 업데이트 로그 / Changelog

| 날짜 | 버전 | 내용 |
|------|------|------|
| 2026-02-03 | v1.0 | 초기 버전 작성 |

---

*Made with Claude by Bella (OZKIZ)*
