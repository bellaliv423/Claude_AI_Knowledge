---
tags:
  - claude
  - enterprise
  - integrations
  - slack
  - figma
  - canva
---

# Claude 기업 앱 통합 완벽 가이드
# Claude Enterprise App Integrations Complete Guide

> **작성일 / Created**: 2026-02-26
> **업데이트 / Updated**: 2026-02-26
> **버전 / Version**: 1.0
> **Author**: Bella (OZKIZ) + Claude (Opus 4.6)

---

## 목차 / Table of Contents

1. [소개 / Introduction](#소개--introduction)
2. [지원 앱 목록 / Supported Apps](#지원-앱-목록--supported-apps)
3. [Slack 통합 / Slack Integration](#slack-통합--slack-integration)
4. [Figma 통합 / Figma Integration](#figma-통합--figma-integration)
5. [Canva 통합 / Canva Integration](#canva-통합--canva-integration)
6. [Box 통합 / Box Integration](#box-통합--box-integration)
7. [Notion 통합 / Notion Integration](#notion-통합--notion-integration)
8. [기타 통합 / Other Integrations](#기타-통합--other-integrations)
9. [설정 방법 / Setup Guide](#설정-방법--setup-guide)
10. [실전 활용 / Practical Use Cases](#실전-활용--practical-use-cases)
11. [FAQ](#faq)
12. [참고 자료 / References](#참고-자료--references)

---

## 소개 / Introduction

Anthropic은 2026년 1월부터 Claude 인터페이스에서 직접 외부 업무 도구를 사용할 수 있는 **Enterprise App Integrations**를 출시했습니다. 별도의 API 코딩 없이 Claude 대화 안에서 바로 Slack 메시지 전송, Figma 디자인 분석, Canva 디자인 생성 등을 수행할 수 있습니다.

| 항목 | 내용 |
|------|------|
| **출시일** | 2026-01 |
| **대상** | Pro, Max, Team, Enterprise 플랜 |
| **설정 URL** | https://claude.ai/directory |
| **방식** | MCP 기반 공식 통합 |

### 핵심 특징

```
Enterprise Integrations의 장점:
├── 코딩 불필요: claude.ai에서 직접 설정
├── 공식 지원: Anthropic이 직접 관리하는 MCP 서버
├── 보안: OAuth 2.0 인증, 데이터 암호화
├── 실시간: 도구가 실시간으로 외부 서비스와 통신
└── 확장성: 새로운 앱이 지속적으로 추가됨
```

---

## 지원 앱 목록 / Supported Apps

### 현재 지원 (2026-02 기준)

| 앱 | 카테고리 | 주요 기능 | 상태 |
|----|----------|----------|------|
| **Slack** | 커뮤니케이션 | 메시지 읽기/전송, 채널 관리 | ✅ 사용 가능 |
| **Figma** | 디자인 | 디자인 분석, 스크린샷, Code Connect | ✅ 사용 가능 |
| **Canva** | 디자인 | 디자인 생성/편집, 에셋 관리 | ✅ 사용 가능 |
| **Box** | 파일 관리 | 파일 검색, 공유, 분석 | ✅ 사용 가능 |
| **Notion** | 생산성 | 페이지 검색/생성, 데이터베이스 관리 | ✅ 사용 가능 |
| **HubSpot** | CRM | 고객 관리, 영업 데이터, 마케팅 | ✅ 사용 가능 |
| **Amplitude** | 분석 | 차트 조회, 코호트 분석, 실험 | ✅ 사용 가능 |
| **WordPress.com** | 웹사이트 | 콘텐츠 작성, 사이트 관리 | ✅ 사용 가능 |
| **Vercel** | 배포 | 프로젝트 관리, 배포, 로그 확인 | ✅ 사용 가능 |
| **Salesforce** | CRM | 고객 관리 | 🔜 예정 |

---

## Slack 통합 / Slack Integration

### 사용 가능한 기능

| 도구 | 설명 |
|------|------|
| `read_channel` | 채널의 메시지 읽기 |
| `send_message` | 채널에 메시지 전송 |
| `search_messages` | 메시지 검색 |
| `list_channels` | 채널 목록 조회 |
| `create_channel` | 새 채널 생성 |

### 활용 예시

```
Claude에게 요청:

1. "지난주 #general 채널의 대화 내용을 요약해줘"
   → read_channel로 메시지 읽기 → 요약 생성

2. "#dev 채널에 '오늘 배포 완료' 메시지를 보내줘"
   → send_message로 메시지 전송

3. "'버그 수정'이 언급된 모든 메시지를 찾아줘"
   → search_messages로 키워드 검색

4. "각 채널의 이번 주 활동을 보고서로 만들어줘"
   → list_channels + read_channel → 보고서 생성
```

### 워크플로우 예시: 일일 보고서 생성

```
사용자: "#dev와 #design 채널의 오늘 대화를 요약하고,
        #daily-report 채널에 보고서를 보내줘"

Claude 동작:
1. read_channel(#dev) → 개발 팀 대화 수집
2. read_channel(#design) → 디자인 팀 대화 수집
3. 내용 분석 및 보고서 작성
4. send_message(#daily-report, 보고서)
```

---

## Figma 통합 / Figma Integration

### 사용 가능한 기능

| 도구 | 설명 |
|------|------|
| `get_design_context` | 디자인 컨텍스트 + 코드 가져오기 |
| `get_screenshot` | 디자인 스크린샷 |
| `get_metadata` | 파일 메타데이터 |
| `get_variable_defs` | 디자인 변수 정의 |
| `get_figjam` | FigJam 보드 내용 |
| `generate_diagram` | FigJam 다이어그램 생성 |
| `get_code_connect_map` | Code Connect 매핑 조회 |
| `add_code_connect_map` | Code Connect 매핑 추가 |

### Design-to-Code 워크플로우

```
1단계: 디자인 가져오기
├── Figma URL 공유: figma.com/design/:fileKey/:fileName?node-id=:nodeId
├── Claude가 get_design_context 호출
└── React + Tailwind 기반 코드 + 스크린샷 반환

2단계: 프로젝트에 맞게 적용
├── Code Connect 매핑 확인 → 기존 컴포넌트 재사용
├── 디자인 토큰 매핑 → 프로젝트 토큰 시스템 연결
├── 어노테이션 확인 → 디자이너 노트 반영
└── 스크린샷 참조 → 시각적 정확성 확인
```

### URL 파싱 규칙

```
Figma URL 형식:
├── figma.com/design/:fileKey/:fileName?node-id=:nodeId
│   → nodeId의 "-"를 ":"로 변환
│
├── figma.com/design/:fileKey/branch/:branchKey/:fileName
│   → branchKey를 fileKey로 사용
│
├── figma.com/make/:makeFileKey/:makeFileName
│   → makeFileKey 사용
│
└── figma.com/board/:fileKey/:fileName
    → FigJam 파일, get_figjam 사용
```

### 활용 예시

```
1. "이 Figma 디자인을 React 컴포넌트로 변환해줘"
   → URL에서 fileKey/nodeId 추출
   → get_design_context로 코드 가져오기
   → 프로젝트 컨벤션에 맞게 변환

2. "이 디자인의 색상 변수를 CSS 변수로 만들어줘"
   → get_variable_defs로 변수 정의 가져오기
   → CSS 변수 파일 생성

3. "시스템 아키텍처 다이어그램을 FigJam에 만들어줘"
   → generate_diagram으로 다이어그램 생성
```

---

## Canva 통합 / Canva Integration

### 사용 가능한 기능

| 도구 | 설명 |
|------|------|
| `search-designs` | 디자인 검색 |
| `get-design` | 디자인 정보 조회 |
| `generate-design` | AI 디자인 생성 |
| `export-design` | 디자인 내보내기 |
| `comment-on-design` | 디자인에 코멘트 |
| `list-brand-kits` | 브랜드 킷 목록 |
| `resize-design` | 디자인 크기 변경 |
| `start-editing-transaction` | 편집 시작 |
| `perform-editing-operations` | 편집 수행 |
| `commit-editing-transaction` | 편집 완료 |

### 활용 예시

```
1. "소셜 미디어용 프로모션 배너를 만들어줘"
   → generate-design으로 AI 디자인 생성
   → 브랜드 킷 적용
   → export-design으로 내보내기

2. "기존 프레젠테이션의 스타일을 변경해줘"
   → search-designs로 프레젠테이션 찾기
   → start-editing-transaction → perform-editing-operations → commit
   → 편집 완료

3. "모든 소셜 미디어 사이즈로 리사이즈해줘"
   → resize-design으로 Instagram, Facebook, Twitter 사이즈 생성
```

---

## Box 통합 / Box Integration

### 주요 기능

```
Box Integration 기능:
├── 파일 검색: 키워드로 Box 내 파일 검색
├── 파일 읽기: 문서 내용 가져오기
├── 파일 공유: 공유 링크 생성
├── 폴더 탐색: 폴더 구조 탐색
└── 파일 분석: Claude로 문서 분석
```

### 활용 예시

```
1. "Box에서 '2026 분기 보고서'를 찾아서 요약해줘"
   → 파일 검색 → 내용 읽기 → 요약 생성

2. "마케팅 폴더의 모든 PDF를 분석하고 핵심 인사이트를 추출해줘"
   → 폴더 탐색 → 파일 읽기 → 분석

3. "이 문서를 팀에 공유하고 코멘트를 남겨줘"
   → 공유 링크 생성 → 코멘트 추가
```

---

## Notion 통합 / Notion Integration

### 사용 가능한 기능

| 도구 | 설명 |
|------|------|
| `notion-search` | 페이지/데이터베이스 검색 |
| `notion-fetch` | 페이지 내용 가져오기 |
| `notion-create-pages` | 새 페이지 생성 |
| `notion-update-page` | 페이지 업데이트 |
| `notion-move-pages` | 페이지 이동 |
| `notion-duplicate-page` | 페이지 복제 |
| `notion-create-database` | 데이터베이스 생성 |
| `notion-create-comment` | 코멘트 추가 |
| `notion-get-comments` | 코멘트 조회 |

### 활용 예시

```
1. "Notion에서 '프로젝트 로드맵'을 찾아서 분석해줘"
   → notion-search → notion-fetch → 분석

2. "이번 주 회의록을 Notion에 작성해줘"
   → notion-create-pages로 새 페이지 생성

3. "버그 트래커 데이터베이스를 만들고 GitHub 이슈를 정리해줘"
   → notion-create-database → notion-create-pages
```

---

## 기타 통합 / Other Integrations

### HubSpot (CRM)

```
HubSpot 기능:
├── search_crm_objects: 고객/거래/회사 검색
├── get_crm_objects: CRM 오브젝트 조회
├── manage_crm_objects: CRM 오브젝트 생성/수정
├── search_owners: 담당자 검색
└── get_user_details: 사용자 정보 조회

활용: "지난달 성사된 거래 목록을 보여줘"
      "신규 리드를 CRM에 추가해줘"
```

### Amplitude (분석)

```
Amplitude 기능:
├── query_chart: 차트 데이터 조회
├── get_charts: 차트 목록
├── get_cohorts: 코호트 분석
├── create_experiment: A/B 테스트 생성
├── get_session_replays: 세션 리플레이
└── query_dataset: 데이터셋 쿼리

활용: "지난 7일간의 사용자 활성 지표를 분석해줘"
      "회원가입 퍼널의 이탈률을 확인해줘"
```

### WordPress.com

```
WordPress 기능:
├── wpcom-mcp-content-authoring: 콘텐츠 작성/관리
├── wpcom-mcp-site-editor-context: 테마/블록 컨텍스트
├── wpcom-mcp-site-settings: 사이트 설정
├── wpcom-mcp-site-statistics: 통계 조회
└── wpcom-mcp-user-profile: 프로필 관리

활용: "새 블로그 포스트를 작성해줘"
      "사이트 방문자 통계를 분석해줘"
```

### Vercel (배포)

```
Vercel 기능:
├── list_projects: 프로젝트 목록
├── deploy_to_vercel: 배포 실행
├── get_deployment_build_logs: 빌드 로그 확인
├── get_runtime_logs: 런타임 로그
├── search_vercel_documentation: 문서 검색
└── check_domain_availability_and_price: 도메인 확인

활용: "최근 배포 상태를 확인해줘"
      "이 프로젝트를 Vercel에 배포해줘"
```

---

## 설정 방법 / Setup Guide

### 1단계: Claude Directory 접속

```
1. https://claude.ai 로그인
2. https://claude.ai/directory 접속
3. 연결하고 싶은 앱 선택
```

### 2단계: OAuth 인증

```
1. 앱 카드에서 "Connect" 클릭
2. 해당 서비스의 OAuth 로그인 페이지로 이동
3. 권한 승인
4. Claude로 자동 리디렉트
```

### 3단계: 사용 시작

```
1. Claude 대화에서 앱 관련 요청
2. Claude가 자동으로 연결된 앱의 도구 사용
3. 결과 확인 및 추가 작업

예: "Slack #general의 최근 메시지를 요약해줘"
    → Claude가 자동으로 Slack 도구 사용
```

### 설정 확인 및 관리

```
연결된 앱 관리:
├── https://claude.ai/directory → 연결 상태 확인
├── 앱 카드에서 "Disconnect" → 연결 해제
├── 권한 범위 확인 → 필요한 권한만 유지
└── 여러 워크스페이스 연결 가능 (Slack 등)
```

---

## 실전 활용 / Practical Use Cases

### 사례 1: 프로젝트 관리 자동화

```
"GitHub의 이번 스프린트 이슈를 Notion에 정리하고,
Slack #team 채널에 요약을 공유해줘"

Claude 동작:
1. Notion에서 스프린트 보드 조회
2. 이슈 상태별 정리 (진행 중 / 완료 / 대기)
3. Notion 페이지 업데이트
4. Slack 메시지 작성 및 전송
```

### 사례 2: 디자인 → 코드 파이프라인

```
"Figma의 이 디자인을 분석하고, Canva에서 마케팅 배너도 만들어줘"

Claude 동작:
1. Figma URL에서 디자인 컨텍스트 가져오기
2. React 컴포넌트 코드 생성
3. 동일한 스타일로 Canva 배너 디자인 생성
4. 결과 링크 제공
```

### 사례 3: 영업 보고서 자동화

```
"HubSpot에서 이번 달 성사된 거래를 가져와서
Notion에 보고서를 만들고, Slack에 공유해줘"

Claude 동작:
1. HubSpot에서 거래 데이터 조회
2. 금액별/담당자별 분석
3. Notion에 보고서 페이지 생성
4. Slack #sales 채널에 요약 전송
```

### 사례 4: 콘텐츠 워크플로우

```
"블로그 초안을 작성하고, WordPress에 게시하고,
소셜 미디어 이미지는 Canva로 만들어줘"

Claude 동작:
1. 블로그 콘텐츠 작성
2. WordPress에 드래프트로 게시
3. Canva에서 소셜 미디어 이미지 생성
4. 편집/미리보기 링크 제공
```

---

## FAQ

### Q1: 무료 플랜에서도 사용 가능한가요?

아니요, **Pro, Max, Team, Enterprise** 플랜에서만 사용 가능합니다.

### Q2: 한 번에 여러 앱을 연결할 수 있나요?

네, 원하는 만큼 여러 앱을 동시에 연결하고 사용할 수 있습니다. Claude가 요청에 따라 적절한 앱의 도구를 자동 선택합니다.

### Q3: API에서도 사용할 수 있나요?

Enterprise Integrations는 주로 **claude.ai** 웹 인터페이스와 **Claude Desktop**에서 사용됩니다. API에서는 **MCP Connector**를 통해 유사한 기능을 구현할 수 있습니다.

### Q4: 데이터 보안은 어떻게 되나요?

- OAuth 2.0으로 안전한 인증
- Claude가 데이터를 학습에 사용하지 않음
- 각 서비스의 권한 범위만큼만 접근
- Enterprise 플랜은 추가 보안 옵션 제공

### Q5: 새로운 앱 통합은 언제 추가되나요?

Anthropic이 지속적으로 새 통합을 추가하고 있습니다. Salesforce 등이 곧 추가 예정입니다. https://claude.ai/directory 에서 최신 목록을 확인하세요.

### Q6: Claude Code에서도 이 통합을 사용할 수 있나요?

Claude Code에서는 MCP 서버 설정을 통해 유사한 기능을 사용할 수 있습니다. `claude_desktop_config.json`에서 MCP 서버를 설정하세요.

---

## 참고 자료 / References

### 공식 문서
- [Claude Directory](https://claude.ai/directory)
- [Anthropic Integrations 발표](https://www.anthropic.com/news)
- [MCP Protocol](https://modelcontextprotocol.io)

### 이 프로젝트의 관련 문서
- [03_MCP_Usage_Guide.md](./03_MCP_Usage_Guide.md) - MCP 활용 가이드
- [09_Files_MCP_Guide.md](./09_Files_MCP_Guide.md) - Files API & MCP Connector
- [12_Claude_Cowork_Plugins_Guide.md](../04_Claude_Desktop/12_Claude_Cowork_Plugins_Guide.md) - Cowork 플러그인

---

## 업데이트 로그 / Changelog

| 날짜 | 버전 | 내용 |
|------|------|------|
| 2026-02-26 | v1.0 | 초기 버전 작성 |

---

*Made with Claude by Bella (OZKIZ)*
