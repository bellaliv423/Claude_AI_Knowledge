---
tags:
  - claude
  - effort
  - optimization
  - opus
---

# Effort Parameter 완벽 가이드
# Effort Parameter Complete Guide

> **작성일 / Created**: 2026-02-05
> **업데이트 / Updated**: 2026-02-05
> **버전 / Version**: 1.0
> **Author**: Bella (OZKIZ) + Claude (Opus 4.5)

---

## 목차 / Table of Contents

1. [소개 / Introduction](#소개--introduction)
2. [Effort 레벨 / Effort Levels](#effort-레벨--effort-levels)
3. [사용 방법 / How to Use](#사용-방법--how-to-use)
4. [성능 비교 / Performance Comparison](#성능-비교--performance-comparison)
5. [Tool Use와 함께 사용 / With Tool Use](#tool-use와-함께-사용--with-tool-use)
6. [Extended Thinking과 함께 사용 / With Extended Thinking](#extended-thinking과-함께-사용--with-extended-thinking)
7. [실전 예제 / Practical Examples](#실전-예제--practical-examples)
8. [비용 최적화 전략 / Cost Optimization](#비용-최적화-전략--cost-optimization)
9. [베스트 프랙티스 / Best Practices](#베스트-프랙티스--best-practices)
10. [FAQ](#faq)
11. [참고 자료 / References](#참고-자료--references)

---

## 소개 / Introduction

### Effort Parameter란?

**Effort Parameter**는 Claude가 응답에 사용하는 토큰 양을 제어하는 기능입니다.
응답의 철저함과 토큰 효율성 사이의 균형을 조절할 수 있습니다.

| 항목 | 내용 |
|------|------|
| **출시일** | 2025-11-24 (Beta) |
| **지원 모델** | Claude Opus 4.5 **전용** |
| **Beta 헤더** | `effort-2025-11-24` |
| **기본값** | `high` (최대 성능) |

### 왜 Effort Parameter를 사용해야 하나요?

1. **비용 절감**: 76%까지 토큰 사용량 감소 가능
2. **속도 향상**: 적은 토큰 = 빠른 응답
3. **유연한 제어**: 작업 복잡도에 따라 조절
4. **단일 모델**: Opus 4.5 하나로 다양한 성능 레벨 구현

### Effort가 영향을 미치는 범위

Effort Parameter는 **모든 토큰**에 영향을 줍니다:

- ✅ 텍스트 응답 및 설명
- ✅ Tool 호출 및 함수 인자
- ✅ Extended Thinking (활성화된 경우)

---

## Effort 레벨 / Effort Levels

### 세 가지 레벨

| 레벨 | 설명 | 사용 사례 |
|------|------|----------|
| **`high`** | 최대 성능. 최상의 결과를 위해 필요한 만큼 토큰 사용. 기본값. | 복잡한 추론, 어려운 코딩, 에이전트 작업 |
| **`medium`** | 균형 잡힌 접근. 적절한 토큰 절약. | 성능과 비용의 균형이 필요한 작업 |
| **`low`** | 가장 효율적. 상당한 토큰 절약, 약간의 성능 감소. | 단순 분류, 빠른 조회, 대량 처리 |

### 레벨별 특성

```
High (기본값)
├── 최대 토큰 사용
├── 최상의 품질
├── 상세한 설명
├── 여러 번의 Tool 호출
└── 종합적인 코드 주석

Medium
├── 적절한 토큰 사용
├── 좋은 품질 유지
├── 핵심 내용 중심
└── 효율적인 Tool 호출

Low
├── 최소 토큰 사용
├── 빠른 응답
├── 간결한 출력
├── 최소 Tool 호출
└── 대량 처리에 적합
```

---

## 사용 방법 / How to Use

### 기본 사용법 (Python)

```python
import anthropic

client = anthropic.Anthropic()

response = client.beta.messages.create(
    model="claude-opus-4-5-20251101",
    betas=["effort-2025-11-24"],  # Beta 헤더 필수!
    max_tokens=4096,
    messages=[{
        "role": "user",
        "content": "마이크로서비스와 모놀리식 아키텍처의 장단점을 분석해줘"
    }],
    output_config={
        "effort": "medium"  # low, medium, high
    }
)

print(response.content[0].text)
```

### TypeScript 사용법

```typescript
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic();

const response = await client.beta.messages.create({
  model: "claude-opus-4-5-20251101",
  betas: ["effort-2025-11-24"],
  max_tokens: 4096,
  messages: [{
    role: "user",
    content: "마이크로서비스와 모놀리식 아키텍처의 장단점을 분석해줘"
  }],
  output_config: {
    effort: "medium"
  }
});

console.log(response.content[0].text);
```

### cURL 사용법

```bash
curl https://api.anthropic.com/v1/messages \
    --header "x-api-key: $ANTHROPIC_API_KEY" \
    --header "anthropic-version: 2023-06-01" \
    --header "anthropic-beta: effort-2025-11-24" \
    --header "content-type: application/json" \
    --data '{
        "model": "claude-opus-4-5-20251101",
        "max_tokens": 4096,
        "messages": [{
            "role": "user",
            "content": "마이크로서비스와 모놀리식 아키텍처의 장단점을 분석해줘"
        }],
        "output_config": {
            "effort": "medium"
        }
    }'
```

### 중요 파라미터 설명

| 파라미터 | 설명 | 필수 |
|----------|------|------|
| `betas` | `["effort-2025-11-24"]` 포함 필수 | ✅ |
| `model` | `claude-opus-4-5-20251101` 만 지원 | ✅ |
| `output_config.effort` | `"low"`, `"medium"`, `"high"` | ❌ (기본: high) |

---

## 성능 비교 / Performance Comparison

### SWE-bench Verified 벤치마크

| 설정 | 점수 | 토큰 사용량 | 비교 |
|------|------|-----------|------|
| **Opus 4.5 (high)** | Sonnet 4.5 + 4.3% | 52% 절약 | 최고 성능 |
| **Opus 4.5 (medium)** | Sonnet 4.5 동일 | **76% 절약** | 최고 효율 |
| **Opus 4.5 (low)** | - | 최대 절약 | 단순 작업용 |
| Sonnet 4.5 | 기준 | 기준 | - |

### 핵심 인사이트

```
🎯 Medium Effort의 놀라운 효율성:
   - Sonnet 4.5와 동일한 성능
   - 76% 적은 토큰 사용
   - = 비용 76% 절감!

🚀 High Effort의 최고 성능:
   - Sonnet 4.5보다 4.3% 높은 성능
   - 48% 적은 토큰 사용
   - = 더 좋은 결과 + 비용 절감
```

---

## Tool Use와 함께 사용 / With Tool Use

### Effort가 Tool 호출에 미치는 영향

**Low Effort**:
- 여러 작업을 적은 Tool 호출로 통합
- Tool 호출 횟수 감소
- 설명 없이 바로 실행
- 완료 후 간결한 확인 메시지

**High Effort**:
- 더 많은 Tool 호출
- 실행 전 계획 설명
- 변경사항 상세 요약
- 종합적인 코드 주석

### 예제: Tool Use + Effort

```python
import anthropic

client = anthropic.Anthropic()

tools = [
    {
        "name": "get_weather",
        "description": "현재 날씨 정보를 가져옵니다",
        "input_schema": {
            "type": "object",
            "properties": {
                "location": {"type": "string", "description": "도시 이름"}
            },
            "required": ["location"]
        }
    },
    {
        "name": "get_forecast",
        "description": "주간 예보를 가져옵니다",
        "input_schema": {
            "type": "object",
            "properties": {
                "location": {"type": "string", "description": "도시 이름"},
                "days": {"type": "integer", "description": "예보 일수"}
            },
            "required": ["location"]
        }
    }
]

# Low effort: 최소한의 Tool 호출
response = client.beta.messages.create(
    model="claude-opus-4-5-20251101",
    betas=["effort-2025-11-24"],
    max_tokens=1024,
    tools=tools,
    messages=[{
        "role": "user",
        "content": "서울 날씨 알려줘"
    }],
    output_config={
        "effort": "low"
    }
)

# High effort: 상세한 Tool 호출 + 설명
response = client.beta.messages.create(
    model="claude-opus-4-5-20251101",
    betas=["effort-2025-11-24"],
    max_tokens=1024,
    tools=tools,
    messages=[{
        "role": "user",
        "content": "서울 날씨 알려줘"
    }],
    output_config={
        "effort": "high"
    }
)
```

---

## Extended Thinking과 함께 사용 / With Extended Thinking

### 두 가지 제어의 차이

| 제어 | 역할 | 범위 |
|------|------|------|
| **Effort Parameter** | 모든 토큰 사용량 제어 | Thinking + 응답 + Tool |
| **Thinking Budget** | Thinking 토큰 최대 한도 | Thinking만 |

### 함께 사용할 때

1. 먼저 작업에 적합한 **Effort 레벨** 결정
2. 그 다음 작업 복잡도에 따라 **Thinking Budget** 설정

### 예제: Effort + Extended Thinking

```python
import anthropic

client = anthropic.Anthropic()

# 복잡한 추론 작업: High effort + 높은 thinking budget
response = client.beta.messages.create(
    model="claude-opus-4-5-20251101",
    betas=["effort-2025-11-24"],
    max_tokens=16000,
    thinking={
        "type": "enabled",
        "budget_tokens": 10000  # Thinking 토큰 한도
    },
    messages=[{
        "role": "user",
        "content": "복잡한 수학 증명을 해줘"
    }],
    output_config={
        "effort": "high"  # 최대 성능
    }
)

# 적절한 추론 작업: Medium effort + 적당한 thinking budget
response = client.beta.messages.create(
    model="claude-opus-4-5-20251101",
    betas=["effort-2025-11-24"],
    max_tokens=8000,
    thinking={
        "type": "enabled",
        "budget_tokens": 5000
    },
    messages=[{
        "role": "user",
        "content": "이 코드의 버그를 찾아줘"
    }],
    output_config={
        "effort": "medium"  # 균형 잡힌 접근
    }
)
```

### 권장 조합

| 작업 유형 | Effort | Thinking Budget |
|----------|--------|-----------------|
| 복잡한 추론/증명 | `high` | 높음 (10000+) |
| 코드 디버깅 | `medium` | 중간 (5000) |
| 간단한 분석 | `low` | 낮음 (2000) |
| 단순 분류 | `low` | 비활성화 |

---

## 실전 예제 / Practical Examples

### 예제 1: 작업 복잡도에 따른 동적 Effort

```python
import anthropic

client = anthropic.Anthropic()

def analyze_with_dynamic_effort(task: str, complexity: str) -> str:
    """작업 복잡도에 따라 Effort 레벨 자동 조절"""

    effort_map = {
        "simple": "low",
        "moderate": "medium",
        "complex": "high"
    }

    response = client.beta.messages.create(
        model="claude-opus-4-5-20251101",
        betas=["effort-2025-11-24"],
        max_tokens=4096,
        messages=[{"role": "user", "content": task}],
        output_config={
            "effort": effort_map.get(complexity, "medium")
        }
    )

    return response.content[0].text

# 사용 예시
# 단순 작업 - low effort
result = analyze_with_dynamic_effort(
    "이 텍스트의 감정이 긍정/부정/중립인지 분류해줘: 오늘 날씨가 좋네요",
    "simple"
)

# 복잡한 작업 - high effort
result = analyze_with_dynamic_effort(
    "이 시스템 아키텍처를 분석하고 개선점을 제안해줘",
    "complex"
)
```

### 예제 2: 대량 처리 최적화

```python
import anthropic
import asyncio

async def batch_classify(texts: list[str]) -> list[dict]:
    """대량 텍스트 분류 - Low effort로 비용 최적화"""

    client = anthropic.AsyncAnthropic()

    async def classify_single(text: str) -> dict:
        response = await client.beta.messages.create(
            model="claude-opus-4-5-20251101",
            betas=["effort-2025-11-24"],
            max_tokens=100,  # 분류니까 짧은 응답
            messages=[{
                "role": "user",
                "content": f"다음 텍스트를 분류해줘 (긍정/부정/중립 중 하나만): {text}"
            }],
            output_config={
                "effort": "low"  # 단순 작업이므로 low
            }
        )
        return {"text": text, "classification": response.content[0].text}

    # 병렬 처리
    results = await asyncio.gather(*[classify_single(t) for t in texts])
    return results

# 사용 예시
texts = ["좋아요!", "별로예요", "그냥 그래요", ...]  # 1000개 텍스트
results = asyncio.run(batch_classify(texts))
```

### 예제 3: 에이전트 서브태스크 최적화

```python
import anthropic

client = anthropic.Anthropic()

def agent_task(task: str) -> str:
    """
    에이전트 작업:
    - 메인 작업: high effort
    - 서브 태스크: low effort
    """

    # 1. 메인 분석 (high effort)
    main_analysis = client.beta.messages.create(
        model="claude-opus-4-5-20251101",
        betas=["effort-2025-11-24"],
        max_tokens=4096,
        messages=[{
            "role": "user",
            "content": f"다음 작업을 분석하고 서브태스크로 나눠줘: {task}"
        }],
        output_config={"effort": "high"}
    )

    subtasks = parse_subtasks(main_analysis.content[0].text)

    # 2. 서브태스크 실행 (low effort로 비용 절감)
    results = []
    for subtask in subtasks:
        result = client.beta.messages.create(
            model="claude-opus-4-5-20251101",
            betas=["effort-2025-11-24"],
            max_tokens=1024,
            messages=[{
                "role": "user",
                "content": subtask
            }],
            output_config={"effort": "low"}  # 서브태스크는 효율적으로
        )
        results.append(result.content[0].text)

    # 3. 최종 종합 (medium effort)
    final = client.beta.messages.create(
        model="claude-opus-4-5-20251101",
        betas=["effort-2025-11-24"],
        max_tokens=2048,
        messages=[{
            "role": "user",
            "content": f"다음 결과들을 종합해줘: {results}"
        }],
        output_config={"effort": "medium"}
    )

    return final.content[0].text
```

### 예제 4: Structured Outputs + Effort

```python
import anthropic
import json

client = anthropic.Anthropic()

def extract_entities_efficient(text: str) -> dict:
    """엔티티 추출 - Structured Outputs + Low Effort"""

    response = client.beta.messages.create(
        model="claude-opus-4-5-20251101",
        betas=["effort-2025-11-24"],
        max_tokens=512,
        messages=[{
            "role": "user",
            "content": f"다음 텍스트에서 엔티티를 추출해줘:\n\n{text}"
        }],
        output_config={
            "effort": "low",  # 추출 작업은 low로 충분
            "format": {
                "type": "json_schema",
                "json_schema": {
                    "name": "entity_extraction",
                    "schema": {
                        "type": "object",
                        "properties": {
                            "people": {"type": "array", "items": {"type": "string"}},
                            "organizations": {"type": "array", "items": {"type": "string"}},
                            "locations": {"type": "array", "items": {"type": "string"}}
                        },
                        "required": ["people", "organizations", "locations"]
                    }
                }
            }
        }
    )

    return json.loads(response.content[0].text)

# 사용 예시
text = "김철수 대리는 서울에 있는 삼성전자에서 일합니다."
entities = extract_entities_efficient(text)
# {"people": ["김철수"], "organizations": ["삼성전자"], "locations": ["서울"]}
```

---

## 비용 최적화 전략 / Cost Optimization

### Opus 4.5 가격

| 항목 | 가격 |
|------|------|
| Input | $5 / 1M tokens |
| Output | $25 / 1M tokens |

### Effort별 예상 비용 절감

| Effort | 토큰 절감 | 비용 절감 (추정) |
|--------|----------|-----------------|
| `high` | 기준 | 0% |
| `medium` | ~50-76% | ~50-76% |
| `low` | ~80%+ | ~80%+ |

### 최적화 전략

```
1. 작업 분류
   ├── 복잡한 추론 → high
   ├── 일반 작업 → medium
   └── 단순 작업 → low

2. 에이전트 구조
   ├── 계획 수립 → high
   ├── 서브태스크 → low
   └── 결과 종합 → medium

3. 대량 처리
   └── 모두 low로 처리

4. 하이브리드 접근
   ├── 중요한 고객 요청 → high
   └── 내부 자동화 → low/medium
```

---

## 베스트 프랙티스 / Best Practices

### 1. High에서 시작하기

```python
# 먼저 high로 테스트
output_config={"effort": "high"}

# 품질 확인 후 medium으로 시도
output_config={"effort": "medium"}

# 품질이 충분하면 medium 사용
```

### 2. 속도가 중요하면 Low 사용

```python
# 실시간 응답이 필요한 경우
output_config={"effort": "low"}
```

### 3. 사용 사례별 테스트

```python
# 동일한 프롬프트로 세 레벨 비교
for effort in ["low", "medium", "high"]:
    response = client.beta.messages.create(
        model="claude-opus-4-5-20251101",
        betas=["effort-2025-11-24"],
        max_tokens=4096,
        messages=[{"role": "user", "content": prompt}],
        output_config={"effort": effort}
    )
    print(f"[{effort}] Tokens: {response.usage.output_tokens}")
    print(f"Response: {response.content[0].text[:200]}...")
```

### 4. 동적 Effort 조절

```python
def get_effort_level(task_type: str) -> str:
    """작업 유형에 따른 Effort 레벨 결정"""

    high_effort_tasks = ["coding", "analysis", "reasoning", "planning"]
    medium_effort_tasks = ["summarization", "translation", "editing"]
    low_effort_tasks = ["classification", "extraction", "lookup"]

    if task_type in high_effort_tasks:
        return "high"
    elif task_type in medium_effort_tasks:
        return "medium"
    else:
        return "low"
```

---

## FAQ

### Q1: Effort Parameter는 무료인가요?

네, 추가 비용 없이 사용할 수 있습니다.
오히려 low/medium을 사용하면 토큰 사용량이 줄어 **비용이 절감**됩니다.

### Q2: Sonnet이나 Haiku에서도 사용 가능한가요?

아니요, **Opus 4.5 전용** 기능입니다.
다른 모델에서는 effort 파라미터가 무시됩니다.

### Q3: effort를 생략하면 어떻게 되나요?

기본값인 **`high`**가 적용됩니다.
```python
# 아래 두 코드는 동일
output_config={"effort": "high"}
# effort 파라미터 생략
```

### Q4: Beta 헤더를 빼면 어떻게 되나요?

API 오류가 발생합니다. Beta 기능이므로 반드시 헤더를 포함해야 합니다:
```python
betas=["effort-2025-11-24"]
```

### Q5: Structured Outputs와 함께 사용 가능한가요?

네, 가능합니다:
```python
output_config={
    "effort": "medium",
    "format": {
        "type": "json_schema",
        "json_schema": {...}
    }
}
```

### Q6: Low effort가 항상 품질이 낮나요?

단순 작업(분류, 추출 등)에서는 low effort도 **충분한 품질**을 제공합니다.
복잡한 추론이 필요한 작업에서만 high를 사용하세요.

---

## 참고 자료 / References

### 공식 문서
- [Effort Parameter 문서](https://platform.claude.com/docs/en/build-with-claude/effort)
- [Claude Opus 4.5 소개](https://www.anthropic.com/news/claude-opus-4-5)
- [API Pricing](https://platform.claude.com/docs/en/about-claude/pricing)

### 관련 자료
- [Cost Efficiency in Claude Opus 4.5](https://chatlyai.app/blog/cost-efficiency-in-claude-opus-4-5)
- [liteLLM - Anthropic Effort Parameter](https://docs.litellm.ai/docs/providers/anthropic_effort)

### 이 프로젝트의 관련 문서
- [01_Claude_Tools_Complete_Guide.md](./01_Claude_Tools_Complete_Guide.md)
- [05_Structured_Outputs_Guide.md](./05_Structured_Outputs_Guide.md)
- [Claude_Opus_4.5_Practical_Guide.md](./Claude_Opus_4.5_Practical_Guide.md)

---

## 업데이트 로그 / Changelog

| 날짜 | 버전 | 내용 |
|------|------|------|
| 2026-02-05 | v1.0 | 초기 버전 작성 |

---

*Made with Claude by Bella (OZKIZ)*
