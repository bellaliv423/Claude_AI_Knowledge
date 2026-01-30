"""
Container 재사용 예제
Container Reuse Example

Author: Bella (OZKIZ)
Created: 2026-01-30

컨테이너를 재사용하여 파일과 상태를 유지하는 방법을 보여줍니다.
"""

import os
from anthropic import Anthropic

def main():
    client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

    print("=" * 50)
    print("1단계: 파일 생성")
    print("=" * 50)

    # 첫 번째 요청: 파일 생성
    response1 = client.beta.messages.create(
        model="claude-sonnet-4-5",
        betas=["code-execution-2025-08-25"],
        max_tokens=4096,
        messages=[{
            "role": "user",
            "content": "1부터 100 사이의 랜덤 숫자를 생성해서 /tmp/number.txt 파일에 저장해줘"
        }],
        tools=[{
            "type": "code_execution_20250825",
            "name": "code_execution"
        }]
    )

    # 컨테이너 ID 추출
    container_id = response1.container.id
    print(f"\nContainer ID: {container_id}")

    for block in response1.content:
        if hasattr(block, 'text'):
            print(f"Response: {block.text}")

    print("\n" + "=" * 50)
    print("2단계: 같은 컨테이너에서 파일 읽기")
    print("=" * 50)

    # 두 번째 요청: 같은 컨테이너 재사용
    response2 = client.beta.messages.create(
        container=container_id,  # 컨테이너 재사용!
        model="claude-sonnet-4-5",
        betas=["code-execution-2025-08-25"],
        max_tokens=4096,
        messages=[{
            "role": "user",
            "content": "/tmp/number.txt 파일을 읽어서 그 숫자의 제곱과 세제곱을 계산해줘"
        }],
        tools=[{
            "type": "code_execution_20250825",
            "name": "code_execution"
        }]
    )

    for block in response2.content:
        if hasattr(block, 'text'):
            print(f"Response: {block.text}")

    print("\n" + "=" * 50)
    print("3단계: 추가 작업")
    print("=" * 50)

    # 세 번째 요청: 계속 같은 컨테이너 사용
    response3 = client.beta.messages.create(
        container=container_id,
        model="claude-sonnet-4-5",
        betas=["code-execution-2025-08-25"],
        max_tokens=4096,
        messages=[{
            "role": "user",
            "content": "/tmp 폴더에 있는 모든 파일 목록을 보여줘"
        }],
        tools=[{
            "type": "code_execution_20250825",
            "name": "code_execution"
        }]
    )

    for block in response3.content:
        if hasattr(block, 'text'):
            print(f"Response: {block.text}")

    print("\n" + "=" * 50)
    print("완료!")
    print(f"사용된 Container ID: {container_id}")
    print("이 ID로 30일간 컨테이너를 재사용할 수 있습니다.")
    print("=" * 50)

if __name__ == "__main__":
    main()
