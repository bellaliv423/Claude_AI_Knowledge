---
tags:
  - claude
  - knowledge-base
  - index
  - readme
---

# Claude AI Knowledge Base

> **Author**: Bella (OZKIZ)
> **Created**: 2026-01-30
> **Purpose**: Claude AI 고급 기능 활용을 위한 종합 지식 베이스

---

## 소개

이 저장소는 Claude AI의 모든 고급 기능을 체계적으로 정리한 지식 베이스입니다.
어떤 디바이스에서든 GitHub에서 클론하여 바로 활용할 수 있습니다.

---

## 파일 구조

```
Claude_AI_Knowledge/
├── README.md                           # 이 파일
├── init.md                             # 시작점 가이드
├── AI_Collaboration_Log.md             # AI 협업 기록 및 기획
├── 01_Claude_Tools_Complete_Guide.md   # Claude 도구 종합 가이드
├── 02_Code_Execution_Setup_Guide.md    # Code Execution 설치 가이드
├── 03_MCP_Usage_Guide.md               # MCP 활용 가이드
├── 04_Claude_Skills_Guide.md           # Claude Skills 문서
├── Boris_Cherny_Claude_Code_Best_Practices.md  # Claude Code 창시자 워크플로우
├── Claude_Opus_4.5_Practical_Guide.md  # Opus 4.5 실전 활용 가이드
└── examples/                           # 예제 코드
    ├── code_execution_basic.py         # 기본 코드 실행
    ├── container_reuse.py              # 컨테이너 재사용
    ├── programmatic_tool_calling.py    # 프로그래매틱 도구 호출
    ├── batch_api.py                    # Batch API 사용
    ├── mcp_client.py                   # MCP 클라이언트
    └── extended_thinking.py            # Extended Thinking 예제
```

---

## 빠른 시작

### 1. 저장소 클론
```bash
git clone https://github.com/YOUR_USERNAME/Claude_AI_Knowledge.git
cd Claude_AI_Knowledge
```

### 2. 환경 설정
```bash
# Python 가상환경 생성
python -m venv venv

# 활성화
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# 패키지 설치
pip install -r requirements.txt
```

### 3. API 키 설정
```bash
# Windows (PowerShell)
$env:ANTHROPIC_API_KEY = "sk-ant-api03-..."

# macOS/Linux
export ANTHROPIC_API_KEY="sk-ant-api03-..."
```

### 4. 테스트 실행
```bash
python examples/code_execution_basic.py
```

---

## 문서 목록

| 문서 | 설명 | 난이도 |
|------|------|--------|
| [01_Claude_Tools_Complete_Guide](./01_Claude_Tools_Complete_Guide.md) | 모든 Claude 도구 종합 가이드 | 초급~고급 |
| [02_Code_Execution_Setup_Guide](./02_Code_Execution_Setup_Guide.md) | Code Execution 설치 및 설정 | 초급 |
| [03_MCP_Usage_Guide](./03_MCP_Usage_Guide.md) | MCP 서버 설정 및 활용 | 중급~고급 |
| [04_Claude_Skills_Guide](./04_Claude_Skills_Guide.md) | Agent Skills 사용법 | 고급 |

---

## 환경별 권장 문서

| 환경 | 권장 문서 |
|------|----------|
| **Claude Web** | 01번 (기본), 02번 (Code Execution) |
| **Claude Desktop** | 01번, 03번 (MCP) |
| **Claude Code (CLI)** | 01번, 04번 (Skills) |
| **API 개발** | 전체 문서 + examples 폴더 |

---

## 요구사항

- Python 3.10+
- Node.js 18+ (MCP 사용 시)
- Anthropic API Key
- Claude Pro 구독 (Code Execution 사용 시)

---

## 라이선스

이 저장소는 개인 학습 및 참고용으로 작성되었습니다.

---

## 업데이트 로그

| 날짜 | 버전 | 내용 |
|------|------|------|
| 2026-01-30 | v1.0 | 초기 버전 작성 |
| 2026-02-02 | v1.1 | AI 협업 문서 추가, 파일 구조 업데이트 |

---

*Made with Claude by Bella (OZKIZ)*
