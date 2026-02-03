"""
Memory Tool & Context Editing 예제 코드
Memory Tool & Context Editing Example Code

작성일: 2026-02-03
Author: Bella (OZKIZ) + Claude (Opus 4.5)
"""

import anthropic
import json
from typing import Any

# 클라이언트 초기화
client = anthropic.Anthropic()

# 간단한 인메모리 저장소
memory_store: dict[str, str] = {}


# =============================================================================
# Memory Tool 예제
# =============================================================================

def handle_memory_tool(tool_input: dict) -> str:
    """Memory tool 요청 처리"""
    action = tool_input.get("action")
    key = tool_input.get("key", "")
    value = tool_input.get("value", "")
    query = tool_input.get("query", "")

    if action == "store":
        memory_store[key] = value
        return f"Successfully stored: {key} = {value}"

    elif action == "retrieve":
        if key:
            result = memory_store.get(key)
            return result if result else f"No memory found for key: {key}"
        elif query:
            matches = {
                k: v for k, v in memory_store.items()
                if query.lower() in k.lower() or query.lower() in v.lower()
            }
            return json.dumps(matches, ensure_ascii=False) if matches else "No matches found"
        return "Please provide a key or query"

    elif action == "list":
        return json.dumps(list(memory_store.keys()), ensure_ascii=False)

    elif action == "delete":
        if key in memory_store:
            del memory_store[key]
            return f"Successfully deleted: {key}"
        return f"Key not found: {key}"

    return f"Unknown action: {action}"


def get_memory_tool_definition() -> dict:
    """Memory tool 정의 반환"""
    return {
        "name": "memory",
        "description": """Store and retrieve information across conversations.

Actions:
- store: Save information with a key-value pair
- retrieve: Get information by key or search by query
- list: List all stored keys
- delete: Remove information by key""",
        "input_schema": {
            "type": "object",
            "properties": {
                "action": {
                    "type": "string",
                    "enum": ["store", "retrieve", "list", "delete"],
                    "description": "The memory action to perform"
                },
                "key": {
                    "type": "string",
                    "description": "The key for the memory item"
                },
                "value": {
                    "type": "string",
                    "description": "The value to store (required for store action)"
                },
                "query": {
                    "type": "string",
                    "description": "Search query for retrieve action"
                }
            },
            "required": ["action"]
        }
    }


def chat_with_memory(user_message: str, conversation: list) -> tuple[str, list]:
    """Memory를 활용한 대화"""

    conversation.append({"role": "user", "content": user_message})

    response = client.messages.create(
        model="claude-opus-4-5-20251101",
        max_tokens=1024,
        system="You are a helpful assistant with memory capabilities. Use the memory tool to remember and recall information the user shares.",
        tools=[get_memory_tool_definition()],
        messages=conversation
    )

    # Tool 호출 루프
    while response.stop_reason == "tool_use":
        tool_results = []

        for block in response.content:
            if block.type == "tool_use":
                result = handle_memory_tool(block.input)
                tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": result
                })
                print(f"  [Memory] {block.input['action']}: {result}")

        conversation.append({"role": "assistant", "content": response.content})
        conversation.append({"role": "user", "content": tool_results})

        response = client.messages.create(
            model="claude-opus-4-5-20251101",
            max_tokens=1024,
            system="You are a helpful assistant with memory capabilities.",
            tools=[get_memory_tool_definition()],
            messages=conversation
        )

    # 최종 응답
    conversation.append({"role": "assistant", "content": response.content})

    final_text = ""
    for block in response.content:
        if hasattr(block, "text"):
            final_text += block.text

    return final_text, conversation


def memory_demo():
    """Memory Tool 데모"""
    print("=" * 60)
    print("Memory Tool Demo")
    print("=" * 60)

    conversation = []

    # 1. 정보 저장
    print("\n[1] 정보 저장하기")
    response, conversation = chat_with_memory(
        "내 이름은 Bella이고, Python을 주로 사용해. 현재 Claude AI Knowledge Base 프로젝트를 진행 중이야. 이 정보들 기억해줘.",
        conversation
    )
    print(f"Claude: {response}\n")

    # 2. 정보 조회
    print("[2] 정보 조회하기")
    response, conversation = chat_with_memory(
        "내가 어떤 프로젝트를 하고 있다고 했지?",
        conversation
    )
    print(f"Claude: {response}\n")

    # 3. 저장된 메모리 확인
    print("[3] 현재 저장된 메모리:")
    print(json.dumps(memory_store, indent=2, ensure_ascii=False))


# =============================================================================
# Context Editing 예제
# =============================================================================

def chat_with_thinking_clear(messages: list) -> dict[str, Any]:
    """Thinking 클리어를 활용한 대화"""

    response = client.messages.create(
        model="claude-opus-4-5-20251101",
        max_tokens=16000,
        betas=["clear_thinking_20251015"],
        thinking={
            "type": "enabled",
            "budget_tokens": 5000
        },
        messages=messages
    )

    thinking_content = None
    text_content = None

    for block in response.content:
        if block.type == "thinking":
            thinking_content = block.thinking
        elif block.type == "text":
            text_content = block.text

    return {
        "thinking": thinking_content,
        "response": text_content,
        "usage": {
            "input_tokens": response.usage.input_tokens,
            "output_tokens": response.usage.output_tokens
        }
    }


def context_editing_demo():
    """Context Editing 데모"""
    print("\n" + "=" * 60)
    print("Context Editing Demo (Thinking Clear)")
    print("=" * 60)

    conversation = []

    # Turn 1
    print("\n[Turn 1]")
    conversation.append({
        "role": "user",
        "content": "재귀와 동적 프로그래밍의 차이점을 설명해줘."
    })

    result1 = chat_with_thinking_clear(conversation)
    print(f"Input tokens: {result1['usage']['input_tokens']}")
    print(f"Output tokens: {result1['usage']['output_tokens']}")
    print(f"Response preview: {result1['response'][:150]}...")

    # 응답 추가
    conversation.append({
        "role": "assistant",
        "content": [
            {"type": "thinking", "thinking": result1["thinking"]},
            {"type": "text", "text": result1["response"]}
        ]
    })

    # Turn 2
    print("\n[Turn 2]")
    conversation.append({
        "role": "user",
        "content": "그러면 피보나치 수열을 두 방식으로 구현해줘."
    })

    result2 = chat_with_thinking_clear(conversation)
    print(f"Input tokens: {result2['usage']['input_tokens']}")
    print(f"Output tokens: {result2['usage']['output_tokens']}")
    print(f"Response preview: {result2['response'][:150]}...")

    # Turn 1의 thinking이 클리어되어 토큰이 크게 증가하지 않음
    print("\n[결과] clear_thinking 덕분에 이전 턴의 thinking이 제거되어 토큰 절약!")


# =============================================================================
# ConversationManager 클래스
# =============================================================================

class ConversationManager:
    """Memory와 Context를 통합 관리하는 클래스"""

    def __init__(self, project_id: str):
        self.project_id = project_id
        self.client = anthropic.Anthropic()
        self.memory: dict[str, str] = {}
        self.conversation: list = []

    def store_memory(self, key: str, value: str):
        """장기 메모리에 저장"""
        self.memory[key] = value

    def get_memory(self, key: str) -> str | None:
        """메모리에서 조회"""
        return self.memory.get(key)

    def get_system_prompt(self) -> str:
        """메모리 기반 시스템 프롬프트 생성"""
        prompt = f"You are a helpful assistant for project: {self.project_id}\n\n"

        if self.memory:
            prompt += "## Known Information\n"
            for k, v in self.memory.items():
                prompt += f"- {k}: {v}\n"
            prompt += "\n"

        return prompt

    def optimize_context(self):
        """컨텍스트 최적화 - 오래된 thinking 제거"""
        for i, msg in enumerate(self.conversation[:-2]):
            if msg["role"] == "assistant" and isinstance(msg["content"], list):
                msg["content"] = [
                    block for block in msg["content"]
                    if not (isinstance(block, dict) and block.get("type") == "thinking")
                ]

    def chat(self, user_message: str, use_thinking: bool = False) -> str:
        """대화 실행"""
        self.conversation.append({"role": "user", "content": user_message})
        self.optimize_context()

        params = {
            "model": "claude-opus-4-5-20251101",
            "max_tokens": 4096,
            "system": self.get_system_prompt(),
            "messages": self.conversation
        }

        if use_thinking:
            params["betas"] = ["clear_thinking_20251015"]
            params["thinking"] = {"type": "enabled", "budget_tokens": 5000}
            params["max_tokens"] = 16000

        response = self.client.messages.create(**params)

        self.conversation.append({
            "role": "assistant",
            "content": response.content
        })

        for block in response.content:
            if hasattr(block, "text"):
                return block.text

        return ""


def conversation_manager_demo():
    """ConversationManager 데모"""
    print("\n" + "=" * 60)
    print("ConversationManager Demo")
    print("=" * 60)

    manager = ConversationManager("claude-ai-knowledge")

    # 메모리 설정
    manager.store_memory("user_name", "Bella")
    manager.store_memory("language", "Python")
    manager.store_memory("project", "Claude AI Knowledge Base")

    print("\n[저장된 메모리]")
    print(json.dumps(manager.memory, indent=2, ensure_ascii=False))

    print("\n[대화 시작]")
    response = manager.chat("안녕! 내 프로젝트에 대해 알고 있어?")
    print(f"Claude: {response}")


# =============================================================================
# Main
# =============================================================================

if __name__ == "__main__":
    print("Memory Tool & Context Editing Examples\n")

    # 1. Memory Tool 데모
    memory_demo()

    # 2. Context Editing 데모
    context_editing_demo()

    # 3. ConversationManager 데모
    conversation_manager_demo()

    print("\n" + "=" * 60)
    print("All demos completed!")
    print("=" * 60)
