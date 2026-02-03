"""
Structured Outputs 예제 코드
Structured Outputs Example Code

작성일: 2026-02-03
Author: Bella (OZKIZ) + Claude (Opus 4.5)
"""

import anthropic
import json
from typing import Any

# 클라이언트 초기화
client = anthropic.Anthropic()


def basic_example():
    """기본 Structured Outputs 예제"""

    response = client.messages.create(
        model="claude-opus-4-5-20251101",
        max_tokens=1024,
        output_config={
            "format": {
                "type": "json_schema",
                "json_schema": {
                    "name": "basic_response",
                    "schema": {
                        "type": "object",
                        "properties": {
                            "answer": {"type": "string"},
                            "confidence": {
                                "type": "number",
                                "minimum": 0,
                                "maximum": 1
                            }
                        },
                        "required": ["answer", "confidence"]
                    }
                }
            }
        },
        messages=[
            {"role": "user", "content": "파이썬의 주요 장점 3가지를 알려주세요."}
        ]
    )

    result = json.loads(response.content[0].text)
    print("=== 기본 예제 ===")
    print(f"답변: {result['answer']}")
    print(f"신뢰도: {result['confidence']}")
    return result


def sentiment_analysis(text: str) -> dict[str, Any]:
    """감정 분석 예제"""

    response = client.messages.create(
        model="claude-sonnet-4-5-20250929",
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


def extract_entities(text: str) -> dict[str, Any]:
    """엔티티 추출 예제"""

    response = client.messages.create(
        model="claude-sonnet-4-5-20250929",
        max_tokens=1024,
        output_config={
            "format": {
                "type": "json_schema",
                "json_schema": {
                    "name": "entity_extraction",
                    "schema": {
                        "type": "object",
                        "properties": {
                            "people": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "properties": {
                                        "name": {"type": "string"},
                                        "role": {"type": "string"}
                                    },
                                    "required": ["name"]
                                }
                            },
                            "organizations": {
                                "type": "array",
                                "items": {"type": "string"}
                            },
                            "locations": {
                                "type": "array",
                                "items": {"type": "string"}
                            },
                            "dates": {
                                "type": "array",
                                "items": {"type": "string"}
                            }
                        },
                        "required": ["people", "organizations", "locations", "dates"]
                    }
                }
            }
        },
        messages=[
            {"role": "user", "content": f"다음 텍스트에서 엔티티를 추출해주세요:\n\n{text}"}
        ]
    )

    return json.loads(response.content[0].text)


def code_review(code: str) -> dict[str, Any]:
    """코드 리뷰 예제"""

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
                            "strengths": {
                                "type": "array",
                                "items": {"type": "string"}
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


def with_extended_thinking(question: str) -> dict[str, Any]:
    """Extended Thinking과 함께 사용하는 예제"""

    response = client.messages.create(
        model="claude-opus-4-5-20251101",
        max_tokens=16000,
        thinking={
            "type": "enabled",
            "budget_tokens": 8000
        },
        output_config={
            "format": {
                "type": "json_schema",
                "json_schema": {
                    "name": "thinking_response",
                    "schema": {
                        "type": "object",
                        "properties": {
                            "answer": {"type": "string"},
                            "reasoning_steps": {
                                "type": "array",
                                "items": {"type": "string"}
                            },
                            "confidence": {
                                "type": "number",
                                "minimum": 0,
                                "maximum": 1
                            }
                        },
                        "required": ["answer", "reasoning_steps", "confidence"]
                    }
                }
            }
        },
        messages=[
            {"role": "user", "content": question}
        ]
    )

    # thinking 블록과 응답 분리
    thinking_content = None
    response_content = None

    for block in response.content:
        if block.type == "thinking":
            thinking_content = block.thinking
        elif block.type == "text":
            response_content = json.loads(block.text)

    return {
        "thinking": thinking_content,
        "response": response_content
    }


if __name__ == "__main__":
    # 1. 기본 예제
    print("\n" + "=" * 50)
    basic_example()

    # 2. 감정 분석
    print("\n" + "=" * 50)
    print("=== 감정 분석 예제 ===")
    sentiment_result = sentiment_analysis(
        "오늘 정말 좋은 하루였어요! 친구들과 맛있는 점심도 먹고, 새 프로젝트도 시작했습니다."
    )
    print(f"감정: {sentiment_result['sentiment']}")
    print(f"신뢰도: {sentiment_result['confidence']}")
    print(f"키워드: {sentiment_result['keywords']}")
    print(f"요약: {sentiment_result['summary']}")

    # 3. 엔티티 추출
    print("\n" + "=" * 50)
    print("=== 엔티티 추출 예제 ===")
    entity_result = extract_entities(
        "2026년 1월 15일, Apple의 CEO 팀 쿡이 도쿄에서 열린 컨퍼런스에서 발표했습니다."
    )
    print(f"인물: {entity_result['people']}")
    print(f"조직: {entity_result['organizations']}")
    print(f"장소: {entity_result['locations']}")
    print(f"날짜: {entity_result['dates']}")

    # 4. 코드 리뷰
    print("\n" + "=" * 50)
    print("=== 코드 리뷰 예제 ===")
    sample_code = '''
def calculate_average(numbers):
    total = 0
    for n in numbers:
        total = total + n
    return total / len(numbers)
'''
    review_result = code_review(sample_code)
    print(f"품질: {review_result['overall_quality']}")
    print(f"점수: {review_result['score']}/100")
    print(f"이슈 수: {len(review_result['issues'])}")
    for issue in review_result['issues']:
        print(f"  - [{issue['severity']}] {issue['message']}")

    print("\n" + "=" * 50)
    print("모든 예제 완료!")
