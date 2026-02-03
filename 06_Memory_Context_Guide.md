# Memory Tool & Context Editing 완벽 가이드
# Memory Tool & Context Editing Complete Guide

> **작성일 / Created**: 2026-02-03
> **업데이트 / Updated**: 2026-02-03
> **버전 / Version**: 1.0
> **Author**: Bella (OZKIZ) + Claude (Opus 4.5)

---

## 목차 / Table of Contents

1. [소개 / Introduction](#소개--introduction)
2. [Memory Tool](#memory-tool)
   - [기본 개념](#memory-tool-기본-개념)
   - [사용 방법](#memory-tool-사용-방법)
   - [실전 예제](#memory-tool-실전-예제)
3. [Context Editing](#context-editing)
   - [기본 개념](#context-editing-기본-개념)
   - [Thinking Block 클리어](#thinking-block-클리어)
   - [실전 예제](#context-editing-실전-예제)
4. [Memory + Context 통합 활용](#memory--context-통합-활용)
5. [주의사항 및 제한](#주의사항-및-제한)
6. [FAQ](#faq)
7. [참고 자료 / References](#참고-자료--references)

---

## 소개 / Introduction

### 왜 Memory와 Context 관리가 중요한가?

Claude API를 사용할 때 두 가지 주요 과제가 있습니다:

1. **세션 간 정보 유지**: 대화가 끝나면 컨텍스트가 사라짐
2. **컨텍스트 윈도우 관리**: 긴 대화에서 토큰 한도 초과

**Memory Tool**과 **Context Editing**은 이 문제를 해결합니다.

| 기능 | 출시일 | 상태 | 목적 |
|------|--------|------|------|
| Memory Tool | 2025-09-29 | Beta | 세션 간 정보 저장/참조 |
| Context Editing | 2025-09-29 | Beta | 컨텍스트 최적화 관리 |

---

## Memory Tool

### Memory Tool 기본 개념

**Memory Tool**은 Claude가 대화 간에 정보를 저장하고 나중에 참조할 수 있게 해주는 도구입니다.

#### 주요 특징
- 사용자 선호도 저장
- 프로젝트 컨텍스트 유지
- 이전 대화의 중요 정보 기억
- 개인화된 응답 제공

#### 작동 방식
```
[대화 1] → Claude가 중요 정보 저장 → [Memory Storage]
                                            ↓
[대화 2] ← Claude가 저장된 정보 참조 ← [Memory Retrieval]
```

### Memory Tool 사용 방법

#### 1. 기본 설정

```python
import anthropic

client = anthropic.Anthropic()

# Memory Tool 정의
memory_tool = {
    "name": "memory",
    "description": "Store and retrieve information across conversations",
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
                "description": "The value to store (for store action)"
            },
            "query": {
                "type": "string",
                "description": "Search query (for retrieve action)"
            }
        },
        "required": ["action"]
    }
}
```

#### 2. 메모리 저장

```python
response = client.messages.create(
    model="claude-opus-4-5-20251101",
    max_tokens=1024,
    tools=[memory_tool],
    messages=[
        {
            "role": "user",
            "content": "내 이름은 Bella이고, Python과 TypeScript를 주로 사용해. 이걸 기억해줘."
        }
    ]
)

# Claude가 memory tool을 호출하여 정보 저장
# tool_use block에서 action: "store" 확인
```

#### 3. 메모리 조회

```python
response = client.messages.create(
    model="claude-opus-4-5-20251101",
    max_tokens=1024,
    tools=[memory_tool],
    messages=[
        {
            "role": "user",
            "content": "내가 주로 사용하는 프로그래밍 언어가 뭐였지?"
        }
    ]
)

# Claude가 memory tool을 호출하여 정보 조회
# tool_use block에서 action: "retrieve" 확인
```

### Memory Tool 실전 예제

#### 예제 1: 사용자 프로필 관리

```python
import anthropic
import json

client = anthropic.Anthropic()

# 간단한 메모리 저장소 (실제로는 DB 사용)
memory_store = {}

def handle_memory_tool(tool_input: dict) -> str:
    """Memory tool 요청 처리"""
    action = tool_input.get("action")
    key = tool_input.get("key", "")
    value = tool_input.get("value", "")
    query = tool_input.get("query", "")

    if action == "store":
        memory_store[key] = value
        return f"Stored: {key} = {value}"

    elif action == "retrieve":
        if key:
            return memory_store.get(key, "Not found")
        elif query:
            # 간단한 검색
            results = {k: v for k, v in memory_store.items() if query.lower() in k.lower() or query.lower() in v.lower()}
            return json.dumps(results) if results else "No matches found"
        return "No key or query provided"

    elif action == "list":
        return json.dumps(list(memory_store.keys()))

    elif action == "delete":
        if key in memory_store:
            del memory_store[key]
            return f"Deleted: {key}"
        return f"Key not found: {key}"

    return "Unknown action"


def chat_with_memory(user_message: str, conversation_history: list) -> str:
    """Memory를 활용한 대화"""

    memory_tool = {
        "name": "memory",
        "description": "Store and retrieve user preferences and important information across conversations. Use 'store' to save new info, 'retrieve' to recall info, 'list' to see all keys, 'delete' to remove.",
        "input_schema": {
            "type": "object",
            "properties": {
                "action": {
                    "type": "string",
                    "enum": ["store", "retrieve", "list", "delete"]
                },
                "key": {"type": "string"},
                "value": {"type": "string"},
                "query": {"type": "string"}
            },
            "required": ["action"]
        }
    }

    conversation_history.append({"role": "user", "content": user_message})

    response = client.messages.create(
        model="claude-opus-4-5-20251101",
        max_tokens=1024,
        system="You are a helpful assistant with memory capabilities. Use the memory tool to remember user preferences and important information.",
        tools=[memory_tool],
        messages=conversation_history
    )

    # Tool 호출 처리
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

        conversation_history.append({"role": "assistant", "content": response.content})
        conversation_history.append({"role": "user", "content": tool_results})

        response = client.messages.create(
            model="claude-opus-4-5-20251101",
            max_tokens=1024,
            system="You are a helpful assistant with memory capabilities.",
            tools=[memory_tool],
            messages=conversation_history
        )

    # 최종 응답 추출
    final_response = ""
    for block in response.content:
        if hasattr(block, "text"):
            final_response += block.text

    conversation_history.append({"role": "assistant", "content": response.content})

    return final_response


# 사용 예시
if __name__ == "__main__":
    history = []

    # 첫 번째 대화: 정보 저장
    print("User: 내 이름은 Bella이고, Python 개발자야. 프로젝트는 Claude AI Knowledge Base야.")
    response1 = chat_with_memory(
        "내 이름은 Bella이고, Python 개발자야. 프로젝트는 Claude AI Knowledge Base야. 이 정보들 기억해줘.",
        history
    )
    print(f"Claude: {response1}\n")

    # 두 번째 대화: 정보 조회
    print("User: 내 프로젝트 이름이 뭐였지?")
    response2 = chat_with_memory("내 프로젝트 이름이 뭐였지?", history)
    print(f"Claude: {response2}\n")

    # 저장된 메모리 확인
    print(f"Memory Store: {memory_store}")
```

#### 예제 2: 프로젝트 컨텍스트 유지

```python
class ProjectMemory:
    """프로젝트별 메모리 관리"""

    def __init__(self, project_id: str):
        self.project_id = project_id
        self.memories = {}

    def store(self, category: str, key: str, value: str):
        if category not in self.memories:
            self.memories[category] = {}
        self.memories[category][key] = value

    def get(self, category: str, key: str = None):
        if category not in self.memories:
            return None
        if key:
            return self.memories[category].get(key)
        return self.memories[category]

    def get_context_summary(self) -> str:
        """Claude에게 전달할 컨텍스트 요약 생성"""
        summary = f"Project: {self.project_id}\n\n"
        for category, items in self.memories.items():
            summary += f"## {category}\n"
            for k, v in items.items():
                summary += f"- {k}: {v}\n"
            summary += "\n"
        return summary


# 사용 예시
project = ProjectMemory("claude-ai-knowledge")
project.store("tech_stack", "language", "Python 3.11")
project.store("tech_stack", "framework", "Anthropic SDK")
project.store("preferences", "code_style", "PEP 8")
project.store("preferences", "documentation", "Korean + English")

# 새 대화 시작 시 컨텍스트 주입
system_prompt = f"""You are a helpful coding assistant.

Here's the project context from previous sessions:
{project.get_context_summary()}

Use this context to provide relevant assistance."""
```

---

## Context Editing

### Context Editing 기본 개념

**Context Editing**은 대화 컨텍스트를 동적으로 관리하는 기능입니다.
주요 기능은 **Thinking Block 클리어**로, Extended Thinking 사용 시 이전 thinking 내용을 제거하여 토큰을 절약합니다.

#### 왜 필요한가?

Extended Thinking 사용 시 문제:
```
[Turn 1] User message + Thinking (5000 tokens) + Response
[Turn 2] User message + 이전 Thinking 포함(5000) + 새 Thinking (5000) + Response
[Turn 3] User message + 이전 Thinking 모두 포함(10000) + 새 Thinking (5000) + Response
→ 컨텍스트 폭발!
```

Context Editing 적용 후:
```
[Turn 1] User message + Thinking (5000 tokens) + Response
[Turn 2] User message + [Thinking 클리어됨] + 새 Thinking (5000) + Response
[Turn 3] User message + [Thinking 클리어됨] + 새 Thinking (5000) + Response
→ 토큰 절약!
```

### Thinking Block 클리어

#### Beta 헤더 설정

```python
import anthropic

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-opus-4-5-20251101",
    max_tokens=16000,
    betas=["clear_thinking_20251015"],  # Beta 기능 활성화
    thinking={
        "type": "enabled",
        "budget_tokens": 10000
    },
    messages=[...]
)
```

#### 작동 방식

1. **자동 클리어**: Beta 헤더 활성화 시 이전 턴의 thinking 블록 자동 제거
2. **응답은 유지**: thinking만 제거되고 실제 응답은 그대로 유지
3. **토큰 절약**: 긴 대화에서 상당한 토큰 절약 효과

### Context Editing 실전 예제

#### 예제 1: Extended Thinking + Context Editing

```python
import anthropic

client = anthropic.Anthropic()

def chat_with_thinking_clear(messages: list) -> dict:
    """Thinking 클리어를 활용한 대화"""

    response = client.messages.create(
        model="claude-opus-4-5-20251101",
        max_tokens=16000,
        betas=["clear_thinking_20251015"],
        thinking={
            "type": "enabled",
            "budget_tokens": 8000
        },
        messages=messages
    )

    # 응답 파싱
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
        "usage": response.usage
    }


def multi_turn_conversation():
    """여러 턴의 대화 예제"""

    conversation = []

    # Turn 1
    conversation.append({
        "role": "user",
        "content": "피보나치 수열의 1000번째 수를 구하는 효율적인 알고리즘을 설계해줘."
    })

    result1 = chat_with_thinking_clear(conversation)
    print(f"Turn 1 - Tokens used: {result1['usage']}")
    print(f"Response: {result1['response'][:200]}...\n")

    # 응답을 대화에 추가 (thinking은 자동으로 클리어됨)
    conversation.append({
        "role": "assistant",
        "content": [
            {"type": "thinking", "thinking": result1["thinking"]},
            {"type": "text", "text": result1["response"]}
        ]
    })

    # Turn 2
    conversation.append({
        "role": "user",
        "content": "그 알고리즘의 시간 복잡도와 공간 복잡도를 분석해줘."
    })

    result2 = chat_with_thinking_clear(conversation)
    print(f"Turn 2 - Tokens used: {result2['usage']}")
    print(f"Response: {result2['response'][:200]}...\n")

    # Turn 1의 thinking이 클리어되어 토큰 절약됨!


if __name__ == "__main__":
    multi_turn_conversation()
```

#### 예제 2: 수동 컨텍스트 관리

```python
def manage_context_manually(conversation: list, max_turns: int = 5) -> list:
    """수동으로 컨텍스트 크기 관리"""

    # 오래된 턴 제거 (최근 N개만 유지)
    if len(conversation) > max_turns * 2:  # user + assistant pairs
        # 시스템 메시지가 있다면 유지
        system_messages = [m for m in conversation if m.get("role") == "system"]
        recent_messages = conversation[-(max_turns * 2):]
        conversation = system_messages + recent_messages

    # Thinking 블록 제거 (이전 턴만)
    cleaned = []
    for i, msg in enumerate(conversation):
        if msg["role"] == "assistant" and i < len(conversation) - 1:
            # 이전 assistant 메시지의 thinking 제거
            if isinstance(msg["content"], list):
                cleaned_content = [
                    block for block in msg["content"]
                    if not (isinstance(block, dict) and block.get("type") == "thinking")
                ]
                cleaned.append({"role": "assistant", "content": cleaned_content})
            else:
                cleaned.append(msg)
        else:
            cleaned.append(msg)

    return cleaned


def summarize_old_context(conversation: list) -> str:
    """오래된 컨텍스트를 요약으로 대체"""

    # 오래된 메시지 추출
    old_messages = conversation[:-6]  # 최근 3턴 제외

    if not old_messages:
        return None

    # 요약 요청
    summary_request = "다음 대화 내용을 핵심만 간단히 요약해줘:\n\n"
    for msg in old_messages:
        role = msg["role"]
        content = msg["content"] if isinstance(msg["content"], str) else str(msg["content"])
        summary_request += f"{role}: {content[:500]}...\n"

    client = anthropic.Anthropic()
    response = client.messages.create(
        model="claude-haiku-4-5-20251015",  # 요약은 가벼운 모델로
        max_tokens=500,
        messages=[{"role": "user", "content": summary_request}]
    )

    return response.content[0].text
```

---

## Memory + Context 통합 활용

### 베스트 프랙티스

```python
class ConversationManager:
    """Memory와 Context를 통합 관리하는 클래스"""

    def __init__(self, project_id: str):
        self.project_id = project_id
        self.client = anthropic.Anthropic()
        self.memory = {}
        self.conversation = []
        self.max_context_tokens = 100000

    def store_memory(self, key: str, value: str):
        """장기 메모리에 저장"""
        self.memory[key] = value

    def get_system_prompt(self) -> str:
        """메모리 기반 시스템 프롬프트 생성"""
        prompt = "You are a helpful assistant.\n\n"

        if self.memory:
            prompt += "## Remembered Information\n"
            for k, v in self.memory.items():
                prompt += f"- {k}: {v}\n"

        return prompt

    def optimize_context(self):
        """컨텍스트 최적화"""
        # 1. 오래된 thinking 블록 제거
        for i, msg in enumerate(self.conversation[:-2]):
            if msg["role"] == "assistant" and isinstance(msg["content"], list):
                msg["content"] = [
                    b for b in msg["content"]
                    if not (isinstance(b, dict) and b.get("type") == "thinking")
                ]

        # 2. 너무 긴 대화는 요약
        if len(self.conversation) > 20:
            self._summarize_old_turns()

    def _summarize_old_turns(self):
        """오래된 대화 요약"""
        old = self.conversation[:10]
        recent = self.conversation[10:]

        # 요약 생성
        summary = self._create_summary(old)

        # 요약으로 대체
        self.conversation = [
            {"role": "user", "content": f"[이전 대화 요약]\n{summary}"},
            {"role": "assistant", "content": "네, 이전 대화 내용을 이해했습니다."}
        ] + recent

    def _create_summary(self, messages: list) -> str:
        """대화 요약 생성"""
        content = "\n".join([
            f"{m['role']}: {str(m['content'])[:200]}"
            for m in messages
        ])

        response = self.client.messages.create(
            model="claude-haiku-4-5-20251015",
            max_tokens=300,
            messages=[{
                "role": "user",
                "content": f"다음 대화의 핵심을 3줄로 요약:\n{content}"
            }]
        )
        return response.content[0].text

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

        # 응답 저장
        self.conversation.append({
            "role": "assistant",
            "content": response.content
        })

        # 텍스트 응답 반환
        for block in response.content:
            if hasattr(block, "text"):
                return block.text

        return ""


# 사용 예시
manager = ConversationManager("my-project")
manager.store_memory("user_name", "Bella")
manager.store_memory("preferred_language", "Python")

response = manager.chat("안녕! 오늘 뭘 도와줄까?")
print(response)
```

---

## 주의사항 및 제한

### Memory Tool 제한사항

| 항목 | 제한 |
|------|------|
| 상태 | Beta (변경 가능) |
| 저장소 | 자체 구현 필요 |
| 보안 | 민감 정보 저장 주의 |

### Context Editing 제한사항

| 항목 | 제한 |
|------|------|
| Beta 헤더 | `clear_thinking_20251015` 필요 |
| 적용 범위 | Thinking 블록만 클리어 |
| 호환성 | Extended Thinking 활성화 시에만 |

### 보안 고려사항

1. **민감 정보**: 비밀번호, API 키 등 저장 금지
2. **암호화**: 필요시 저장 전 암호화
3. **접근 제어**: 사용자별 메모리 분리

---

## FAQ

### Q1: Memory Tool은 Anthropic이 제공하는 저장소를 사용하나요?

아니요, Memory Tool은 **도구 정의**만 제공합니다. 실제 저장소(DB, 파일 등)는 개발자가 구현해야 합니다.

### Q2: Context Editing은 어떤 모델에서 사용 가능한가요?

Extended Thinking을 지원하는 모델에서 사용 가능합니다:
- Claude Opus 4.5
- Claude Sonnet 4.5

### Q3: Memory와 System Prompt의 차이점은?

| 구분 | Memory Tool | System Prompt |
|------|-------------|---------------|
| 지속성 | 세션 간 유지 | 요청마다 전송 |
| 동적성 | Claude가 스스로 업데이트 | 개발자가 설정 |
| 용도 | 학습된 정보 | 고정된 지침 |

### Q4: 컨텍스트 윈도우를 최대한 활용하려면?

1. Thinking 클리어 활성화
2. 오래된 대화 요약
3. 불필요한 메시지 제거
4. 핵심 정보만 Memory에 저장

---

## 참고 자료 / References

### 공식 문서
- [Memory Tool 문서](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)
- [Context Editing 문서](https://platform.claude.com/docs/en/build-with-claude/context-editing)
- [Extended Thinking 문서](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)

### 관련 문서
- [01_Claude_Tools_Complete_Guide.md](./01_Claude_Tools_Complete_Guide.md)
- [05_Structured_Outputs_Guide.md](./05_Structured_Outputs_Guide.md)
- [NEW_FEATURES_TODO_2026.md](./NEW_FEATURES_TODO_2026.md)

---

## 업데이트 로그 / Changelog

| 날짜 | 버전 | 내용 |
|------|------|------|
| 2026-02-03 | v1.0 | 초기 버전 작성 |

---

*Made with Claude by Bella (OZKIZ)*
