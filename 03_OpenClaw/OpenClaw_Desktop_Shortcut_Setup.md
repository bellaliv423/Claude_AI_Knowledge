---
tags:
  - openclaw
  - windows
  - shortcut
  - desktop
---

# OpenClaw 바탕화면 바로가기 설정 가이드

> **목적:** Windows 바탕화면에서 더블클릭으로 OpenClaw TUI 실행
> **최종 수정:** 2026-02-24
> **작성자:** Bella + Claude Code
> **환경:** Windows 11 Home, WSL2 + Ubuntu, Node.js v22.17.0

---

## 1. 현재 작동하는 바로가기

### OpenClaw.bat

**경로:** `C:\Users\User\Desktop\OpenClaw.bat`

```bat
@echo off
title OpenClaw - Sonnet 4.6
wsl -e bash -c "source ~/.bashrc 2>/dev/null && npx openclaw tui"
pause
```

**기본 모델:** `claude-sonnet-4-6` (openclaw.json에서 설정됨)

---

## 2. 필수 환경

| 항목 | 버전/상태 | 확인 명령 |
|------|-----------|-----------|
| WSL2 + Ubuntu | Running, VERSION 2 | `wsl --list --verbose` |
| Node.js (WSL 내) | v22.17.0 | `wsl -e bash -c "node -v"` |
| OpenClaw (WSL 내) | 2026.2.2-3 | `wsl -e bash -c "npx openclaw --version"` |
| Anthropic API Key | 설정됨 | WSL `~/.bashrc` 또는 auth-profiles.json |

---

## 3. 모델 변경 방법

OpenClaw.bat에서 `--model` 옵션은 지원되지 않음. 설정 파일에서 변경:

```bash
# WSL Ubuntu에서 실행
npx openclaw config set agents.defaults.model.primary "anthropic/claude-sonnet-4-6"
```

또는 직접 편집:
```bash
nano ~/.openclaw/openclaw.json
```

```json
{
  "agents": {
    "defaults": {
      "model": {
        "primary": "anthropic/claude-sonnet-4-6"
      }
    }
  }
}
```

**사용 가능한 모델:**
| 모델 ID | 별칭 |
|----------|------|
| `anthropic/claude-opus-4-6` | opus |
| `anthropic/claude-sonnet-4-6` | sonnet |
| `anthropic/claude-haiku-4-5` | haiku |

---

## 4. 설정 과정에서 발생한 오류와 해결

### 오류 1: WSL 먹통 (아무 반응 없음)

**증상:** `wsl` 또는 `wsl --list --verbose` 입력 시 무응답
**원인:** WSL 서비스 멈춤
**해결:**
```powershell
# PowerShell에서
wsl --shutdown
# 5초 대기 후
wsl --list --verbose
```

안 되면 **컴퓨터 재부팅** (가장 확실)

### 오류 2: Windows Terminal 세미콜론 탭 분리

**증상:** `wt -p "Ubuntu" -- bash -c "cmd1; cmd2; cmd3"` 실행 시 여러 탭이 열림
**원인:** Windows Terminal이 `;`를 탭 구분자로 인식
**해결:** `wt` 대신 `wsl -e bash -c` 사용

```bat
:: 잘못된 방법 (탭이 쪼개짐)
wt -p "Ubuntu" -- bash -c "source ~/.bashrc; npx openclaw tui"

:: 올바른 방법
wsl -e bash -c "source ~/.bashrc 2>/dev/null && npx openclaw tui"
```

### 오류 3: `--model` 옵션 미지원

**증상:** `error: unknown option '--model'`
**원인:** OpenClaw TUI는 `--model` CLI 옵션을 지원하지 않음
**해결:** `~/.openclaw/openclaw.json`에서 모델 설정 (Section 3 참고)

### 오류 4: 401 API Key 에러

**증상:** TUI 실행 시 인증 실패
**해결:**
```bash
nano ~/.openclaw/agents/main/agent/auth-profiles.json
# "key" 값을 새 API 키로 교체
pkill -9 -f openclaw && npx openclaw tui
```

API 키 발급: https://console.anthropic.com/settings/keys

---

## 5. 초기 설치 (컴퓨터 초기화 시)

### Step 1: WSL2 + Ubuntu 설치
```powershell
wsl --install -d Ubuntu
# 재부팅 후 Ubuntu 초기 설정 (사용자명/비밀번호)
```

### Step 2: Node.js 설치 (WSL 내)
```bash
curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -
sudo apt-get install -y nodejs
node -v  # v22.x 확인
```

### Step 3: OpenClaw 설치 + 온보딩
```bash
npx openclaw onboard
# 안내에 따라 API 키 입력, 워크스페이스 설정
```

### Step 4: 바탕화면 바로가기 생성
`C:\Users\User\Desktop\OpenClaw.bat` 파일 생성:
```bat
@echo off
title OpenClaw - Sonnet 4.6
wsl -e bash -c "source ~/.bashrc 2>/dev/null && npx openclaw tui"
pause
```

### Step 5: 테스트
```powershell
# PowerShell에서 WSL 상태 확인
wsl --list --verbose
# NAME      STATE           VERSION
# * Ubuntu    Stopped         2

# OpenClaw 버전 확인
wsl -e bash -c "source ~/.bashrc 2>/dev/null && npx openclaw --version"
# 2026.2.2-3

# 바탕화면 OpenClaw.bat 더블클릭
```

---

## 6. 주요 파일 경로

| 파일 | 경로 |
|------|------|
| OpenClaw 설정 | `~/.openclaw/openclaw.json` (WSL) |
| API 키 (인증) | `~/.openclaw/agents/main/agent/auth-profiles.json` (WSL) |
| 워크스페이스 | `~/.openclaw/workspace` (WSL) |
| 바탕화면 바로가기 | `C:\Users\User\Desktop\OpenClaw.bat` |

---

*Last Updated: 2026-02-24*
*이 문서는 OpenClaw 바탕화면 바로가기 설정 및 트러블슈팅을 위해 작성되었습니다.*
