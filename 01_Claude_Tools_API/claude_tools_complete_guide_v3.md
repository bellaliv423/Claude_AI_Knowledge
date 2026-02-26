---
tags:
  - claude
  - tools
  - api
  - v3
  - comprehensive
---

# 🛠️ Claude 도구 종합 가이드 v3.0
# Claude Tools Complete Guide v3.0

> **작성자**: Bella (OZKIZ)
> **작성일**: 2026-01-30
> **버전**: v3.0  
> **용도**: 모든 Claude 도구 및 기능의 설정, 활용, 프롬프트 완벽 정리

---

## 📋 목차

1. [도구 호환성 매트릭스](#1-도구-호환성-매트릭스)
2. [Claude 환경별 특징](#2-claude-환경별-특징)
3. [Server Tools (서버 도구)](#3-server-tools-서버-도구)
4. [Client Tools (클라이언트 도구)](#4-client-tools-클라이언트-도구)
5. [Capabilities (기능)](#5-capabilities-기능)
6. [SDK 기능 및 베타 기능](#6-sdk-기능-및-베타-기능)
7. [실전 프롬프트 모음](#7-실전-프롬프트-모음)
8. [문제 해결 가이드](#8-문제-해결-가이드)

---

# 1. 도구 호환성 매트릭스

## 🎯 환경별 도구/기능 사용 가능 여부

### Tools (도구)

| 도구 | Claude Web | Claude Desktop | Claude Code | Claude Chrome | API |
|------|:----------:|:--------------:|:-----------:|:-------------:|:---:|
| **Web Search** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Web Fetch** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Code Execution** | ✅ Pro+ | ✅ Pro+ | ❌ | ❌ | ✅ |
| **Computer Use** | ❌ | ✅ | ❌ | ✅ | ✅ |
| **Text Editor** | ❌ | ✅ | ✅ | ❌ | ✅ |
| **Bash Tool** | ❌ | ✅ | ✅ | ❌ | ✅ |
| **Memory Tool** | ✅ | ✅ | ✅ | ❌ | ✅ |
| **MCP Connector** | ❌ | ✅ | ✅ | ❌ | ✅ |

### Capabilities (기능)

| 기능 | Claude Web | Claude Desktop | Claude Code | Claude Chrome | API |
|------|:----------:|:--------------:|:-----------:|:-------------:|:---:|
| **PDF Support** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Vision (이미지)** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Streaming** | ✅ | ✅ | ✅ | ✅ | ✅ | 🆕
| **Extended Thinking** | ✅ | ✅ | ✅ | ❌ | ✅ | 🆕
| **Files API** | ❌ | ❌ | ❌ | ❌ | ✅ |
| **Prompt Caching** | ❌ | ❌ | ❌ | ❌ | ✅ |
| **Batch Processing** | ❌ | ❌ | ❌ | ❌ | ✅ |
| **Structured Outputs** | ❌ | ❌ | ❌ | ❌ | ✅ |
| **Citations** | ❌ | ❌ | ❌ | ❌ | ✅ |
| **Multilingual** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Search Results** | ❌ | ❌ | ❌ | ❌ | ✅ |
| **Embeddings** | ❌ | ❌ | ❌ | ❌ | ⚠️ 외부 |
| **Token Counting** | ❌ | ❌ | ❌ | ❌ | ✅ 🆓 |

### SDK/베타 기능

| 기능 | Claude Web | Claude Desktop | Claude Code | Claude Chrome | API |
|------|:----------:|:--------------:|:-----------:|:-------------:|:---:|
| **Tool Runner** | ❌ | ❌ | ❌ | ❌ | ✅ SDK |
| **Fine-grained Streaming** | ❌ | ❌ | ❌ | ❌ | ✅ Beta |
| **Strict Tool Use** | ❌ | ❌ | ❌ | ❌ | ✅ |
| **Effort** | ❌ | ❌ | ❌ | ❌ | ✅ Beta 🆕 |
| **Context Editing** | ❌ | ❌ | ❌ | ❌ | ✅ Beta 🆕 |

### 📌 범례
- ✅ = 사용 가능
- ❌ = 사용 불가
- ✅ Pro+ = Pro 이상 플랜 필요 ($20/월)
- ✅ SDK = SDK 설치 필요
- ✅ Beta = 베타 헤더 필요
- ⚠️ 외부 = Anthropic 제공 안 함 (외부 서비스 사용)
- 🆓 = 무료
- 🆕 = v3.0에서 새로 추가

---

# 2. Claude 환경별 특징

## 🌐 Claude Web (claude.ai)

| 항목 | 내용 |
|------|------|
| **접속 방법** | https://claude.ai |
| **필요 조건** | 계정 생성 |
| **플랜** | Free / Pro ($20) / Team ($30) |
| **주요 기능** | 대화, 파일 업로드, 웹 검색, Code Execution (Pro+), PDF, 이미지, Streaming |
| **제한** | Computer Use, Bash Tool 사용 불가 |

### 설정 방법
1. https://claude.ai 접속
2. 계정 생성/로그인
3. 설정 → 기능 활성화 (Web Search, Artifacts 등)

### 지원 파일 형식
```
📄 문서: PDF, DOCX, TXT, MD, HTML
📊 데이터: CSV, XLSX, JSON
🖼️ 이미지: PNG, JPG, JPEG, GIF, WEBP
💻 코드: PY, JS, TS, 등 대부분 코드 파일
```

---

## 🖥️ Claude Desktop

| 항목 | 내용 |
|------|------|
| **다운로드** | https://claude.ai/download |
| **지원 OS** | Windows, macOS |
| **주요 기능** | 모든 기능 + Computer Use + MCP + Extended Thinking |
| **특징** | 로컬 파일 접근, 시스템 통합 |

### 설치 방법

**Windows:**
```bash
# 1. 다운로드 페이지에서 설치 파일 다운로드
# 2. Claude-Setup.exe 실행
# 3. 설치 완료 후 로그인
```

**macOS:**
```bash
# 1. 다운로드 페이지에서 DMG 파일 다운로드
# 2. Claude.app을 Applications 폴더로 이동
# 3. 실행 후 로그인
```

### MCP 설정 (고급)
```json
// macOS: ~/Library/Application Support/Claude/claude_desktop_config.json
// Windows: %APPDATA%\Claude\claude_desktop_config.json

{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/folder"]
    }
  }
}
```

---

## 💻 Claude Code (CLI)

| 항목 | 내용 |
|------|------|
| **설치** | `npm install -g @anthropic-ai/claude-code` |
| **용도** | 터미널에서 코딩 작업 자동화 |
| **주요 기능** | 파일 편집, Bash 명령, 코드 생성 |

### 설치 방법
```bash
# Node.js 필요 (v18+)
npm install -g @anthropic-ai/claude-code

# API 키 설정
export ANTHROPIC_API_KEY="sk-ant-api03-..."

# 사용
claude-code "이 프로젝트의 README 작성해줘"
```

### 주요 명령어
```bash
# 기본 사용
claude-code "요청 내용"

# 파일 지정
claude-code --file main.py "이 코드 리팩토링해줘"

# 대화 모드
claude-code --interactive

# 모델 지정
claude-code --model claude-sonnet-4-5 "요청"
```

---

## 🌐 Claude Chrome Extension

| 항목 | 내용 |
|------|------|
| **설치** | Chrome Web Store에서 설치 |
| **용도** | 브라우저 자동화, 웹 페이지 분석 |
| **주요 기능** | Computer Use, 페이지 읽기, 클릭 자동화 |

### 설치 방법
1. Chrome Web Store에서 "Claude" 검색
2. "Chrome에 추가" 클릭
3. 확장 프로그램에서 Claude 아이콘 클릭
4. Anthropic 계정으로 로그인

### 주요 사용법
```
"이 페이지 요약해줘"
"로그인 버튼 클릭해줘"
"이 양식 작성해줘"
"이 페이지의 모든 링크 추출해줘"
```

---

## 🔧 Claude API

| 항목 | 내용 |
|------|------|
| **접속** | https://console.anthropic.com |
| **용도** | 프로그래밍 방식으로 Claude 사용 |
| **가격** | 토큰 기반 과금 |

### 설정 방법

**1. API 키 발급**
```
1. https://console.anthropic.com 접속
2. API Keys 메뉴
3. "Create Key" 클릭
4. 키 이름 입력 후 생성
5. 키 복사 (한 번만 표시됨!)
```

**2. 환경 변수 설정**

Windows (PowerShell):
```powershell
# 임시 설정
$env:ANTHROPIC_API_KEY = "sk-ant-api03-..."

# 영구 설정
[System.Environment]::SetEnvironmentVariable("ANTHROPIC_API_KEY", "sk-ant-api03-...", "User")
```

macOS/Linux:
```bash
# ~/.bashrc 또는 ~/.zshrc에 추가
export ANTHROPIC_API_KEY="sk-ant-api03-..."

# 적용
source ~/.bashrc
```

**3. SDK 설치**
```bash
# Python
pip install anthropic

# Node.js
npm install @anthropic-ai/sdk

# Ruby
gem install anthropic
```

---

# 3. Server Tools (서버 도구)

> Anthropic 서버에서 실행되는 도구. 개발자가 구현할 필요 없음!

---

## 🔍 Web Search Tool

### 개요
| 항목 | 내용 |
|------|------|
| **목적** | 실시간 웹 검색 |
| **버전** | `web_search_20250305` |
| **환경** | 모든 환경 |
| **비용** | 검색당 추가 요금 |

### API 사용법
```python
import anthropic

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1024,
    tools=[{
        "type": "web_search_20250305",
        "name": "web_search",
        "max_uses": 5  # 최대 검색 횟수 (선택)
    }],
    messages=[{
        "role": "user",
        "content": "2026년 AI 트렌드 검색해줘"
    }]
)

print(response.content)
```

### 프롬프트 예시 (Claude Web/Desktop)
```
최신 AI 뉴스 검색해서 요약해줘

한국 스타트업 투자 동향 찾아줘

OZKIZ 키즈 패션 시장 트렌드 검색해줘
```

---

## 🌐 Web Fetch Tool

### 개요
| 항목 | 내용 |
|------|------|
| **목적** | 특정 URL 콘텐츠 가져오기 |
| **버전** | 내장 도구 |
| **환경** | 모든 환경 |
| **제한** | 로그인 필요한 페이지 불가 |

### 프롬프트 예시
```
https://docs.anthropic.com 이 문서 요약해줘

이 URL의 가격 정보 추출해줘: https://example.com/pricing

https://github.com/anthropic/sdk 이 저장소 README 분석해줘
```

---

## 💻 Code Execution Tool

### 개요
| 항목 | 내용 |
|------|------|
| **목적** | Python 코드 실행, 파일 생성 |
| **버전** | `code_execution_20250825` |
| **환경** | Claude Web (Pro+), Claude Desktop (Pro+), API |
| **Python** | 3.11.12 |
| **인터넷** | ❌ 차단됨 |

### API 사용법
```python
import anthropic

client = anthropic.Anthropic()

response = client.beta.messages.create(
    model="claude-sonnet-4-5",
    betas=["code-execution-2025-08-25"],  # 베타 헤더 필수!
    max_tokens=4096,
    messages=[{
        "role": "user",
        "content": "1부터 100까지 합 계산해줘"
    }],
    tools=[{
        "type": "code_execution_20250825",
        "name": "code_execution"
    }]
)
```

### 프롬프트 예시 (Claude Web/Desktop)
```
이 엑셀 파일 분석해서 월별 매출 차트 만들어줘
[파일 첨부]

다음 데이터로 파이 차트 그려줘:
- 한국: 40%
- 일본: 25%
- 미국: 20%
- 기타: 15%

마인드맵 그려줘. 중심: OZKIZ Business
```

### 사용 가능한 라이브러리
```
numpy, pandas, matplotlib, seaborn, scipy, 
scikit-learn, pillow, openpyxl, xlrd, 
python-docx, reportlab, beautifulsoup4
```

### 제한사항
- ❌ 인터넷 연결 없음 (pip install 불가)
- ❌ 외부 API 호출 불가
- ⏰ 컨테이너 30일 후 만료
- 💾 파일 시스템은 세션 간 유지

---

# 4. Client Tools (클라이언트 도구)

> 개발자 시스템에서 실행되는 도구. 구현이 필요함!

---

## 🖱️ Computer Use Tool

### 개요
| 항목 | 내용 |
|------|------|
| **목적** | 컴퓨터 화면 조작 (마우스, 키보드) |
| **버전** | `computer_20250124` |
| **환경** | Claude Desktop, Claude Chrome, API |
| **주의** | 보안 위험! 격리 환경 권장 |

### 지원 액션
| 액션 | 설명 | 예시 |
|------|------|------|
| `screenshot` | 화면 캡처 | 현재 화면 상태 확인 |
| `mouse_move` | 마우스 이동 | 특정 좌표로 이동 |
| `left_click` | 왼쪽 클릭 | 버튼 클릭 |
| `right_click` | 오른쪽 클릭 | 컨텍스트 메뉴 |
| `double_click` | 더블 클릭 | 파일 열기 |
| `type` | 텍스트 입력 | 텍스트 타이핑 |
| `key` | 키 입력 | Enter, Ctrl+C 등 |
| `scroll` | 스크롤 | 페이지 스크롤 |

### 프롬프트 예시 (Claude Desktop)
```
Chrome 열어서 google.com 접속해줘

메모장 열어서 오늘 할 일 목록 작성해줘

바탕화면에 새 폴더 만들어줘
```

---

## 📝 Text Editor Tool

### 개요
| 항목 | 내용 |
|------|------|
| **목적** | 파일 읽기/쓰기/수정 |
| **버전** | `text_editor_20250124` |
| **환경** | Claude Desktop, Claude Code, API |

### 지원 명령
| 명령 | 설명 |
|------|------|
| `view` | 파일 내용 보기 |
| `create` | 새 파일 생성 |
| `str_replace` | 텍스트 교체 |
| `insert` | 텍스트 삽입 |

### 프롬프트 예시
```
config.json 파일 내용 보여줘

새 파일 hello.py 만들어서 Hello World 출력하는 코드 작성해줘

main.py에서 "localhost"를 "0.0.0.0"으로 바꿔줘
```

---

## 🖥️ Bash Tool

### 개요
| 항목 | 내용 |
|------|------|
| **목적** | Shell 명령 실행 |
| **버전** | `bash_20250124` |
| **환경** | Claude Desktop, Claude Code, API |
| **세션** | 대화 내 유지 |

### 지원 명령 예시
```bash
# 파일 시스템
ls -la
cd /path/to/dir
mkdir new_folder

# Git
git status
git add .
git commit -m "message"

# 시스템 정보
uname -a
df -h
```

---

## 🧠 Memory Tool

### 개요
| 항목 | 내용 |
|------|------|
| **목적** | 대화 간 정보 기억 |
| **환경** | Claude Web, Claude Desktop, Claude Code, API |
| **지속성** | 대화 세션 간 유지 |

### 프롬프트 예시
```
나는 벨라야. OZKIZ에서 일해. 이거 기억해줘

내 이름 뭐라고 했지?

이 정보 기억에서 삭제해줘: [정보]
```

---

# 5. Capabilities (기능)

> API에서 사용 가능한 다양한 기능들

---

## ⚡ Streaming (스트리밍) 🆕

### 개요 / 概述
| 항목 | 내용 |
|------|------|
| **목적** | 실시간 응답 스트리밍 (SSE) |
| **환경** | 모든 환경 |
| **방식** | Server-Sent Events |
| **장점** | 긴 응답도 즉시 시작, 사용자 경험 향상 |

### 왜 사용하나요? / 為什麼要使用？
```
❌ 스트리밍 없이: 전체 응답 생성 후 한 번에 표시 (느림!)
✅ 스트리밍 사용: 생성되는 대로 실시간 표시 (빠름!)
```

### SDK 사용법 (Python)
```python
import anthropic

client = anthropic.Anthropic()

# 방법 1: text_stream 사용
with client.messages.stream(
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello"}],
    model="claude-sonnet-4-5",
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)
```

### cURL 사용법
```bash
curl https://api.anthropic.com/v1/messages \
     --header "x-api-key: $ANTHROPIC_API_KEY" \
     --header "anthropic-version: 2023-06-01" \
     --header "content-type: application/json" \
     --data '{
         "model": "claude-sonnet-4-5",
         "messages": [{"role": "user", "content": "Hello"}],
         "max_tokens": 256,
         "stream": true
     }'
```

### 이벤트 타입
| 이벤트 | 설명 |
|--------|------|
| `message_start` | 메시지 시작 (빈 content) |
| `content_block_start` | 콘텐츠 블록 시작 |
| `content_block_delta` | 콘텐츠 조각 (text, tool input 등) |
| `content_block_stop` | 콘텐츠 블록 종료 |
| `message_delta` | 메시지 변경 (stop_reason 등) |
| `message_stop` | 메시지 종료 |
| `ping` | 연결 유지 |

### 델타 타입
| 델타 타입 | 용도 |
|-----------|------|
| `text_delta` | 텍스트 응답 |
| `input_json_delta` | Tool use 입력 |
| `thinking_delta` | Extended thinking |
| `signature_delta` | Thinking 서명 |

### Tool Use와 함께 스트리밍
```python
# Tool use 스트리밍은 partial JSON으로 전달됨
# SDK가 자동으로 누적해서 파싱해줌
with client.messages.stream(
    model="claude-sonnet-4-5",
    max_tokens=1024,
    tools=[...],
    messages=[{"role": "user", "content": "What's the weather?"}]
) as stream:
    for event in stream:
        if event.type == "content_block_delta":
            print(event.delta)
```

### 에러 처리
```python
# 스트리밍 중 에러가 발생할 수 있음
# overloaded_error: 서버 과부하
try:
    with client.messages.stream(...) as stream:
        for text in stream.text_stream:
            print(text, end="")
except anthropic.APIError as e:
    print(f"API Error: {e}")
```

### OZKIZ 활용 예시
```
# 긴 보고서 생성 시 스트리밍 유용
"OZKIZ 월간 매출 보고서 작성해줘" 
→ 스트리밍으로 실시간으로 내용 확인하면서 기다릴 수 있음!
```

---

## 🧠 Extended Thinking (확장된 사고) 🆕

### 개요 / 概述
| 항목 | 내용 |
|------|------|
| **목적** | 복잡한 문제에 단계별 추론 |
| **환경** | Claude Web, Desktop, API |
| **지원 모델** | Opus 4.5, Opus 4.1, Opus 4, Sonnet 4.5, Sonnet 4, Haiku 4.5 |
| **특징** | 사고 과정을 볼 수 있음! |

### 왜 사용하나요? / 為什麼要使用？
```
❌ 일반 응답: "답은 12,231입니다"
✅ Extended Thinking: 
   [thinking] "27 × 453을 계산해보자. 
              453 = 400 + 50 + 3
              27 × 400 = 10,800
              27 × 50 = 1,350
              27 × 3 = 81
              합계: 12,231"
   [answer] "27 × 453 = 12,231입니다"
```

### API 사용법
```python
import anthropic

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=16000,
    thinking={
        "type": "enabled",
        "budget_tokens": 10000  # 사고에 사용할 최대 토큰
    },
    messages=[{
        "role": "user",
        "content": "27 * 453을 계산해줘"
    }]
)

# 응답 구조
for block in response.content:
    if block.type == "thinking":
        print(f"🧠 사고 과정: {block.thinking}")
    elif block.type == "text":
        print(f"📝 최종 답변: {block.text}")
```

### 응답 형식
```json
{
  "content": [
    {
      "type": "thinking",
      "thinking": "단계별 추론 과정...",
      "signature": "EqQBCgIYAhIM1gbcDa..."  // 무결성 검증용
    },
    {
      "type": "text",
      "text": "최종 답변..."
    }
  ]
}
```

### 파라미터 설명
| 파라미터 | 설명 |
|----------|------|
| `type` | `"enabled"` - 활성화 |
| `budget_tokens` | 사고에 사용할 최대 토큰 (min: 1024) |

### 스트리밍과 함께 사용
```python
with client.messages.stream(
    model="claude-sonnet-4-5",
    max_tokens=16000,
    stream=True,
    thinking={
        "type": "enabled",
        "budget_tokens": 10000
    },
    messages=[{"role": "user", "content": "복잡한 문제..."}]
) as stream:
    for event in stream:
        # thinking_delta: 사고 과정
        # text_delta: 최종 답변
        print(event)
```

### Tool Use와 함께 사용
```python
# Tool Use + Extended Thinking
# 주의: tool_choice는 "auto" 또는 "none"만 가능!
response = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=16000,
    thinking={
        "type": "enabled",
        "budget_tokens": 10000
    },
    tools=[...],
    tool_choice={"type": "auto"},  # ⚠️ "any", "tool" 사용 불가!
    messages=[...]
)
```

### Interleaved Thinking (베타)
```python
# Tool 호출 사이에도 사고 가능
response = client.beta.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=16000,
    betas=["interleaved-thinking-2025-05-14"],  # 베타 헤더
    thinking={
        "type": "enabled",
        "budget_tokens": 10000
    },
    tools=[...],
    messages=[...]
)
```

### Thinking 요약 (Claude 4 모델)
```
Claude 4 모델은 보안상 요약된 사고 과정을 반환합니다.
- 사고의 핵심 내용은 유지
- 전체 사고 토큰은 청구됨
- Claude Sonnet 3.7은 전체 사고 반환
```

### Redacted Thinking (수정된 사고)
```json
// 안전 시스템에 의해 일부 사고가 암호화됨
{
  "type": "redacted_thinking",
  "data": "EmwKAhgBEgy3va3pzix..."  // 암호화된 내용
}
```

### 최적 사용 사례
| 작업 | 추천 budget_tokens |
|------|---------------------|
| 간단한 수학 | 2,000 - 5,000 |
| 코딩 문제 | 10,000 - 20,000 |
| 복잡한 분석 | 20,000 - 50,000 |
| 매우 복잡한 추론 | 50,000+ |

### OZKIZ 활용 예시
```
"OZKIZ의 2025년 매출 데이터를 분석해서 
 2026년 성장 전략을 제안해줘.
 단계별로 생각하면서 분석해줘."

→ Extended Thinking으로 더 정교한 분석 가능!
```

### 제한사항
- ❌ temperature, top_k 수정 불가
- ❌ 응답 미리 채우기(pre-fill) 불가
- ❌ tool_choice: "any" 또는 "tool" 불가
- ✅ top_p는 0.95-1.0 범위에서 설정 가능

---

## 🎚️ Effort (노력 수준) 🆕 **베타!**

### 개요 / 概述
| 항목 | 내용 |
|------|------|
| **목적** | 응답 품질 vs 토큰 사용량 조절 |
| **환경** | API only |
| **지원 모델** | **Claude Opus 4.5 전용!** |
| **상태** | 베타 (헤더 필요) |

### 왜 사용하나요? / 為什麼要使用？
```
🔴 high (기본): 최고 품질, 많은 토큰 사용
🟡 medium: 균형 잡힌 품질과 효율성
🟢 low: 빠른 응답, 적은 토큰, 간단한 작업에 적합
```

### 베타 헤더
```
anthropic-beta: effort-2025-11-24
```

### API 사용법
```python
import anthropic

client = anthropic.Anthropic()

# Effort 파라미터 사용
response = client.beta.messages.create(
    model="claude-opus-4-5-20251101",  # Opus 4.5만 지원!
    betas=["effort-2025-11-24"],
    max_tokens=4096,
    messages=[{
        "role": "user",
        "content": "마이크로서비스와 모놀리식 아키텍처 비교해줘"
    }],
    output_config={
        "effort": "medium"  # high, medium, low
    }
)
```

### 노력 수준별 특징
| 수준 | 설명 | 사용 사례 |
|------|------|----------|
| **high** | 최대 능력, 최고 품질 | 복잡한 추론, 어려운 코딩, 에이전트 작업 |
| **medium** | 균형 잡힌 접근 | 적당한 복잡도, 비용 효율성 필요 |
| **low** | 최고 효율성, 빠른 응답 | 간단한 분류, 빠른 조회, 서브에이전트 |

### Tool Use와 함께 사용
```python
# 낮은 effort = 적은 tool 호출
response = client.beta.messages.create(
    model="claude-opus-4-5-20251101",
    betas=["effort-2025-11-24"],
    max_tokens=4096,
    tools=[...],
    output_config={"effort": "low"},  # 간단하게 처리
    messages=[...]
)
```

### Extended Thinking과 함께 사용
```python
# Effort는 thinking 토큰에도 영향을 줌!
response = client.beta.messages.create(
    model="claude-opus-4-5-20251101",
    betas=["effort-2025-11-24"],
    max_tokens=20000,
    thinking={
        "type": "enabled",
        "budget_tokens": 16000
    },
    output_config={"effort": "high"},  # 깊은 사고
    messages=[...]
)
```

### OZKIZ 활용 예시
```python
# 간단한 상품 분류 → low effort
"이 상품이 어떤 카테고리인지 분류해줘: 꽃무늬 원피스"

# 복잡한 전략 분석 → high effort
"OZKIZ의 미국 시장 진출 전략을 분석하고 
 경쟁사 대비 차별화 포인트를 제안해줘"
```

### 베스트 프랙티스
```
1. 기본값은 high → 필요시 낮춤
2. 간단한 작업에는 low 사용 (비용/속도 절약)
3. 복잡한 추론에는 high 유지
4. 작업별로 동적으로 조절 가능
```

---

## 📝 Context Editing (컨텍스트 편집) 🆕 **베타!**

### 개요 / 概述
| 항목 | 내용 |
|------|------|
| **목적** | 자동 컨텍스트 관리 (긴 대화 최적화) |
| **환경** | API only |
| **상태** | 베타 (헤더 필요) |
| **종류** | Server-side + Client-side (SDK) |

### 왜 사용하나요? / 為什麼要使用？
```
문제: 긴 대화 → 컨텍스트 윈도우 초과 → 에러!

해결:
🔧 Server-side: 오래된 tool 결과/thinking 블록 자동 삭제
🔧 Client-side: SDK가 대화 요약 후 교체
```

### 베타 헤더
```
anthropic-beta: context-management-2025-06-27
```

### 지원 모델
- Claude Opus 4.5, 4.1, 4
- Claude Sonnet 4.5, 4
- Claude Haiku 4.5

---

### 1️⃣ Tool Result Clearing (도구 결과 삭제)

```python
import anthropic

client = anthropic.Anthropic()

# 기본 사용
response = client.beta.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=4096,
    betas=["context-management-2025-06-27"],
    messages=[...],
    tools=[...],
    context_management={
        "edits": [
            {"type": "clear_tool_uses_20250919"}
        ]
    }
)
```

### 상세 설정
```python
context_management={
    "edits": [{
        "type": "clear_tool_uses_20250919",
        "trigger": {
            "type": "input_tokens",
            "value": 30000  # 30k 토큰 초과 시 트리거
        },
        "keep": {
            "type": "tool_uses",
            "value": 3  # 최근 3개 tool use 유지
        },
        "clear_at_least": {
            "type": "input_tokens",
            "value": 5000  # 최소 5k 토큰 삭제
        },
        "exclude_tools": ["web_search"]  # web_search 결과는 유지
    }]
}
```

| 옵션 | 기본값 | 설명 |
|------|--------|------|
| `trigger` | 100,000 토큰 | 언제 삭제 시작할지 |
| `keep` | 3 tool uses | 몇 개 유지할지 |
| `clear_at_least` | None | 최소 삭제량 |
| `exclude_tools` | None | 제외할 도구 |
| `clear_tool_inputs` | false | 도구 호출도 삭제할지 |

---

### 2️⃣ Thinking Block Clearing (사고 블록 삭제)

```python
context_management={
    "edits": [{
        "type": "clear_thinking_20251015",
        "keep": {
            "type": "thinking_turns",
            "value": 2  # 최근 2턴의 thinking 유지
        }
    }]
}
```

| 옵션 | 기본값 | 설명 |
|------|--------|------|
| `keep` | 1 turn | 몇 턴 유지할지 |
| `"all"` | - | 모든 thinking 유지 (캐시 최적화) |

---

### 3️⃣ 두 전략 함께 사용

```python
# 주의: clear_thinking이 먼저 와야 함!
context_management={
    "edits": [
        {
            "type": "clear_thinking_20251015",
            "keep": {"type": "thinking_turns", "value": 2}
        },
        {
            "type": "clear_tool_uses_20250919",
            "trigger": {"type": "input_tokens", "value": 50000},
            "keep": {"type": "tool_uses", "value": 5}
        }
    ]
}
```

---

### 4️⃣ Client-side Compaction (SDK)

```python
# Python/TypeScript SDK의 tool_runner에서 사용
runner = client.beta.messages.tool_runner(
    model="claude-sonnet-4-5",
    max_tokens=4096,
    tools=[...],
    messages=[...],
    compaction_control={
        "enabled": True,
        "context_token_threshold": 100000  # 100k 토큰 초과 시
    }
)

# 자동으로 대화 요약 후 교체됨!
for message in runner:
    print(f"Tokens used: {message.usage.input_tokens}")

final = runner.until_done()
```

### Compaction 작동 방식
```
1. 토큰 사용량 체크 (threshold 초과 시)
2. Claude에게 요약 요청 (자동)
3. 전체 대화 → 요약으로 교체
4. 요약부터 대화 계속!
```

### Compaction 설정 옵션
| 옵션 | 기본값 | 설명 |
|------|--------|------|
| `enabled` | - | 활성화 여부 |
| `context_token_threshold` | 100,000 | 트리거 임계값 |
| `model` | 동일 | 요약에 사용할 모델 |
| `summary_prompt` | 기본 프롬프트 | 커스텀 요약 프롬프트 |

---

### 응답에서 확인
```json
{
  "context_management": {
    "applied_edits": [
      {
        "type": "clear_thinking_20251015",
        "cleared_thinking_turns": 3,
        "cleared_input_tokens": 15000
      },
      {
        "type": "clear_tool_uses_20250919",
        "cleared_tool_uses": 8,
        "cleared_input_tokens": 50000
      }
    ]
  }
}
```

### Memory Tool과 함께 사용
```python
# Context Editing + Memory Tool = 최강 조합!
# 중요한 정보를 Memory에 저장 → 나중에 참조 가능
response = client.beta.messages.create(
    model="claude-sonnet-4-5",
    betas=["context-management-2025-06-27"],
    tools=[
        {"type": "memory_20250818", "name": "memory"},
        # 다른 도구들...
    ],
    context_management={
        "edits": [{"type": "clear_tool_uses_20250919"}]
    },
    messages=[...]
)
```

### OZKIZ 활용 예시
```
# 긴 에이전트 작업에서 컨텍스트 관리
"OZKIZ의 모든 상품 데이터를 분석하고,
 카테고리별 베스트셀러를 찾아서,
 각 국가별 추천 상품 리스트를 만들어줘"

→ 많은 tool 호출 필요
→ Context Editing으로 자동 관리!
```

---

## 💾 Prompt Caching (프롬프트 캐싱) - 업데이트!

### 개요 / 概述
| 항목 | 내용 |
|------|------|
| **목적** | 반복 프롬프트 비용/속도 최적화 |
| **환경** | API only |
| **캐시 시간** | 5분 (기본) / **1시간 (추가 요금)** 🆕 |
| **최소 토큰** | 모델별 상이 (1024~4096) |

### 왜 사용하나요? / 為什麼要使用？
```
❌ 캐싱 없이: 매번 전체 프롬프트 처리 (비용 100%)
✅ 캐싱 사용: 캐시 히트 시 10% 비용만!
```

### 기본 사용법
```python
import anthropic

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1024,
    system=[
        {
            "type": "text",
            "text": "You are a helpful assistant."
        },
        {
            "type": "text",
            "text": "<the entire contents of a book>",  # 큰 문서
            "cache_control": {"type": "ephemeral"}  # 캐싱!
        }
    ],
    messages=[{"role": "user", "content": "이 책 요약해줘"}]
)
```

### 1시간 캐시 (NEW!)
```python
# 5분이 너무 짧을 때 → 1시간 캐시 사용!
system=[
    {
        "type": "text",
        "text": "<long document>",
        "cache_control": {
            "type": "ephemeral",
            "ttl": "1h"  # 🆕 1시간 캐시!
        }
    }
]
```

### 캐시 TTL 비교
| TTL | 비용 | 사용 사례 |
|-----|------|----------|
| **5분 (기본)** | 쓰기 1.25x, 읽기 0.1x | 자주 사용되는 프롬프트 |
| **1시간** 🆕 | 쓰기 2x, 읽기 0.1x | 긴 에이전트 작업, 간헐적 사용 |

### 가격표 (업데이트)
| 모델 | 기본 입력 | 5분 캐시 쓰기 | 1시간 캐시 쓰기 | 캐시 읽기 |
|------|----------|---------------|-----------------|----------|
| Opus 4.5 | $5/M | $6.25/M | $10/M | $0.50/M |
| Sonnet 4.5 | $3/M | $3.75/M | $6/M | $0.30/M |
| Haiku 4.5 | $1/M | $1.25/M | $2/M | $0.10/M |

### 최소 캐시 토큰
| 모델 | 최소 토큰 |
|------|----------|
| Claude Opus 4.5 | 4,096 |
| Claude Sonnet 4.5/4, Opus 4.1/4 | 1,024 |
| Claude Haiku 4.5 | 4,096 |
| Claude Haiku 3.5/3 | 2,048 |

### 캐시 무효화 조건
| 변경 사항 | Tools | System | Messages |
|-----------|:-----:|:------:|:--------:|
| Tool 정의 변경 | ❌ | ❌ | ❌ |
| Web Search 토글 | ✅ | ❌ | ❌ |
| Citations 토글 | ✅ | ❌ | ❌ |
| Tool choice 변경 | ✅ | ✅ | ❌ |
| 이미지 추가/삭제 | ✅ | ✅ | ❌ |
| Thinking 설정 변경 | ✅ | ✅ | ❌ |

✅ = 캐시 유지, ❌ = 캐시 무효화

### TTL 혼합 사용
```python
# 1시간 캐시가 5분 캐시보다 먼저 와야 함!
system=[
    {
        "type": "text",
        "text": "<rarely changing content>",
        "cache_control": {"type": "ephemeral", "ttl": "1h"}  # 먼저!
    },
    {
        "type": "text",
        "text": "<frequently changing content>",
        "cache_control": {"type": "ephemeral", "ttl": "5m"}  # 나중!
    }
]
```

### 캐시 성능 모니터링
```json
{
  "usage": {
    "input_tokens": 50,
    "cache_creation_input_tokens": 0,
    "cache_read_input_tokens": 100000,  // 캐시 히트!
    "output_tokens": 500,
    "cache_creation": {
      "ephemeral_5m_input_tokens": 0,
      "ephemeral_1h_input_tokens": 0
    }
  }
}
```

### OZKIZ 활용 예시
```python
# OZKIZ 상품 카탈로그를 캐싱
system=[
    {"type": "text", "text": "You are an OZKIZ sales assistant."},
    {
        "type": "text",
        "text": "<전체 상품 카탈로그 10만 토큰>",
        "cache_control": {"type": "ephemeral", "ttl": "1h"}
    }
]

# 바이어 질문에 빠르게 응답!
"SS26 컬렉션에서 원피스 추천해줘"
→ 캐시 히트로 빠른 응답!
```

---

## 📄 PDF Support (PDF 지원)

### 개요
| 항목 | 내용 |
|------|------|
| **목적** | PDF 문서 내용 분석 |
| **환경** | 모든 환경 |
| **최대 크기** | 32MB |
| **최대 페이지** | 100페이지 |

### Claude Web/Desktop 사용
```
[PDF 파일 첨부]
이 문서 요약해줘

이 계약서의 주요 조항 분석해줘

이 보고서에서 핵심 수치 추출해줘
```

### API 사용법 (Base64)
```python
import anthropic
import base64

client = anthropic.Anthropic()

# PDF를 Base64로 인코딩
with open("document.pdf", "rb") as f:
    pdf_data = base64.standard_b64encode(f.read()).decode("utf-8")

response = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=4096,
    messages=[{
        "role": "user",
        "content": [
            {
                "type": "document",
                "source": {
                    "type": "base64",
                    "media_type": "application/pdf",
                    "data": pdf_data
                }
            },
            {"type": "text", "text": "이 문서 요약해줘"}
        ]
    }]
)
```

### 토큰 계산
```
PDF 토큰 = 페이지당 약 1,500 토큰 (텍스트 기준)
이미지가 많은 PDF = 이미지 토큰도 추가됨
```

### 제한사항
- ❌ 암호화된 PDF
- ❌ 100페이지 초과
- ❌ 32MB 초과
- ⚠️ 스캔 PDF는 OCR 품질에 따라 다름

---

## 🖼️ Vision (이미지 분석)

### 개요
| 항목 | 내용 |
|------|------|
| **목적** | 이미지 내용 분석 |
| **환경** | 모든 환경 |
| **지원 형식** | PNG, JPG, JPEG, GIF, WEBP |
| **최대 크기** | 20MB |

### Claude Web/Desktop 사용
```
[이미지 첨부]
이 이미지 설명해줘

이 차트 분석해줘

이 제품 사진에서 특징 찾아줘
```

### API 사용법 (Base64)
```python
import anthropic
import base64

client = anthropic.Anthropic()

with open("image.png", "rb") as f:
    image_data = base64.standard_b64encode(f.read()).decode("utf-8")

response = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1024,
    messages=[{
        "role": "user",
        "content": [
            {
                "type": "image",
                "source": {
                    "type": "base64",
                    "media_type": "image/png",
                    "data": image_data
                }
            },
            {"type": "text", "text": "이 이미지 설명해줘"}
        ]
    }]
)
```

### API 사용법 (URL)
```python
response = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1024,
    messages=[{
        "role": "user",
        "content": [
            {
                "type": "image",
                "source": {
                    "type": "url",
                    "url": "https://example.com/image.png"
                }
            },
            {"type": "text", "text": "이 이미지 분석해줘"}
        ]
    }]
)
```

### 토큰 계산
| 이미지 크기 | 토큰 |
|------------|------|
| 작은 이미지 (~100x100) | ~100 토큰 |
| 중간 이미지 (~500x500) | ~500 토큰 |
| 큰 이미지 (~1000x1000) | ~1,500 토큰 |

---

## 📁 Files API (파일 API)

### 개요
| 항목 | 내용 |
|------|------|
| **목적** | 파일 업로드 후 재사용 |
| **환경** | API only |
| **장점** | 동일 파일 여러 번 사용 시 효율적 |

### 사용법
```python
import anthropic

client = anthropic.Anthropic()

# 1. 파일 업로드
file = client.beta.files.upload(
    file=open("document.pdf", "rb")
)

# 2. 파일 ID로 참조
response = client.beta.messages.create(
    model="claude-sonnet-4-5",
    betas=["files-api-2025-04-14"],
    max_tokens=4096,
    messages=[{
        "role": "user",
        "content": [
            {"type": "file", "file_id": file.id},
            {"type": "text", "text": "이 문서 요약해줘"}
        ]
    }]
)
```

---

## 📦 Batch Processing (배치 처리)

### 개요
| 항목 | 내용 |
|------|------|
| **목적** | 대량 요청 효율적 처리 |
| **환경** | API only |
| **할인** | 50% |
| **처리 시간** | 최대 24시간 |

### 사용법
```python
import anthropic

client = anthropic.Anthropic()

# 1. 배치 생성
batch = client.batches.create(
    requests=[
        {
            "custom_id": "req-1",
            "params": {
                "model": "claude-sonnet-4-5",
                "max_tokens": 1024,
                "messages": [{"role": "user", "content": "Hello"}]
            }
        },
        # 더 많은 요청들...
    ]
)

# 2. 상태 확인
status = client.batches.retrieve(batch.id)
print(status.status)  # "processing" or "completed"

# 3. 결과 가져오기
if status.status == "completed":
    results = client.batches.results(batch.id)
```

---

## 📊 Structured Outputs (구조화된 출력)

### 개요
| 항목 | 내용 |
|------|------|
| **목적** | JSON 형식 강제 |
| **환경** | API only |
| **방법** | Tool Use 또는 JSON Mode |

### Tool Use 방식 (권장)
```python
import anthropic

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1024,
    tools=[{
        "name": "get_product_info",
        "description": "상품 정보 추출",
        "strict": True,  # 스키마 100% 보장
        "input_schema": {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "price": {"type": "number"},
                "category": {"type": "string"}
            },
            "required": ["name", "price", "category"]
        }
    }],
    tool_choice={"type": "tool", "name": "get_product_info"},
    messages=[{
        "role": "user",
        "content": "상품명: 플라워 원피스, 가격: 35000원, 카테고리: 원피스"
    }]
)
```

---

## 📎 Citations (인용)

### 개요
| 항목 | 내용 |
|------|------|
| **목적** | 문서 출처 표시 |
| **환경** | API only |
| **지원** | PDF, Text, Custom 문서 |

### 사용법
```python
import anthropic

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1024,
    documents=[
        {
            "type": "document",
            "source": {
                "type": "text",
                "media_type": "text/plain",
                "data": "문서 내용..."
            },
            "title": "문서 제목",
            "context": "이 문서는..."
        }
    ],
    messages=[{
        "role": "user",
        "content": "이 문서에서 핵심 내용을 인용해서 설명해줘"
    }],
    citations={"enabled": True}
)

# 응답에 출처 정보 포함됨!
```

---

## 🌍 Multilingual Support (다국어 지원)

### 지원 언어 성능 (Tier 1)
| 언어 | 읽기 | 쓰기 | 대화 |
|------|:----:|:----:|:----:|
| 영어 | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| 한국어 | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| 중국어 | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| 일본어 | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| 스페인어 | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |

### OZKIZ 활용 예시
```
# 한국어 → 영어 바이어 이메일
"이 상품 설명을 미국 바이어용 영어로 번역해줘"

# 다국어 상품 설명
"이 원피스 설명을 영어, 일본어, 중국어로 각각 작성해줘"
```

---

## 🔢 Token Counting (토큰 카운팅)

### 개요
| 항목 | 내용 |
|------|------|
| **목적** | 토큰 수 미리 계산 |
| **환경** | API only |
| **비용** | 🆓 무료! |

### 사용법
```python
import anthropic

client = anthropic.Anthropic()

# 토큰 수 계산 (무료!)
result = client.messages.count_tokens(
    model="claude-sonnet-4-5",
    messages=[{"role": "user", "content": "Hello, world!"}]
)

print(f"입력 토큰: {result.input_tokens}")
```

---

# 6. SDK 기능 및 베타 기능

## 🔧 Tool Runner (SDK)

### 개요
| 항목 | 내용 |
|------|------|
| **목적** | 도구 실행 자동화 |
| **환경** | Python/TypeScript SDK |
| **장점** | 도구 호출 루프 자동 처리 |

### 사용법
```python
import anthropic

client = anthropic.Anthropic()

# 도구 정의
tools = [{
    "name": "get_weather",
    "description": "날씨 조회",
    "input_schema": {...}
}]

# Tool Runner 사용
runner = client.beta.messages.tool_runner(
    model="claude-sonnet-4-5",
    max_tokens=1024,
    tools=tools,
    messages=[{"role": "user", "content": "서울 날씨 알려줘"}]
)

# 자동으로 도구 호출 처리!
final = runner.until_done()
print(final.content[0].text)
```

---

## ⚡ Fine-grained Tool Streaming (베타)

### 개요
| 항목 | 내용 |
|------|------|
| **목적** | Tool 파라미터 빠른 스트리밍 |
| **환경** | API only |
| **베타 헤더** | `fine-grained-tool-streaming-2025-05-14` |

### 효과
```
기존 (15초 지연):
Chunk 1: '{"'
Chunk 2: 'query": "Ty'
...

Fine-grained (3초 지연):
Chunk 1: '{"query": "TypeScript new features'
Chunk 2: ' comparison"}'
```

---

## 🔒 Strict Tool Use

### 개요
| 항목 | 내용 |
|------|------|
| **목적** | 도구 입력 스키마 100% 보장 |
| **환경** | API |
| **효과** | 타입 불일치, 필수 필드 누락 방지 |

### 사용법
```python
tools = [{
    "name": "create_order",
    "description": "새 주문을 생성합니다",
    "strict": True,  # ⬅️ 이것만 추가!
    "input_schema": {
        "type": "object",
        "properties": {
            "product_id": {"type": "string"},
            "quantity": {"type": "integer"}
        },
        "required": ["product_id", "quantity"]
    }
}]
```

---

## 🔗 MCP Connector

### 개요
| 항목 | 내용 |
|------|------|
| **목적** | MCP 서버 연결 |
| **환경** | Claude Desktop, Claude Code, API |
| **용도** | 외부 서비스 통합 (DB, 파일시스템 등) |

### Claude Desktop 설정
```json
// macOS: ~/Library/Application Support/Claude/claude_desktop_config.json
// Windows: %APPDATA%\Claude\claude_desktop_config.json

{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/Users/bella/Documents"]
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "ghp_..."
      }
    }
  }
}
```

### 인기 MCP 서버
| 서버 | 용도 | 패키지 |
|------|------|--------|
| filesystem | 파일 시스템 접근 | `@modelcontextprotocol/server-filesystem` |
| postgres | PostgreSQL DB | `@modelcontextprotocol/server-postgres` |
| github | GitHub API | `@modelcontextprotocol/server-github` |
| slack | Slack 연동 | `@modelcontextprotocol/server-slack` |
| google-drive | 구글 드라이브 | `@modelcontextprotocol/server-google-drive` |

---

# 7. 실전 프롬프트 모음

## 📊 데이터 분석 (Code Execution)

### 매출 분석
```
[CSV 파일 첨부]

이 매출 데이터 분석해줘:
1. 월별 총 매출 계산
2. 전월 대비 성장률
3. TOP 10 상품
4. 국가별 매출 비중 파이 차트
5. 인사이트 정리

한국어로 설명하고 차트도 만들어줘.
```

### 차트 생성
```
다음 데이터로 마인드맵 그려줘:

중심: OZKIZ Business Strategy
브랜치: Marketing, Sales, Product, Operations, Finance, HR

각 브랜치별 서브 항목 3-4개씩.
예쁜 색상으로, PNG 고화질로 저장.
```

---

## 📄 PDF 분석

### 계약서 분석
```
[PDF 파일 첨부]

이 계약서 분석해줘:
1. 계약 당사자
2. 계약 기간
3. 금액/결제 조건
4. 주요 의무 사항
5. 위약금/페널티 조항
6. 해지 조건

중요한 리스크 포인트도 알려줘.
```

---

## 🖼️ 이미지 분석

### 상품 분석
```
[상품 이미지 첨부]

이 제품 분석해줘:
1. 제품 유형
2. 색상/패턴
3. 예상 소재
4. 타겟 고객층
5. 경쟁 제품 대비 특징

마케팅 포인트도 추천해줘.
```

---

## 🔍 웹 검색

### 트렌드 조사
```
2026년 키즈 패션 트렌드 검색해서 정리해줘.
- 주요 트렌드 5가지
- 인기 색상
- 인기 소재
- 주요 브랜드 동향
```

---

## 🧠 Extended Thinking 활용

### 복잡한 분석 요청
```
OZKIZ의 미국 시장 진출 전략을 분석해줘.

단계별로 깊이 생각하면서:
1. 현재 미국 키즈 패션 시장 분석
2. 주요 경쟁사 파악
3. OZKIZ의 강점/약점
4. 시장 진입 전략 3가지 제안
5. 예상 ROI 계산

너의 사고 과정도 보여줘.
```

---

## 🖥️ 컴퓨터 조작 (Computer Use)

### 파일 정리
```
Downloads 폴더에서 30일 이상 된 파일들을 
Archive 폴더로 이동해줘.

단, 실행 전에 이동할 파일 목록 먼저 보여줘.
```

---

## 📝 파일 편집 (Text Editor / Bash)

### 코드 수정
```
main.py 파일에서:
1. 모든 print() → logging.info()로 변경
2. 파일 상단에 import logging 추가
3. 변경 사항 보여줘
```

---

# 8. 문제 해결 가이드

## ❓ 자주 발생하는 문제

### Code Execution 안 됨
```
증상: "Code Execution을 사용할 수 없습니다"

해결:
1. 플랜 확인 → Pro 이상 필요 ($20/월)
2. 설정 → 기능 → Code Execution 활성화
3. 브라우저 새로고침
```

### API 키 에러
```
증상: "Invalid API key"

해결:
1. 키가 "sk-ant-api03-"로 시작하는지 확인
2. 환경 변수 설정 확인:
   - Windows: echo %ANTHROPIC_API_KEY%
   - Mac/Linux: echo $ANTHROPIC_API_KEY
3. 새 터미널/IDE 재시작
```

### PDF 분석 안 됨
```
증상: PDF 내용을 읽지 못함

해결:
1. 파일 크기 확인 (32MB 이하)
2. 페이지 수 확인 (100페이지 이하)
3. 암호화/보호 해제 확인
4. 스캔 PDF의 경우 OCR 품질 확인
```

### Extended Thinking 안 됨
```
증상: thinking 블록이 없음

해결:
1. 지원 모델 확인 (Sonnet 4.5, Opus 4.5 등)
2. thinking 파라미터 설정 확인
3. budget_tokens 최소 1024 이상
4. tool_choice가 "any"나 "tool"이면 안 됨!
```

### Context Editing 안 됨
```
증상: context_management가 작동 안 함

해결:
1. 베타 헤더 확인: context-management-2025-06-27
2. 지원 모델 확인 (Claude 4 계열)
3. clear_thinking은 edits 배열 맨 앞에!
```

### Prompt Caching 캐시 미스
```
증상: cache_read_input_tokens가 0

해결:
1. 최소 토큰 확인 (모델별 1024~4096)
2. cache_control 위치 확인
3. 프롬프트 내용이 동일한지 확인
4. 5분 이내 요청인지 확인 (또는 1시간)
```

### Computer Use 안 됨
```
증상: 화면 조작이 작동 안 함

해결:
1. Claude Desktop 최신 버전인지 확인
2. 시스템 권한 확인 (화면 녹화, 접근성)
3. macOS: 시스템 설정 → 개인 정보 → 접근성 → Claude 허용
4. Windows: 관리자 권한으로 실행
```

### MCP 연결 안 됨
```
증상: MCP 서버가 인식되지 않음

해결:
1. config 파일 경로 확인
2. JSON 문법 검사 (쉼표, 따옴표)
3. npx 명령어 수동 테스트
4. Claude Desktop 재시작
```

---

## 📞 도움 받기

| 채널 | 용도 | 링크 |
|------|------|------|
| **Anthropic 문서** | 공식 가이드 | docs.anthropic.com |
| **Support** | 기술 지원 | support.anthropic.com |
| **Discord** | 커뮤니티 | discord.gg/anthropic |
| **GitHub** | SDK 이슈 | github.com/anthropics/anthropic-sdk-python |

---

## 📊 가격 정리

### 플랜별 가격
| 플랜 | 가격 | 포함 기능 |
|------|------|----------|
| **Claude Free** | $0 | 기본 대화, 웹 검색, PDF, 이미지 |
| **Claude Pro** | $20/월 | + Code Execution, Extended Thinking, 더 많은 사용량 |
| **Claude Team** | $30/월/인 | + 팀 기능, 관리 도구 |
| **API** | 토큰당 과금 | 모든 도구/기능 사용 가능 |

### API 토큰 가격 (2026년 1월 기준)
| 모델 | 입력 | 출력 |
|------|------|------|
| Claude Opus 4.5 | $5/M | $25/M |
| Claude Sonnet 4.5 | $3/M | $15/M |
| Claude Haiku 4.5 | $1/M | $5/M |

*M = 1백만 토큰*

### 추가 비용
| 기능 | 비용 |
|------|------|
| Web Search | 검색당 추가 요금 |
| Prompt Caching (5분) | 쓰기 1.25x, 읽기 0.1x |
| Prompt Caching (1시간) 🆕 | 쓰기 2x, 읽기 0.1x |
| Batch Processing | 50% 할인 |

---

## 📝 업데이트 로그

| 날짜 | 버전 | 내용 |
|------|------|------|
| 2026-01-30 | v1.0 | 초기 버전 작성 |
| 2026-01-30 | v2.0 | Capabilities 섹션 추가 (PDF, Vision, Files API, Caching, Batch) |
| 2026-01-30 | v2.1 | Structured Outputs 추가 (JSON Outputs, Strict Tool Use) |
| 2026-01-30 | v2.2 | Search Results (RAG 인용) 추가 |
| 2026-01-30 | v2.3 | Files API, Vision 상세 업데이트 |
| 2026-01-30 | v2.4 | Embeddings (Voyage AI), Token Counting 추가 |
| 2026-01-30 | v2.5 | Citations (문서 인용) 추가 |
| 2026-01-30 | v2.6 | Multilingual Support 추가 |
| 2026-01-30 | **v3.0** | 🆕 **Streaming, Extended Thinking, Effort, Context Editing, Prompt Caching 1시간** |

---

## 🗺️ 전체 도구/기능 구조도

```
┌─────────────────────────────────────────────────────────────┐
│                    🧠 Claude Ecosystem v3.0                 │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  📱 SERVER TOOLS (Anthropic 서버에서 실행) - 3개            │
│  ├── Web Search Tool (웹 검색)                              │
│  ├── Web Fetch Tool (웹 콘텐츠 가져오기)                     │
│  └── Code Execution Tool (Python 실행 + 파일 생성)          │
│                                                             │
│  💻 CLIENT TOOLS (개발자 시스템에서 실행) - 4개              │
│  ├── Computer Use Tool (화면 조작)                          │
│  ├── Text Editor Tool (파일 수정)                           │
│  ├── Bash Tool (Shell 명령)                                 │
│  └── Memory Tool (정보 기억)                                │
│                                                             │
│  📄 CAPABILITIES (내장 기능) - 14개                         │
│  ├── Streaming ⚡ (실시간 응답) ⬅️ NEW!                     │
│  ├── Extended Thinking 🧠 (깊은 추론) ⬅️ NEW!               │
│  ├── PDF Support (PDF 분석)                                 │
│  ├── Vision (이미지 분석)                                   │
│  ├── Files API (파일 업로드/재사용)                         │
│  ├── Prompt Caching (캐싱 - 5분/1시간) ⬅️ 업데이트!         │
│  ├── Batch Processing (대량 처리)                           │
│  ├── Structured Outputs (JSON 형식 강제)                    │
│  ├── Citations (문서 인용 - PDF/Text)                       │
│  ├── Search Results (출처 인용/RAG)                         │
│  ├── Embeddings ⚠️ (의미 검색 - Voyage AI 외부)             │
│  ├── Token Counting 🆓 (토큰 수 미리 계산)                   │
│  └── Multilingual Support 🌍 (15개+ 언어 지원)              │
│                                                             │
│  ⚡ SDK/베타 기능 - 5개                                     │
│  ├── Tool Runner (자동 도구 실행)                           │
│  ├── Strict Tool Use (스키마 보장)                          │
│  ├── Fine-grained Streaming (빠른 스트리밍)                 │
│  ├── Effort 🎚️ (노력 수준) ⬅️ NEW! Beta, Opus 4.5 전용      │
│  └── Context Editing 📝 (컨텍스트 관리) ⬅️ NEW! Beta        │
│                                                             │
│  🔗 외부 연동                                                │
│  └── MCP Connector (MCP 서버 연결)                          │
│                                                             │
│  📊 총 27개 기능!                                           │
└─────────────────────────────────────────────────────────────┘
```

---

*이 가이드는 Bella(OZKIZ)가 Claude 도구를 효율적으로 사용하기 위해 작성했습니다.*
*本指南由 Bella（OZKIZ）編寫，用於高效使用 Claude 工具。*

**마지막 업데이트**: 2026-01-30 (v3.0)
