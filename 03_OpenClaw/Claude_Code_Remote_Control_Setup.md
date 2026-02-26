---
tags:
  - claude-code
  - remote-control
  - setup
  - mobile
  - 2026
---

# Claude Code Remote Control 설치 & 활용 가이드
# Claude Code Remote Control Setup & Usage Guide

> **작성일**: 2026-02-26
> **환경**: Windows 11 + Claude Code v2.1.59
> **구독**: Claude Max ($100/월)
> **Author**: Bella (OZKIZ) + Claude Opus 4.6

---

## 목차

1. [Remote Control이란?](#1-remote-control이란)
2. [요구사항](#2-요구사항)
3. [설치 과정 (실제 기록)](#3-설치-과정-실제-기록)
4. [사용 방법](#4-사용-방법)
5. [자동 활성화 설정](#5-자동-활성화-설정)
6. [보안 모델](#6-보안-모델)
7. [Remote Control vs Claude Code on the Web](#7-remote-control-vs-claude-code-on-the-web)
8. [활용 시나리오](#8-활용-시나리오)
9. [제한사항 & 문제 해결](#9-제한사항--문제-해결)
10. [참고 자료](#10-참고-자료)

---

## 1. Remote Control이란?

> 내 PC에서 돌아가는 Claude Code 세션을 **스마트폰/태블릿/다른 PC 브라우저**에서 원격으로 조작하는 기능

### 핵심 개념

```
┌──────────────┐                    ┌──────────────────┐
│   내 PC      │   ← TLS 암호화 →   │  폰/태블릿/브라우저 │
│  Claude Code │   Anthropic API    │  (리모컨 역할)     │
│  (본체)       │                    │                    │
└──────────────┘                    └──────────────────┘
```

- **PC가 본체**: 파일 수정, 테스트 실행, Git 등 모든 작업은 PC에서 실행
- **폰은 리모컨**: 지시를 내리고 결과를 확인하는 "창" 역할
- **클라우드 아님**: 코드와 파일이 클라우드로 전송되지 않음

### Claude Code on the Web와의 차이

| 항목 | Remote Control | Claude Code on the Web |
|------|---------------|----------------------|
| 실행 위치 | **내 PC** (로컬) | Anthropic 클라우드 |
| 파일 접근 | 로컬 파일시스템 직접 | 클라우드 환경 (GitHub 연동) |
| MCP 서버 | 로컬 MCP 그대로 사용 | 사용 불가 |
| 사용 시점 | 진행 중인 작업을 이어갈 때 | 새 작업을 빠르게 시작할 때 |
| 병렬 작업 | 1개 세션만 | 여러 세션 동시 가능 |

---

## 2. 요구사항

| 항목 | 조건 | 확인 방법 |
|------|------|----------|
| **구독 플랜** | Pro 또는 Max (API 키 불가) | claude.ai에서 확인 |
| **Claude Code 버전** | v2.1.52 이상 | `claude --version` |
| **인증** | claude.ai 로그인 완료 | `/login` |
| **워크스페이스 신뢰** | 프로젝트에서 1회 이상 실행 | 해당 디렉토리에서 `claude` 실행 |
| **Claude 앱 (선택)** | iOS 또는 Android | 앱스토어에서 설치 |

### 현재 지원 범위 (2026-02-26 기준)

| 플랜 | 지원 여부 |
|------|----------|
| Free | ✕ |
| Pro | ✅ (곧 지원 예정, 현재 일부) |
| Max / Max+ | ✅ 완전 지원 |
| Team | ✕ (아직 미지원) |
| Enterprise | ✕ (아직 미지원) |

---

## 3. 설치 과정 (실제 기록)

### 실제 환경
- Windows 11 Home
- Claude Code v2.1.59
- Claude Max 플랜 (huang 계정)
- 2026-02-26 설정

### Step 1: Claude Code 실행

```bash
# 터미널 (PowerShell 또는 CMD)에서
claude
```

화면 확인:
```
╭─── Claude Code v2.1.59 ─────────────────────────╮
│         Welcome back 벨라!                       │
│   Opus 4.6 · Claude Max · huang                 │
╰──────────────────────────────────────────────────╯
```

### Step 2: 로그인 확인

```
❯ /login
  ⎿  Login successful
```

이미 로그인되어 있으면 "Login successful" 또는 "Already logged in" 메시지가 나옵니다.

### Step 3: Remote Control 시작

```
❯ /remote-control
  ⎿  (no content)

  /remote-control is active. Code in CLI or at
  https://claude.ai/code/session_019hs4E6TkgwH4UiKE71tbzs
```

> **참고**: `/rc`를 입력하면 "Unknown skill: rc" 에러가 발생할 수 있습니다.
> `/remote-control` 전체 명령어를 사용하세요.

### Step 4: 폰에서 연결

**방법 A: URL 직접 열기**
- 터미널에 표시된 URL을 복사하여 브라우저에서 열기

**방법 B: QR 코드 스캔**
- 스페이스바를 누르면 QR 코드가 나타남
- Claude 모바일 앱으로 스캔

**방법 C: Claude 앱에서 찾기**
1. Claude 앱 열기
2. Code 탭 (또는 세션 목록) 확인
3. 세션 이름 옆에 **초록 점** = 온라인 상태
4. 터치하여 연결

### Step 5: 연결 확인

폰에서 메시지를 보내면 PC 터미널에서도 동시에 대화가 표시됩니다.
양방향 동기화가 정상 작동하면 성공!

---

## 4. 사용 방법

### 기본 명령어

| 명령어 | 위치 | 설명 |
|--------|------|------|
| `/remote-control` | Claude Code 세션 안 | 현재 세션을 원격 제어로 전환 |
| `/rc` | Claude Code 세션 안 | 위와 동일 (축약, 버전에 따라 미지원) |
| `claude remote-control` | 쉘 (터미널) | 새 원격 제어 세션 시작 |
| `/rename "이름"` | Claude Code 세션 안 | 세션 이름 지정 (원격에서 찾기 쉬움) |
| `/mobile` | Claude Code 세션 안 | 모바일 앱 다운로드 QR 코드 |

### 쉘에서 직접 시작 (새 세션)

```bash
# 프로젝트 디렉토리에서
cd D:\AI_coding_project_all\Claude_Smart_Korea
claude remote-control

# 옵션
claude remote-control --verbose        # 상세 로그
claude remote-control --sandbox        # 샌드박싱 활성화
claude remote-control --no-sandbox     # 샌드박싱 비활성화
```

### 기존 세션에서 전환

```
# Claude Code 대화 중에
/rename "마케팅 프로젝트"
/remote-control
```

→ 세션 이름이 "마케팅 프로젝트"로 표시되어 폰에서 찾기 쉬움

### 연결 후 사용

| 폰에서 입력 | PC에서 일어나는 일 |
|------------|-------------------|
| "이 파일 수정해줘" | PC의 실제 파일이 수정됨 |
| "npm test 실행해줘" | PC에서 테스트 실행됨 |
| "git commit하고 push 해줘" | PC에서 실제로 Git 작업 |
| "빌드 에러 수정해줘" | PC에서 에러 분석 & 수정 |

---

## 5. 자동 활성화 설정

매번 `/remote-control` 치기 귀찮을 때:

```
/config
→ "Enable Remote Control for all sessions" → true
```

이후 Claude Code를 실행할 때마다 자동으로 Remote Control이 활성화됩니다.

비활성화하려면:
```
/config
→ "Enable Remote Control for all sessions" → false
```

---

## 6. 보안 모델

### 통신 구조

```
내 PC (Claude Code)
    │
    ├── 아웃바운드 HTTPS만 사용
    │   (인바운드 포트 열지 않음!)
    │
    ▼
Anthropic API (TLS 암호화)
    │
    ├── 메시지 중계
    │
    ▼
폰/브라우저 (원격 접속)
```

### 보안 특징

| 항목 | 설명 |
|------|------|
| **인바운드 포트** | 열지 않음 — PC가 외부에 노출되지 않음 |
| **통신 암호화** | TLS (Anthropic API 경유, 일반 Claude Code와 동일) |
| **인증 토큰** | 단기 수명, 용도별 분리 (하나가 유출되어도 제한적) |
| **파일 처리** | 로컬에서만 — 코드/파일이 클라우드로 전송되지 않음 |
| **MCP 서버** | 로컬에서만 실행 — 원격으로 접근 불가 |

### 안전하게 사용하기

1. ✅ 공공 Wi-Fi에서도 사용 가능 (TLS 암호화)
2. ✅ VPN 불필요 (아웃바운드만 사용)
3. ⚠️ 세션 URL을 다른 사람과 공유하지 마세요
4. ⚠️ 외출 시 PC 잠금 화면 설정 권장

---

## 7. Remote Control vs Claude Code on the Web

| 기능 | Remote Control | Claude Code on the Web |
|------|---------------|----------------------|
| **실행 환경** | 내 PC (로컬) | Anthropic 클라우드 |
| **로컬 파일** | ✅ 직접 접근 | ✕ (GitHub만) |
| **MCP 서버** | ✅ 로컬 MCP 유지 | ✕ |
| **프로젝트 설정** | ✅ 그대로 유지 | 별도 설정 필요 |
| **병렬 세션** | 1개만 | 여러 개 동시 |
| **PC 필요** | ✅ (켜져있어야 함) | ✕ (클라우드) |
| **시작 속도** | 빠름 (기존 세션 이어감) | 환경 셋업 필요 |
| **추천 상황** | 작업 중 자리 비울 때 | 새 작업/빠른 시작 |

### 언제 어떤 것을 사용할까?

- **Remote Control**: "집에서 시작한 작업을 카페에서 이어갈 때"
- **Claude Code on the Web**: "노트북 없이 폰만으로 새 작업 시작할 때"
- **Teleport**: 웹 세션 ↔ 로컬 세션 간 전환 가능

---

## 8. 활용 시나리오

### 시나리오 1: 출근길 코딩

```
1. 집에서 Claude Code 실행 → /remote-control
2. 지하철에서 폰으로 연결
3. "어제 작업하던 API 엔드포인트 마저 구현해줘"
4. 회사 도착 → PC에서 결과 확인
```

### 시나리오 2: 회의 중 모니터링

```
1. 미팅 전 Claude Code에서 긴 작업 시작
2. 회의 중 폰으로 진행 상황 확인
3. 필요시 "테스트 추가해줘" 지시
4. 회의 끝나면 PC에서 결과 리뷰
```

### 시나리오 3: 카페 작업

```
1. 집 PC에서 remote-control 활성화
2. 카페에서 노트북 브라우저로 claude.ai/code 접속
3. 집 PC의 프로젝트를 그대로 이어서 작업
4. 로컬 MCP 서버, 환경변수 모두 사용 가능
```

### 시나리오 4: 고객 대응

```
1. OpenClaw + WhatsApp으로 고객 문의 수신
2. 복잡한 기술 문의 → Remote Control로 코드 확인
3. 폰에서 "이 에러 원인 분석해줘" 지시
4. 답변 준비되면 고객에게 전달
```

---

## 9. 제한사항 & 문제 해결

### 제한사항

| 제한 | 설명 |
|------|------|
| 동시 세션 | 1개만 가능 |
| 터미널 종료 | 터미널 닫으면 세션 종료 |
| 네트워크 타임아웃 | 10분 이상 네트워크 끊기면 세션 종료 |
| 절전 모드 | PC 절전 시 연결 끊김 (깨어나면 자동 재연결) |
| Team/Enterprise | 아직 미지원 |

### 문제 해결

| 문제 | 해결 방법 |
|------|----------|
| `/rc` → "Unknown skill" | `/remote-control` 전체 명령어 사용 |
| 연결이 안 됨 | PC가 켜져있고 Claude Code가 실행 중인지 확인 |
| QR 코드가 안 보임 | 스페이스바를 눌러 QR 토글 |
| 폰에서 세션이 안 보임 | claude.ai/code에서 직접 URL 접속 |
| "Login successful" 후 안 됨 | Claude Code 업데이트: `npm update -g @anthropic-ai/claude-code` |
| 자꾸 끊김 | PC 절전 모드 비활성화, `--verbose`로 로그 확인 |

### 절전 방지 설정 (Windows)

```
설정 → 시스템 → 전원 및 배터리 → 화면 및 절전
→ "절전 모드" → "안 함"으로 설정
```

---

## 10. 참고 자료

### 공식 문서
- [Remote Control 공식 문서](https://code.claude.com/docs/en/remote-control)
- [Claude Code CLI Reference](https://code.claude.com/docs/en/cli-reference)
- [Claude Code 보안](https://code.claude.com/docs/en/security)

### 뉴스 & 리뷰
- [Simon Willison - Claude Code Remote Control](https://simonwillison.net/2026/Feb/25/claude-code-remote-control/)
- [VentureBeat - Anthropic releases mobile Claude Code](https://venturebeat.com/orchestration/anthropic-just-released-a-mobile-version-of-claude-code-called-remote)
- [MacStories - Hands-On with Remote Control](https://www.macstories.net/stories/hands-on-with-claude-code-remote-control/)

### 관련 가이드 (이 폴더 내)
- [OpenClaw + Claude 최신 기능 종합 가이드](./13_OpenClaw_Claude_Latest_Features_2026.md)
- [OpenClaw 완전 가이드](./11_OpenClaw_Complete_Guide.md)

---

## 업데이트 로그

| 날짜 | 내용 |
|------|------|
| 2026-02-26 | v1.0 초기 작성 — 실제 설치 기록 포함 |

---

*Made with Claude Opus 4.6 by Bella (OZKIZ)*
