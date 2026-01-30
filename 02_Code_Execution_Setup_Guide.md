# Code Execution 설치 가이드
# Code Execution Setup Guide

> **Author**: Bella (OZKIZ)
> **Created**: 2026-01-30
> **Version**: v1.0
> **Purpose**: Claude Code Execution 기능 설치 및 설정 완벽 가이드

---

## 목차

1. [개요](#1-개요)
2. [사전 요구사항](#2-사전-요구사항)
3. [환경별 설치 가이드](#3-환경별-설치-가이드)
4. [API 키 설정](#4-api-키-설정)
5. [기본 사용법](#5-기본-사용법)
6. [고급 기능](#6-고급-기능)
7. [문제 해결](#7-문제-해결)

---

# 1. 개요

## Code Execution이란?

Claude가 Python 코드를 실행하고, 파일을 생성하며, 데이터를 분석할 수 있게 해주는 기능입니다.

| 항목 | 내용 |
|------|------|
| **버전** | `code_execution_20250825` |
| **베타 헤더** | `code-execution-2025-08-25` |
| **Python 버전** | 3.11.12 |
| **인터넷 연결** | 차단됨 (보안) |
| **컨테이너 수명** | 30일 |

## 사용 가능 환경

| 환경 | 사용 가능 | 요구 조건 |
|------|:--------:|----------|
| Claude Web | O | Pro 이상 플랜 |
| Claude Desktop | O | Pro 이상 플랜 |
| Claude Code (CLI) | X | - |
| API | O | API 키 |

---

# 2. 사전 요구사항

## Claude Web/Desktop 사용 시

- Claude Pro 구독 ($20/월) 이상
- 최신 버전의 브라우저 또는 앱

## API 사용 시

### 필수 소프트웨어

| 소프트웨어 | 최소 버전 | 확인 명령 |
|-----------|---------|----------|
| Python | 3.10+ | `python --version` |
| pip | 21.0+ | `pip --version` |

### 패키지 설치

```bash
# Anthropic SDK 설치
pip install anthropic

# 최신 버전으로 업그레이드
pip install --upgrade anthropic

# 버전 확인 (0.77.0 이상 필요)
pip show anthropic | grep Version
```

---

# 3. 환경별 설치 가이드

## A. Claude Web (가장 쉬움)

### 단계 1: Pro 플랜 구독
1. https://claude.ai 접속
2. 설정 -> 플랜 -> Pro 업그레이드
3. 결제 정보 입력 ($20/월)

### 단계 2: 기능 활성화
1. 설정 -> 기능
2. "Code Execution" 토글 활성화
3. 페이지 새로고침

### 단계 3: 사용
```
프롬프트 예시:
"1부터 100까지의 합을 계산해줘"
"이 CSV 파일 분석해줘" [파일 첨부]
"막대 차트 그려줘"
```

---

## B. Claude Desktop

### 단계 1: 앱 설치

**Windows:**
1. https://claude.ai/download 접속
2. Windows 버전 다운로드
3. `Claude-Setup.exe` 실행
4. 설치 완료 후 로그인

**macOS:**
1. https://claude.ai/download 접속
2. macOS 버전 다운로드
3. DMG 파일 열기
4. Claude.app을 Applications로 드래그
5. 실행 후 로그인

### 단계 2: Pro 플랜 확인
- 앱 내에서 Pro 플랜 로그인 필요

### 단계 3: 사용
- Claude Web과 동일하게 사용

---

## C. API 사용 (개발자용)

### 단계 1: Python 환경 설정

```bash
# 가상환경 생성 (권장)
python -m venv claude_env

# 활성화
# Windows
claude_env\Scripts\activate
# macOS/Linux
source claude_env/bin/activate

# Anthropic SDK 설치
pip install anthropic
```

### 단계 2: API 키 발급

1. https://console.anthropic.com 접속
2. 계정 생성 또는 로그인
3. "API Keys" 메뉴 클릭
4. "Create Key" 클릭
5. 키 이름 입력 (예: "code-execution-key")
6. 생성된 키 복사 (한 번만 표시됨!)

### 단계 3: 환경 변수 설정

**Windows (PowerShell):**
```powershell
# 임시 설정 (현재 세션만)
$env:ANTHROPIC_API_KEY = "sk-ant-api03-..."

# 영구 설정
[System.Environment]::SetEnvironmentVariable("ANTHROPIC_API_KEY", "sk-ant-api03-...", "User")

# 확인
echo $env:ANTHROPIC_API_KEY
```

**Windows (CMD):**
```cmd
# 임시 설정
set ANTHROPIC_API_KEY=sk-ant-api03-...

# 영구 설정 (시스템 환경 변수)
setx ANTHROPIC_API_KEY "sk-ant-api03-..."
```

**macOS/Linux:**
```bash
# ~/.bashrc 또는 ~/.zshrc에 추가
echo 'export ANTHROPIC_API_KEY="sk-ant-api03-..."' >> ~/.bashrc

# 적용
source ~/.bashrc

# 확인
echo $ANTHROPIC_API_KEY
```

### 단계 4: 테스트 코드 실행

```python
# test_code_execution.py
import os
from anthropic import Anthropic

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

response = client.beta.messages.create(
    model="claude-sonnet-4-5",
    betas=["code-execution-2025-08-25"],
    max_tokens=4096,
    messages=[{
        "role": "user",
        "content": "2 + 2를 계산해줘"
    }],
    tools=[{
        "type": "code_execution_20250825",
        "name": "code_execution"
    }]
)

print("Response:")
for block in response.content:
    print(f"Type: {block.type}")
    if hasattr(block, 'text'):
        print(f"Text: {block.text}")
```

```bash
python test_code_execution.py
```

---

# 4. API 키 설정

## API 키 형식

```
sk-ant-api03-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

- `sk-ant-api03-`로 시작
- 총 약 100자 이상의 문자열

## 보안 주의사항

```
절대 하지 말 것:
- Git에 API 키 커밋
- 공개 저장소에 업로드
- 코드에 직접 하드코딩
- 스크린샷에 노출

권장 방법:
- 환경 변수 사용
- .env 파일 + .gitignore
- 시크릿 매니저 사용
```

## .env 파일 사용법

```bash
# .env 파일 생성
ANTHROPIC_API_KEY=sk-ant-api03-...
```

```python
# Python에서 사용
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("ANTHROPIC_API_KEY")
```

```bash
# .gitignore에 추가
echo ".env" >> .gitignore
```

---

# 5. 기본 사용법

## 간단한 계산

```python
response = client.beta.messages.create(
    model="claude-sonnet-4-5",
    betas=["code-execution-2025-08-25"],
    max_tokens=4096,
    messages=[{
        "role": "user",
        "content": "피보나치 수열의 처음 20개 숫자를 계산해줘"
    }],
    tools=[{
        "type": "code_execution_20250825",
        "name": "code_execution"
    }]
)
```

## 파일 업로드 및 분석

```python
# 1. 파일 업로드
file_response = client.beta.files.upload(
    file=open("sales_data.csv", "rb")
)

# 2. 분석 요청
response = client.beta.messages.create(
    model="claude-sonnet-4-5",
    betas=["code-execution-2025-08-25", "files-api-2025-04-14"],
    max_tokens=4096,
    messages=[{
        "role": "user",
        "content": [
            {"type": "text", "text": "이 CSV 파일을 분석하고 시각화해줘"},
            {"type": "container_upload", "file_id": file_response.id}
        ]
    }],
    tools=[{
        "type": "code_execution_20250825",
        "name": "code_execution"
    }]
)
```

## 차트 생성

```python
response = client.beta.messages.create(
    model="claude-sonnet-4-5",
    betas=["code-execution-2025-08-25"],
    max_tokens=4096,
    messages=[{
        "role": "user",
        "content": """
        다음 데이터로 파이 차트를 그려줘:
        - 한국: 40%
        - 일본: 25%
        - 미국: 20%
        - 기타: 15%

        예쁜 색상으로, PNG 파일로 저장해줘.
        """
    }],
    tools=[{
        "type": "code_execution_20250825",
        "name": "code_execution"
    }]
)
```

---

# 6. 고급 기능

## Container 재사용

컨테이너를 재사용하여 파일과 상태를 유지합니다.

```python
# 첫 번째 요청
response1 = client.beta.messages.create(
    model="claude-sonnet-4-5",
    betas=["code-execution-2025-08-25"],
    max_tokens=4096,
    messages=[{
        "role": "user",
        "content": "랜덤 숫자를 생성해서 /tmp/number.txt에 저장해줘"
    }],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}]
)

# 컨테이너 ID 추출
container_id = response1.container.id
print(f"Container ID: {container_id}")

# 두 번째 요청 - 같은 컨테이너 사용
response2 = client.beta.messages.create(
    container=container_id,
    model="claude-sonnet-4-5",
    betas=["code-execution-2025-08-25"],
    max_tokens=4096,
    messages=[{
        "role": "user",
        "content": "/tmp/number.txt 파일을 읽어서 그 숫자의 제곱을 계산해줘"
    }],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}]
)
```

## 스트리밍

실시간으로 응답을 받습니다.

```python
with client.beta.messages.stream(
    model="claude-sonnet-4-5",
    betas=["code-execution-2025-08-25"],
    max_tokens=4096,
    messages=[{"role": "user", "content": "복잡한 분석을 수행해줘"}],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}]
) as stream:
    for event in stream:
        if event.type == "content_block_delta":
            print(event.delta, end="", flush=True)
```

## Batch 처리

대량의 요청을 효율적으로 처리합니다.

```python
batch = client.beta.messages.batches.create(
    requests=[
        {
            "custom_id": f"analysis-{i}",
            "params": {
                "model": "claude-sonnet-4-5",
                "max_tokens": 4096,
                "messages": [{"role": "user", "content": f"데이터셋 {i} 분석해줘"}],
                "tools": [{"type": "code_execution_20250825", "name": "code_execution"}]
            }
        }
        for i in range(10)
    ],
    betas=["code-execution-2025-08-25"]
)
```

---

# 7. 문제 해결

## "Invalid API key" 에러

```
원인: API 키가 잘못되었거나 설정되지 않음

해결:
1. 키가 "sk-ant-api03-"로 시작하는지 확인
2. 환경 변수가 올바르게 설정되었는지 확인
   - Windows: echo %ANTHROPIC_API_KEY%
   - Mac/Linux: echo $ANTHROPIC_API_KEY
3. 터미널/IDE 재시작
4. 새 API 키 발급
```

## "Beta feature not enabled" 에러

```
원인: 베타 헤더가 누락됨

해결:
betas=["code-execution-2025-08-25"] 파라미터 확인
```

## "Tool not found" 에러

```
원인: 도구 타입이 잘못됨

해결:
tools=[{"type": "code_execution_20250825", "name": "code_execution"}]
- 타입: code_execution_20250825 (날짜 형식 주의)
- 이름: code_execution
```

## 코드 실행 시간 초과

```
원인: 코드가 너무 오래 실행됨

해결:
1. 코드 최적화
2. 데이터셋 크기 줄이기
3. 복잡한 작업 분할
```

## 패키지 없음 에러

```
원인: 사용하려는 패키지가 설치되어 있지 않음

해결:
사전 설치된 패키지만 사용 가능:
- numpy, pandas, matplotlib, seaborn
- scipy, scikit-learn, pillow
- openpyxl, xlrd, python-docx
- reportlab, beautifulsoup4

pip install은 인터넷 차단으로 불가
```

---

## 사용 가능한 라이브러리 전체 목록

```python
# 데이터 처리
import numpy as np
import pandas as pd

# 시각화
import matplotlib.pyplot as plt
import seaborn as sns

# 과학 계산
import scipy
from sklearn import *

# 이미지 처리
from PIL import Image

# 파일 처리
import openpyxl  # Excel
import xlrd      # Excel (구버전)
from docx import Document  # Word

# PDF 생성
from reportlab.pdfgen import canvas

# HTML 파싱
from bs4 import BeautifulSoup

# 기본 라이브러리
import json
import csv
import datetime
import math
import random
import re
import os
```

---

## 가격

| 항목 | 가격 |
|------|------|
| 무료 제공 | 월 1,550시간 |
| 추가 사용 | $0.05/시간/컨테이너 |
| 최소 과금 단위 | 5분 |

---

## 체크리스트

설정 완료 확인:

- [ ] Python 3.10+ 설치됨
- [ ] anthropic 패키지 설치됨 (0.77.0+)
- [ ] API 키 발급됨
- [ ] 환경 변수 설정됨
- [ ] 테스트 코드 실행 성공

---

*Made with Claude by Bella (OZKIZ)*
