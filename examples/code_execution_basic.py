"""
Code Execution 기본 예제
Basic Code Execution Example

Author: Bella (OZKIZ)
Created: 2026-01-30
"""

import os
from anthropic import Anthropic

def main():
    # 클라이언트 초기화
    client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

    # 기본 코드 실행 요청
    response = client.beta.messages.create(
        model="claude-sonnet-4-5",
        betas=["code-execution-2025-08-25"],
        max_tokens=4096,
        messages=[{
            "role": "user",
            "content": "1부터 10까지의 합을 계산하고, 그 결과의 제곱근도 구해줘"
        }],
        tools=[{
            "type": "code_execution_20250825",
            "name": "code_execution"
        }]
    )

    # 응답 출력
    print("=" * 50)
    print("Code Execution 결과")
    print("=" * 50)

    for block in response.content:
        print(f"\nType: {block.type}")
        if hasattr(block, 'text'):
            print(f"Text: {block.text}")
        elif hasattr(block, 'content'):
            print(f"Content: {block.content}")

    print("\n" + "=" * 50)

if __name__ == "__main__":
    main()
