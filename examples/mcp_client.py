"""
MCP 클라이언트 예제
MCP Client Example

Author: Bella (OZKIZ)
Created: 2026-01-30

MCP 서버에 연결하여 Claude API와 함께 사용하는 방법을 보여줍니다.
"""

import os
import asyncio
from anthropic import Anthropic

# MCP 패키지 필요: pip install mcp
try:
    from mcp import ClientSession, StdioServerParameters
    from mcp.client.stdio import stdio_client
    MCP_AVAILABLE = True
except ImportError:
    MCP_AVAILABLE = False
    print("MCP 패키지가 설치되지 않았습니다.")
    print("설치: pip install mcp")


async def main():
    if not MCP_AVAILABLE:
        print("MCP 패키지를 먼저 설치해주세요.")
        return

    print("=" * 50)
    print("MCP 클라이언트 예제")
    print("=" * 50)

    # MCP 서버 파라미터 (파일시스템 서버 예시)
    server_params = StdioServerParameters(
        command="npx",
        args=["-y", "@modelcontextprotocol/server-filesystem", os.path.expanduser("~")]
    )

    print("\n1. MCP 서버 연결 중...")

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # 세션 초기화
            await session.initialize()
            print("   연결 성공!")

            # 사용 가능한 도구 목록 가져오기
            print("\n2. 사용 가능한 도구 목록:")
            mcp_tools = await session.list_tools()

            for tool in mcp_tools.tools:
                print(f"   - {tool.name}: {tool.description}")

            # Claude API 형식으로 변환
            print("\n3. Claude API 형식으로 변환...")
            claude_tools = []
            for tool in mcp_tools.tools:
                claude_tools.append({
                    "name": tool.name,
                    "description": tool.description or "",
                    "input_schema": tool.inputSchema
                })

            # Claude API 호출
            print("\n4. Claude API 호출...")
            client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

            response = client.messages.create(
                model="claude-sonnet-4-5",
                max_tokens=1024,
                tools=claude_tools,
                messages=[{
                    "role": "user",
                    "content": "홈 디렉토리의 파일 목록을 보여줘"
                }]
            )

            # 도구 호출 처리
            print("\n5. 응답 처리...")
            for block in response.content:
                if block.type == "tool_use":
                    print(f"\n   도구 호출: {block.name}")
                    print(f"   입력: {block.input}")

                    # MCP 서버로 도구 실행
                    result = await session.call_tool(block.name, block.input)
                    print(f"   결과: {result.content[:200]}...")  # 처음 200자만

                elif block.type == "text":
                    print(f"\n   응답: {block.text}")

    print("\n" + "=" * 50)
    print("완료!")
    print("=" * 50)


def run_sync():
    """동기 방식으로 실행"""
    asyncio.run(main())


if __name__ == "__main__":
    run_sync()
