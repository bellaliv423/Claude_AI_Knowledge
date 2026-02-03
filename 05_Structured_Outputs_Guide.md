# Structured Outputs 완벽 가이드
# Structured Outputs Complete Guide

> **작성일 / Created**: 2026-02-03
> **업데이트 / Updated**: 2026-02-03
> **버전 / Version**: 1.0
> **Author**: Bella (OZKIZ) + Claude (Opus 4.5)

---

## 목차 / Table of Contents

1. [소개 / Introduction](#소개--introduction)
2. [주요 특징 / Key Features](#주요-특징--key-features)
3. [사용 방법 / How to Use](#사용-방법--how-to-use)
4. [JSON 스키마 작성법 / JSON Schema Writing](#json-스키마-작성법--json-schema-writing)
5. [실전 예제 / Practical Examples](#실전-예제--practical-examples)
6. [마이그레이션 가이드 / Migration Guide](#마이그레이션-가이드--migration-guide)
7. [주의사항 및 제한 / Limitations](#주의사항-및-제한--limitations)
8. [FAQ](#faq)
9. [참고 자료 / References](#참고-자료--references)

---

## 소개 / Introduction

### Structured Outputs란?

**Structured Outputs**는 Claude API가 **JSON 스키마를 100% 보장**하여 응답을 반환하는 기능입니다.
기존의 JSON 모드와 달리, 사용자가 정의한 스키마에 정확히 맞는 구조화된 데이터를 생성합니다.

| 항목 | 내용 |
|------|------|
| **출시일** | 2026-01-29 (GA - 정식 출시) |
| **이전 상태** | Beta (2025-05부터) |
| **지원 모델** | Claude Sonnet 4.5, Opus 4.5, Haiku 4.5 |
| **주요 변경** | `output_format` → `output_config.format` |

### 왜 Structured Outputs를 사용해야 하나요?

1. **100% 스키마 보장**: 정의한 JSON 스키마에 정확히 맞는 응답
2. **파싱 오류 제거**: 더 이상 JSON 파싱 에러 걱정 없음
3. **타입 안정성**: 필드 타입이 항상 일치
4. **개발 생산성**: 복잡한 검증 로직 불필요

---

## 주요 특징 / Key Features

### 1. JSON Schema 지원

표준 JSON Schema (Draft 2020-12)를 지원합니다.

```json
{
  "type": "object",
  "properties": {
    "name": { "type": "string" },
    "age": { "type": "integer" },
    "email": { "type": "string", "format": "email" }
  },
  "required": ["name", "age"]
}
```

### 2. 중첩 객체 지원

복잡한 중첩 구조도 완벽하게 지원합니다.

```json
{
  "type": "object",
  "properties": {
    "user": {
      "type": "object",
      "properties": {
        "profile": {
          "type": "object",
          "properties": {
            "name": { "type": "string" }
          }
        }
      }
    }
  }
}
```

### 3. 배열 및 Enum 지원

```json
{
  "type": "object",
  "properties": {
    "tags": {
      "type": "array",
      "items": { "type": "string" }
    },
    "status": {
      "type": "string",
      "enum": ["pending", "approved", "rejected"]
    }
  }
}
```

---

## 사용 방법 / How to Use

### 기본 구조

```python
import anthropic

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-opus-4-5-20251101",
    max_tokens=1024,
    output_config={
        "format": {
            "type": "json_schema",
            "json_schema": {
                "name": "response_schema",
                "schema": {
                    "type": "object",
                    "properties": {
                        "answer": { "type": "string" },
                        "confidence": { "type": "number" }
                    },
                    "required": ["answer", "confidence"]
                }
            }
        }
    },
    messages=[
        {"role": "user", "content": "파이썬의 장점을 알려주세요."}
    ]
)

# 응답은 항상 정의된 스키마를 따름
import json
result = json.loads(response.content[0].text)
print(result["answer"])
print(result["confidence"])
```

### 파라미터 설명

| 파라미터 | 설명 |
|----------|------|
| `output_config` | 출력 설정 객체 |
| `output_config.format` | 출력 형식 설정 |
| `format.type` | `"json_schema"` 고정 |
| `format.json_schema.name` | 스키마 이름 (필수) |
| `format.json_schema.schema` | JSON Schema 정의 (필수) |

---

## JSON 스키마 작성법 / JSON Schema Writing

### 기본 타입

```python
# 문자열
{"type": "string"}

# 숫자 (정수)
{"type": "integer"}

# 숫자 (실수 포함)
{"type": "number"}

# 불리언
{"type": "boolean"}

# Null
{"type": "null"}

# 배열
{"type": "array", "items": {"type": "string"}}

# 객체
{"type": "object", "properties": {...}}
```

### 제약 조건

```python
# 문자열 길이 제한
{
    "type": "string",
    "minLength": 1,
    "maxLength": 100
}

# 숫자 범위 제한
{
    "type": "integer",
    "minimum": 0,
    "maximum": 100
}

# 배열 길이 제한
{
    "type": "array",
    "items": {"type": "string"},
    "minItems": 1,
    "maxItems": 10
}

# Enum (선택지 제한)
{
    "type": "string",
    "enum": ["low", "medium", "high"]
}
```

### 필수 필드 지정

```python
{
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "email": {"type": "string"},
        "age": {"type": "integer"}
    },
    "required": ["name", "email"]  # name과 email은 필수
}
```

---

## 실전 예제 / Practical Examples

### 예제 1: 감정 분석 API

```python
import anthropic
import json

client = anthropic.Anthropic()

def analyze_sentiment(text: str) -> dict:
    """텍스트 감정 분석"""

    response = client.messages.create(
        model="claude-opus-4-5-20251101",
        max_tokens=512,
        output_config={
            "format": {
                "type": "json_schema",
                "json_schema": {
                    "name": "sentiment_analysis",
                    "schema": {
                        "type": "object",
                        "properties": {
                            "sentiment": {
                                "type": "string",
                                "enum": ["positive", "negative", "neutral"]
                            },
                            "confidence": {
                                "type": "number",
                                "minimum": 0,
                                "maximum": 1
                            },
                            "keywords": {
                                "type": "array",
                                "items": {"type": "string"},
                                "maxItems": 5
                            },
                            "summary": {
                                "type": "string",
                                "maxLength": 200
                            }
                        },
                        "required": ["sentiment", "confidence", "keywords", "summary"]
                    }
                }
            }
        },
        messages=[
            {"role": "user", "content": f"다음 텍스트의 감정을 분석해주세요:\n\n{text}"}
        ]
    )

    return json.loads(response.content[0].text)

# 사용 예시
result = analyze_sentiment("오늘 정말 좋은 하루였어요! 친구들과 맛있는 점심도 먹고.")
print(f"감정: {result['sentiment']}")
print(f"신뢰도: {result['confidence']}")
print(f"키워드: {result['keywords']}")
```

### 예제 2: 데이터 추출

```python
def extract_contact_info(text: str) -> dict:
    """텍스트에서 연락처 정보 추출"""

    response = client.messages.create(
        model="claude-sonnet-4-5-20250929",
        max_tokens=512,
        output_config={
            "format": {
                "type": "json_schema",
                "json_schema": {
                    "name": "contact_extraction",
                    "schema": {
                        "type": "object",
                        "properties": {
                            "name": {"type": "string"},
                            "email": {"type": "string"},
                            "phone": {"type": "string"},
                            "company": {"type": "string"},
                            "position": {"type": "string"},
                            "found_fields": {
                                "type": "array",
                                "items": {"type": "string"}
                            }
                        },
                        "required": ["found_fields"]
                    }
                }
            }
        },
        messages=[
            {"role": "user", "content": f"다음 텍스트에서 연락처 정보를 추출해주세요:\n\n{text}"}
        ]
    )

    return json.loads(response.content[0].text)

# 사용 예시
text = """
안녕하세요, 김철수입니다.
ABC 회사의 개발팀장으로 일하고 있습니다.
연락처: kim@abc.com / 010-1234-5678
"""
result = extract_contact_info(text)
print(result)
```

### 예제 3: 코드 리뷰 분석

```python
def review_code(code: str) -> dict:
    """코드 리뷰 결과 생성"""

    response = client.messages.create(
        model="claude-opus-4-5-20251101",
        max_tokens=2048,
        output_config={
            "format": {
                "type": "json_schema",
                "json_schema": {
                    "name": "code_review",
                    "schema": {
                        "type": "object",
                        "properties": {
                            "overall_quality": {
                                "type": "string",
                                "enum": ["excellent", "good", "acceptable", "needs_improvement", "poor"]
                            },
                            "score": {
                                "type": "integer",
                                "minimum": 0,
                                "maximum": 100
                            },
                            "issues": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "properties": {
                                        "severity": {
                                            "type": "string",
                                            "enum": ["critical", "warning", "suggestion"]
                                        },
                                        "line": {"type": "integer"},
                                        "message": {"type": "string"},
                                        "fix_suggestion": {"type": "string"}
                                    },
                                    "required": ["severity", "message"]
                                }
                            },
                            "summary": {"type": "string"}
                        },
                        "required": ["overall_quality", "score", "issues", "summary"]
                    }
                }
            }
        },
        messages=[
            {"role": "user", "content": f"다음 코드를 리뷰해주세요:\n\n```python\n{code}\n```"}
        ]
    )

    return json.loads(response.content[0].text)
```

### 예제 4: 비동기 (Async) 사용

```python
import anthropic
import asyncio
import json

async def analyze_async(text: str) -> dict:
    """비동기 분석"""

    client = anthropic.AsyncAnthropic()

    response = await client.messages.create(
        model="claude-sonnet-4-5-20250929",
        max_tokens=512,
        output_config={
            "format": {
                "type": "json_schema",
                "json_schema": {
                    "name": "analysis",
                    "schema": {
                        "type": "object",
                        "properties": {
                            "result": {"type": "string"},
                            "score": {"type": "number"}
                        },
                        "required": ["result", "score"]
                    }
                }
            }
        },
        messages=[
            {"role": "user", "content": text}
        ]
    )

    return json.loads(response.content[0].text)

# 여러 요청 병렬 처리
async def main():
    texts = ["텍스트1", "텍스트2", "텍스트3"]
    results = await asyncio.gather(*[analyze_async(t) for t in texts])
    return results

results = asyncio.run(main())
```

---

## 마이그레이션 가이드 / Migration Guide

### Beta에서 GA로 마이그레이션

**이전 (Beta):**
```python
response = client.messages.create(
    model="claude-opus-4-5-20251101",
    max_tokens=1024,
    output_format={  # 이전 방식
        "type": "json_schema",
        "json_schema": {...}
    },
    messages=[...]
)
```

**현재 (GA):**
```python
response = client.messages.create(
    model="claude-opus-4-5-20251101",
    max_tokens=1024,
    output_config={  # 새로운 방식
        "format": {
            "type": "json_schema",
            "json_schema": {...}
        }
    },
    messages=[...]
)
```

### 주요 변경 사항

| 이전 | 현재 |
|------|------|
| `output_format` | `output_config.format` |
| Beta 헤더 필요 | 헤더 불필요 |
| 일부 모델만 지원 | Sonnet/Opus/Haiku 4.5 전체 지원 |

---

## 주의사항 및 제한 / Limitations

### 지원되지 않는 기능

1. **$ref / definitions**: 스키마 참조 미지원
2. **anyOf / oneOf / allOf**: 복합 타입 미지원
3. **additionalProperties**: 동적 속성 미지원
4. **patternProperties**: 패턴 기반 속성 미지원

### 제한 사항

| 항목 | 제한 |
|------|------|
| 스키마 최대 깊이 | 10 레벨 |
| 속성 최대 개수 | 100개 |
| 배열 최대 아이템 | 스키마에서 지정 |

### 비용 고려사항

- Structured Outputs 사용 시 약간의 추가 토큰 소모
- 복잡한 스키마일수록 응답 생성에 더 많은 토큰 필요
- **권장**: 필요한 필드만 정의하여 비용 최적화

---

## FAQ

### Q1: Structured Outputs와 기존 JSON 모드의 차이점?

| 항목 | JSON 모드 | Structured Outputs |
|------|----------|-------------------|
| 스키마 보장 | X | O (100%) |
| 타입 검증 | X | O |
| 필수 필드 보장 | X | O |
| 사용 편의성 | 높음 | 매우 높음 |

### Q2: 스트리밍과 함께 사용 가능한가요?

네, 가능합니다:

```python
with client.messages.stream(
    model="claude-opus-4-5-20251101",
    max_tokens=1024,
    output_config={
        "format": {
            "type": "json_schema",
            "json_schema": {...}
        }
    },
    messages=[...]
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)
```

### Q3: Extended Thinking과 함께 사용 가능한가요?

네, 함께 사용 가능합니다:

```python
response = client.messages.create(
    model="claude-opus-4-5-20251101",
    max_tokens=16000,
    thinking={
        "type": "enabled",
        "budget_tokens": 10000
    },
    output_config={
        "format": {
            "type": "json_schema",
            "json_schema": {...}
        }
    },
    messages=[...]
)
```

### Q4: 스키마 검증 실패 시 어떻게 되나요?

Claude는 스키마를 항상 준수하므로 검증 실패가 발생하지 않습니다.
만약 요청 자체의 스키마가 잘못되었다면 API 에러가 발생합니다.

---

## 참고 자료 / References

### 공식 문서
- [Structured Outputs 문서](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)
- [API Reference](https://platform.claude.com/docs/en/api/messages)
- [JSON Schema 표준](https://json-schema.org/)

### 관련 문서
- [01_Claude_Tools_Complete_Guide.md](./01_Claude_Tools_Complete_Guide.md)
- [NEW_FEATURES_TODO_2026.md](./NEW_FEATURES_TODO_2026.md)

---

## 업데이트 로그 / Changelog

| 날짜 | 버전 | 내용 |
|------|------|------|
| 2026-02-03 | v1.0 | 초기 버전 작성 |

---

*Made with Claude by Bella (OZKIZ)*
