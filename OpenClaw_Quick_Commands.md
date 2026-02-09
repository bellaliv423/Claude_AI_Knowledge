# OpenClaw 빠른 실행 가이드 / Quick Commands

> **Last Updated**: 2026-02-04
> **GitHub**: https://github.com/bellaliv423/Claude_AI_Knowledge

---

## 터미널별 실행 명령어 / Commands by Terminal

### 1. Ubuntu 탭 (Windows Terminal) - 권장 ⭐

```bash
# TUI 실행 (대화 모드)
source ~/.bashrc && npx openclaw tui

# Gateway만 실행 (백그라운드 서비스)
source ~/.bashrc && npx openclaw gateway --port 18789

# 상태 확인
npx openclaw doctor

# WhatsApp 메시지 전송
npx openclaw message send --target '+821097805690' --message '메시지 내용'
```

### 2. PowerShell / CMD

```powershell
# WSL 진입 후 실행 (권장)
wsl
source ~/.bashrc && npx openclaw tui

# 한 줄로 실행 (TUI 화면 깨질 수 있음)
wsl -e bash -c "source ~/.bashrc && npx openclaw tui"

# Gateway 시작 (백그라운드)
wsl -e bash -c "source ~/.bashrc && npx openclaw gateway --port 18789 &"

# 메시지 전송 (TUI 없이)
wsl -e bash -c "source ~/.bashrc && npx openclaw message send --target '+821097805690' --message '메시지'"
```

### 3. Claude Code에서 요청

Claude Code에서 아래처럼 요청하면 됩니다:
- "OpenClaw 켜줘"
- "OpenClaw Gateway 시작해줘"
- "WhatsApp으로 메시지 보내줘"

---

## 명령어 요약표 / Command Summary

| 작업 | Ubuntu 탭 | PowerShell/CMD |
|------|-----------|----------------|
| **TUI 실행** | `source ~/.bashrc && npx openclaw tui` | `wsl` → 같은 명령어 |
| **Gateway 시작** | `npx openclaw gateway --port 18789` | `wsl -e bash -c "npx openclaw gateway"` |
| **상태 확인** | `npx openclaw doctor` | `wsl -e bash -c "npx openclaw doctor"` |
| **메시지 전송** | `npx openclaw message send --target '번호' --message '내용'` | `wsl -e bash -c "..."` |
| **프로세스 종료** | `pkill -f openclaw` | `wsl -e bash -c "pkill -f openclaw"` |

---

## 자주 쓰는 명령어 (복사용) / Copy-Paste Commands

### TUI 실행 (가장 많이 사용)
```bash
source ~/.bashrc && npx openclaw tui
```

### Gateway + TUI 동시 실행
```bash
source ~/.bashrc && npx openclaw gateway --port 18789 & sleep 3 && npx openclaw tui
```

### 모든 프로세스 종료 후 재시작
```bash
pkill -f openclaw; sleep 2; source ~/.bashrc && npx openclaw tui
```

---

## 문제 해결 / Troubleshooting

| 문제 | 해결 방법 |
|------|----------|
| TUI 화면이 안 보임 | Ubuntu 탭 사용 또는 `wsl` 진입 후 실행 |
| HTTP 401 에러 | `source ~/.bashrc` 실행 후 재시도 |
| Gateway 연결 실패 | `pkill -f openclaw` 후 재시작 |
| WhatsApp 연결 끊김 | `npx openclaw doctor`로 상태 확인 |

---

## 환경 설정 파일 위치 / Config Locations

| 파일 | 경로 | 용도 |
|------|------|------|
| API 키 | `~/.bashrc` | ANTHROPIC_API_KEY 환경변수 |
| OpenClaw 설정 | `~/.openclaw/openclaw.json` | 전체 설정 |
| 백업용 .env | `D:\Claude_AI_Knowledge\.env` | API 키 백업 (Git 제외) |

---

## 참고 / Notes

- **Ubuntu 탭**이 가장 안정적입니다
- Gateway는 TUI 실행 시 자동으로 시작됩니다
- API 키 문제 시 `source ~/.bashrc` 먼저 실행하세요
