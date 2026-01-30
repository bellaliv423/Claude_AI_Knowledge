"""
Extended Thinking 예제
Extended Thinking Example

Author: Bella (OZKIZ)
Created: 2026-01-30

Claude가 더 깊이 생각하게 하는 기능을 보여줍니다.
복잡한 문제 해결에 유용합니다.
"""

import os
from anthropic import Anthropic

def main():
    client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

    print("=" * 50)
    print("Extended Thinking 예제")
    print("=" * 50)

    # 복잡한 문제
    problem = """
    다음 논리 퍼즐을 풀어줘:

    5명의 사람 (Alice, Bob, Carol, David, Eve)이 일렬로 서 있습니다.
    - Alice는 Bob 바로 옆에 서 있지 않습니다.
    - Carol은 맨 끝에 서 있습니다.
    - David는 Eve의 오른쪽 어딘가에 서 있습니다.
    - Bob은 가운데(3번째 위치)에 서 있습니다.

    5명의 순서를 왼쪽부터 구해줘.
    """

    print(f"\n문제:\n{problem}")
    print("-" * 50)

    # Extended Thinking 활성화
    response = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=16000,
        thinking={
            "type": "enabled",
            "budget_tokens": 10000  # 생각에 할당할 토큰 수
        },
        messages=[{
            "role": "user",
            "content": problem
        }]
    )

    # 응답 처리
    print("\n응답:")
    print("-" * 50)

    for block in response.content:
        if block.type == "thinking":
            print("\n[생각 과정]")
            print("-" * 30)
            # 생각 과정 출력 (길면 요약)
            thinking_text = block.thinking
            if len(thinking_text) > 500:
                print(thinking_text[:500] + "...")
                print(f"\n(총 {len(thinking_text)}자의 생각 과정)")
            else:
                print(thinking_text)
            print("-" * 30)

        elif block.type == "text":
            print("\n[최종 답변]")
            print(block.text)

    # 토큰 사용량
    print("\n" + "=" * 50)
    print("토큰 사용량:")
    print(f"  입력: {response.usage.input_tokens}")
    print(f"  출력: {response.usage.output_tokens}")
    print("=" * 50)

if __name__ == "__main__":
    main()
