"""
Batch API 예제
Batch API Example

Author: Bella (OZKIZ)
Created: 2026-01-30

대량의 요청을 비동기로 처리하는 방법을 보여줍니다.
50% 비용 절감 효과가 있습니다.
"""

import os
import time
from anthropic import Anthropic

def main():
    client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

    print("=" * 50)
    print("Batch API 예제")
    print("=" * 50)

    # 배치 요청 생성
    requests = [
        {
            "custom_id": "translate-ko-en",
            "params": {
                "model": "claude-sonnet-4-5",
                "max_tokens": 1024,
                "messages": [{
                    "role": "user",
                    "content": "다음을 영어로 번역해줘: 안녕하세요, 만나서 반갑습니다."
                }]
            }
        },
        {
            "custom_id": "translate-ko-ja",
            "params": {
                "model": "claude-sonnet-4-5",
                "max_tokens": 1024,
                "messages": [{
                    "role": "user",
                    "content": "다음을 일본어로 번역해줘: 안녕하세요, 만나서 반갑습니다."
                }]
            }
        },
        {
            "custom_id": "translate-ko-zh",
            "params": {
                "model": "claude-sonnet-4-5",
                "max_tokens": 1024,
                "messages": [{
                    "role": "user",
                    "content": "다음을 중국어로 번역해줘: 안녕하세요, 만나서 반갑습니다."
                }]
            }
        },
        {
            "custom_id": "summarize",
            "params": {
                "model": "claude-sonnet-4-5",
                "max_tokens": 1024,
                "messages": [{
                    "role": "user",
                    "content": "Claude AI의 주요 특징을 3줄로 요약해줘"
                }]
            }
        },
        {
            "custom_id": "code-review",
            "params": {
                "model": "claude-sonnet-4-5",
                "max_tokens": 1024,
                "messages": [{
                    "role": "user",
                    "content": "다음 코드를 리뷰해줘: def add(a, b): return a + b"
                }]
            }
        }
    ]

    print(f"\n총 {len(requests)}개의 요청을 배치로 처리합니다.")
    print("-" * 50)

    # 배치 생성
    print("\n1. 배치 생성 중...")
    batch = client.beta.messages.batches.create(requests=requests)

    batch_id = batch.id
    print(f"   배치 ID: {batch_id}")
    print(f"   상태: {batch.processing_status}")

    # 상태 확인 (폴링)
    print("\n2. 처리 상태 확인 중...")
    while True:
        status = client.beta.messages.batches.retrieve(batch_id)
        print(f"   상태: {status.processing_status}")

        if status.processing_status == "ended":
            break

        print("   10초 후 다시 확인...")
        time.sleep(10)

    # 결과 가져오기
    print("\n3. 결과 가져오기...")
    print("-" * 50)

    results = client.beta.messages.batches.results(batch_id)

    for result in results:
        print(f"\n[{result.custom_id}]")
        if result.result.type == "succeeded":
            message = result.result.message
            for block in message.content:
                if hasattr(block, 'text'):
                    print(f"   {block.text[:100]}...")  # 처음 100자만 출력
        else:
            print(f"   오류: {result.result.error}")

    print("\n" + "=" * 50)
    print("배치 처리 완료!")
    print(f"처리된 요청 수: {len(requests)}")
    print("=" * 50)

if __name__ == "__main__":
    main()
