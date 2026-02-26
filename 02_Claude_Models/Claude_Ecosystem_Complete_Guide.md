---
tags:
  - claude
  - ecosystem
  - overview
  - comprehensive
---

# Claude 생태계 완벽 가이드
# Claude Ecosystem Complete Guide

> **작성자**: Bella (OZKIZ) + Claude (Opus 4.5)
> **작성일**: 2026-02-05
> **대상**: Claude 도구들을 처음 접하는 분들, GPTers 스터디원
> **목적**: Claude Code, Claude AI(웹), OpenClaw의 차이점과 협업 방법 이해

---

## 목차

1. [한눈에 보는 Claude 도구 비교](#1-한눈에-보는-claude-도구-비교)
2. [각 도구 상세 설명](#2-각-도구-상세-설명)
3. [사용 시나리오별 추천](#3-사용-시나리오별-추천)
4. [도구 간 협업 시너지](#4-도구-간-협업-시너지)
5. [OpenClaw 심화 활용법](#5-openclaw-심화-활용법)
6. [실전 워크플로우 예시](#6-실전-워크플로우-예시)
7. [비용 비교 및 최적화](#7-비용-비교-및-최적화)
8. [설치 및 설정 요약](#8-설치-및-설정-요약)
9. [FAQ](#9-faq)

---

## 1. 한눈에 보는 Claude 도구 비교

### 🎯 핵심 차이점 요약

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        Claude 생태계 도구 비교                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Claude AI (Web)          Claude Code              OpenClaw                 │
│  ════════════════         ═══════════════          ═══════════════          │
│  📱 브라우저 채팅           💻 터미널 코딩           🦞 24/7 AI 비서          │
│  ├─ 문서 작성              ├─ 코드 개발              ├─ 메신저 연동           │
│  ├─ 웹 검색                ├─ 파일 편집              ├─ 자동화 실행           │
│  ├─ 이미지 분석            ├─ Git 작업               ├─ 브라우저 제어         │
│  └─ 지식 정리              └─ 프로젝트 관리          └─ 스마트홈 제어         │
│                                                                             │
│  "생각하는 AI"            "코딩하는 AI"            "행동하는 AI"            │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 📊 기능 비교표

| 기능 | Claude AI (웹) | Claude Code | OpenClaw |
|------|:-------------:|:-----------:|:--------:|
| **실행 위치** | 클라우드 (웹) | 로컬 (터미널) | 로컬 (서버) |
| **접근 방법** | 브라우저 | CLI 터미널 | WhatsApp/Telegram 등 |
| **파일 접근** | 업로드만 | ✅ 직접 접근 | ✅ 직접 접근 |
| **코드 실행** | ✅ (Pro+) | ✅ | ✅ |
| **웹 검색** | ✅ | ✅ | ✅ (스킬) |
| **Git 작업** | ❌ | ✅ | ✅ |
| **브라우저 제어** | ❌ | ❌ | ✅ |
| **24/7 상시 운영** | ❌ | ❌ | ✅ |
| **메신저 연동** | ❌ | ❌ | ✅ 13개 |
| **음성 제어** | ❌ | ❌ | ✅ |
| **크론 자동화** | ❌ | ❌ | ✅ |
| **Projects 기능** | ✅ | ❌ | ❌ |
| **Artifacts** | ✅ | ❌ | ❌ |

### 🎨 비유로 이해하기

| 도구 | 비유 | 설명 |
|------|------|------|
| **Claude AI (웹)** | 📚 똑똑한 선생님 | 질문하면 답변해주고, 문서도 만들어줌 |
| **Claude Code** | 👨‍💻 개발자 동료 | 코드를 직접 작성하고, 파일도 수정해줌 |
| **OpenClaw** | 🤖 24시간 비서 | 메신저로 지시하면 알아서 일처리 |

---

## 2. 각 도구 상세 설명

### 🌐 Claude AI (웹) - claude.ai

#### 개요
```
접속: https://claude.ai
플랜: Free / Pro ($20/월) / Max ($100/월) / Team ($30/월)
특징: 브라우저에서 바로 사용, 가장 접근성 높음
```

#### 주요 기능

| 기능 | 설명 | 플랜 |
|------|------|------|
| **대화** | 일반적인 AI 채팅 | Free+ |
| **Projects** | 프로젝트별 컨텍스트 관리 | Pro+ |
| **Artifacts** | 코드/문서를 별도 패널로 생성 | Pro+ |
| **Code Execution** | Python 코드 실행 | Pro+ |
| **웹 검색** | 실시간 정보 검색 | Free+ |
| **파일 업로드** | PDF, 이미지, 코드 분석 | Free+ |
| **Extended Thinking** | 깊은 추론 모드 | Pro+ |

#### Bella의 활용법
```
✅ 문서 작성 (보고서, 가이드북)
✅ 지식 정리 및 학습
✅ 웹앱 서비스 설계 (기획 단계)
✅ Stitch 디자인 설계
✅ Projects로 프로젝트별 컨텍스트 관리
```

#### 장점 vs 한계

| 장점 | 한계 |
|------|------|
| ✅ 설치 없이 바로 사용 | ❌ 로컬 파일 직접 수정 불가 |
| ✅ Projects로 컨텍스트 관리 | ❌ 자동화 루틴 불가 |
| ✅ Artifacts로 시각적 결과물 | ❌ Git 작업 불가 |
| ✅ Extended Thinking 지원 | ❌ 24/7 상시 운영 불가 |

---

### 💻 Claude Code (CLI)

#### 개요
```
설치: npm install -g @anthropic-ai/claude-code
실행: claude (터미널에서)
특징: 코드 프로젝트에 특화, 파일 직접 편집
```

#### 주요 기능

| 기능 | 설명 |
|------|------|
| **파일 읽기/쓰기** | 프로젝트 파일 직접 수정 |
| **코드 생성** | 새 파일 생성, 리팩토링 |
| **Git 작업** | commit, push, PR 생성 |
| **터미널 명령** | npm, docker 등 실행 |
| **MCP 연동** | 외부 서비스 연결 |
| **Multi-agent** | 여러 에이전트 병렬 실행 |

#### Bella의 활용법
```
✅ 프로젝트별 개발 설계
  - D:\OzKiz_Global_Automation
  - D:\AI_coding_project_all\gangnam-beauty-website
  - D:\AI_coding_project_all\connect-k-platform
  - D:\AI_coding_project_all\k_info
  - D:\AI_coding_project_all\seoulmusttry

✅ 자동화 플로우 개발
  - D:\Obsidian_mcp_GPETers (MCP 연동)
  - D:\Claude_AI_Knowledge (지식 관리)

✅ 코드 리뷰 및 디버깅
✅ 문서 자동 생성 (README, 가이드)
```

#### 장점 vs 한계

| 장점 | 한계 |
|------|------|
| ✅ 로컬 파일 직접 편집 | ❌ 브라우저 제어 불가 |
| ✅ Git 완벽 통합 | ❌ 24/7 상시 운영 불가 |
| ✅ 터미널 명령 실행 | ❌ 메신저 연동 없음 |
| ✅ 무료 (API 비용만) | ❌ 터미널 친숙도 필요 |

---

### 🦞 OpenClaw (Personal AI Agent)

#### 개요
```
설치: npm install -g openclaw@latest
실행: npx openclaw tui
특징: 24시간 실행, 메신저 연동, 실제 작업 수행
```

#### 주요 기능

| 기능 | 설명 |
|------|------|
| **멀티채널** | WhatsApp, Telegram, Slack, Discord 등 13개 |
| **브라우저 제어** | 웹 자동화 (Playwright 기반) |
| **파일 작업** | 로컬 파일 읽기/쓰기 |
| **크론 스케줄** | 정기 작업 자동 실행 |
| **Skills** | Notion, Spotify, Gmail 등 연동 |
| **TUI/WebUI** | 터미널 또는 웹 대시보드 |
| **음성 제어** | macOS/iOS에서 음성 명령 |

#### 현재 활용 중인 기능 (Bella)
```
✅ TUI 채팅 (Claude와 대화)
✅ WhatsApp 연동 (핸드폰 → 컴퓨터)
```

#### 더 활용할 수 있는 기능
```
🔜 브라우저 자동화 (웹 스크래핑, 자동 로그인)
🔜 크론 자동화 (매일 아침 뉴스 요약)
🔜 Skills 연동 (Notion, Gmail)
🔜 Telegram 봇 (또 다른 채널)
🔜 Claude Code와 연계 (코드 작업 지시)
```

#### 장점 vs 한계

| 장점 | 한계 |
|------|------|
| ✅ 24/7 상시 운영 | ❌ 초기 설정 복잡 |
| ✅ 메신저로 어디서든 접근 | ❌ 서버/PC 상시 가동 필요 |
| ✅ 브라우저 제어 가능 | ❌ API 비용 발생 |
| ✅ 진정한 "행동하는 AI" | ❌ 보안 주의 필요 |

---

## 3. 사용 시나리오별 추천

### 📋 작업 유형별 최적 도구

| 작업 유형 | 추천 도구 | 이유 |
|----------|----------|------|
| 문서 작성 | Claude AI (웹) | Artifacts, Projects 활용 |
| 코드 개발 | Claude Code | 파일 직접 편집, Git 통합 |
| 24시간 자동화 | OpenClaw | 크론, 상시 운영 |
| 웹 자동화 | OpenClaw | 브라우저 제어 |
| 메신저 AI 비서 | OpenClaw | WhatsApp/Telegram 연동 |
| 빠른 질문 | Claude AI (웹) | 설치 없이 즉시 |
| 프로젝트 관리 | Claude AI (웹) | Projects 기능 |
| 이미지 분석 | Claude AI (웹) | Vision 기능 |
| 스마트홈 제어 | OpenClaw | Skills 연동 |

### 🎯 Bella의 워크플로우

```
┌─────────────────────────────────────────────────────────────┐
│                    Bella의 AI 워크플로우                     │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  [기획/설계 단계]                                           │
│       │                                                     │
│       ▼                                                     │
│  Claude AI (웹) ─────────────────────────────────────────┐  │
│  • 문서 작성                                              │  │
│  • 서비스 설계                                            │  │
│  • 지식 정리                                              │  │
│  • Stitch 디자인                                          │  │
│       │                                                   │  │
│       ▼                                                   │  │
│  [개발 단계]                                              │  │
│       │                                                   │  │
│       ▼                                                   │  │
│  Claude Code ─────────────────────────────────────────────┤  │
│  • 프로젝트 개발                                          │  │
│  • 자동화 플로우                                          │  │
│  • 코드 리뷰                                              │  │
│  • Git 관리                                               │  │
│       │                                                   │  │
│       ▼                                                   │  │
│  [운영/자동화 단계]                                       │  │
│       │                                                   │  │
│       ▼                                                   │  │
│  OpenClaw ────────────────────────────────────────────────┤  │
│  • 24/7 비서 운영                                         │  │
│  • WhatsApp 연동                                          │  │
│  • 정기 자동화                                            │  │
│  • 알림/보고                                              │  │
│                                                           │  │
└───────────────────────────────────────────────────────────┘
```

---

## 4. 도구 간 협업 시너지

### 🔗 협업 패턴 1: Claude AI → Claude Code

```
[시나리오] 새 웹앱 개발

1️⃣ Claude AI (웹)에서 기획
   "쇼핑몰 웹앱 기획서 작성해줘"
   → Projects에 저장
   → Artifacts로 와이어프레임 생성

2️⃣ Claude Code에서 개발
   "D:\AI_coding_project_all\new-shop에서
    방금 기획한 쇼핑몰 프로젝트 시작해줘"
   → 코드 생성, 파일 구조 설정

3️⃣ Claude Code에서 배포
   "Git commit하고 Vercel 배포해줘"
```

### 🔗 협업 패턴 2: Claude Code → OpenClaw

```
[시나리오] 개발 알림 자동화

1️⃣ Claude Code에서 개발 완료
   "빌드 완료되면 알림 스크립트 만들어줘"

2️⃣ OpenClaw가 알림 전송
   WhatsApp으로 "빌드 완료!" 메시지 받기

3️⃣ OpenClaw에서 추가 작업
   "배포 결과 확인하고 보고해줘"
```

### 🔗 협업 패턴 3: 전체 통합 워크플로우

```
[시나리오] 일일 업무 자동화

🌅 아침 (OpenClaw 크론)
├─ 뉴스 요약 → WhatsApp으로 전송
├─ 일정 확인 → 오늘 할 일 알림
└─ 이메일 체크 → 중요 메일 요약

📱 외출 중 (OpenClaw + WhatsApp)
├─ "오늘 회의 자료 정리해줘"
├─ "코드 리뷰 결과 알려줘"
└─ "서버 상태 확인해줘"

💻 작업 시 (Claude Code)
├─ 코드 개발
├─ 문서 작성
└─ Git 작업

📝 기획 시 (Claude AI 웹)
├─ 문서 작성
├─ 아이디어 정리
└─ Projects로 컨텍스트 관리

🌙 저녁 (OpenClaw 크론)
├─ 오늘 작업 요약
├─ 내일 할 일 정리
└─ 백업 실행
```

---

## 5. OpenClaw 심화 활용법

### 🦞 현재 vs 활용 가능한 기능

| 기능 | 현재 사용 | 활용 가능 |
|------|:--------:|:--------:|
| TUI 채팅 | ✅ | - |
| WhatsApp 연동 | ✅ | - |
| 브라우저 자동화 | ❌ | ✅ |
| 크론 자동화 | ❌ | ✅ |
| Skills (Notion) | ❌ | ✅ |
| Skills (Gmail) | ❌ | ✅ |
| Telegram 봇 | ❌ | ✅ |
| 음성 제어 | ❌ | ✅ (macOS) |

### 🌐 브라우저 자동화 활용

```bash
# 브라우저 설치
npx openclaw browser install

# 브라우저 시작
npx openclaw browser start
```

**활용 예시:**
```
💬 "네이버에서 '강남 맛집' 검색해서 상위 10개 정리해줘"
💬 "내 Gmail에서 읽지 않은 메일 요약해줘"
💬 "이 웹사이트에서 가격 정보 모아줘"
```

### ⏰ 크론 자동화 활용

```bash
# 크론 설정
npx openclaw cron add --name "morning-news" --schedule "0 8 * * *" --message "오늘 IT 뉴스 요약해줘"
```

**활용 예시:**
```
🌅 매일 아침 8시: 뉴스 요약 → WhatsApp 전송
📊 매주 월요일: 주간 업무 정리
🔄 매시간: 서버 상태 체크
```

### 🔌 Skills 활용

```bash
# Skills 목록 확인
npx openclaw skills list

# Notion 스킬 설치
npx openclaw skills install notion

# Gmail 스킬 설치
npx openclaw skills install himalaya
```

**활용 예시:**
```
💬 "Notion에 오늘 회의록 추가해줘"
💬 "Gmail에서 지난주 받은 뉴스레터 정리해줘"
💬 "Spotify에서 집중 플레이리스트 틀어줘"
```

### 📱 멀티채널 활용

```bash
# Telegram 봇 추가
npx openclaw configure --section channels
```

**채널별 용도:**
```
📱 WhatsApp: 개인 업무 (현재 사용 중)
💬 Telegram: 자동화 알림 전용
💼 Slack: 팀 협업 (필요시)
```

---

## 6. 실전 워크플로우 예시

### 📚 워크플로우 1: 블로그 포스팅 자동화

```
┌─────────────────────────────────────────────────────────────┐
│           블로그 포스팅 워크플로우                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1️⃣ 아이디어 정리 (Claude AI 웹)                           │
│     └─ Projects에 "블로그" 프로젝트 생성                   │
│     └─ "AI 트렌드 블로그 주제 5개 추천해줘"                │
│                                                             │
│  2️⃣ 초안 작성 (Claude AI 웹)                               │
│     └─ "OpenClaw 소개 글 작성해줘"                         │
│     └─ Artifacts로 마크다운 생성                           │
│                                                             │
│  3️⃣ 파일 저장 (Claude Code)                                │
│     └─ "D:\Blog\posts에 오늘 날짜로 저장해줘"              │
│     └─ Git commit                                          │
│                                                             │
│  4️⃣ 발행 알림 (OpenClaw)                                   │
│     └─ "블로그 발행 완료" WhatsApp 알림                    │
│     └─ SNS 공유 자동화 (선택)                              │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 💼 워크플로우 2: 프로젝트 개발 사이클

```
┌─────────────────────────────────────────────────────────────┐
│           프로젝트 개발 사이클                               │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  [기획] Claude AI 웹                                        │
│     └─ 요구사항 정리                                       │
│     └─ 기술 스택 결정                                      │
│     └─ 와이어프레임 (Artifacts)                            │
│             │                                               │
│             ▼                                               │
│  [개발] Claude Code                                         │
│     └─ 프로젝트 초기화                                     │
│     └─ 코드 작성                                           │
│     └─ 테스트 작성                                         │
│     └─ Git 관리                                            │
│             │                                               │
│             ▼                                               │
│  [모니터링] OpenClaw                                        │
│     └─ 빌드 상태 알림                                      │
│     └─ 에러 알림                                           │
│     └─ 일일 리포트                                         │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 🏠 워크플로우 3: 일상 자동화

```
┌─────────────────────────────────────────────────────────────┐
│           일상 자동화 (OpenClaw 중심)                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  🌅 아침 루틴 (크론 8:00)                                   │
│     ├─ 오늘 날씨 요약                                      │
│     ├─ 일정 확인                                           │
│     ├─ 뉴스 요약                                           │
│     └─ WhatsApp으로 전송                                   │
│                                                             │
│  📱 외출 중 (WhatsApp 명령)                                 │
│     ├─ "집 불 꺼줘" (스마트홈)                             │
│     ├─ "회의 자료 보내줘"                                  │
│     └─ "서버 상태 확인해줘"                                │
│                                                             │
│  🌙 저녁 루틴 (크론 22:00)                                  │
│     ├─ 오늘 할 일 완료 체크                                │
│     ├─ 내일 일정 미리보기                                  │
│     └─ 백업 실행                                           │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 7. 비용 비교 및 최적화

### 💰 도구별 비용

| 도구 | 비용 | 비고 |
|------|------|------|
| **Claude AI (웹)** | Free / $20 (Pro) / $100 (Max) | 구독제 |
| **Claude Code** | API 사용량 기반 | $3~15/1M 토큰 (Sonnet) |
| **OpenClaw** | API 사용량 기반 | 24/7 시 $30~100/월 예상 |

### 📊 월 비용 예상 (개인 사용자)

| 사용 패턴 | Claude AI | Claude Code | OpenClaw | 총합 |
|----------|-----------|-------------|----------|------|
| 가벼운 사용 | $20 (Pro) | $10 | $15 | ~$45/월 |
| 보통 사용 | $20 (Pro) | $30 | $40 | ~$90/월 |
| 무거운 사용 | $100 (Max) | $70 | $80 | ~$250/월 |

### 💡 비용 최적화 팁

```
1️⃣ 모델 선택 최적화
   • 간단한 작업: Haiku ($0.25/1M)
   • 일반 작업: Sonnet ($3/1M) ← 권장
   • 복잡한 작업: Opus ($15/1M)

2️⃣ OpenClaw 로컬 LLM 활용
   • Ollama + Llama 3.3 = 무료!
   • 간단한 자동화는 로컬 모델로

3️⃣ 캐싱 활용
   • Claude Code: 프롬프트 캐싱 활용
   • OpenClaw: 세션 메모리로 컨텍스트 재사용

4️⃣ 작업 분배
   • 문서 작업 → Claude AI (구독 내 무제한)
   • 코딩 작업 → Claude Code (API)
   • 자동화 → OpenClaw (API + 로컬)
```

---

## 8. 설치 및 설정 요약

### 📦 각 도구 설치 요약

#### Claude AI (웹)
```
1. https://claude.ai 접속
2. 계정 생성/로그인
3. (선택) Pro 플랜 구독
```

#### Claude Code
```bash
# 설치
npm install -g @anthropic-ai/claude-code

# 실행
claude

# 처음 실행 시 API 키 설정 또는 OAuth 로그인
```

#### OpenClaw
```bash
# 설치 (WSL Ubuntu에서)
npm install -g openclaw@latest

# 온보딩
npx openclaw onboard

# 실행
npx openclaw tui
```

### 🔑 API 키 관리

```
[API 키 발급처]
• Anthropic: https://console.anthropic.com/settings/keys
• OpenAI: https://platform.openai.com/api-keys

[저장 위치]
• Claude Code: 첫 실행 시 자동 설정
• OpenClaw: ~/.openclaw/agents/main/agent/auth-profiles.json
```

### 📁 주요 폴더 정리

```
D:\Claude_AI_Knowledge       ← Claude 관련 문서/가이드
D:\OpenClaw                  ← OpenClaw 프로젝트 폴더
D:\OpenClaw-MyGuides_BELLA   ← OpenClaw 개인 가이드 (GitHub)
D:\Obsidian_mcp_GPETers      ← MCP 연동 노트
D:\OzKiz_Global_Automation   ← 자동화 프로젝트
D:\AI_coding_project_all\    ← 개발 프로젝트들
```

---

## 9. FAQ

### Q1: 세 도구를 모두 써야 하나요?
```
아니요! 필요에 따라 선택하세요:
• 문서/기획만 → Claude AI (웹) 충분
• 코딩 중심 → Claude Code 추가
• 24/7 자동화 필요 → OpenClaw 추가
```

### Q2: OpenClaw vs Claude Code, 뭐가 다른가요?
```
• Claude Code: "내가 터미널에서 직접 지시"
• OpenClaw: "메신저로 언제 어디서든 지시 + 자동화"

Claude Code는 개발 작업에 특화,
OpenClaw는 24시간 비서 역할에 특화
```

### Q3: OpenClaw를 Claude Code처럼 코딩에 쓸 수 있나요?
```
네! 하지만 Claude Code가 더 적합해요.
• OpenClaw: 메신저로 "파일 수정해줘" 가능
• Claude Code: 터미널에서 직접 편집, Git 통합

코딩 = Claude Code, 자동화 = OpenClaw 권장
```

### Q4: 비용이 부담돼요. 무료로 쓸 수 있나요?
```
가능해요!
• Claude AI: Free 플랜 사용
• Claude Code: Ollama 로컬 모델 사용
• OpenClaw: Ollama 연동으로 무료 운영

단, 성능은 Claude API보다 낮을 수 있어요.
```

### Q5: Windows에서 OpenClaw 어떻게 쓰나요?
```
WSL2 (Ubuntu) 필수!
1. wsl --install -d Ubuntu
2. Ubuntu 터미널에서 npm install -g openclaw@latest
3. npx openclaw tui
```

---

## 참고 자료

### 공식 문서
- [Claude AI](https://claude.ai)
- [Claude Code](https://docs.anthropic.com/en/docs/claude-code)
- [OpenClaw Docs](https://docs.openclaw.ai)
- [OpenClaw GitHub](https://github.com/openclaw/openclaw)

### Bella의 가이드
- `D:\Claude_AI_Knowledge\01_Claude_Tools_Complete_Guide.md`
- `D:\Claude_AI_Knowledge\11_OpenClaw_Complete_Guide.md`
- `D:\OpenClaw-MyGuides_BELLA\OpenClaw_Beginner_Guide.md`

### 외부 참고
- [갓대희 블로그 - OpenClaw 설치 가이드](https://goddaehee.tistory.com/504)

---

*Made with Claude Code by Bella (OZKIZ) - 2026-02-05*
*For GPTers Study Group*
