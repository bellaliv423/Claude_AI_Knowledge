---
tags:
  - claude
  - claude-code
  - cli
  - agent-sdk
  - v2
---

# Claude Code v2 완벽 가이드
# Claude Code v2 Complete Guide

> **작성일 / Created**: 2026-02-26
> **업데이트 / Updated**: 2026-02-26
> **버전 / Version**: 1.0
> **Author**: Bella (OZKIZ) + Claude (Opus 4.6)

---

## 목차 / Table of Contents

1. [소개 / Introduction](#소개--introduction)
2. [v2.0 주요 변경 / v2.0 Major Changes](#v20-주요-변경--v20-major-changes)
3. [새로운 명령어 / New Commands](#새로운-명령어--new-commands)
4. [단축키 & UI / Shortcuts & UI](#단축키--ui--shortcuts--ui)
5. [Claude Agent SDK](#claude-agent-sdk)
6. [Skills 시스템 / Skills System](#skills-시스템--skills-system)
7. [Hooks 시스템 / Hooks System](#hooks-시스템--hooks-system)
8. [v2.1.x 업데이트 / v2.1.x Updates](#v21x-업데이트--v21x-updates)
9. [설정 & 커스터마이징 / Configuration](#설정--커스터마이징--configuration)
10. [실전 워크플로우 / Practical Workflows](#실전-워크플로우--practical-workflows)
11. [FAQ](#faq)
12. [참고 자료 / References](#참고-자료--references)

---

## 소개 / Introduction

**Claude Code v2**는 Anthropic의 공식 CLI(Command Line Interface) 도구의 대규모 업데이트입니다. 새로운 UI, Agent SDK, Skills 시스템 등 다양한 기능이 추가되었습니다.

| 항목 | 내용 |
|------|------|
| **v2.0 출시** | 2025년 하반기 |
| **최신 버전** | v2.1.x (2026-02 기준) |
| **설치** | `npm install -g @anthropic-ai/claude-code` |
| **실행** | `claude` |
| **호환** | macOS, Linux, Windows (WSL/Git Bash) |

### v1 → v2 주요 변화 요약

| 영역 | v1 | v2 |
|------|----|----|
| **UI** | 기본 터미널 | 새로운 VS Code 확장 + 개선된 TUI |
| **SDK** | Claude Code SDK | **Claude Agent SDK** (이름 변경) |
| **도구 관리** | 정적 | Skills + Hooks 지원 |
| **컨텍스트** | 수동 관리 | 자동 Compaction + Thinking 토글 |
| **히스토리** | 기본 | Ctrl+R 검색 + 세션 재개 |
| **명령어** | 기본 | `/rewind`, `/usage`, `/debug`, `/teleport` 추가 |

---

## v2.0 주요 변경 / v2.0 Major Changes

### 1. 새로운 VS Code 확장

Claude Code v2는 VS Code와 더 깊이 통합됩니다:

```
VS Code Extension 기능:
├── 인라인 코드 편집 제안
├── 파일 diff 미리보기
├── 터미널 내장 Claude Code 패널
├── 사이드바에서 대화 관리
└── 도구 호출 시각화
```

### 2. Claude Agent SDK (이름 변경)

```
이전: Claude Code SDK
현재: Claude Agent SDK

변경 사항:
├── 패키지: @anthropic-ai/claude-code-sdk → @anthropic-ai/claude-agent-sdk
├── 커스텀 에이전트 빌딩 지원 강화
├── 다중 에이전트 오케스트레이션
└── 프로그래밍 방식으로 Claude Code 사용
```

### 3. Context Compaction

긴 대화에서 자동으로 컨텍스트를 압축합니다:

```
동작 방식:
1. 대화가 컨텍스트 한도에 도달
2. 이전 메시지를 자동 요약
3. 핵심 정보만 보존
4. 대화를 끊김 없이 계속

= 무한 대화 길이 (실질적)
```

### 4. Adaptive Thinking (Opus 4.6)

```
Opus 4.6의 Adaptive Thinking:
├── 간단한 질문 → 짧은 thinking
├── 복잡한 문제 → 깊은 thinking
├── Tab 키로 thinking 표시 토글 (sticky)
└── 세션 내 thinking 설정 유지
```

---

## 새로운 명령어 / New Commands

### `/rewind` - 코드 변경 취소

```bash
# Claude Code 내에서:
/rewind

# 동작:
# 1. Claude가 한 마지막 코드 변경을 되돌림
# 2. Git 기반으로 안전하게 롤백
# 3. 여러 번 호출 가능 (여러 단계 되돌리기)
```

### `/usage` - 사용량 확인

```bash
# Claude Code 내에서:
/usage

# 표시 내용:
# - 현재 플랜 (Pro/Max)
# - 남은 메시지 수
# - 토큰 사용량
# - 리셋 시간
```

### `/debug` - 세션 디버깅

```bash
# Claude Code 내에서:
/debug

# 동작:
# - 현재 세션 상태 표시
# - 에러 로그 확인
# - MCP 연결 상태 진단
# - 환경 설정 검증
```

### `/teleport` - 세션 이동

```bash
# Claude Code 내에서:
/teleport

# 동작:
# - 현재 CLI 세션을 claude.ai/code 웹으로 이동
# - 대화 컨텍스트 유지
# - 브라우저에서 이어서 작업 가능
```

### `/help` - 도움말

```bash
/help

# 모든 명령어와 단축키 표시
```

### 기타 슬래시 명령어

| 명령어 | 설명 |
|--------|------|
| `/clear` | 대화 초기화 |
| `/compact` | 수동 컨텍스트 압축 |
| `/config` | 설정 열기 |
| `/cost` | 비용 정보 |
| `/doctor` | 환경 진단 |
| `/fast` | Fast mode 토글 (동일 모델, 빠른 출력) |
| `/init` | CLAUDE.md 초기화 |
| `/login` | 로그인 |
| `/logout` | 로그아웃 |
| `/model` | 모델 변경 |
| `/permissions` | 권한 설정 |
| `/pr` | PR 생성 |
| `/review` | 코드 리뷰 |

---

## 단축키 & UI / Shortcuts & UI

### 키보드 단축키

| 단축키 | 동작 |
|--------|------|
| **Tab** | Thinking 표시 토글 (sticky) |
| **Ctrl+R** | 히스토리 검색 |
| **Shift+Enter** | 줄바꿈 (설정 불필요) |
| **Ctrl+C** | 현재 작업 중단 |
| **Ctrl+D** | 세션 종료 |
| **Esc** | 현재 작업 취소 |

### Thinking 토글 (Tab 키)

```
Tab 키 동작:
├── 첫 번째 Tab: Thinking 블록 표시/숨기기 토글
├── "Sticky" 설정: 세션 내 선택 유지
├── Thinking 표시 시: 추론 과정 실시간 확인 가능
└── Thinking 숨기기 시: 결과만 표시 (깔끔한 출력)
```

### 히스토리 검색 (Ctrl+R)

```
Ctrl+R 기능:
├── 이전 대화/명령어 검색
├── 키워드 기반 필터링
├── 세션 재개 가능
└── 최근 세션 목록 표시
```

### 세션 재개

```bash
# 이전 세션 이어서 시작
claude --resume

# 특정 세션 ID로 재개
claude --resume <session-id>

# PR 기반 세션 재개 (v2.1+)
claude --from-pr 123
claude --from-pr https://github.com/owner/repo/pull/123
```

---

## Claude Agent SDK

### 개요 / Overview

**Claude Agent SDK** (이전 Claude Code SDK)는 Claude Code의 기능을 프로그래밍 방식으로 사용할 수 있게 해주는 SDK입니다.

### 설치

```bash
npm install @anthropic-ai/claude-agent-sdk
```

### 기본 사용법

```typescript
import { ClaudeAgent } from '@anthropic-ai/claude-agent-sdk';

const agent = new ClaudeAgent({
  model: 'claude-opus-4-6',
  workingDirectory: './my-project'
});

// 단일 작업 실행
const result = await agent.run('이 프로젝트의 버그를 찾아서 수정해줘');
console.log(result.output);
console.log(result.filesModified);
```

### 커스텀 에이전트 구축

```typescript
import { ClaudeAgent } from '@anthropic-ai/claude-agent-sdk';

// 코드 리뷰 에이전트
const reviewAgent = new ClaudeAgent({
  model: 'claude-opus-4-6',
  systemPrompt: `당신은 시니어 코드 리뷰어입니다.
  보안 취약점, 성능 이슈, 코드 스타일을 검토합니다.`,
  tools: ['Read', 'Glob', 'Grep'],  // 읽기 전용 도구만
  maxTurns: 10
});

const review = await reviewAgent.run('src/ 폴더의 코드를 리뷰해줘');
```

### 다중 에이전트 오케스트레이션

```typescript
import { ClaudeAgent, AgentOrchestrator } from '@anthropic-ai/claude-agent-sdk';

// 전문 에이전트 정의
const planner = new ClaudeAgent({
  model: 'claude-opus-4-6',
  systemPrompt: '작업을 분석하고 실행 계획을 세웁니다.',
  tools: ['Read', 'Glob', 'Grep']
});

const coder = new ClaudeAgent({
  model: 'claude-opus-4-6',
  systemPrompt: '계획에 따라 코드를 작성합니다.',
  tools: ['Read', 'Write', 'Edit', 'Bash']
});

const tester = new ClaudeAgent({
  model: 'claude-sonnet-4-6',
  systemPrompt: '작성된 코드를 테스트합니다.',
  tools: ['Read', 'Bash']
});

// 오케스트레이션
const orchestrator = new AgentOrchestrator([planner, coder, tester]);
const result = await orchestrator.run('로그인 기능을 구현해줘');
```

---

## Skills 시스템 / Skills System

### 개요

Skills는 Claude Code에 특정 작업을 수행하는 재사용 가능한 지침을 추가하는 시스템입니다.

### Skill 구조

```markdown
---
name: code-review
description: 코드 리뷰를 수행합니다
model: claude-opus-4-6
tools: [Read, Glob, Grep]
hooks:
  on_start: echo "리뷰 시작"
  on_complete: echo "리뷰 완료"
---

# 코드 리뷰 스킬

다음 기준으로 코드를 리뷰합니다:
1. 보안 취약점
2. 성능 이슈
3. 코드 가독성
4. 테스트 커버리지

## 출력 형식
- 심각도: Critical / High / Medium / Low
- 파일: 해당 파일 경로
- 설명: 이슈 상세 설명
- 제안: 개선 방안
```

### Skill 호출

```bash
# Claude Code 내에서 / 로 스킬 호출
/code-review src/

# 또는 대화 중 자연어로
"src/ 폴더를 코드 리뷰해줘"
```

### Skill 특징 (v2.1+)

```
Skills v2.1 기능:
├── Forked context: 스킬이 별도 컨텍스트에서 실행
├── Hot reload: 스킬 파일 변경 시 자동 반영
├── Custom agents: 스킬 내에서 커스텀 에이전트 정의
├── Frontmatter hooks: 스킬에 직접 hooks 추가
└── 도구 제한: 스킬별로 사용 가능한 도구 설정
```

---

## Hooks 시스템 / Hooks System

### 개요

Hooks는 Claude Code의 특정 이벤트에 셸 명령을 연결하는 시스템입니다.

### Hook 이벤트

| 이벤트 | 시점 | 용도 |
|--------|------|------|
| `pre_tool_call` | 도구 호출 전 | 검증, 로깅 |
| `post_tool_call` | 도구 호출 후 | 결과 처리 |
| `on_notification` | 알림 발생 시 | 사용자 통보 |
| `on_error` | 에러 발생 시 | 에러 처리 |

### 설정 방법

```json
// .claude/settings.json
{
  "hooks": {
    "pre_tool_call": [
      {
        "matcher": "Edit|Write",
        "command": "echo 'File modification detected: $TOOL_INPUT'"
      }
    ],
    "post_tool_call": [
      {
        "matcher": "Bash",
        "command": "echo 'Command executed: $TOOL_INPUT' >> ~/.claude/audit.log"
      }
    ]
  }
}
```

### 실전 예제: 자동 린트

```json
{
  "hooks": {
    "post_tool_call": [
      {
        "matcher": "Edit|Write",
        "command": "npx eslint --fix $TOOL_FILE 2>/dev/null || true"
      }
    ]
  }
}
```

---

## v2.1.x 업데이트 / v2.1.x Updates

### `--from-pr` 플래그

```bash
# PR 번호로 세션 시작
claude --from-pr 123

# PR URL로 세션 시작
claude --from-pr https://github.com/owner/repo/pull/123

# PR 생성 시 자동 세션 연결
/pr  # PR 생성 → 세션 자동 연결
```

### 응답 언어 설정

```bash
# 설정에서 언어 변경
/config

# 또는 환경 변수
export CLAUDE_RESPONSE_LANGUAGE=ko  # 한국어
export CLAUDE_RESPONSE_LANGUAGE=ja  # 일본어
export CLAUDE_RESPONSE_LANGUAGE=es  # 스페인어
```

### 도구 권한 와일드카드

```json
// .claude/settings.json
{
  "permissions": {
    "allow": [
      "Bash(*-h*)",         // -h 플래그 포함 명령 허용
      "Bash(npm test*)",    // npm test 허용
      "Read(*)",            // 모든 파일 읽기 허용
      "Edit(src/**)"        // src/ 하위만 편집 허용
    ]
  }
}
```

### Claude in Chrome Beta

```bash
# Chrome 브라우저 제어 활성화
claude --chrome

# 웹 자동화 예시:
# "이 웹페이지의 폼을 채워줘"
# "로그인 후 대시보드 스크린샷 찍어줘"
# "이 웹앱의 E2E 테스트를 실행해줘"
```

### PDF 향상

```bash
# 특정 페이지 범위 읽기
# Claude Code 내에서:
"report.pdf의 5~10페이지만 읽어줘"

# API에서:
# Read tool에 pages 파라미터 추가
# pages: "1-5", "3", "10-20"
```

### 기타 v2.1.x 개선

| 기능 | 설명 |
|------|------|
| **mTLS/프록시** | 기업 네트워크 지원 |
| **OAuth 토큰** | 만료 처리 수정 |
| **커스텀 스피너** | `spinnerVerbs` 설정 가능 |
| **일본어 IME** | 전각 스페이스 지원 |
| **MCP OAuth** | `--client-id`, `--client-secret` 옵션 |
| **Sandbox 수정** | "Read-only file system" 오류 해결 |

---

## 설정 & 커스터마이징 / Configuration

### CLAUDE.md 파일

```markdown
# CLAUDE.md - 프로젝트 설정

## 프로젝트 규칙
- TypeScript 사용
- ESLint + Prettier 적용
- 테스트 커버리지 80% 이상

## 코딩 스타일
- 함수명: camelCase
- 컴포넌트: PascalCase
- 상수: UPPER_SNAKE_CASE

## 금지 사항
- console.log 사용 금지 (logger 사용)
- any 타입 사용 금지
```

### 설정 파일 위치

```
~/.claude/
├── settings.json      # 글로벌 설정
├── permissions.json   # 권한 설정
├── hooks/             # 글로벌 hooks
└── skills/            # 글로벌 skills

프로젝트/
├── CLAUDE.md          # 프로젝트별 설정
├── .claude/
│   ├── settings.json  # 프로젝트별 설정
│   ├── hooks/         # 프로젝트별 hooks
│   └── skills/        # 프로젝트별 skills
```

### 주요 설정 옵션

```json
// .claude/settings.json
{
  "model": "claude-opus-4-6",
  "maxTurns": 50,
  "responseLanguage": "ko",
  "spinnerVerbs": ["생각 중", "분석 중", "코딩 중"],
  "permissions": {
    "allow": ["Read(*)", "Glob(*)", "Grep(*)"],
    "deny": ["Bash(rm -rf*)"]
  },
  "hooks": { ... }
}
```

---

## 실전 워크플로우 / Practical Workflows

### 워크플로우 1: 프로젝트 초기화

```bash
# 1. 프로젝트 디렉토리에서 시작
cd my-project

# 2. CLAUDE.md 초기화
claude
/init

# 3. 프로젝트 구조 설명
"이 Next.js 프로젝트의 구조를 분석하고 CLAUDE.md를 작성해줘"
```

### 워크플로우 2: 버그 수정

```bash
# 1. 이슈 기반 세션
claude

# 2. 버그 설명
"GitHub Issue #42의 버그를 수정해줘. 사용자가 로그인 후 리다이렉트되지 않는 문제야"

# 3. 수정 확인 후 PR 생성
/pr
```

### 워크플로우 3: 코드 리뷰 + PR

```bash
# 1. PR 기반 세션
claude --from-pr 123

# 2. 리뷰
"이 PR의 변경 사항을 리뷰하고 개선점을 제안해줘"

# 3. 문제 있으면 직접 수정
"제안한 개선점을 직접 적용해줘"
```

### 워크플로우 4: 대규모 리팩토링

```bash
claude

# Plan Mode로 시작
"src/legacy/ 폴더를 TypeScript로 마이그레이션하고 싶어. 계획을 세워줘"

# 계획 확인 후 실행
"계획대로 진행해줘"

# 중간에 문제 시 되돌리기
/rewind
```

---

## FAQ

### Q1: Claude Code를 업데이트하려면?

```bash
npm update -g @anthropic-ai/claude-code
```

### Q2: CLAUDE.md는 Git에 커밋해야 하나요?

팀 프로젝트라면 커밋을 권장합니다. 팀원 모두가 같은 컨텍스트로 Claude를 사용할 수 있습니다.

### Q3: Windows에서 사용 가능한가요?

WSL(Windows Subsystem for Linux) 또는 Git Bash를 통해 사용 가능합니다. 네이티브 PowerShell에서도 동작하지만 일부 제한이 있습니다 (`$_` 변수 치환 등).

### Q4: 오프라인에서 사용 가능한가요?

Claude Code는 Anthropic API에 연결이 필요합니다. 오프라인 사용은 불가능합니다.

### Q5: Max 플랜과 Pro 플랜의 차이는?

Max 플랜은 더 많은 메시지 수, 더 긴 컨텍스트, 우선 처리를 제공합니다. `/usage`로 현재 사용량을 확인하세요.

### Q6: Agent SDK와 Claude Code는 별개인가요?

Agent SDK는 Claude Code의 기능을 프로그래밍 방식으로 사용하게 해주는 라이브러리입니다. Claude Code CLI 위에 구축됩니다.

---

## 참고 자료 / References

### 공식 자료
- [Claude Code 공식 문서](https://docs.anthropic.com/en/docs/claude-code)
- [Claude Code CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)
- [Claude Agent SDK](https://github.com/anthropics/claude-code)
- [Claude Code VS Code Extension](https://marketplace.visualstudio.com/items?itemName=anthropics.claude-code)

### 이 프로젝트의 관련 문서
- [01_Claude_Tools_Complete_Guide.md](./01_Claude_Tools_Complete_Guide.md) - 도구 종합 가이드
- [04_Claude_Skills_Guide.md](./04_Claude_Skills_Guide.md) - Skills 가이드
- [Boris_Cherny_Claude_Code_Best_Practices.md](../05_Best_Practices/Boris_Cherny_Claude_Code_Best_Practices.md) - 베스트 프랙티스

---

## 업데이트 로그 / Changelog

| 날짜 | 버전 | 내용 |
|------|------|------|
| 2026-02-26 | v1.0 | 초기 버전 작성 |

---

*Made with Claude by Bella (OZKIZ)*
