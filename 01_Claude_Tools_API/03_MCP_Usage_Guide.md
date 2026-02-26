---
tags:
  - claude
  - mcp
  - model-context-protocol
  - integration
---

# MCP 활용 가이드
# Model Context Protocol Usage Guide

> **Author**: Bella (OZKIZ)
> **Created**: 2026-01-30
> **Version**: v1.0
> **Purpose**: MCP 서버 설정 및 활용 완벽 가이드

---

## 목차

1. [MCP란?](#1-mcp란)
2. [지원 환경](#2-지원-환경)
3. [기본 설정](#3-기본-설정)
4. [인기 MCP 서버](#4-인기-mcp-서버)
5. [실전 활용 예제](#5-실전-활용-예제)
6. [커스텀 MCP 서버 만들기](#6-커스텀-mcp-서버-만들기)
7. [API에서 MCP 사용](#7-api에서-mcp-사용)
8. [문제 해결](#8-문제-해결)

---

# 1. MCP란?

## Model Context Protocol

MCP(Model Context Protocol)는 Claude가 외부 시스템과 통신할 수 있게 해주는 프로토콜입니다.

### 주요 기능

| 기능 | 설명 |
|------|------|
| **Resources** | 외부 데이터 읽기 (파일, DB 등) |
| **Tools** | 외부 작업 실행 (API 호출, 파일 생성 등) |
| **Prompts** | 재사용 가능한 프롬프트 템플릿 |

### MCP의 장점

```
- 로컬 파일 시스템 접근
- 데이터베이스 연결
- 외부 API 통합
- Git 저장소 관리
- Slack, Discord 등 메시징
- Google Drive, Notion 등 클라우드 서비스
```

---

# 2. 지원 환경

| 환경 | MCP 지원 | 설정 방법 |
|------|:--------:|----------|
| Claude Desktop | O | config 파일 |
| Claude Code (CLI) | O | config 파일 |
| Claude Web | X | - |
| API | O | 직접 구현 |

---

# 3. 기본 설정

## 설정 파일 위치

| OS | 경로 |
|----|------|
| **Windows** | `%APPDATA%\Claude\claude_desktop_config.json` |
| **macOS** | `~/Library/Application Support/Claude/claude_desktop_config.json` |
| **Linux** | `~/.config/Claude/claude_desktop_config.json` |

## 기본 설정 구조

```json
{
  "mcpServers": {
    "서버이름": {
      "command": "실행명령",
      "args": ["인자1", "인자2"],
      "env": {
        "환경변수": "값"
      }
    }
  }
}
```

## 설정 예시

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "C:/Users/Bella/Documents"
      ]
    }
  }
}
```

## 설정 적용

1. 설정 파일 저장
2. Claude Desktop 완전 종료 (트레이에서도)
3. Claude Desktop 재시작

---

# 4. 인기 MCP 서버

## 파일 시스템 (Filesystem)

로컬 파일 읽기/쓰기/검색

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "C:/Users/Bella/Projects",
        "C:/Users/Bella/Documents"
      ]
    }
  }
}
```

### 사용 예시
```
"Projects 폴더에서 Python 파일 찾아줘"
"README.md 파일 내용 보여줘"
"새 파일 config.json 만들어줘"
```

---

## PostgreSQL 데이터베이스

```json
{
  "mcpServers": {
    "postgres": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-postgres",
        "postgresql://user:password@localhost:5432/mydb"
      ]
    }
  }
}
```

### 사용 예시
```
"users 테이블에서 최근 가입한 10명 보여줘"
"매출 데이터 분석해줘"
"새 테이블 만들어줘"
```

---

## SQLite 데이터베이스

```json
{
  "mcpServers": {
    "sqlite": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-sqlite",
        "C:/Users/Bella/data/mydb.sqlite"
      ]
    }
  }
}
```

---

## GitHub

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "ghp_xxxxxxxxxxxxxxxxxxxx"
      }
    }
  }
}
```

### GitHub Token 발급
1. GitHub 설정 -> Developer settings
2. Personal access tokens -> Tokens (classic)
3. Generate new token
4. repo, read:user 권한 선택
5. 토큰 복사

### 사용 예시
```
"내 저장소 목록 보여줘"
"ozkiz/project의 이슈 목록 가져와줘"
"새 이슈 만들어줘"
"PR 목록 확인해줘"
```

---

## Slack

```json
{
  "mcpServers": {
    "slack": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-slack"],
      "env": {
        "SLACK_BOT_TOKEN": "xoxb-xxxxxxxxxxxx",
        "SLACK_TEAM_ID": "T0123456789"
      }
    }
  }
}
```

### Slack Token 발급
1. https://api.slack.com/apps 접속
2. Create New App -> From scratch
3. OAuth & Permissions -> Bot Token Scopes 추가:
   - channels:read
   - chat:write
   - users:read
4. Install to Workspace
5. Bot User OAuth Token 복사

### 사용 예시
```
"#general 채널 최근 메시지 보여줘"
"팀원들에게 회의 알림 보내줘"
"오늘 중요한 메시지 요약해줘"
```

---

## Google Drive

```json
{
  "mcpServers": {
    "gdrive": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-google-drive"],
      "env": {
        "GOOGLE_CLIENT_ID": "xxxxx.apps.googleusercontent.com",
        "GOOGLE_CLIENT_SECRET": "xxxxx"
      }
    }
  }
}
```

---

## Notion

```json
{
  "mcpServers": {
    "notion": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-notion"],
      "env": {
        "NOTION_API_KEY": "secret_xxxxxxxxxxxx"
      }
    }
  }
}
```

---

## 브라우저 자동화 (Puppeteer)

```json
{
  "mcpServers": {
    "puppeteer": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-puppeteer"]
    }
  }
}
```

### 사용 예시
```
"https://example.com 스크린샷 찍어줘"
"이 페이지에서 모든 링크 추출해줘"
"로그인 폼 자동으로 채워줘"
```

---

## 메모리 (영구 저장)

```json
{
  "mcpServers": {
    "memory": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-memory"]
    }
  }
}
```

### 사용 예시
```
"내 이름은 벨라야. 기억해줘"
"OZKIZ 프로젝트 정보 저장해줘"
"저장된 정보 보여줘"
```

---

## 전체 설정 예시

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "C:/Users/Bella/Projects"
      ]
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "ghp_xxxx"
      }
    },
    "postgres": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-postgres",
        "postgresql://localhost/mydb"
      ]
    },
    "memory": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-memory"]
    }
  }
}
```

---

# 5. 실전 활용 예제

## 프로젝트 관리

```
프롬프트:
"Projects 폴더에서 모든 package.json 파일을 찾아서
각 프로젝트의 dependencies 목록을 정리해줘"
```

## 데이터베이스 분석

```
프롬프트:
"PostgreSQL에서 지난 달 매출 데이터를 가져와서
일별 추이 분석하고 인사이트 정리해줘"
```

## GitHub 자동화

```
프롬프트:
"bellaliv423/Claude_AI_Knowledge 저장소에
README.md 파일 업데이트하는 PR 만들어줘"
```

## 문서 정리

```
프롬프트:
"Documents 폴더에서 모든 .md 파일을 읽어서
목차와 요약을 만들어줘"
```

---

# 6. 커스텀 MCP 서버 만들기

## 기본 구조 (Python)

```python
# my_mcp_server.py
from mcp.server import Server
from mcp.types import Tool, TextContent

app = Server("my-server")

@app.list_tools()
async def list_tools():
    return [
        Tool(
            name="get_weather",
            description="도시의 날씨를 가져옵니다",
            inputSchema={
                "type": "object",
                "properties": {
                    "city": {"type": "string", "description": "도시명"}
                },
                "required": ["city"]
            }
        )
    ]

@app.call_tool()
async def call_tool(name: str, arguments: dict):
    if name == "get_weather":
        city = arguments["city"]
        # 실제 날씨 API 호출
        return [TextContent(type="text", text=f"{city}의 날씨: 맑음, 20°C")]

if __name__ == "__main__":
    import asyncio
    asyncio.run(app.run())
```

## 설정에 추가

```json
{
  "mcpServers": {
    "my-weather": {
      "command": "python",
      "args": ["C:/path/to/my_mcp_server.py"]
    }
  }
}
```

---

# 7. API에서 MCP 사용

## MCP 도구를 Claude API에 연결

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
import anthropic

async def main():
    # MCP 서버 연결
    server_params = StdioServerParameters(
        command="npx",
        args=["-y", "@modelcontextprotocol/server-filesystem", "/path"]
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            # MCP 도구 목록 가져오기
            mcp_tools = await session.list_tools()

            # Claude API 형식으로 변환
            claude_tools = []
            for tool in mcp_tools.tools:
                claude_tools.append({
                    "name": tool.name,
                    "description": tool.description or "",
                    "input_schema": tool.inputSchema
                })

            # Claude API 호출
            client = anthropic.Anthropic()
            response = client.messages.create(
                model="claude-sonnet-4-5",
                max_tokens=1024,
                tools=claude_tools,
                messages=[{
                    "role": "user",
                    "content": "현재 폴더의 파일 목록 보여줘"
                }]
            )

            # 도구 호출 처리
            for block in response.content:
                if block.type == "tool_use":
                    # MCP 서버로 도구 실행
                    result = await session.call_tool(
                        block.name,
                        block.input
                    )
                    print(f"Tool result: {result}")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
```

---

# 8. 문제 해결

## MCP 서버가 인식되지 않음

```
원인: 설정 파일 경로 또는 문법 오류

해결:
1. 설정 파일 경로 확인
   - Windows: %APPDATA%\Claude\claude_desktop_config.json
   - macOS: ~/Library/Application Support/Claude/

2. JSON 문법 검사
   - 쉼표, 따옴표 확인
   - https://jsonlint.com 에서 검증

3. Claude Desktop 완전 재시작
```

## "Command not found" 에러

```
원인: npx 또는 실행 파일을 찾을 수 없음

해결:
1. Node.js 설치 확인: node --version
2. npm 설치 확인: npm --version
3. PATH 환경 변수 확인
4. 절대 경로 사용:
   "command": "C:/Program Files/nodejs/npx.cmd"
```

## 서버 연결 실패

```
원인: 서버가 시작되지 않거나 충돌

해결:
1. 수동으로 서버 실행 테스트:
   npx -y @modelcontextprotocol/server-filesystem /path

2. 로그 확인:
   - Windows: %APPDATA%\Claude\logs\
   - macOS: ~/Library/Logs/Claude/

3. 포트 충돌 확인
```

## 권한 오류

```
원인: 파일/폴더 접근 권한 없음

해결:
1. 경로에 접근 가능한지 확인
2. 관리자 권한으로 Claude 실행
3. 읽기/쓰기 권한 확인
```

## 환경 변수가 적용되지 않음

```
원인: env 설정 오류

해결:
1. 환경 변수 이름 확인 (대소문자 구분)
2. 값에 특수문자 있으면 이스케이프
3. 시스템 환경 변수로 설정 시도
```

---

## MCP 서버 목록

| 서버 | 패키지 | 용도 |
|------|--------|------|
| Filesystem | `@modelcontextprotocol/server-filesystem` | 파일 시스템 |
| PostgreSQL | `@modelcontextprotocol/server-postgres` | PostgreSQL DB |
| SQLite | `@modelcontextprotocol/server-sqlite` | SQLite DB |
| GitHub | `@modelcontextprotocol/server-github` | GitHub API |
| Slack | `@modelcontextprotocol/server-slack` | Slack 연동 |
| Google Drive | `@modelcontextprotocol/server-google-drive` | Google Drive |
| Notion | `@modelcontextprotocol/server-notion` | Notion 연동 |
| Puppeteer | `@modelcontextprotocol/server-puppeteer` | 브라우저 자동화 |
| Memory | `@modelcontextprotocol/server-memory` | 영구 저장 |
| Brave Search | `@modelcontextprotocol/server-brave-search` | 웹 검색 |
| Fetch | `@modelcontextprotocol/server-fetch` | HTTP 요청 |

더 많은 서버: https://github.com/modelcontextprotocol/servers

---

*Made with Claude by Bella (OZKIZ)*
