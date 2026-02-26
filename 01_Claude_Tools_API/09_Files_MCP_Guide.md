---
tags:
  - claude
  - files-api
  - mcp
  - mcp-connector
  - integration
---

# Files API & MCP Connector 완벽 가이드
# Files API & MCP Connector Complete Guide

> **작성일 / Created**: 2026-02-26
> **업데이트 / Updated**: 2026-02-26
> **버전 / Version**: 1.0
> **Author**: Bella (OZKIZ) + Claude (Opus 4.6)

---

## 목차 / Table of Contents

1. [소개 / Introduction](#소개--introduction)
2. [Files API](#files-api)
3. [MCP Connector](#mcp-connector)
4. [Files API + MCP 연동 / Integration](#files-api--mcp-연동--integration)
5. [실전 예제 / Practical Examples](#실전-예제--practical-examples)
6. [베스트 프랙티스 / Best Practices](#베스트-프랙티스--best-practices)
7. [FAQ](#faq)
8. [참고 자료 / References](#참고-자료--references)

---

## 소개 / Introduction

Claude API는 파일 관리와 외부 도구 연결을 위한 두 가지 강력한 기능을 제공합니다:

| 기능 | 출시일 | 상태 | 핵심 역할 |
|------|--------|------|----------|
| **Files API** | 2025-05-22 | Beta | 파일 업로드 및 Messages API에서 참조 |
| **MCP Connector** | 2025-05-22 | Beta | 원격 MCP 서버 직접 연결 (클라이언트 불필요) |

### 왜 이 기능들이 중요한가?

```
기존 방식:
├── 파일 → Base64 인코딩 → messages에 직접 포함 → 매번 전송
├── MCP → 로컬 클라이언트 설정 → 프록시 서버 운영 → 복잡한 설정
└── 제한: 파일 크기 제한, 반복 전송 비용, 설정 복잡도

새로운 방식:
├── Files API → 한 번 업로드 → ID로 참조 → 재사용 가능
├── MCP Connector → API에서 직접 연결 → 클라이언트 불필요
└── 장점: 효율적, 간편, 확장 가능
```

---

## Files API

### 개요 / Overview

**Files API**는 파일을 Anthropic 서버에 업로드하고, 이후 Messages API 호출에서 파일 ID로 참조할 수 있게 해줍니다. 같은 파일을 여러 대화에서 반복 사용할 때 특히 유용합니다.

| 항목 | 내용 |
|------|------|
| **출시일** | 2025-05-22 (Beta) |
| **Beta 헤더** | `files-api-2025-04-14` |
| **지원 형식** | PDF, 이미지(PNG/JPG/GIF/WEBP), 텍스트, CSV 등 |
| **최대 파일 크기** | 32MB |
| **파일 보존 기간** | 업로드 후 최대 30일 |
| **API 엔드포인트** | `POST /v1/files` |

### 파일 업로드 / Upload

#### Python

```python
import anthropic

client = anthropic.Anthropic()

# 파일 업로드
with open("report.pdf", "rb") as f:
    uploaded_file = client.beta.files.create(
        file=f,
        purpose="messages"  # Messages API에서 사용
    )

print(f"File ID: {uploaded_file.id}")
print(f"Filename: {uploaded_file.filename}")
print(f"Size: {uploaded_file.size_bytes} bytes")
```

#### TypeScript

```typescript
import Anthropic from '@anthropic-ai/sdk';
import * as fs from 'fs';

const client = new Anthropic();

const file = await client.beta.files.create({
  file: fs.createReadStream("report.pdf"),
  purpose: "messages"
});

console.log(`File ID: ${file.id}`);
```

#### cURL

```bash
curl https://api.anthropic.com/v1/files \
    --header "x-api-key: $ANTHROPIC_API_KEY" \
    --header "anthropic-version: 2023-06-01" \
    --header "anthropic-beta: files-api-2025-04-14" \
    -F "file=@report.pdf" \
    -F "purpose=messages"
```

### 파일 참조 / Reference in Messages

```python
import anthropic

client = anthropic.Anthropic()

# 업로드된 파일을 Messages에서 참조
response = client.beta.messages.create(
    model="claude-sonnet-4-5-20250929",
    betas=["files-api-2025-04-14"],
    max_tokens=4096,
    messages=[{
        "role": "user",
        "content": [
            {
                "type": "file",
                "source": {
                    "type": "file_id",
                    "file_id": uploaded_file.id  # 업로드된 파일 ID
                }
            },
            {
                "type": "text",
                "text": "이 보고서의 핵심 내용을 요약해줘"
            }
        ]
    }]
)

print(response.content[0].text)
```

### 파일 관리 / File Management

```python
import anthropic

client = anthropic.Anthropic()

# 파일 목록 조회
files = client.beta.files.list()
for f in files.data:
    print(f"{f.id}: {f.filename} ({f.size_bytes} bytes)")

# 파일 정보 조회
file_info = client.beta.files.retrieve(file_id="file-abc123")
print(f"Status: {file_info.status}")  # "uploaded" | "processing" | "ready"

# 파일 삭제
client.beta.files.delete(file_id="file-abc123")
```

### 파일 유형별 사용

| 파일 유형 | content type | 예시 |
|-----------|-------------|------|
| **PDF** | `file` | 보고서, 논문, 계약서 분석 |
| **이미지** | `image` | 스크린샷 분석, 차트 해석 |
| **CSV/Excel** | `file` | 데이터 분석, 통계 처리 |
| **텍스트** | `file` | 코드 리뷰, 문서 분석 |
| **JSON** | `file` | API 응답 분석, 설정 검토 |

### Base64 vs Files API 비교

| 항목 | Base64 (기존) | Files API (새로운) |
|------|--------------|-------------------|
| **전송 방식** | 매 요청마다 인코딩 포함 | 한 번 업로드, ID로 참조 |
| **재사용** | 매번 재전송 필요 | 파일 ID로 무한 재사용 |
| **크기 제한** | ~5MB (인코딩 후) | **32MB** |
| **비용** | 매번 토큰 소비 | 첫 업로드만 비용 |
| **관리** | 불가능 | 목록/조회/삭제 가능 |
| **보존** | 요청 중만 | 최대 30일 |

---

## MCP Connector

### 개요 / Overview

**MCP Connector**는 Claude API에서 직접 원격 MCP(Model Context Protocol) 서버에 연결하는 기능입니다. 별도의 MCP 클라이언트를 구현하지 않아도 됩니다.

| 항목 | 내용 |
|------|------|
| **출시일** | 2025-05-22 (Beta) |
| **Beta 헤더** | `mcp-connector-2025-05-14` |
| **프로토콜** | MCP over SSE (Server-Sent Events) |
| **인증** | OAuth 2.0 지원 |
| **용도** | 원격 MCP 서버 도구를 API에서 직접 사용 |

### MCP Connector의 장점

```
기존 MCP 사용 방식:
├── 1. MCP 서버 실행 (로컬/원격)
├── 2. MCP 클라이언트 코드 작성
├── 3. 클라이언트 ↔ 서버 통신 관리
├── 4. 도구 호출 결과를 Claude에 전달
└── = 복잡한 설정 + 유지보수

MCP Connector 방식:
├── 1. MCP 서버 URL 제공
├── 2. Claude API가 직접 연결
└── = 간편한 설정, 유지보수 최소화
```

### 사용 방법 / How to Use

#### 기본 사용법

```python
import anthropic

client = anthropic.Anthropic()

response = client.beta.messages.create(
    model="claude-sonnet-4-5-20250929",
    betas=["mcp-connector-2025-05-14"],
    max_tokens=4096,
    mcp_servers=[
        {
            "type": "url",
            "url": "https://my-mcp-server.example.com/sse",
            "name": "my-tools"
        }
    ],
    messages=[{
        "role": "user",
        "content": "데이터베이스에서 최근 주문 목록을 가져와줘"
    }]
)

print(response.content[0].text)
```

#### OAuth 인증 포함

```python
import anthropic

client = anthropic.Anthropic()

response = client.beta.messages.create(
    model="claude-sonnet-4-5-20250929",
    betas=["mcp-connector-2025-05-14"],
    max_tokens=4096,
    mcp_servers=[
        {
            "type": "url",
            "url": "https://secure-mcp.example.com/sse",
            "name": "secure-tools",
            "authorization_token": "Bearer your-oauth-token-here"
        }
    ],
    messages=[{
        "role": "user",
        "content": "내 Slack 채널 목록을 보여줘"
    }]
)
```

#### 다중 MCP 서버 연결

```python
import anthropic

client = anthropic.Anthropic()

response = client.beta.messages.create(
    model="claude-sonnet-4-5-20250929",
    betas=["mcp-connector-2025-05-14"],
    max_tokens=4096,
    mcp_servers=[
        {
            "type": "url",
            "url": "https://github-mcp.example.com/sse",
            "name": "github-tools"
        },
        {
            "type": "url",
            "url": "https://notion-mcp.example.com/sse",
            "name": "notion-tools"
        },
        {
            "type": "url",
            "url": "https://slack-mcp.example.com/sse",
            "name": "slack-tools"
        }
    ],
    messages=[{
        "role": "user",
        "content": "GitHub의 최근 이슈를 Notion에 정리하고 Slack에 알림 보내줘"
    }]
)
```

### MCP 서버 도구 자동 검색

MCP Connector는 연결된 서버의 도구를 **자동으로 검색**합니다:

```
연결 과정:
1. Claude API → MCP 서버에 SSE 연결
2. MCP 서버 → 사용 가능한 도구 목록 반환
3. Claude → 도구 목록을 컨텍스트에 추가
4. Claude → 필요한 도구 자동 호출
5. MCP 서버 → 도구 실행 결과 반환
6. Claude → 최종 응답 생성
```

### MCP Connector 설정 옵션

| 옵션 | 필수 | 설명 |
|------|------|------|
| `type` | ✅ | `"url"` (현재 유일한 타입) |
| `url` | ✅ | MCP 서버 SSE 엔드포인트 |
| `name` | ✅ | 서버 식별 이름 |
| `authorization_token` | ❌ | OAuth Bearer 토큰 |
| `tool_configuration` | ❌ | 도구 필터링 설정 |

### 도구 필터링

```python
mcp_servers=[
    {
        "type": "url",
        "url": "https://my-mcp.example.com/sse",
        "name": "my-tools",
        "tool_configuration": {
            "allowed_tools": ["read_file", "search_code"],
            # 또는
            "blocked_tools": ["delete_file", "execute_command"]
        }
    }
]
```

---

## Files API + MCP 연동 / Integration

### 파일 업로드 → MCP 도구로 분석

```python
import anthropic

client = anthropic.Anthropic()

# 1. 파일 업로드
with open("sales_data.csv", "rb") as f:
    file = client.beta.files.create(file=f, purpose="messages")

# 2. MCP 서버의 분석 도구와 함께 사용
response = client.beta.messages.create(
    model="claude-sonnet-4-5-20250929",
    betas=["files-api-2025-04-14", "mcp-connector-2025-05-14"],
    max_tokens=4096,
    mcp_servers=[{
        "type": "url",
        "url": "https://analytics-mcp.example.com/sse",
        "name": "analytics"
    }],
    messages=[{
        "role": "user",
        "content": [
            {
                "type": "file",
                "source": {"type": "file_id", "file_id": file.id}
            },
            {
                "type": "text",
                "text": "이 매출 데이터를 분석하고 대시보드에 추가해줘"
            }
        ]
    }]
)
```

---

## 실전 예제 / Practical Examples

### 예제 1: 문서 관리 시스템

```python
import anthropic
from pathlib import Path

client = anthropic.Anthropic()

class DocumentManager:
    """Files API를 활용한 문서 관리 시스템"""

    def __init__(self):
        self.file_registry = {}  # filename -> file_id 매핑

    def upload(self, filepath: str) -> str:
        """파일 업로드 및 등록"""
        with open(filepath, "rb") as f:
            result = client.beta.files.create(
                file=f,
                purpose="messages"
            )
        self.file_registry[Path(filepath).name] = result.id
        return result.id

    def analyze(self, filename: str, question: str) -> str:
        """등록된 파일에 대해 질문"""
        file_id = self.file_registry.get(filename)
        if not file_id:
            return f"파일 '{filename}'이 등록되지 않았습니다."

        response = client.beta.messages.create(
            model="claude-sonnet-4-5-20250929",
            betas=["files-api-2025-04-14"],
            max_tokens=4096,
            messages=[{
                "role": "user",
                "content": [
                    {"type": "file", "source": {"type": "file_id", "file_id": file_id}},
                    {"type": "text", "text": question}
                ]
            }]
        )
        return response.content[0].text

    def compare(self, file1: str, file2: str, criteria: str) -> str:
        """두 파일 비교 분석"""
        id1 = self.file_registry.get(file1)
        id2 = self.file_registry.get(file2)

        response = client.beta.messages.create(
            model="claude-sonnet-4-5-20250929",
            betas=["files-api-2025-04-14"],
            max_tokens=4096,
            messages=[{
                "role": "user",
                "content": [
                    {"type": "file", "source": {"type": "file_id", "file_id": id1}},
                    {"type": "file", "source": {"type": "file_id", "file_id": id2}},
                    {"type": "text", "text": f"두 문서를 다음 기준으로 비교해줘: {criteria}"}
                ]
            }]
        )
        return response.content[0].text

# 사용 예시
dm = DocumentManager()
dm.upload("contract_v1.pdf")
dm.upload("contract_v2.pdf")

summary = dm.analyze("contract_v1.pdf", "계약 조건을 요약해줘")
diff = dm.compare("contract_v1.pdf", "contract_v2.pdf", "변경된 조항")
```

### 예제 2: MCP 기반 워크플로우 자동화

```python
import anthropic

client = anthropic.Anthropic()

def automated_workflow(task: str) -> str:
    """MCP 서버를 활용한 자동화 워크플로우"""

    response = client.beta.messages.create(
        model="claude-sonnet-4-5-20250929",
        betas=["mcp-connector-2025-05-14"],
        max_tokens=4096,
        mcp_servers=[
            {
                "type": "url",
                "url": "https://github-mcp.example.com/sse",
                "name": "github",
                "authorization_token": "Bearer ghp_xxx"
            },
            {
                "type": "url",
                "url": "https://slack-mcp.example.com/sse",
                "name": "slack",
                "authorization_token": "Bearer xoxb-xxx"
            },
            {
                "type": "url",
                "url": "https://notion-mcp.example.com/sse",
                "name": "notion",
                "authorization_token": "Bearer ntn_xxx"
            }
        ],
        messages=[{
            "role": "user",
            "content": task
        }]
    )

    return response.content[0].text

# 사용 예시
result = automated_workflow(
    "GitHub의 열린 이슈 중 버그 라벨이 붙은 것을 "
    "Notion 데이터베이스에 정리하고, "
    "Slack #dev 채널에 요약을 공유해줘"
)
```

### 예제 3: 다중 파일 배치 분석

```python
import anthropic
import asyncio
from pathlib import Path

async def batch_analyze_files(folder: str, question: str) -> list[dict]:
    """폴더 내 모든 파일을 배치 분석"""

    client = anthropic.AsyncAnthropic()
    results = []

    # 1. 모든 파일 업로드
    file_ids = {}
    for filepath in Path(folder).glob("*.pdf"):
        with open(filepath, "rb") as f:
            uploaded = await client.beta.files.create(
                file=f,
                purpose="messages"
            )
        file_ids[filepath.name] = uploaded.id

    # 2. 각 파일에 대해 병렬 분석
    async def analyze_one(name: str, fid: str) -> dict:
        response = await client.beta.messages.create(
            model="claude-sonnet-4-5-20250929",
            betas=["files-api-2025-04-14"],
            max_tokens=2048,
            messages=[{
                "role": "user",
                "content": [
                    {"type": "file", "source": {"type": "file_id", "file_id": fid}},
                    {"type": "text", "text": question}
                ]
            }]
        )
        return {"filename": name, "analysis": response.content[0].text}

    tasks = [analyze_one(name, fid) for name, fid in file_ids.items()]
    results = await asyncio.gather(*tasks)
    return results

# 사용 예시
results = asyncio.run(batch_analyze_files(
    "./reports/",
    "이 보고서의 핵심 수치와 결론을 추출해줘"
))
for r in results:
    print(f"=== {r['filename']} ===")
    print(r['analysis'])
```

---

## 베스트 프랙티스 / Best Practices

### Files API

```
1. 파일 재사용 최적화
   ├── 자주 사용하는 파일은 ID 캐싱
   ├── 30일 보존 기간 활용
   └── 불필요한 파일은 즉시 삭제

2. 파일 크기 관리
   ├── PDF: 페이지 수 확인 (대형 PDF 분할 고려)
   ├── 이미지: 해상도 최적화 (불필요하게 크지 않게)
   └── CSV: 필요한 열/행만 추출 후 업로드

3. 에러 핸들링
   ├── 업로드 실패 시 재시도 로직
   ├── 파일 상태 확인 (processing → ready)
   └── 만료된 파일 ID 사용 방지
```

### MCP Connector

```
1. 서버 선택
   ├── 공식/검증된 MCP 서버 사용
   ├── SSE 프로토콜 지원 확인
   └── 응답 시간이 빠른 서버 선택

2. 보안
   ├── OAuth 토큰은 환경 변수로 관리
   ├── tool_configuration으로 권한 최소화
   ├── 민감한 도구는 blocked_tools로 차단
   └── HTTPS 필수

3. 성능
   ├── 필요한 MCP 서버만 연결
   ├── 도구 필터링으로 불필요한 도구 제외
   └── 서버 응답 시간 모니터링
```

---

## FAQ

### Q1: Files API로 업로드한 파일은 안전한가요?

파일은 Anthropic의 보안 인프라에 저장되며, 30일 후 자동 삭제됩니다. API 키 소유자만 접근할 수 있습니다.

### Q2: MCP Connector로 로컬 MCP 서버에 연결할 수 있나요?

MCP Connector는 **공개 URL**이 필요합니다. 로컬 서버는 ngrok 등으로 터널링하거나 클라우드에 배포해야 합니다. 로컬 MCP 서버는 기존 Claude Desktop/Code 방식을 사용하세요.

### Q3: 파일 업로드 후 바로 사용할 수 있나요?

대부분의 파일은 즉시 사용 가능합니다. 대용량 파일은 `processing` 상태일 수 있으므로, `retrieve`로 상태를 확인하세요.

### Q4: MCP Connector의 타임아웃은?

기본 타임아웃은 약 60초입니다. MCP 서버가 이보다 오래 걸리면 에러가 발생합니다.

### Q5: Files API와 Base64 방식을 혼용할 수 있나요?

네, 같은 messages 배열에서 `file_id`와 `base64` 소스를 혼용할 수 있습니다.

---

## 참고 자료 / References

### 공식 문서
- [Files API](https://platform.claude.com/docs/en/build-with-claude/files)
- [MCP Connector](https://platform.claude.com/docs/en/agents-and-tools/mcp-connector)
- [MCP Protocol](https://modelcontextprotocol.io)
- [Tool Use Overview](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)

### 이 프로젝트의 관련 문서
- [01_Claude_Tools_Complete_Guide.md](./01_Claude_Tools_Complete_Guide.md) - 도구 종합 가이드
- [03_MCP_Usage_Guide.md](./03_MCP_Usage_Guide.md) - MCP 활용 가이드
- [08_New_Tools_Guide.md](./08_New_Tools_Guide.md) - 새로운 도구 가이드

---

## 업데이트 로그 / Changelog

| 날짜 | 버전 | 내용 |
|------|------|------|
| 2026-02-26 | v1.0 | 초기 버전 작성 |

---

*Made with Claude by Bella (OZKIZ)*
