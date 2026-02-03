# OpenClaw Setup Log - 2026-02-03
# OpenClaw 설치 기록

> **Date**: 2026-02-03
> **Environment**: Windows 11 + WSL2 Ubuntu
> **OpenClaw Version**: 2026.2.1 (ed4529e)
> **Author**: Bella (OZKIZ)

---

## 설치 환경 / Installation Environment

| 항목 | 값 |
|------|-----|
| OS | Windows 10.0.26100.7623 |
| WSL | Ubuntu (WSL2) |
| Node.js | v22+ |
| 설치 방법 | `npm install -g openclaw@latest` |

---

## 온보딩 설정 내용 / Onboarding Configuration

### 1. 기본 설정 (QuickStart)

```
Gateway port: 18789
Gateway bind: Loopback (127.0.0.1)
Gateway auth: Token (default)
Tailscale exposure: Off
```

### 2. AI 모델 설정

| 항목 | 설정값 |
|------|--------|
| Provider | Anthropic |
| Auth method | Anthropic API key |
| Default model | `anthropic/claude-sonnet-4-5` |

### 3. 채널 설정 (WhatsApp)

```
Channel: WhatsApp (QR link)
WhatsApp DM Policy: allowlist
Personal phone: +821097805690
allowFrom: ["+821097805690"]
```

**WhatsApp 연결 과정:**
1. QR 코드 스캔 (WhatsApp > Linked Devices)
2. 연결 후 자동 재시작 (code 515)
3. Web session ready 확인

### 4. 스킬 설정

```
Eligible skills: 7
Missing requirements: 42
Blocked by allowlist: 0
```

**설치 시도한 스킬:**
- wacli (WhatsApp CLI) - 실패 (brew not installed)

**스킵한 API 키 설정:**
- GOOGLE_PLACES_API_KEY (goplaces) - No
- GOOGLE_PLACES_API_KEY (local-places) - No
- GEMINI_API_KEY (nano-banana-pro) - No
- NOTION_API_KEY (notion) - No
- ELEVENLABS_API_KEY (sag) - No

### 5. Hooks 설정

**사용 가능한 Hooks:**
- boot-md - 부팅 시 MD 파일 로드
- command-logger - 명령어 로깅
- session-memory - 세션 메모리 저장

**설정**: (진행 중)

---

## 생성된 파일 / Created Files

```
~/.openclaw/
├── openclaw.json          # 메인 설정 파일
├── workspace/             # 작업 디렉토리
├── credentials/
│   └── whatsapp/
│       └── default/       # WhatsApp 인증 정보
└── agents/
    └── main/
        └── sessions/      # 세션 저장소
```

---

## 설정 파일 예시 / Configuration Example

`~/.openclaw/openclaw.json`:
```json
{
  "gateway": {
    "port": 18789,
    "bind": "127.0.0.1",
    "auth": {
      "mode": "token"
    }
  },
  "model": {
    "provider": "anthropic",
    "default": "anthropic/claude-sonnet-4-5"
  },
  "channels": {
    "whatsapp": {
      "dmPolicy": "allowlist",
      "allowFrom": ["+821097805690"]
    }
  }
}
```

---

## 다음 단계 / Next Steps

1. [ ] Hooks 설정 완료 (Skip for now 또는 선택)
2. [ ] 온보딩 완료
3. [ ] Gateway 시작: `npx openclaw gateway`
4. [ ] WhatsApp 테스트 메시지 전송
5. [ ] (선택) Homebrew 설치 후 추가 스킬 설치

---

## 유용한 명령어 / Useful Commands

```bash
# Gateway 시작
npx openclaw gateway --port 18789 --verbose

# 상태 확인
npx openclaw doctor

# 보안 감사
npx openclaw security audit --deep

# 메시지 전송 테스트
npx openclaw message send --to +821097805690 --message "Hello from OpenClaw"

# 에이전트 실행
npx openclaw agent --message "오늘 할 일 정리해줘"
```

---

## 문제 해결 기록 / Troubleshooting Log

| 문제 | 원인 | 해결 |
|------|------|------|
| wacli 설치 실패 | Homebrew 미설치 | 나중에 brew 설치 후 재시도 |
| npm 모듈 오류 (Windows) | npm 손상 | WSL2로 전환 |
| **HTTP 401 authentication_error** | **API 키 무효** | **아래 해결 방법 참조** |

---

## 현재 상태 (2026-02-03 저녁) / Current Status

**설치 완료된 것:**
- OpenClaw 2026.2.1 설치됨
- WhatsApp 연결됨 (+821097805690)
- Gateway 서비스 설치됨
- TUI 실행 가능

**해결 필요한 문제:**
```
HTTP 401 authentication_error: invalid x-api-key
```

**집에서 해야 할 것:**

### Step 1: 새 API 키 발급
1. https://platform.claude.com 접속
2. Settings > API Keys
3. 새 키 생성 (기존 키 삭제 권장)

### Step 2: API 키 설정
```bash
# WSL 터미널에서
wsl
npx openclaw config set anthropic.apiKey "sk-ant-새로운키"
```

### Step 3: 테스트
```bash
npx openclaw tui
# TUI에서 메시지 입력 테스트
```

---

## 참고 / References

- [OpenClaw Docs](https://docs.openclaw.ai)
- [OpenClaw GitHub](https://github.com/openclaw/openclaw)
- [WhatsApp Channel Docs](https://docs.openclaw.ai/channels/whatsapp)
- [Security Guide](https://docs.openclaw.ai/gateway/security)

---

*Made with Claude by Bella (OZKIZ)*
