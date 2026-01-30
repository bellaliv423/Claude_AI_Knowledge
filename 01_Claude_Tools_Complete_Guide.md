# Claude 도구 종합 가이드
# Claude Tools Complete Guide

> **Author**: Bella (OZKIZ)
> **Created**: 2026-01-30
> **Version**: v1.1
> **Purpose**: 모든 Claude 도구의 설정, 활용, 프롬프트 완벽 정리

---

## 목차

1. [도구 호환성 매트릭스](#1-도구-호환성-매트릭스)
2. [Claude 환경별 특징](#2-claude-환경별-특징)
3. [Server Tools (서버 도구)](#3-server-tools-서버-도구)
4. [Client Tools (클라이언트 도구)](#4-client-tools-클라이언트-도구)
5. [SDK 기능 및 베타 기능](#5-sdk-기능-및-베타-기능)
6. [고급 기능](#6-고급-기능)
7. [실전 프롬프트 모음](#7-실전-프롬프트-모음)
8. [문제 해결 가이드](#8-문제-해결-가이드)

---

# 1. 도구 호환성 매트릭스

## 환경별 도구 사용 가능 여부

| 도구 | Claude Web | Claude Desktop | Claude Code | Claude Chrome | API |
|------|:----------:|:--------------:|:-----------:|:-------------:|:---:|
| **Web Search** | O | O | O | O | O |
| **Web Fetch** | O | O | O | O | O |
| **Code Execution** | O Pro+ | O Pro+ | X | X | O |
| **Computer Use** | X | O | X | O | O |
| **Text Editor** | X | O | O | X | O |
| **Bash Tool** | X | O | O | X | O |
| **Memory Tool** | O | O | O | X | O |
| **MCP Connector** | X | O | O | X | O |
| **Tool Runner** | X | X | X | X | O SDK |
| **Fine-grained Streaming** | X | X | X | X | O Beta |
| **Extended Thinking** | O | O | O | O | O |
| **Batch API** | X | X | X | X | O |

### 범례
- O = 사용 가능
- X = 사용 불가
- O Pro+ = Pro 이상 플랜 필요
- O SDK = SDK 설치 필요
- O Beta = 베타 헤더 필요

---

# 2. Claude 환경별 특징

## Claude Web (claude.ai)

| 항목 | 내용 |
|------|------|
| **접속 방법** | https://claude.ai |
| **필요 조건** | 계정 생성 |
| **플랜** | Free / Pro ($20) / Team ($30) |
| **주요 기능** | 대화, 파일 업로드, 웹 검색, Code Execution (Pro+) |
| **제한** | Computer Use, Bash Tool 사용 불가 |

---

## Claude Desktop

| 항목 | 내용 |
|------|------|
| **다운로드** | https://claude.ai/download |
| **지원 OS** | Windows, macOS |
| **주요 기능** | 모든 기능 + Computer Use + MCP |
| **특징** | 로컬 파일 접근, 시스템 통합 |

### MCP 설정
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

## Claude Code (CLI)

| 항목 | 내용 |
|------|------|
| **설치** | `npm install -g @anthropic-ai/claude-code` |
| **용도** | 터미널에서 코딩 작업 자동화 |
| **주요 기능** | 파일 편집, Bash 명령, 코드 생성 |

### 설치 방법
```bash
npm install -g @anthropic-ai/claude-code
export ANTHROPIC_API_KEY="sk-ant-api03-..."
claude-code "프로젝트 README 작성해줘"
```

---

## Claude Chrome Extension

| 항목 | 내용 |
|------|------|
| **설치** | Chrome Web Store |
| **용도** | 브라우저 자동화, 웹 페이지 분석 |
| **주요 기능** | Computer Use, 페이지 읽기, 클릭 자동화 |

---

## Claude API

| 항목 | 내용 |
|------|------|
| **접속** | https://console.anthropic.com |
| **용도** | 프로그래밍 방식으로 Claude 사용 |
| **가격** | 토큰 기반 과금 |

---

# 3. Server Tools (서버 도구)

## Web Search Tool

| 항목 | 내용 |
|------|------|
| **목적** | 실시간 웹 검색 |
| **버전** | `web_search_20250305` |
| **환경** | 모든 환경 |

```python
response = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1024,
    tools=[{
        "type": "web_search_20250305",
        "name": "web_search",
        "max_uses": 5
    }],
    messages=[{"role": "user", "content": "2026년 AI 트렌드 검색해줘"}]
)
```

---

## Code Execution Tool

| 항목 | 내용 |
|------|------|
| **목적** | Python 코드 실행, 파일 생성 |
| **버전** | `code_execution_20250825` |
| **환경** | Claude Web (Pro+), Claude Desktop (Pro+), API |
| **Python** | 3.11.12 |

```python
response = client.beta.messages.create(
    model="claude-sonnet-4-5",
    betas=["code-execution-2025-08-25"],
    max_tokens=4096,
    messages=[{"role": "user", "content": "1부터 100까지 합 계산해줘"}],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}]
)
```

### 사용 가능한 라이브러리
```
numpy, pandas, matplotlib, seaborn, scipy,
scikit-learn, pillow, openpyxl, xlrd,
python-docx, reportlab, beautifulsoup4
```

---

# 4. Client Tools (클라이언트 도구)

## Computer Use Tool

| 항목 | 내용 |
|------|------|
| **목적** | 컴퓨터 화면 조작 |
| **버전** | `computer_20250124` |
| **환경** | Claude Desktop, Claude Chrome, API |

### 지원 액션
| 액션 | 설명 |
|------|------|
| `screenshot` | 화면 캡처 |
| `mouse_move` | 마우스 이동 |
| `left_click` | 왼쪽 클릭 |
| `right_click` | 오른쪽 클릭 |
| `double_click` | 더블 클릭 |
| `type` | 텍스트 입력 |
| `key` | 키 입력 |
| `scroll` | 스크롤 |

---

## Text Editor Tool

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

---

## Bash Tool

| 항목 | 내용 |
|------|------|
| **목적** | Shell 명령 실행 |
| **버전** | `bash_20250124` |
| **환경** | Claude Desktop, Claude Code, API |

---

# 5. SDK 기능 및 베타 기능

## Tool Runner

자동으로 도구 호출을 처리하는 SDK 기능.

```python
from anthropic import beta_tool

@beta_tool
def get_weather(location: str) -> str:
    """지정된 위치의 날씨를 가져옵니다."""
    return '{"temp": 20, "condition": "sunny"}'

runner = client.beta.messages.tool_runner(
    model="claude-sonnet-4-5",
    tools=[get_weather],
    messages=[{"role": "user", "content": "서울 날씨 알려줘"}]
)

result = runner.until_done()
```

---

## Fine-grained Tool Streaming

도구 파라미터를 더 빠르게 스트리밍하는 베타 기능.

```bash
curl https://api.anthropic.com/v1/messages \
  -H "anthropic-beta: fine-grained-tool-streaming-2025-05-14" \
  -d '{"stream": true, ...}'
```

---

## Strict Tool Use

도구 입력 스키마를 100% 보장.

```python
tools = [{
    "name": "create_order",
    "strict": True,  # 스키마 100% 준수 보장
    "input_schema": {...}
}]
```

---

# 6. 고급 기능

## Container 재사용

Code Execution에서 컨테이너를 재사용하여 파일과 상태를 유지.

```python
# 첫 번째 요청
response1 = client.beta.messages.create(
    model="claude-sonnet-4-5",
    betas=["code-execution-2025-08-25"],
    max_tokens=4096,
    messages=[{
        "role": "user",
        "content": "랜덤 숫자를 /tmp/number.txt에 저장해줘"
    }],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}]
)

# 컨테이너 ID 추출
container_id = response1.container.id

# 두 번째 요청 - 같은 컨테이너 재사용
response2 = client.beta.messages.create(
    container=container_id,  # 컨테이너 재사용!
    model="claude-sonnet-4-5",
    betas=["code-execution-2025-08-25"],
    max_tokens=4096,
    messages=[{
        "role": "user",
        "content": "/tmp/number.txt 파일 읽어서 제곱 계산해줘"
    }],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}]
)
```

### 장점
- 파일 시스템 상태 유지
- 설치한 패키지 유지
- 변수 및 환경 유지
- 컨테이너는 30일 후 만료

---

## Programmatic Tool Calling

Claude가 코드 내에서 다른 도구를 프로그래매틱하게 호출.

```python
response = client.beta.messages.create(
    model="claude-sonnet-4-5",
    betas=["advanced-tool-use-2025-11-20"],
    max_tokens=4096,
    messages=[{
        "role": "user",
        "content": "5개 도시 날씨 가져와서 가장 따뜻한 곳 찾아줘"
    }],
    tools=[
        {
            "type": "code_execution_20250825",
            "name": "code_execution"
        },
        {
            "name": "get_weather",
            "description": "도시의 날씨를 가져옵니다",
            "input_schema": {
                "type": "object",
                "properties": {
                    "city": {"type": "string"}
                },
                "required": ["city"]
            },
            "allowed_callers": ["code_execution_20250825"]  # 코드에서 호출 허용
        }
    ]
)
```

### 장점
- 효율적인 다중 도구 워크플로우
- Claude 컨텍스트 도달 전 데이터 필터링
- 복잡한 조건 로직 처리

---

## Batch API

대량의 요청을 비동기로 처리.

```python
# 배치 생성
batch = client.beta.messages.batches.create(
    requests=[
        {
            "custom_id": "request-1",
            "params": {
                "model": "claude-sonnet-4-5",
                "max_tokens": 1024,
                "messages": [{"role": "user", "content": "안녕하세요"}]
            }
        },
        {
            "custom_id": "request-2",
            "params": {
                "model": "claude-sonnet-4-5",
                "max_tokens": 1024,
                "messages": [{"role": "user", "content": "오늘 날씨 어때?"}]
            }
        }
    ]
)

# 배치 ID 저장
batch_id = batch.id

# 상태 확인
status = client.beta.messages.batches.retrieve(batch_id)
print(status.processing_status)  # "in_progress" or "ended"

# 결과 가져오기 (완료 후)
results = client.beta.messages.batches.results(batch_id)
for result in results:
    print(result.custom_id, result.result.message.content)
```

### 장점
- 50% 비용 절감
- 대량 처리에 최적화
- 24시간 내 처리 보장

---

## Extended Thinking

Claude가 더 깊이 생각하게 하는 기능.

```python
response = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=16000,
    thinking={
        "type": "enabled",
        "budget_tokens": 10000  # 생각에 할당할 토큰
    },
    messages=[{
        "role": "user",
        "content": "이 복잡한 수학 문제를 단계별로 풀어줘: ..."
    }]
)

# 응답에서 thinking 블록 확인
for block in response.content:
    if block.type == "thinking":
        print("Thinking:", block.thinking)
    elif block.type == "text":
        print("Answer:", block.text)
```

### 사용 시나리오
- 복잡한 수학 문제
- 다단계 추론
- 코드 디버깅
- 전략적 계획

---

# 7. 실전 프롬프트 모음

## 데이터 분석

```
[CSV 파일 첨부]

이 매출 데이터 분석해줘:
1. 월별 총 매출 계산
2. 전월 대비 성장률
3. TOP 10 상품
4. 국가별 매출 비중 파이 차트
5. 인사이트 정리
```

## 웹 검색

```
2026년 키즈 패션 트렌드 검색해서 정리해줘:
- 주요 트렌드 5가지
- 인기 색상
- 인기 소재
- 주요 브랜드 동향
```

## 컴퓨터 조작

```
Chrome 열어서 google.com 접속해줘
메모장 열어서 오늘 할 일 목록 작성해줘
```

## 파일 편집

```
main.py 파일에서:
1. 모든 print() -> logging.info()로 변경
2. 파일 상단에 import logging 추가
3. 변경 사항 보여줘
```

---

# 8. 문제 해결 가이드

## Code Execution 안 됨
```
해결:
1. 플랜 확인 -> Pro 이상 필요 ($20/월)
2. 설정 -> 기능 -> Code Execution 활성화
3. 브라우저 새로고침
```

## API 키 에러
```
해결:
1. 키가 "sk-ant-api03-"로 시작하는지 확인
2. 환경 변수 설정 확인
3. 새 터미널/IDE 재시작
```

## Computer Use 안 됨
```
해결:
1. Claude Desktop 최신 버전 확인
2. 시스템 권한 확인 (화면 녹화, 접근성)
3. macOS: 시스템 설정 -> 개인 정보 -> 접근성
4. Windows: 관리자 권한으로 실행
```

---

## 가격 정리

### 플랜 가격
| 플랜 | 가격 | 포함 기능 |
|------|------|----------|
| **Claude Free** | $0 | 기본 대화, 웹 검색 |
| **Claude Pro** | $20/월 | + Code Execution, 더 많은 사용량 |
| **Claude Team** | $30/월/인 | + 팀 기능, 관리 도구 |

### API 토큰 가격 (2026년 1월 기준)
| 모델 | 입력 | 출력 |
|------|------|------|
| Claude Opus 4.5 | $15/M | $75/M |
| Claude Sonnet 4.5 | $3/M | $15/M |
| Claude Haiku 4.5 | $0.25/M | $1.25/M |

*M = 1백만 토큰*

---

## 업데이트 로그

| 날짜 | 버전 | 내용 |
|------|------|------|
| 2026-01-30 | v1.0 | 초기 버전 작성 |
| 2026-01-30 | v1.1 | 고급 기능 추가 (Container, Programmatic Tool, Batch API, Extended Thinking) |

---

*Made with Claude by Bella (OZKIZ)*
