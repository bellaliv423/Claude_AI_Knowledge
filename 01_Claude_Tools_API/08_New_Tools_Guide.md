---
tags:
  - claude
  - tools
  - web-fetch
  - tool-search
  - programmatic-tool-calling
---

# Claude 새로운 도구 완벽 가이드
# Claude New Tools Complete Guide

> **작성일 / Created**: 2026-02-26
> **업데이트 / Updated**: 2026-02-26
> **버전 / Version**: 1.0
> **Author**: Bella (OZKIZ) + Claude (Opus 4.6)

---

## 목차 / Table of Contents

1. [소개 / Introduction](#소개--introduction)
2. [Web Fetch Tool](#web-fetch-tool)
3. [Tool Search Tool](#tool-search-tool)
4. [Programmatic Tool Calling](#programmatic-tool-calling)
5. [Fine-grained Tool Streaming](#fine-grained-tool-streaming)
6. [도구 조합 활용 / Combining Tools](#도구-조합-활용--combining-tools)
7. [베스트 프랙티스 / Best Practices](#베스트-프랙티스--best-practices)
8. [FAQ](#faq)
9. [참고 자료 / References](#참고-자료--references)

---

## 소개 / Introduction

Claude API는 2025년 하반기부터 여러 강력한 도구를 새로 도입했습니다.
이 가이드에서는 **Web Fetch**, **Tool Search**, **Programmatic Tool Calling**, **Fine-grained Tool Streaming** 등 최신 도구들을 다룹니다.

### 도구 요약 / Tools Summary

| 도구 | 출시일 | 상태 | 핵심 기능 |
|------|--------|------|----------|
| **Web Fetch** | 2025-09-10 | Beta | 웹페이지/PDF 전체 내용 가져오기 |
| **Tool Search** | 2025-11-24 | Beta | 대규모 도구 카탈로그 동적 검색 |
| **Programmatic Tool Calling** | 2025-11-24 | Beta | 코드 실행 내에서 도구 호출 |
| **Fine-grained Tool Streaming** | 2025-06-11 | Beta | 도구 파라미터 실시간 스트리밍 |

---

## Web Fetch Tool

### 개요 / Overview

**Web Fetch Tool**은 Claude가 웹페이지, PDF, 텍스트 파일의 전체 내용을 직접 가져올 수 있게 해주는 도구입니다. 기존의 Web Search(검색 결과 요약)와 달리, 특정 URL의 **전체 콘텐츠**를 읽어옵니다.

| 항목 | 내용 |
|------|------|
| **출시일** | 2025-09-10 (Beta) |
| **Beta 헤더** | `web-fetch-2025-09-10` |
| **지원 형식** | HTML, PDF, 일반 텍스트 |
| **최대 크기** | 약 500KB (텍스트 기준) |
| **용도** | 문서 분석, 데이터 추출, 코드 참조 |

### 사용 방법 / How to Use

#### Python 기본 사용법

```python
import anthropic

client = anthropic.Anthropic()

response = client.beta.messages.create(
    model="claude-sonnet-4-5-20250929",
    betas=["web-fetch-2025-09-10"],
    max_tokens=4096,
    tools=[{
        "type": "web_fetch",
        "name": "web_fetch"
    }],
    messages=[{
        "role": "user",
        "content": "https://example.com/api-docs 페이지의 내용을 읽고 요약해줘"
    }]
)

print(response.content)
```

#### TypeScript 사용법

```typescript
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic();

const response = await client.beta.messages.create({
  model: "claude-sonnet-4-5-20250929",
  betas: ["web-fetch-2025-09-10"],
  max_tokens: 4096,
  tools: [{
    type: "web_fetch",
    name: "web_fetch"
  }],
  messages: [{
    role: "user",
    content: "https://example.com/api-docs 페이지의 내용을 읽고 요약해줘"
  }]
});
```

#### cURL 사용법

```bash
curl https://api.anthropic.com/v1/messages \
    --header "x-api-key: $ANTHROPIC_API_KEY" \
    --header "anthropic-version: 2023-06-01" \
    --header "anthropic-beta: web-fetch-2025-09-10" \
    --header "content-type: application/json" \
    --data '{
        "model": "claude-sonnet-4-5-20250929",
        "max_tokens": 4096,
        "tools": [{"type": "web_fetch", "name": "web_fetch"}],
        "messages": [{
            "role": "user",
            "content": "https://example.com/docs 를 읽고 요약해줘"
        }]
    }'
```

### Web Fetch vs Web Search 비교

| 비교 항목 | Web Fetch | Web Search |
|-----------|-----------|------------|
| **입력** | 특정 URL | 검색 키워드 |
| **출력** | 페이지 전체 콘텐츠 | 검색 결과 요약 |
| **용도** | 특정 문서 분석 | 정보 탐색 |
| **PDF 지원** | ✅ 전체 내용 추출 | ❌ |
| **최신 정보** | URL에 따라 다름 | 실시간 검색 |

### 실전 예제: 문서 분석 에이전트

```python
import anthropic

client = anthropic.Anthropic()

def analyze_documentation(url: str, question: str) -> str:
    """URL의 문서를 가져와서 질문에 답변"""

    messages = [{
        "role": "user",
        "content": f"{url} 문서를 읽고 다음 질문에 답해줘: {question}"
    }]

    response = client.beta.messages.create(
        model="claude-sonnet-4-5-20250929",
        betas=["web-fetch-2025-09-10"],
        max_tokens=4096,
        tools=[{"type": "web_fetch", "name": "web_fetch"}],
        messages=messages
    )

    # 에이전트 루프: tool_use 응답 처리
    while response.stop_reason == "tool_use":
        tool_results = []
        for block in response.content:
            if block.type == "tool_use":
                # Web Fetch 결과는 자동으로 반환됨
                tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": block.input.get("result", "")
                })

        messages.append({"role": "assistant", "content": response.content})
        messages.append({"role": "user", "content": tool_results})

        response = client.beta.messages.create(
            model="claude-sonnet-4-5-20250929",
            betas=["web-fetch-2025-09-10"],
            max_tokens=4096,
            tools=[{"type": "web_fetch", "name": "web_fetch"}],
            messages=messages
        )

    return response.content[0].text

# 사용
result = analyze_documentation(
    "https://platform.claude.com/docs/en/build-with-claude/tool-use",
    "Tool Use에서 parallel 호출은 어떻게 하나요?"
)
print(result)
```

---

## Tool Search Tool

### 개요 / Overview

**Tool Search Tool**은 수백 개의 도구가 등록된 대규모 카탈로그에서 관련 도구를 동적으로 검색하고 로드할 수 있게 해주는 기능입니다. 모든 도구를 한 번에 컨텍스트에 넣지 않아도 됩니다.

| 항목 | 내용 |
|------|------|
| **출시일** | 2025-11-24 (Beta) |
| **Beta 헤더** | `tool-search-2025-11-24` |
| **용도** | 대규모 도구 관리, 동적 도구 로딩 |
| **장점** | 컨텍스트 절약, 확장성 향상 |

### 왜 Tool Search가 필요한가?

```
기존 방식 (Static):
├── 모든 도구를 messages에 포함
├── 도구 100개 → 컨텍스트 대폭 소비
├── 관련 없는 도구도 포함
└── 확장성 제한

Tool Search 방식 (Dynamic):
├── 필요한 도구만 동적 검색
├── 도구 1000개도 OK
├── 관련 도구만 로드
└── 무한 확장 가능
```

### 사용 방법 / How to Use

#### 도구 정의 (Deferred Tools)

```python
import anthropic

client = anthropic.Anthropic()

# 도구를 "deferred"로 등록
deferred_tools = [
    {
        "type": "custom",
        "name": "get_weather",
        "description": "도시의 현재 날씨를 조회합니다",
        "input_schema": {
            "type": "object",
            "properties": {
                "city": {"type": "string"}
            },
            "required": ["city"]
        }
    },
    {
        "type": "custom",
        "name": "get_stock_price",
        "description": "주식 현재가를 조회합니다",
        "input_schema": {
            "type": "object",
            "properties": {
                "ticker": {"type": "string"}
            },
            "required": ["ticker"]
        }
    },
    # ... 수백 개의 도구 등록 가능
]

# Tool Search를 활성화하여 도구 제공
response = client.beta.messages.create(
    model="claude-sonnet-4-5-20250929",
    betas=["tool-search-2025-11-24"],
    max_tokens=4096,
    tools=[
        {
            "type": "tool_search",
            "name": "tool_search",
            "deferred_tools": deferred_tools
        }
    ],
    messages=[{
        "role": "user",
        "content": "서울 날씨 어때?"
    }]
)
```

### 동작 방식

```
1. 사용자 요청 수신
   └── "서울 날씨 어때?"

2. Claude가 Tool Search 실행
   └── 키워드: "날씨", "weather"
   └── 매칭된 도구: get_weather

3. 도구 로드 및 호출
   └── get_weather(city="서울")
   └── 결과 반환

4. 최종 응답 생성
   └── "서울의 현재 날씨는..."
```

### 실전 예제: 다기능 어시스턴트

```python
import anthropic

client = anthropic.Anthropic()

# 다양한 도메인의 도구 등록
all_tools = [
    # 날씨 도구
    {"type": "custom", "name": "get_weather", "description": "현재 날씨 조회", ...},
    {"type": "custom", "name": "get_forecast", "description": "주간 날씨 예보", ...},

    # 금융 도구
    {"type": "custom", "name": "get_stock_price", "description": "주식 현재가", ...},
    {"type": "custom", "name": "get_exchange_rate", "description": "환율 조회", ...},

    # 일정 도구
    {"type": "custom", "name": "create_event", "description": "캘린더 이벤트 생성", ...},
    {"type": "custom", "name": "list_events", "description": "캘린더 이벤트 목록", ...},

    # 이메일 도구
    {"type": "custom", "name": "send_email", "description": "이메일 발송", ...},
    {"type": "custom", "name": "read_inbox", "description": "받은편지함 읽기", ...},

    # ... 100개 이상의 도구
]

response = client.beta.messages.create(
    model="claude-sonnet-4-5-20250929",
    betas=["tool-search-2025-11-24"],
    max_tokens=4096,
    tools=[{
        "type": "tool_search",
        "name": "tool_search",
        "deferred_tools": all_tools
    }],
    messages=[{
        "role": "user",
        "content": "다음 주 월요일에 '팀 미팅' 일정을 잡고, 팀원들에게 이메일로 알려줘"
    }]
)
# Claude가 자동으로 create_event + send_email 도구를 찾아 사용
```

---

## Programmatic Tool Calling

### 개요 / Overview

**Programmatic Tool Calling**은 Claude의 코드 실행 환경 내에서 직접 도구를 호출할 수 있게 해주는 기능입니다. 기존 방식과 달리, Claude가 코드 블록 안에서 프로그래밍적으로 도구를 사용합니다.

| 항목 | 내용 |
|------|------|
| **출시일** | 2025-11-24 (Beta) |
| **Beta 헤더** | `programmatic-tool-calling-2025-11-24` |
| **장점** | 지연시간 감소, 토큰 절약, 복잡한 로직 처리 |
| **요구사항** | Code Execution 활성화 필요 |

### 기존 방식 vs Programmatic 방식

```
기존 방식 (왕복):
  사용자 → Claude → [tool_use] → 서버 → [tool_result] → Claude → 응답
  = 여러 번의 API 호출 왕복

Programmatic 방식 (코드 내):
  사용자 → Claude → [코드 실행 + 도구 호출] → 응답
  = 한 번의 실행에서 도구 호출까지 처리
```

### 사용 방법 / How to Use

```python
import anthropic

client = anthropic.Anthropic()

# 도구를 programmatic으로 등록
tools = [
    {
        "type": "custom",
        "name": "calculate_tax",
        "description": "세금 계산",
        "input_schema": {
            "type": "object",
            "properties": {
                "income": {"type": "number"},
                "country": {"type": "string"}
            },
            "required": ["income", "country"]
        }
    },
    {
        "type": "custom",
        "name": "get_exchange_rate",
        "description": "환율 조회",
        "input_schema": {
            "type": "object",
            "properties": {
                "from_currency": {"type": "string"},
                "to_currency": {"type": "string"}
            },
            "required": ["from_currency", "to_currency"]
        }
    }
]

response = client.beta.messages.create(
    model="claude-sonnet-4-5-20250929",
    betas=["programmatic-tool-calling-2025-11-24"],
    max_tokens=4096,
    tools=tools,
    messages=[{
        "role": "user",
        "content": "연봉 1억원의 한국 세금을 계산하고, 세후 소득을 USD로 변환해줘"
    }]
)
```

### 장점 비교

| 항목 | 기존 Tool Use | Programmatic Tool Calling |
|------|--------------|--------------------------|
| **API 왕복** | 도구마다 1회 | 코드 내 일괄 처리 |
| **지연시간** | 높음 (왕복마다) | 낮음 (한 번에 처리) |
| **토큰 사용** | 높음 (매번 컨텍스트) | 낮음 (코드 내 처리) |
| **복잡한 로직** | 어려움 | 코드로 자유롭게 |
| **조건부 호출** | 불편 | if/else로 간단히 |
| **반복 호출** | 비효율적 | for 루프로 효율적 |

### 실전 예제: 복합 데이터 분석

```python
import anthropic

client = anthropic.Anthropic()

tools = [
    {
        "type": "custom",
        "name": "query_database",
        "description": "데이터베이스 쿼리 실행",
        "input_schema": {
            "type": "object",
            "properties": {
                "sql": {"type": "string"},
                "database": {"type": "string"}
            },
            "required": ["sql", "database"]
        }
    },
    {
        "type": "custom",
        "name": "create_chart",
        "description": "차트 생성",
        "input_schema": {
            "type": "object",
            "properties": {
                "data": {"type": "object"},
                "chart_type": {"type": "string"}
            },
            "required": ["data", "chart_type"]
        }
    }
]

# Claude가 코드 내에서:
# 1. 데이터 조회 (query_database)
# 2. 결과 가공 (Python 코드)
# 3. 차트 생성 (create_chart)
# 이 모든 것을 한 번의 실행에서 처리
response = client.beta.messages.create(
    model="claude-sonnet-4-5-20250929",
    betas=["programmatic-tool-calling-2025-11-24"],
    max_tokens=4096,
    tools=tools,
    messages=[{
        "role": "user",
        "content": "지난 6개월 매출 데이터를 조회하고, 월별 추이 차트를 만들어줘"
    }]
)
```

---

## Fine-grained Tool Streaming

### 개요 / Overview

**Fine-grained Tool Streaming**은 도구 호출 시 파라미터가 생성되는 대로 실시간으로 스트리밍하는 기능입니다.

| 항목 | 내용 |
|------|------|
| **출시일** | 2025-06-11 (Beta) |
| **Beta 헤더** | `fine-grained-tool-streaming-2025-05-14` |
| **용도** | 긴 도구 파라미터의 실시간 표시 |
| **장점** | 사용자 경험 개선, 진행 상황 확인 |

### 사용 방법 / How to Use

```python
import anthropic

client = anthropic.Anthropic()

# 스트리밍 활성화
with client.beta.messages.stream(
    model="claude-sonnet-4-5-20250929",
    betas=["fine-grained-tool-streaming-2025-05-14"],
    max_tokens=4096,
    tools=[{
        "type": "custom",
        "name": "write_code",
        "description": "코드 파일 생성",
        "input_schema": {
            "type": "object",
            "properties": {
                "filename": {"type": "string"},
                "code": {"type": "string"}
            },
            "required": ["filename", "code"]
        }
    }],
    messages=[{
        "role": "user",
        "content": "Python으로 웹 스크래퍼를 작성해줘"
    }]
) as stream:
    for event in stream:
        if event.type == "content_block_delta":
            if hasattr(event.delta, "partial_json"):
                # 도구 파라미터가 실시간으로 스트리밍됨
                print(event.delta.partial_json, end="", flush=True)
            elif hasattr(event.delta, "text"):
                print(event.delta.text, end="", flush=True)
```

### 기존 스트리밍과 비교

| 항목 | 기존 스트리밍 | Fine-grained Streaming |
|------|-------------|----------------------|
| **텍스트** | 실시간 | 실시간 |
| **도구 파라미터** | 완료 후 한 번에 | **실시간 조각별** |
| **긴 코드 생성** | 대기 후 표시 | 작성 중 실시간 표시 |
| **사용자 경험** | 도구 호출 시 멈춤 | 연속적 피드백 |

---

## 도구 조합 활용 / Combining Tools

### Web Fetch + Tool Search

```python
# 대규모 도구 카탈로그 + 웹 콘텐츠 분석
response = client.beta.messages.create(
    model="claude-sonnet-4-5-20250929",
    betas=["web-fetch-2025-09-10", "tool-search-2025-11-24"],
    max_tokens=4096,
    tools=[
        {"type": "web_fetch", "name": "web_fetch"},
        {
            "type": "tool_search",
            "name": "tool_search",
            "deferred_tools": analysis_tools
        }
    ],
    messages=[{
        "role": "user",
        "content": "이 URL의 데이터를 분석해줘: https://example.com/data.csv"
    }]
)
```

### 모든 도구 동시 활용

```python
response = client.beta.messages.create(
    model="claude-sonnet-4-5-20250929",
    betas=[
        "web-fetch-2025-09-10",
        "tool-search-2025-11-24",
        "programmatic-tool-calling-2025-11-24",
        "fine-grained-tool-streaming-2025-05-14"
    ],
    max_tokens=4096,
    tools=[
        {"type": "web_fetch", "name": "web_fetch"},
        {
            "type": "tool_search",
            "name": "tool_search",
            "deferred_tools": all_tools
        }
    ],
    messages=[{
        "role": "user",
        "content": "복합 작업 요청"
    }]
)
```

---

## 베스트 프랙티스 / Best Practices

### 1. Web Fetch 사용 시

```
✅ 권장:
├── 특정 URL의 문서 분석에 사용
├── PDF, API 문서 등 구조화된 콘텐츠에 적합
├── 에러 핸들링 포함 (URL 접근 불가 시)
└── 결과 크기 확인 (500KB 제한)

❌ 피할 것:
├── 일반 검색 대용으로 사용 (→ Web Search 사용)
├── 동적 JavaScript 렌더링 페이지 (제한적)
├── 로그인 필요한 페이지
└── 매우 큰 파일 다운로드
```

### 2. Tool Search 사용 시

```
✅ 권장:
├── 도구가 10개 이상일 때 사용
├── 도구 설명을 명확하고 구체적으로 작성
├── 카테고리별 그룹핑 고려
└── 자주 사용하는 도구는 직접 포함

❌ 피할 것:
├── 도구 수가 적을 때 (직접 포함이 나음)
├── 모호한 도구 설명
└── 동일 기능의 중복 도구
```

### 3. Programmatic Tool Calling 사용 시

```
✅ 권장:
├── 여러 도구를 연속 호출해야 할 때
├── 조건부 로직이 필요할 때
├── 반복 처리가 필요할 때
└── 중간 데이터 가공이 필요할 때

❌ 피할 것:
├── 단일 도구 호출 (기존 방식이 간단)
├── 도구 간 의존성이 없는 경우
└── 디버깅이 어려운 복잡한 중첩
```

---

## FAQ

### Q1: Web Fetch로 어떤 사이트든 접근할 수 있나요?

공개된 웹페이지에 접근 가능합니다. 로그인이 필요하거나 robots.txt로 차단된 사이트, JavaScript 렌더링이 필요한 SPA는 제한될 수 있습니다.

### Q2: Tool Search에 등록할 수 있는 도구 수 제한이 있나요?

명시적 상한은 없지만, 수천 개까지 효과적으로 사용 가능합니다. 도구 설명이 명확할수록 검색 정확도가 높아집니다.

### Q3: Programmatic Tool Calling은 Code Execution이 필요한가요?

네, 코드 실행 환경이 활성화되어 있어야 합니다. Claude Pro 이상의 구독에서 사용 가능합니다.

### Q4: 여러 Beta 기능을 동시에 사용할 수 있나요?

네, `betas` 배열에 여러 Beta 헤더를 포함하면 됩니다:
```python
betas=[
    "web-fetch-2025-09-10",
    "tool-search-2025-11-24",
    "programmatic-tool-calling-2025-11-24"
]
```

### Q5: 이 기능들이 GA(정식 출시)되면 Beta 헤더가 필요 없어지나요?

맞습니다. GA 이후에는 Beta 헤더 없이 바로 사용할 수 있으며, API 파라미터 구조가 약간 변경될 수 있습니다.

---

## 참고 자료 / References

### 공식 문서
- [Web Fetch Tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool)
- [Tool Search Tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool)
- [Programmatic Tool Calling](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling)
- [Tool Use Overview](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)

### 이 프로젝트의 관련 문서
- [01_Claude_Tools_Complete_Guide.md](./01_Claude_Tools_Complete_Guide.md) - 도구 종합 가이드
- [03_MCP_Usage_Guide.md](./03_MCP_Usage_Guide.md) - MCP 활용 가이드
- [07_Effort_Parameter_Guide.md](./07_Effort_Parameter_Guide.md) - Effort 파라미터

---

## 업데이트 로그 / Changelog

| 날짜 | 버전 | 내용 |
|------|------|------|
| 2026-02-26 | v1.0 | 초기 버전 작성 |

---

*Made with Claude by Bella (OZKIZ)*
