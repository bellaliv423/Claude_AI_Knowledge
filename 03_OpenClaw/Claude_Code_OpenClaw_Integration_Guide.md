# Claude Code + OpenClaw 통합 활용 완전 가이드

> **작성일**: 2026-02-27 | **OpenClaw**: v2026.2.2-3 | **Claude Code**: v2.1.62
> **목적**: Claude Code에서 OpenClaw을 직접 호출하여 WhatsApp 메시지/파일 전송, 에이전트 대화, 크론 자동화, 브라우저 제어 등을 수행하는 완전 가이드

---

## 0. 사전 준비 (매 세션 1회)

### 0-1. Gateway 시작
```bash
# Claude Code에서 실행 (백그라운드)
wsl -d Ubuntu -- bash -c "source ~/.bashrc 2>/dev/null && npx openclaw gateway"
```

### 0-2. Gateway 상태 확인
```bash
wsl -d Ubuntu -- bash -c "curl -s -o /dev/null -w '%{http_code}' http://localhost:18789/"
# 200이면 정상
```

### 0-3. WhatsApp 연결 확인
```bash
wsl -d Ubuntu -- bash -c "source ~/.bashrc 2>/dev/null && npx openclaw channels status 2>&1"
# whatsapp: linked 확인
```

> **WhatsApp이 끊어진 경우**: 별도 터미널에서 `wsl -d Ubuntu` → `npx openclaw channels login --channel whatsapp --account default` → QR 코드 스캔

### 0-4. 한 줄 체크 (Claude가 세션 시작 시 실행)
```bash
wsl -d Ubuntu -- bash -c "source ~/.bashrc 2>/dev/null && curl -s -o /dev/null -w '%{http_code}' http://localhost:18789/ && echo ' Gateway OK' || echo 'Gateway DOWN'"
```

---

## 1. 기본 명령어 모음

### 1-1. WhatsApp 메시지 보내기
```bash
wsl -d Ubuntu -- bash -c "source ~/.bashrc 2>/dev/null && npx openclaw message send -t '+821097805690' -m '보낼 메시지 내용'"
```

### 1-2. WhatsApp 파일 첨부 보내기
```bash
# Windows 경로를 WSL 경로로 변환 필요: D:\path\file → /mnt/d/path/file
wsl -d Ubuntu -- bash -c "source ~/.bashrc 2>/dev/null && npx openclaw message send -t '+821097805690' -m '파일 설명' --media '/mnt/d/경로/파일명'"
```

### 1-3. 에이전트 대화 (OpenClaw AI에게 질문)
```bash
# 기본 대화 (결과를 터미널에 출력)
wsl -d Ubuntu -- bash -c "source ~/.bashrc 2>/dev/null && npx openclaw agent --to '+821097805690' --message '질문 내용' --json"

# 결과를 WhatsApp으로 직접 전송
wsl -d Ubuntu -- bash -c "source ~/.bashrc 2>/dev/null && npx openclaw agent --to '+821097805690' --message '질문 내용' --deliver"

# 세션 유지 대화 (맥락 이어감)
wsl -d Ubuntu -- bash -c "source ~/.bashrc 2>/dev/null && npx openclaw agent --session-id 'my-session' --message '이전 대화 이어서 질문' --json"
```

### 1-4. 메시지 읽기 (WhatsApp 수신 메시지 확인)
```bash
wsl -d Ubuntu -- bash -c "source ~/.bashrc 2>/dev/null && npx openclaw message read --help 2>&1"
```

### 1-5. 메시지 검색
```bash
wsl -d Ubuntu -- bash -c "source ~/.bashrc 2>/dev/null && npx openclaw message search --help 2>&1"
```

---

## 2. 자동 발송 도구 (auto_deliver.py)

### 위치
`D:\Claude_AI_Knowledge\tools\auto_deliver.py`

### 사용법
```bash
# 업무 이메일 (bella@ozkiz.com)
python D:/Claude_AI_Knowledge/tools/auto_deliver.py --file "파일경로" --to work

# 개인 이메일 (kndli.210@gmail.com)
python D:/Claude_AI_Knowledge/tools/auto_deliver.py --file "파일경로" --to personal

# 이메일 둘 다
python D:/Claude_AI_Knowledge/tools/auto_deliver.py --file "파일경로" --to both

# WhatsApp 파일 첨부 발송
python D:/Claude_AI_Knowledge/tools/auto_deliver.py --file "파일경로" --to whatsapp

# 이메일 + WhatsApp 전부
python D:/Claude_AI_Knowledge/tools/auto_deliver.py --file "파일경로" --to all
```

---

## 3. 크론 자동화 (정기 작업)

### 3-1. 매일 아침 브리핑 (예: 매일 08:00 KST)
```bash
wsl -d Ubuntu -- bash -c "source ~/.bashrc 2>/dev/null && npx openclaw cron add \
  --name 'morning-briefing' \
  --description '매일 아침 브리핑' \
  --cron '0 8 * * *' \
  --tz 'Asia/Seoul' \
  --message '오늘 날씨와 주요 뉴스를 간단히 요약해줘. 한국어로.' \
  --deliver \
  --to '+821097805690' \
  --channel whatsapp"
```

### 3-2. 주간 업무 리마인더 (매주 월요일 09:00)
```bash
wsl -d Ubuntu -- bash -c "source ~/.bashrc 2>/dev/null && npx openclaw cron add \
  --name 'weekly-reminder' \
  --description '주간 업무 리마인더' \
  --cron '0 9 * * 1' \
  --tz 'Asia/Seoul' \
  --message '이번 주 OZKIZ 업무 체크리스트를 정리해줘' \
  --deliver \
  --to '+821097805690' \
  --channel whatsapp"
```

### 3-3. 크론 관리 명령어
```bash
# 목록 확인
wsl -d Ubuntu -- bash -c "source ~/.bashrc 2>/dev/null && npx openclaw cron list"

# 즉시 실행 (테스트용)
wsl -d Ubuntu -- bash -c "source ~/.bashrc 2>/dev/null && npx openclaw cron run --name 'morning-briefing'"

# 비활성화
wsl -d Ubuntu -- bash -c "source ~/.bashrc 2>/dev/null && npx openclaw cron disable --name 'morning-briefing'"

# 활성화
wsl -d Ubuntu -- bash -c "source ~/.bashrc 2>/dev/null && npx openclaw cron enable --name 'morning-briefing'"

# 삭제
wsl -d Ubuntu -- bash -c "source ~/.bashrc 2>/dev/null && npx openclaw cron rm --name 'morning-briefing'"

# 실행 이력
wsl -d Ubuntu -- bash -c "source ~/.bashrc 2>/dev/null && npx openclaw cron runs --name 'morning-briefing'"
```

---

## 4. 비즈니스 활용 시나리오

### 4-1. OZKIZ 고객 응대 자동화
```bash
# 고객 문의 요약 요청
wsl -d Ubuntu -- bash -c "source ~/.bashrc 2>/dev/null && npx openclaw agent \
  --session-id 'ozkiz-cs' \
  --message '최근 WhatsApp 고객 문의 내용을 요약하고 긴급한 건이 있으면 알려줘' \
  --deliver --to '+821097805690' --channel whatsapp"
```

### 4-2. 파일 생성 후 자동 배포
Claude Code에서 문서/프레젠테이션 작업 완료 후:
```bash
# 이메일 + WhatsApp 동시 발송
python D:/Claude_AI_Knowledge/tools/auto_deliver.py --file "D:/작업폴더/완성파일.pptx" --to all
```

### 4-3. 마케팅 콘텐츠 전달
```bash
# 이미지/영상 WhatsApp 전송 (50MB 이하)
wsl -d Ubuntu -- bash -c "source ~/.bashrc 2>/dev/null && npx openclaw message send \
  -t '+821097805690' \
  -m '[마케팅] 새 SNS 콘텐츠 확인해주세요' \
  --media '/mnt/d/Marketing/content.jpg'"
```

### 4-4. 일일 매출/재고 보고서 자동화
```bash
wsl -d Ubuntu -- bash -c "source ~/.bashrc 2>/dev/null && npx openclaw cron add \
  --name 'daily-sales-report' \
  --description '일일 매출 요약' \
  --cron '0 20 * * *' \
  --tz 'Asia/Seoul' \
  --message '오늘 OZKIZ 업무 마감 체크리스트: 주문 처리 상태, 내일 출고 예정, 고객 문의 미처리 건을 정리해줘' \
  --deliver --to '+821097805690' --channel whatsapp"
```

### 4-5. SNS/소셜 운영 도우미
```bash
# 인스타그램 캡션 생성 요청
wsl -d Ubuntu -- bash -c "source ~/.bashrc 2>/dev/null && npx openclaw agent \
  --session-id 'social-media' \
  --message '아기 봄 외출복 신상품 인스타그램 캡션 3개 만들어줘. 해시태그 포함. 한국어+영어' \
  --json"

# 결과를 WhatsApp으로 전달
wsl -d Ubuntu -- bash -c "source ~/.bashrc 2>/dev/null && npx openclaw agent \
  --session-id 'social-media' \
  --message '위 캡션 중 1번을 수정해서 보내줘' \
  --deliver --to '+821097805690' --channel whatsapp"
```

---

## 5. 고급 기능

### 5-1. 브라우저 제어 (웹 자동화)
```bash
# 브라우저 시작
wsl -d Ubuntu -- bash -c "source ~/.bashrc 2>/dev/null && npx openclaw browser start"

# URL 열기
wsl -d Ubuntu -- bash -c "source ~/.bashrc 2>/dev/null && npx openclaw browser open 'https://example.com'"

# 스크린샷 캡처
wsl -d Ubuntu -- bash -c "source ~/.bashrc 2>/dev/null && npx openclaw browser screenshot"

# 페이지 스냅샷 (AI 분석용)
wsl -d Ubuntu -- bash -c "source ~/.bashrc 2>/dev/null && npx openclaw browser snapshot"
```

### 5-2. 메모리 검색 (OpenClaw이 기억하는 내용)
```bash
# 의미 검색
wsl -d Ubuntu -- bash -c "source ~/.bashrc 2>/dev/null && npx openclaw memory search '고객 응대 방법'"

# 메모리 인덱싱
wsl -d Ubuntu -- bash -c "source ~/.bashrc 2>/dev/null && npx openclaw memory index"
```

### 5-3. 날씨 확인 (ready 스킬)
```bash
wsl -d Ubuntu -- bash -c "source ~/.bashrc 2>/dev/null && npx openclaw agent \
  --message '서울 오늘 날씨 알려줘' --json"
```

### 5-4. Gateway 비용 확인
```bash
wsl -d Ubuntu -- bash -c "source ~/.bashrc 2>/dev/null && npx openclaw gateway usage-cost"
```

### 5-5. 진단 (문제 발생 시)
```bash
wsl -d Ubuntu -- bash -c "source ~/.bashrc 2>/dev/null && npx openclaw doctor"
```

---

## 6. 현재 사용 가능한 스킬 (8/50)

| 스킬 | 설명 | 활용 |
|------|------|------|
| coding-agent | Claude Code/Codex 연동 | 코딩 작업 위임 |
| weather | 날씨 조회 | 아침 브리핑에 포함 |
| openai-image-gen | 이미지 생성 | 마케팅 콘텐츠 제작 |
| openai-whisper-api | 음성 → 텍스트 | 음성 메모 변환 |
| skill-creator | 커스텀 스킬 제작 | 나만의 자동화 만들기 |
| healthcheck | 보안 점검 | 시스템 상태 확인 |
| tmux | 원격 세션 제어 | 장시간 작업 관리 |
| bluebubbles | BlueBubbles 플러그인 | iMessage 연동 |

---

## 7. Windows 경로 → WSL 경로 변환 규칙

| Windows | WSL |
|---------|-----|
| `D:\Claude_AI_Knowledge\file.pdf` | `/mnt/d/Claude_AI_Knowledge/file.pdf` |
| `C:\Users\User\Desktop\file.pptx` | `/mnt/c/Users/User/Desktop/file.pptx` |

**규칙**: `드라이브:\` → `/mnt/드라이브소문자/`, `\` → `/`

---

## 8. 트러블슈팅

### Gateway가 안 뜰 때
```bash
# 1. 기존 프로세스 정리
wsl -d Ubuntu -- bash -c "pkill -f 'openclaw gateway' 2>/dev/null; rm -f ~/.openclaw/.gateway.lock"
# 2. 재시작
wsl -d Ubuntu -- bash -c "source ~/.bashrc 2>/dev/null && npx openclaw gateway"
```

### WhatsApp 메시지가 안 갈 때
```bash
# 채널 상태 확인
wsl -d Ubuntu -- bash -c "source ~/.bashrc 2>/dev/null && npx openclaw channels status"
# linked가 아니면 재로그인 필요 (QR 스캔)
```

### systemctl 오류 (WSL 환경)
WSL에서 `systemctl --user` 미지원 → Gateway는 항상 포그라운드/nohup으로 실행
```bash
# nohup 방식 (터미널 닫아도 유지)
wsl -d Ubuntu -- bash -c "nohup npx openclaw gateway > /tmp/oc-gw.log 2>&1 &"
```

---

## 9. Claude Code 프롬프트 템플릿

### 파일 완성 → 자동 발송
> "이 파일을 완성했으면 auto_deliver.py로 이메일과 WhatsApp 모두 보내줘"

### 아침 브리핑 크론 등록
> "매일 아침 8시에 날씨+오늘 할 일 브리핑을 WhatsApp으로 보내는 크론 등록해줘"

### OpenClaw 에이전트에게 질문 전달
> "OpenClaw에게 '오늘 고객 문의 요약해줘'라고 전달하고 결과를 WhatsApp으로 보내줘"

### SNS 콘텐츠 생성
> "OZKIZ 신상품 인스타 캡션 만들어서 WhatsApp으로 보내줘"

### Gateway 시작
> "OpenClaw Gateway 시작하고 상태 확인해줘"

---

## 10. 주요 설정 정보

| 항목 | 값 |
|------|-----|
| OpenClaw 버전 | 2026.2.2-3 |
| Gateway 포트 | 18789 |
| Gateway 토큰 | `0a9cb4b74379f11f6cb3cb51eccf5cf7b5732728cfb872e4` |
| 기본 모델 | anthropic/claude-sonnet-4-6 |
| 에이전트 이름 | 貝拉 (Bella) |
| WhatsApp 번호 | +821097805690 |
| WhatsApp 정책 | allowlist (허용 목록 방식) |
| 미디어 최대 크기 | 50MB |
| 최대 동시 에이전트 | 4 |
| 메모리 임베딩 | OpenAI text-embedding-3-small |
| 설정 파일 | `~/.openclaw/openclaw.json` (WSL 내) |
| auto_deliver.py | `D:\Claude_AI_Knowledge\tools\auto_deliver.py` |

---

## 부록: 향후 확장 가능한 스킬 (설치 시 사용 가능)

| 스킬 | 용도 | OZKIZ 활용 |
|------|------|-----------|
| github | GitHub 이슈/PR 관리 | claude-smart-korea 프로젝트 |
| himalaya | 이메일 CLI | 고객 이메일 자동 응답 |
| notion | Notion 연동 | 업무 문서 관리 |
| trello | Trello 보드 관리 | 프로젝트 태스크 추적 |
| slack | Slack 연동 | 팀 커뮤니케이션 |
| bird (Twitter/X) | 트위터 자동화 | SNS 마케팅 |
| summarize | URL/영상 요약 | 콘텐츠 리서치 |
| nano-pdf | PDF 편집 | 문서 자동 편집 |
| gog (Google Workspace) | Gmail/Calendar/Drive | 일정 + 파일 관리 |
