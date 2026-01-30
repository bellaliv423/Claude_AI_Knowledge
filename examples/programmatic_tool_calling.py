"""
Programmatic Tool Calling 예제
Programmatic Tool Calling Example

Author: Bella (OZKIZ)
Created: 2026-01-30

Claude가 코드 내에서 다른 도구를 프로그래매틱하게 호출하는 방법을 보여줍니다.
"""

import os
import json
from anthropic import Anthropic

def main():
    client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

    print("=" * 50)
    print("Programmatic Tool Calling 예제")
    print("=" * 50)

    # Code Execution이 다른 도구를 호출할 수 있도록 설정
    response = client.beta.messages.create(
        model="claude-sonnet-4-5",
        betas=["code-execution-2025-08-25"],
        max_tokens=4096,
        messages=[{
            "role": "user",
            "content": """
            다음 5개 도시의 날씨를 가져와서 가장 따뜻한 도시를 찾아줘:
            - 서울
            - 도쿄
            - 뉴욕
            - 런던
            - 시드니
            """
        }],
        tools=[
            # Code Execution 도구
            {
                "type": "code_execution_20250825",
                "name": "code_execution"
            },
            # 날씨 도구 (Code Execution에서 호출 가능)
            {
                "name": "get_weather",
                "description": "지정된 도시의 현재 날씨 정보를 가져옵니다",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "city": {
                            "type": "string",
                            "description": "도시 이름"
                        },
                        "unit": {
                            "type": "string",
                            "enum": ["celsius", "fahrenheit"],
                            "description": "온도 단위"
                        }
                    },
                    "required": ["city"]
                },
                # Code Execution에서 이 도구를 호출할 수 있도록 허용
                "allowed_callers": ["code_execution_20250825"]
            }
        ]
    )

    # 응답 처리
    print("\n응답:")
    for block in response.content:
        print(f"\nType: {block.type}")

        if block.type == "tool_use":
            print(f"Tool: {block.name}")
            print(f"Input: {json.dumps(block.input, indent=2, ensure_ascii=False)}")

            # 도구 호출 시뮬레이션 (실제로는 API 호출)
            if block.name == "get_weather":
                city = block.input.get("city", "Unknown")
                # 시뮬레이션된 날씨 데이터
                weather_data = {
                    "서울": {"temp": 5, "condition": "맑음"},
                    "도쿄": {"temp": 10, "condition": "흐림"},
                    "뉴욕": {"temp": -2, "condition": "눈"},
                    "런던": {"temp": 8, "condition": "비"},
                    "시드니": {"temp": 28, "condition": "맑음"},
                }
                result = weather_data.get(city, {"temp": 0, "condition": "알 수 없음"})
                print(f"Result: {city} - {result['temp']}°C, {result['condition']}")

        elif hasattr(block, 'text'):
            print(f"Text: {block.text}")

    print("\n" + "=" * 50)

if __name__ == "__main__":
    main()
