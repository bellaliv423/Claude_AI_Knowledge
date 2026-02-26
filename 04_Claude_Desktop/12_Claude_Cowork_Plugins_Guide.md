---
tags:
  - claude
  - cowork
  - plugins
  - desktop
---

# Claude Cowork & Plugins 완벽 가이드
# Claude Cowork & Plugins Complete Guide

> **작성일 / Created**: 2026-02-05
> **업데이트 / Updated**: 2026-02-05
> **버전 / Version**: 1.0
> **Author**: Bella (OZKIZ) + Claude (Opus 4.5)

---

## 목차 / Table of Contents

1. [소개 / Introduction](#소개--introduction)
2. [요구 사항 / Requirements](#요구-사항--requirements)
3. [Cowork 시작하기 / Getting Started](#cowork-시작하기--getting-started)
4. [공식 플러그인 목록 / Official Plugins](#공식-플러그인-목록--official-plugins)
5. [플러그인 설치 / Plugin Installation](#플러그인-설치--plugin-installation)
6. [플러그인 구조 / Plugin Structure](#플러그인-구조--plugin-structure)
7. [플러그인 사용법 / Using Plugins](#플러그인-사용법--using-plugins)
8. [커스텀 플러그인 만들기 / Creating Custom Plugins](#커스텀-플러그인-만들기--creating-custom-plugins)
9. [실전 예제 / Practical Examples](#실전-예제--practical-examples)
10. [제한 사항 / Limitations](#제한-사항--limitations)
11. [FAQ](#faq)
12. [참고 자료 / References](#참고-자료--references)

---

## 소개 / Introduction

### Claude Cowork란?

**Claude Cowork**는 Claude Code의 기능을 비개발자도 사용할 수 있도록 확장한 에이전트 도구입니다.
한 번에 하나의 프롬프트에 응답하는 대신, 복잡한 다단계 작업을 자율적으로 수행합니다.

| 항목 | 내용 |
|------|------|
| **출시일** | 2026-01 (Research Preview) |
| **플랫폼** | macOS Desktop Only |
| **대상** | Pro, Max, Team, Enterprise 플랜 |
| **특징** | 로컬 파일 접근, 다단계 작업 자동화 |

### Cowork Plugins란?

**Plugins**는 Cowork의 기능을 역할별로 확장하는 모듈입니다.
2026-01-30에 11개의 공식 오픈소스 플러그인이 출시되었습니다.

| 항목 | 내용 |
|------|------|
| **출시일** | 2026-01-30 |
| **플러그인 수** | 11개 공식 플러그인 |
| **라이선스** | Apache 2.0 |
| **GitHub** | https://github.com/anthropics/knowledge-work-plugins |

### 왜 Cowork & Plugins를 사용해야 하나요?

1. **코딩 불필요**: 마크다운과 JSON만으로 구성
2. **역할 특화**: 직무별 최적화된 워크플로우
3. **도구 통합**: Slack, Notion, Jira 등 수십 개 도구 연결
4. **자동화**: 반복 작업을 Claude에게 위임
5. **커스터마이징**: 조직에 맞게 수정 가능

---

## 요구 사항 / Requirements

### Cowork 요구 사항

| 항목 | 요구 사항 |
|------|----------|
| **OS** | macOS Only (Windows/Linux 미지원) |
| **앱** | Claude Desktop App |
| **플랜** | Pro, Max, Team, Enterprise |
| **인터넷** | 필수 (상시 연결) |
| **주의** | 작업 중 앱을 열어 두어야 함 |

### Plugins 요구 사항

| 항목 | 요구 사항 |
|------|----------|
| **Cowork용** | Pro, Max 플랜 |
| **Claude Code용** | Claude Code 설치 |

---

## Cowork 시작하기 / Getting Started

### 1단계: Cowork 모드 진입

1. **Claude Desktop** 앱 실행 (macOS)
2. 상단의 모드 선택기에서 **"Chat"** 옆의 **"Cowork"** 탭 클릭
3. "Tasks" 모드로 전환됨

### 2단계: 작업 요청

```
"이번 주 회의록 폴더에 있는 모든 파일을 요약해서
주간 리포트 Excel로 만들어줘"
```

### 3단계: 계획 검토 및 실행

- Claude가 작업 계획을 제시
- 계획 검토 후 진행 허용
- Claude가 자율적으로 작업 수행
- 완료된 파일이 로컬에 저장됨

### Cowork 핵심 기능

| 기능 | 설명 |
|------|------|
| **로컬 파일 접근** | 업로드 없이 직접 파일 읽기/쓰기 |
| **Sub-agent 조율** | 병렬 작업 스트림 관리 |
| **전문 문서 생성** | Excel (수식 포함), PowerPoint, 서식 문서 |
| **장시간 작업** | 타임아웃 없이 긴 작업 수행 |
| **VM 격리** | 가상 머신에서 안전하게 실행 |

---

## 공식 플러그인 목록 / Official Plugins

Anthropic이 제공하는 11개 공식 플러그인:

### 1. Productivity (생산성)

| 항목 | 내용 |
|------|------|
| **용도** | 작업, 일정, 워크플로우 관리 |
| **커넥터** | Slack, Notion, Asana, Linear, Jira, Monday, ClickUp, Microsoft 365 |
| **명령어** | `/productivity:daily-standup`, `/productivity:task-review` |

### 2. Sales (영업)

| 항목 | 내용 |
|------|------|
| **용도** | 잠재고객 리서치, 통화 준비, 파이프라인 리뷰 |
| **커넥터** | Slack, HubSpot, Close, Clay, ZoomInfo, Notion, Fireflies |
| **명령어** | `/sales:call-prep`, `/sales:prospect-research` |

### 3. Customer Support (고객 지원)

| 항목 | 내용 |
|------|------|
| **용도** | 티켓 분류, 응답 작성, 에스컬레이션, KB 문서 |
| **커넥터** | Slack, Intercom, HubSpot, Guru, Jira, Notion |
| **명령어** | `/customer-support:triage`, `/customer-support:draft-response` |

### 4. Product Management (제품 관리)

| 항목 | 내용 |
|------|------|
| **용도** | 스펙 작성, 로드맵, 사용자 리서치, 경쟁 분석 |
| **커넥터** | Slack, Linear, Figma, Amplitude, Pendo, Intercom |
| **명령어** | `/product-management:write-spec`, `/product-management:roadmap` |

### 5. Marketing (마케팅)

| 항목 | 내용 |
|------|------|
| **용도** | 콘텐츠 작성, 캠페인 기획, 브랜드 가이드, 성과 리포트 |
| **커넥터** | Slack, Canva, Figma, HubSpot, Ahrefs, SimilarWeb |
| **명령어** | `/marketing:content-draft`, `/marketing:campaign-plan` |

### 6. Legal (법무)

| 항목 | 내용 |
|------|------|
| **용도** | 계약 검토, NDA 분류, 컴플라이언스, 리스크 평가 |
| **커넥터** | Slack, Box, Egnyte, Jira, Microsoft 365 |
| **명령어** | `/legal:contract-review`, `/legal:nda-triage` |

### 7. Finance (재무)

| 항목 | 내용 |
|------|------|
| **용도** | 분개, 계정 조정, 재무제표, 차이 분석 |
| **커넥터** | Snowflake, Databricks, BigQuery, Slack, Microsoft 365 |
| **명령어** | `/finance:reconciliation`, `/finance:variance-analysis` |

### 8. Data (데이터)

| 항목 | 내용 |
|------|------|
| **용도** | SQL 쿼리, 통계 분석, 대시보드, 데이터 검증 |
| **커넥터** | Snowflake, Databricks, BigQuery, Hex, Amplitude |
| **명령어** | `/data:write-query`, `/data:build-dashboard` |

### 9. Enterprise Search (기업 검색)

| 항목 | 내용 |
|------|------|
| **용도** | 이메일, 채팅, 문서, 위키 통합 검색 |
| **커넥터** | Slack, Notion, Guru, Jira, Asana, Microsoft 365 |
| **명령어** | `/enterprise-search:find`, `/enterprise-search:summarize` |

### 10. Bio Research (생물학 연구)

| 항목 | 내용 |
|------|------|
| **용도** | 전임상 연구, 문헌 검색, 유전체 분석 |
| **커넥터** | PubMed, BioRender, bioRxiv, ClinicalTrials.gov, ChEMBL |
| **명령어** | `/bio-research:literature-search`, `/bio-research:genomics` |

### 11. Cowork Plugin Management (플러그인 관리)

| 항목 | 내용 |
|------|------|
| **용도** | 커스텀 플러그인 생성 및 관리 |
| **특징** | Plugin Create 기능으로 새 플러그인 생성 |
| **명령어** | `/plugin:create`, `/plugin:list` |

---

## 플러그인 설치 / Plugin Installation

### Cowork에서 설치

```
1. claude.com/plugins 접속
2. 원하는 플러그인 선택
3. "Install" 클릭
4. Cowork에서 자동 활성화
```

### Claude Code에서 설치

```bash
# 1. 마켓플레이스 추가
claude plugin marketplace add anthropics/knowledge-work-plugins

# 2. 특정 플러그인 설치
claude plugin install sales@knowledge-work-plugins
claude plugin install data@knowledge-work-plugins
claude plugin install productivity@knowledge-work-plugins

# 3. 설치된 플러그인 확인
claude plugin list
```

### 설치 후 확인

설치 완료 후:
- **Skills**: 자동 활성화 (관련 컨텍스트에서 자동 적용)
- **Slash Commands**: `/플러그인명:명령어` 형식으로 사용 가능

```bash
# 예시: Sales 플러그인 설치 후
/sales:call-prep "고객사 ABC 미팅 준비"
/sales:prospect-research "스타트업 X 조사"
```

---

## 플러그인 구조 / Plugin Structure

### 디렉토리 구조

```
plugin-name/
├── .claude-plugin/
│   └── plugin.json       # 플러그인 매니페스트
├── .mcp.json             # MCP 커넥터 설정
├── commands/             # Slash 명령어 (명시적 호출)
│   ├── call-prep.md
│   └── prospect-research.md
└── skills/               # 도메인 지식 (자동 활성화)
    ├── best-practices.md
    └── workflows.json
```

### plugin.json 예시

```json
{
  "name": "sales",
  "version": "1.0.0",
  "description": "Sales productivity plugin for Claude",
  "author": "Anthropic",
  "license": "Apache-2.0",
  "skills": ["skills/"],
  "commands": ["commands/"],
  "connectors": [".mcp.json"]
}
```

### .mcp.json 예시

```json
{
  "mcpServers": {
    "hubspot": {
      "command": "npx",
      "args": ["-y", "@anthropic/mcp-server-hubspot"],
      "env": {
        "HUBSPOT_API_KEY": "${HUBSPOT_API_KEY}"
      }
    },
    "slack": {
      "command": "npx",
      "args": ["-y", "@anthropic/mcp-server-slack"],
      "env": {
        "SLACK_TOKEN": "${SLACK_TOKEN}"
      }
    }
  }
}
```

### 구성 요소 설명

| 구성 요소 | 설명 | 호출 방식 |
|----------|------|----------|
| **Skills** | 도메인 전문 지식, 베스트 프랙티스, 워크플로우 | 자동 (컨텍스트 기반) |
| **Commands** | 명시적으로 호출하는 작업 | 수동 (`/명령어`) |
| **Connectors** | 외부 도구 연결 (MCP 서버) | 자동 (Skills/Commands에서 사용) |

---

## 플러그인 사용법 / Using Plugins

### Slash Commands 사용

```bash
# 영업 - 통화 준비
/sales:call-prep "내일 ABC 고객사 미팅, 담당자 김철수 상무"

# 데이터 - SQL 쿼리 작성
/data:write-query "지난 30일간 일별 매출 추이"

# 재무 - 계정 조정
/finance:reconciliation "2026년 1월 은행 계좌 조정"

# 마케팅 - 콘텐츠 초안
/marketing:content-draft "신제품 런칭 블로그 포스트"

# 법무 - 계약 검토
/legal:contract-review "첨부된 서비스 계약서 검토해줘"
```

### Skills 자동 활성화 예시

플러그인 설치 후, 관련 작업 시 자동으로 도메인 지식이 적용됩니다:

```
사용자: "이번 분기 매출 데이터 분석해줘"

Claude: (data 플러그인의 skills 자동 적용)
- SQL 쿼리 베스트 프랙티스 적용
- 데이터 시각화 권장 사항 포함
- 통계 분석 방법론 적용
```

### 커넥터 사용 예시

플러그인이 외부 도구와 연결되면:

```
사용자: "/sales:call-prep 내일 미팅 준비해줘"

Claude:
1. HubSpot에서 고객 정보 조회
2. Slack에서 관련 대화 검색
3. Fireflies에서 이전 미팅 녹취록 확인
4. 종합 브리핑 문서 생성
```

---

## 커스텀 플러그인 만들기 / Creating Custom Plugins

### 방법 1: Plugin Create 사용 (No-Code)

```bash
# Cowork에서
/plugin:create

# Claude가 대화형으로 플러그인 생성 안내
# - 플러그인 이름
# - 용도
# - 필요한 커넥터
# - Slash commands
```

### 방법 2: 수동 생성

#### Step 1: 디렉토리 생성

```bash
mkdir my-custom-plugin
cd my-custom-plugin
mkdir -p .claude-plugin commands skills
```

#### Step 2: plugin.json 생성

```json
{
  "name": "my-custom-plugin",
  "version": "1.0.0",
  "description": "우리 회사 맞춤 플러그인",
  "author": "Your Name",
  "license": "MIT",
  "skills": ["skills/"],
  "commands": ["commands/"]
}
```

#### Step 3: Skill 파일 생성

`skills/company-knowledge.md`:

```markdown
# 회사 지식 베이스

## 우리 회사 소개
- 회사명: ABC 주식회사
- 설립: 2020년
- 주요 제품: SaaS 플랫폼

## 용어 정의
- MRR: Monthly Recurring Revenue (월간 반복 매출)
- ARR: Annual Recurring Revenue (연간 반복 매출)
- CAC: Customer Acquisition Cost (고객 획득 비용)

## 업무 프로세스
1. 고객 문의 → Zendesk 티켓 생성
2. 기술 지원 → Jira 이슈 연결
3. 에스컬레이션 → Slack #support-escalation
```

#### Step 4: Command 파일 생성

`commands/weekly-report.md`:

```markdown
# Weekly Report Generator

## 설명
주간 업무 보고서를 자동으로 생성합니다.

## 입력
- 기간 (기본: 지난 주)
- 팀 (선택)

## 출력
- Excel 파일: 주간_보고서_YYYY-MM-DD.xlsx
- 포함 내용:
  - 완료된 작업
  - 진행 중인 작업
  - 다음 주 계획
  - 이슈 및 블로커

## 워크플로우
1. Jira에서 완료된 이슈 조회
2. Slack에서 주요 논의 요약
3. Notion에서 회의록 확인
4. Excel 보고서 생성
```

#### Step 5: 플러그인 설치

```bash
# Claude Code에서
claude plugin install ./my-custom-plugin
```

### 기존 플러그인 커스터마이징

공식 플러그인을 포크하여 수정:

```bash
# 1. 포크
git clone https://github.com/anthropics/knowledge-work-plugins
cd knowledge-work-plugins/sales

# 2. 커넥터 수정 (.mcp.json)
# 우리 회사에서 사용하는 CRM으로 변경

# 3. Skills 수정
# 우리 회사 영업 프로세스 추가

# 4. 설치
claude plugin install ./sales
```

---

## 실전 예제 / Practical Examples

### 예제 1: 주간 영업 리포트 자동화

```
사용자:
/sales:pipeline-review 이번 주 파이프라인 리뷰하고
팀장님께 보낼 주간 보고서 만들어줘

Claude:
1. HubSpot에서 파이프라인 데이터 조회
2. 주요 딜 상태 변화 분석
3. 위험 딜 식별
4. Excel 리포트 생성 (차트 포함)
5. 요약 이메일 초안 작성

[생성된 파일]
- 주간_영업_리포트_2026-02-05.xlsx
- 이메일_초안.txt
```

### 예제 2: 고객 지원 티켓 분류

```
사용자:
/customer-support:triage 오늘 들어온 티켓들 분류하고
긴급한 건 정리해줘

Claude:
1. Intercom에서 신규 티켓 조회 (42건)
2. 긴급도 분류:
   - Critical: 3건 (서비스 장애)
   - High: 8건 (기능 오류)
   - Medium: 15건 (사용 문의)
   - Low: 16건 (기능 요청)
3. Critical 티켓 상세 브리핑 생성
4. Slack #support-urgent에 알림 전송
```

### 예제 3: 데이터 분석 자동화

```
사용자:
/data:build-dashboard 지난 분기 매출 데이터로
경영진 보고용 대시보드 만들어줘

Claude:
1. BigQuery에서 매출 데이터 쿼리
2. 주요 지표 계산:
   - 총 매출: ₩12.5B (+15% YoY)
   - MRR: ₩1.2B
   - Churn Rate: 2.3%
3. 시각화 생성 (차트 6개)
4. PowerPoint 대시보드 생성
5. 인사이트 요약 (3줄)

[생성된 파일]
- Q4_매출_대시보드.pptx
- 상세_데이터.xlsx
```

### 예제 4: 법무 계약 검토

```
사용자:
/legal:contract-review 첨부한 서비스 계약서 검토해줘.
특히 책임 제한 조항 중점적으로 봐줘

Claude:
1. 계약서 파싱 (32페이지)
2. 주요 조항 식별:
   - 책임 제한: 섹션 8 (위험 요소 발견)
   - 지적재산권: 섹션 12 (표준)
   - 종료 조건: 섹션 15 (검토 필요)
3. 위험 평가 리포트 생성
4. 수정 권고사항 목록화

[생성된 파일]
- 계약검토_리포트.docx
- 위험_요약.md
```

---

## 제한 사항 / Limitations

### Cowork 제한 사항

| 제한 | 설명 |
|------|------|
| **macOS 전용** | Windows, Linux 미지원 |
| **프로젝트 미통합** | Claude 프로젝트와 연동 불가 |
| **세션 간 메모리 없음** | 이전 세션 기억 불가 |
| **세션 공유 불가** | 다른 사용자와 세션 공유 불가 |
| **GSuite 미지원** | Google Workspace 직접 연동 불가 |
| **앱 상시 실행** | 작업 중 Desktop 앱 열어둬야 함 |

### Plugins 제한 사항

| 제한 | 설명 |
|------|------|
| **플랜 제한** | Pro, Max 플랜만 사용 가능 |
| **커넥터 설정 필요** | 외부 도구 연결 시 API 키 필요 |
| **조직 공유 미지원** | 조직 내 플러그인 공유 기능 준비 중 |

### 토큰 사용량 주의

Cowork는 일반 채팅보다 **상당히 많은 토큰**을 소모합니다:

- 복잡한 다단계 작업 수행
- 여러 도구 동시 조회
- 파일 생성 및 처리

**권장사항:**
- 관련 작업은 묶어서 요청
- 단순 작업은 일반 Chat 모드 사용
- Cowork는 파일 접근이 필요한 복잡한 작업에 사용

---

## FAQ

### Q1: Cowork와 Claude Code의 차이점?

| 항목 | Cowork | Claude Code |
|------|--------|-------------|
| **대상** | 비개발자 | 개발자 |
| **인터페이스** | GUI (Desktop App) | CLI (터미널) |
| **주요 용도** | 문서, 분석, 자동화 | 코딩, 개발 |
| **플랫폼** | macOS만 | Windows, macOS, Linux |

### Q2: 플러그인은 무료인가요?

네, 공식 플러그인은 모두 **무료**이며 **오픈소스**(Apache 2.0)입니다.
단, Cowork 자체를 사용하려면 Pro 이상의 유료 플랜이 필요합니다.

### Q3: 커넥터 API 키는 어디서 설정하나요?

```bash
# 환경 변수로 설정
export SLACK_TOKEN="xoxb-..."
export HUBSPOT_API_KEY="..."

# 또는 .env 파일 사용
# .mcp.json에서 ${ENV_VAR} 형식으로 참조
```

### Q4: 플러그인을 조직 전체에 배포할 수 있나요?

현재는 개인 설치만 가능합니다.
**조직 공유 및 Private Marketplace** 기능은 개발 중입니다.

### Q5: 내 데이터는 안전한가요?

- Cowork는 **가상 머신(VM)**에서 격리 실행
- 파일 접근은 **명시적 권한 부여** 후에만 가능
- 민감한 파일 작업 시 항상 계획 검토 권장

### Q6: GSuite (Google Docs, Sheets)를 사용할 수 있나요?

현재 **GSuite 직접 연동은 미지원**입니다.
대안:
- 파일을 다운로드하여 로컬에서 작업
- Microsoft 365 사용 (지원됨)

---

## 참고 자료 / References

### 공식 문서
- [Getting started with Cowork](https://support.claude.com/en/articles/13345190-getting-started-with-cowork)
- [Knowledge Work Plugins (GitHub)](https://github.com/anthropics/knowledge-work-plugins)
- [Anthropic News - Cowork Plugins](https://www.anthropic.com/news)

### 관련 기사
- [TechCrunch - Anthropic brings agentic plugins to Cowork](https://techcrunch.com/2026/01/30/anthropic-brings-agentic-plugins-to-cowork/)
- [The New Stack - Anthropic brings plugins to Cowork](https://thenewstack.io/anthropic-brings-plugins-to-cowork/)

### 이 프로젝트의 관련 문서
- [03_MCP_Usage_Guide.md](./03_MCP_Usage_Guide.md) - MCP 연결 방법
- [04_Claude_Skills_Guide.md](./04_Claude_Skills_Guide.md) - Skills 작성법
- [NEW_FEATURES_TODO_2026.md](./NEW_FEATURES_TODO_2026.md) - 최신 기능 목록

---

## 업데이트 로그 / Changelog

| 날짜 | 버전 | 내용 |
|------|------|------|
| 2026-02-05 | v1.0 | 초기 버전 작성 |

---

*Made with Claude by Bella (OZKIZ)*
