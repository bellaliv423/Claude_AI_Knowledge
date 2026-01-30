# Claude Skills 가이드
# Claude Agent Skills Guide

> **Author**: Bella (OZKIZ)
> **Created**: 2026-01-30
> **Version**: v1.0
> **Purpose**: Claude Agent Skills 사용법 완벽 가이드

---

## 목차

1. [Agent Skills란?](#1-agent-skills란)
2. [지원 환경](#2-지원-환경)
3. [기본 사용법](#3-기본-사용법)
4. [내장 Skills](#4-내장-skills)
5. [커스텀 Skills 만들기](#5-커스텀-skills-만들기)
6. [API에서 Skills 사용](#6-api에서-skills-사용)
7. [실전 예제](#7-실전-예제)
8. [문제 해결](#8-문제-해결)

---

# 1. Agent Skills란?

## 개요

Agent Skills는 Claude의 기능을 확장하는 모듈식 능력입니다.
지침, 스크립트, 리소스로 구성되어 Claude가 특정 작업을 더 잘 수행할 수 있게 합니다.

### 구성 요소

| 구성 요소 | 설명 |
|----------|------|
| **Instructions** | 작업 수행 방법에 대한 지침 |
| **Scripts** | 실행 가능한 코드 |
| **Resources** | 참조 데이터, 템플릿 등 |

### 장점

```
- 복잡한 작업 자동화
- 재사용 가능한 워크플로우
- 일관된 출력 형식
- 도메인 전문 지식 캡슐화
```

---

# 2. 지원 환경

| 환경 | Skills 지원 | 비고 |
|------|:-----------:|------|
| Claude Code (CLI) | O | 슬래시 명령어 |
| API | O | Code Execution 필요 |
| Claude Desktop | 제한적 | MCP 통해 가능 |
| Claude Web | X | - |

---

# 3. 기본 사용법

## Claude Code에서

### 슬래시 명령어

```bash
# 도움말
/help

# 커밋 생성
/commit

# PR 리뷰
/review-pr 123

# 코드 설명
/explain

# 테스트 생성
/test
```

### 사용 예시

```bash
# Claude Code 실행
claude

# 대화 중 Skills 사용
> /commit
> /review-pr 456
> /explain src/main.py
```

---

# 4. 내장 Skills

## /commit - Git 커밋

변경사항을 분석하고 커밋 메시지 생성

```bash
/commit

# 옵션
/commit -m "커밋 메시지"  # 메시지 지정
/commit --amend           # 수정 커밋
```

### 동작 과정
1. `git status` 확인
2. `git diff` 분석
3. 커밋 메시지 생성
4. 사용자 확인 후 커밋

---

## /review-pr - PR 리뷰

Pull Request 코드 리뷰

```bash
/review-pr 123

# GitHub URL로도 가능
/review-pr https://github.com/user/repo/pull/123
```

### 리뷰 내용
- 코드 품질 분석
- 버그 가능성 탐지
- 개선 제안
- 보안 이슈 확인

---

## /explain - 코드 설명

코드의 동작 원리 설명

```bash
/explain                    # 현재 파일
/explain src/main.py        # 특정 파일
/explain src/               # 디렉토리 전체
```

---

## /test - 테스트 생성

코드에 대한 테스트 케이스 자동 생성

```bash
/test                       # 현재 파일
/test src/utils.py          # 특정 파일
/test --coverage            # 커버리지 목표
```

---

## /fix - 버그 수정

에러 메시지를 분석하고 수정 제안

```bash
/fix "에러 메시지"
/fix                        # 마지막 에러 자동 감지
```

---

## /refactor - 리팩토링

코드 품질 개선 제안

```bash
/refactor src/main.py
/refactor --style clean     # 클린 코드 스타일
/refactor --performance     # 성능 최적화
```

---

## /docs - 문서 생성

코드 문서화

```bash
/docs                       # README 생성
/docs src/api/              # API 문서 생성
/docs --format markdown     # 마크다운 형식
```

---

# 5. 커스텀 Skills 만들기

## 스킬 구조

```
my-skill/
├── skill.json          # 스킬 메타데이터
├── instructions.md     # 지침
├── scripts/           # 실행 스크립트
│   └── main.py
└── resources/         # 리소스 파일
    └── template.md
```

## skill.json

```json
{
  "name": "my-custom-skill",
  "version": "1.0.0",
  "description": "나만의 커스텀 스킬",
  "author": "Bella",
  "instructions": "instructions.md",
  "scripts": [
    {
      "name": "main",
      "path": "scripts/main.py",
      "description": "메인 스크립트"
    }
  ],
  "resources": [
    {
      "name": "template",
      "path": "resources/template.md"
    }
  ],
  "inputs": [
    {
      "name": "target",
      "type": "string",
      "description": "대상 파일 또는 폴더",
      "required": true
    }
  ]
}
```

## instructions.md

```markdown
# My Custom Skill

## 목적
이 스킬은 [목적]을 위해 사용됩니다.

## 사용 방법
1. 대상 파일을 지정합니다
2. 분석을 수행합니다
3. 결과를 출력합니다

## 출력 형식
- 요약
- 상세 분석
- 권장 사항
```

## scripts/main.py

```python
import sys
import json

def main(target: str):
    """
    메인 스크립트
    """
    result = {
        "target": target,
        "analysis": "분석 결과...",
        "recommendations": ["권장 사항 1", "권장 사항 2"]
    }
    return json.dumps(result, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    print(main(target))
```

## 스킬 등록

```bash
# Claude Code 설정 디렉토리에 복사
cp -r my-skill ~/.claude/skills/

# 또는 설정 파일에 경로 추가
# ~/.claude/config.json
{
  "skills": {
    "paths": ["~/.claude/skills", "/path/to/my/skills"]
  }
}
```

---

# 6. API에서 Skills 사용

## Code Execution과 함께 사용

```python
import anthropic

client = anthropic.Anthropic()

# 스킬 정의
skill_instructions = """
# 코드 리뷰 스킬

## 지침
1. 코드를 분석합니다
2. 버그 가능성을 찾습니다
3. 개선점을 제안합니다

## 출력 형식
- 요약
- 이슈 목록
- 권장 사항
"""

response = client.beta.messages.create(
    model="claude-sonnet-4-5",
    betas=["code-execution-2025-08-25"],
    max_tokens=4096,
    system=skill_instructions,
    messages=[{
        "role": "user",
        "content": """
        다음 코드를 리뷰해줘:

        ```python
        def calculate(a, b):
            return a / b
        ```
        """
    }],
    tools=[{
        "type": "code_execution_20250825",
        "name": "code_execution"
    }]
)
```

## 스킬 체인

여러 스킬을 연결하여 복잡한 워크플로우 구성

```python
# 1단계: 코드 분석
analysis_response = client.messages.create(
    model="claude-sonnet-4-5",
    system="코드 분석 스킬 지침...",
    messages=[{"role": "user", "content": code}]
)

# 2단계: 테스트 생성
test_response = client.messages.create(
    model="claude-sonnet-4-5",
    system="테스트 생성 스킬 지침...",
    messages=[
        {"role": "user", "content": code},
        {"role": "assistant", "content": analysis_response.content[0].text},
        {"role": "user", "content": "이 분석을 바탕으로 테스트를 생성해줘"}
    ]
)

# 3단계: 문서화
docs_response = client.messages.create(
    model="claude-sonnet-4-5",
    system="문서화 스킬 지침...",
    messages=[{"role": "user", "content": f"코드: {code}\n분석: {analysis}"}]
)
```

---

# 7. 실전 예제

## 예제 1: 자동 코드 리뷰 봇

```python
# code_review_skill.py

SKILL_INSTRUCTIONS = """
# 코드 리뷰 스킬

## 역할
시니어 개발자로서 코드를 리뷰합니다.

## 체크리스트
- [ ] 코드 스타일 일관성
- [ ] 에러 처리
- [ ] 성능 이슈
- [ ] 보안 취약점
- [ ] 테스트 커버리지

## 출력 형식
### 요약
전체 평가 (1-10점)

### 이슈
| 심각도 | 위치 | 설명 | 해결 방법 |
|--------|------|------|----------|

### 잘한 점
- 항목 1
- 항목 2

### 개선 제안
1. 제안 1
2. 제안 2
"""

def review_code(code: str) -> str:
    client = anthropic.Anthropic()
    response = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=4096,
        system=SKILL_INSTRUCTIONS,
        messages=[{
            "role": "user",
            "content": f"다음 코드를 리뷰해주세요:\n\n```\n{code}\n```"
        }]
    )
    return response.content[0].text
```

## 예제 2: 문서 자동 생성

```python
# docs_skill.py

SKILL_INSTRUCTIONS = """
# API 문서 생성 스킬

## 역할
코드를 분석하여 API 문서를 생성합니다.

## 출력 형식
# API 문서

## 개요
[프로젝트 설명]

## 엔드포인트

### `GET /api/endpoint`
**설명**: ...
**파라미터**: ...
**응답**: ...
**예시**: ...
"""

def generate_docs(code: str) -> str:
    client = anthropic.Anthropic()
    response = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=8192,
        system=SKILL_INSTRUCTIONS,
        messages=[{
            "role": "user",
            "content": f"다음 코드의 API 문서를 생성해주세요:\n\n{code}"
        }]
    )
    return response.content[0].text
```

## 예제 3: 테스트 자동 생성

```python
# test_skill.py

SKILL_INSTRUCTIONS = """
# 테스트 생성 스킬

## 역할
코드에 대한 포괄적인 테스트 케이스를 생성합니다.

## 테스트 유형
- 단위 테스트
- 경계값 테스트
- 에러 케이스
- 통합 테스트

## 출력 형식
pytest 형식의 테스트 코드
"""

def generate_tests(code: str) -> str:
    client = anthropic.Anthropic()
    response = client.beta.messages.create(
        model="claude-sonnet-4-5",
        betas=["code-execution-2025-08-25"],
        max_tokens=4096,
        system=SKILL_INSTRUCTIONS,
        messages=[{
            "role": "user",
            "content": f"다음 코드에 대한 테스트를 생성해주세요:\n\n{code}"
        }],
        tools=[{
            "type": "code_execution_20250825",
            "name": "code_execution"
        }]
    )
    return response.content
```

---

# 8. 문제 해결

## 스킬이 인식되지 않음

```
원인: 스킬 경로가 잘못됨

해결:
1. 스킬 디렉토리 확인
2. skill.json 문법 검사
3. Claude Code 재시작
```

## 스킬 실행 실패

```
원인: 스크립트 오류

해결:
1. 스크립트 수동 실행 테스트
   python scripts/main.py test
2. 의존성 확인
3. 권한 확인
```

## 출력이 예상과 다름

```
원인: 지침이 불명확함

해결:
1. instructions.md 구체화
2. 예시 추가
3. 출력 형식 명시
```

---

## 스킬 개발 팁

### 1. 명확한 지침
```markdown
# 좋은 예
"각 함수에 대해 다음 정보를 추출하세요:
- 함수명
- 파라미터 (이름, 타입, 설명)
- 반환값
- 사용 예시"

# 나쁜 예
"함수를 분석하세요"
```

### 2. 구조화된 출력
```markdown
# 좋은 예
"다음 JSON 형식으로 출력하세요:
{
  "summary": "...",
  "issues": [...],
  "score": 0-10
}"

# 나쁜 예
"분석 결과를 알려주세요"
```

### 3. 에러 처리
```python
def main(target):
    try:
        # 작업 수행
        return {"status": "success", "result": ...}
    except FileNotFoundError:
        return {"status": "error", "message": "파일을 찾을 수 없습니다"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
```

---

## 유용한 스킬 아이디어

| 스킬 | 설명 |
|------|------|
| **changelog** | Git 히스토리에서 변경 로그 생성 |
| **migrate** | 데이터베이스 마이그레이션 생성 |
| **i18n** | 다국어 번역 파일 생성 |
| **security-audit** | 보안 취약점 스캔 |
| **dependency-check** | 의존성 업데이트 확인 |
| **api-client** | API 클라이언트 코드 생성 |
| **mock-data** | 테스트용 목 데이터 생성 |

---

*Made with Claude by Bella (OZKIZ)*
