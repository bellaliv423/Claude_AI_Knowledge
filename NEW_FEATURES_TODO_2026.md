# Claude 최신 기능 업데이트 대기 목록
# Claude Latest Features Update Queue

> **조사일 / Research Date:** 2026-02-06 (Updated)
> **상태 / Status:** 문서화 대기 중
> **GitHub**: https://github.com/bellaliv423/Claude_AI_Knowledge

---

## 🆕 신규 발견 기능 (2026-02-06 조사)

### Claude Opus 4.6 (최신 발표!) 🔥
| 항목 | 내용 |
|------|------|
| **발표일** | 2026-02-05 |
| **모델 ID** | `claude-opus-4-6` |
| **컨텍스트** | **1M 토큰** (Opus급 최초!) |
| **최대 출력** | **128K 토큰** |
| **가격** | $5(입력)/$25(출력) per 1M — **3배 저렴!** |
| **벤치마크** | Terminal-Bench 2.0 1위, Humanity's Last Exam 1위, GDPval-AA +144 Elo |
| **신기능** | Adaptive Thinking, Effort Controls, Context Compaction, Agent Teams |
| **문서화** | ✅ `08_Claude_Opus_4.6_Update_Guide.md` 완료! |
| **공식 링크** | https://www.anthropic.com/news/claude-opus-4-6 |

---

### Claude Cowork Plugins (코워크 플러그인)
| 항목 | 내용 |
|------|------|
| **출시일** | 2026-01-30 |
| **기능** | 역할별 맞춤 플러그인으로 Cowork 확장 |
| **플러그인 수** | 11개 오픈소스 플러그인 출시 |
| **카테고리** | Productivity, Enterprise Search, Marketing, Sales, Finance, Legal, Data Analysis, Customer Support, Product Management, Biology Research |
| **특징** | Plugin Create로 커스텀 플러그인 생성 가능 |
| **대상** | Pro, Max 플랜 사용자 |
| **GitHub** | https://github.com/anthropics/knowledge-work-plugins |
| **참고** | Sub-agents, Slash commands, Connectors 포함 |

---

### Enterprise App Integrations (기업 앱 통합)
| 항목 | 내용 |
|------|------|
| **출시일** | 2026-01 |
| **기능** | Claude 인터페이스에서 직접 업무 도구 사용 |
| **지원 앱** | Slack, Canva, Figma, Box, Clay |
| **예정** | Salesforce (곧 추가) |
| **대상** | Pro, Max, Team, Enterprise 플랜 |
| **설정 URL** | https://claude.ai/directory |

---

### Claude in Chrome Beta (브라우저 제어)
| 항목 | 내용 |
|------|------|
| **출시일** | 2026-02 (Beta) |
| **기능** | Claude Code에서 브라우저 제어 |
| **용도** | 웹 자동화, 테스트, 데이터 수집 |

---

### Claude's New Constitution (새 헌법)
| 항목 | 내용 |
|------|------|
| **발표일** | 2026-01-22 |
| **내용** | Claude의 새로운 원칙 및 가치관 체계 |
| **문서 링크** | https://www.anthropic.com/news/claude-new-constitution |

---

### GitHub 공식 통합
| 항목 | 내용 |
|------|------|
| **출시일** | 2026-02-04 |
| **기능** | GitHub에서 Claude 공식 지원 (Public Preview) |
| **참고** | Codex와 함께 발표됨 |
| **문서 링크** | https://github.blog/changelog/2026-02-04-claude-and-codex-are-now-available-in-public-preview-on-github/ |

---

### 주요 파트너십 발표
| 날짜 | 파트너 | 내용 |
|------|--------|------|
| 2026-01-28 | ServiceNow | 고객 앱 Claude 탑재 |
| 2026-01-27 | UK Government | GOV.UK AI 어시스턴트 |
| 2026-01 | NASA | Perseverance 로버 화성 네비게이션 |
| 2026-02 | Anthropic Legal | 법률 기술 진출 |

---

### 🚨 루머: Claude 5 / Sonnet 5
| 항목 | 내용 |
|------|------|
| **발견일** | 2026-02 초 |
| **모델 ID** | `claude-sonnet-5@20260203` |
| **출처** | Google Vertex AI 로그에서 발견 |
| **상태** | 미확인 (공식 발표 없음) |

---

## 즉시 문서화 필요 (High Priority)

### 1. Structured Outputs (구조화된 출력)
| 항목 | 내용 |
|------|------|
| **출시일** | 2026-01-29 (GA) |
| **기능** | JSON 스키마 100% 보장 |
| **주요 변경** | `output_format` → `output_config.format` |
| **지원 모델** | Sonnet 4.5, Opus 4.5, Haiku 4.5 |
| **문서 링크** | https://platform.claude.com/docs/en/build-with-claude/structured-outputs |
| **예정 파일** | `05_Structured_Outputs_Guide.md` |

```python
# 예시 코드
response = client.messages.create(
    model="claude-opus-4-5-20251101",
    max_tokens=1024,
    output_config={
        "format": {
            "type": "json_schema",
            "json_schema": {
                "name": "response",
                "schema": {"type": "object", "properties": {...}}
            }
        }
    },
    messages=[...]
)
```

---

### 2. Memory Tool (메모리 도구)
| 항목 | 내용 |
|------|------|
| **출시일** | 2025-09-29 (Beta) |
| **기능** | 대화 간 정보 저장 및 참조 |
| **용도** | 사용자 선호도, 프로젝트 컨텍스트 유지 |
| **문서 링크** | https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool |
| **예정 파일** | `06_Memory_Context_Guide.md` |

---

### 3. Context Editing (컨텍스트 편집)
| 항목 | 내용 |
|------|------|
| **출시일** | 2025-09-29 (Beta) |
| **기능** | 자동 컨텍스트 관리, thinking block 클리어 |
| **Beta 헤더** | `clear_thinking_20251015` |
| **문서 링크** | https://platform.claude.com/docs/en/build-with-claude/context-editing |
| **예정 파일** | `06_Memory_Context_Guide.md` (Memory와 통합) |

---

### 4. Effort Parameter (노력 파라미터)
| 항목 | 내용 |
|------|------|
| **출시일** | 2025-11-24 (Beta) |
| **기능** | 토큰 사용량 vs 응답 품질 조절 |
| **지원 모델** | Opus 4.5 전용 |
| **효과** | medium effort에서 Sonnet 4.5 점수 달성하면서 76% 토큰 절약 |
| **문서 링크** | https://platform.claude.com/docs/en/build-with-claude/effort |
| **예정 파일** | `07_Effort_Parameter_Guide.md` |

```python
# 예시 코드
response = client.messages.create(
    model="claude-opus-4-5-20251101",
    max_tokens=4096,
    effort="medium",  # low, medium, high
    messages=[...]
)
```

---

## 중요 기능 (Medium Priority)

### 5. Programmatic Tool Calling
| 항목 | 내용 |
|------|------|
| **출시일** | 2025-11-24 (Beta) |
| **기능** | 코드 실행 내에서 도구 호출 |
| **장점** | 지연시간 감소, 토큰 사용량 절감 |
| **문서 링크** | https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling |

---

### 6. Tool Search Tool
| 항목 | 내용 |
|------|------|
| **출시일** | 2025-11-24 (Beta) |
| **기능** | 대규모 도구 카탈로그에서 동적 검색/로드 |
| **용도** | 수백 개 도구 관리 시 유용 |
| **문서 링크** | https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool |

---

### 7. Web Fetch Tool
| 항목 | 내용 |
|------|------|
| **출시일** | 2025-09-10 (Beta) |
| **기능** | 웹페이지/PDF 전체 내용 가져오기 |
| **문서 링크** | https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool |

---

### 8. Files API
| 항목 | 내용 |
|------|------|
| **출시일** | 2025-05-22 (Beta) |
| **기능** | 파일 업로드 및 Messages API에서 참조 |
| **문서 링크** | https://platform.claude.com/docs/en/build-with-claude/files |

---

### 9. MCP Connector
| 항목 | 내용 |
|------|------|
| **출시일** | 2025-05-22 (Beta) |
| **기능** | 원격 MCP 서버 직접 연결 (클라이언트 코드 없이) |
| **문서 링크** | https://platform.claude.com/docs/en/agents-and-tools/mcp-connector |

---

### 10. Interleaved Thinking
| 항목 | 내용 |
|------|------|
| **출시일** | 2025-05-22 (Beta) |
| **기능** | 도구 호출 사이에 thinking 수행 |
| **Beta 헤더** | `interleaved-thinking-2025-05-14` |
| **문서 링크** | https://platform.claude.com/docs/en/build-with-claude/extended-thinking#interleaved-thinking |

---

## 추가 기능 (Lower Priority)

### 11. Fine-grained Tool Streaming
- **출시일**: 2025-06-11
- **Beta 헤더**: `fine-grained-tool-streaming-2025-05-14`
- 도구 파라미터 실시간 스트리밍

### 12. Citations
- **출시일**: 2025-01-23
- 응답 내 출처 인용 기능

### 13. Search Results (GA)
- **출시일**: 2025-08-08
- RAG 애플리케이션용 자연스러운 인용

### 14. Code Execution Tool v2
- **출시일**: 2025-09-02
- Python → Bash 명령 실행 + 다른 언어 지원

### 15. Health Data Integration
- **출시일**: 2026-02
- iOS/Android 건강 데이터 분석 (Pro/Max 플랜, 미국 한정)

---

## 모델 업데이트 정리

| 모델 | 모델 ID | 가격 (Input/Output) | 상태 |
|------|---------|---------------------|------|
| **Opus 4.5** | `claude-opus-4-5-20251101` | $5 / $25 per M | 최신 |
| **Sonnet 4.5** | `claude-sonnet-4-5-20250929` | - | 최신 |
| **Haiku 4.5** | `claude-haiku-4-5-20251015` | - | 최신 |
| Opus 4.1 | `claude-opus-4-1-20250805` | - | 사용 가능 |
| Opus 3 | `claude-3-opus-20240229` | - | **퇴역됨** (2026-01-05) |

---

## Claude Code 업데이트 정리

### v2.0 주요 변경
- 새 VS Code 확장 (새 UI)
- `/rewind` - 코드 변경 취소
- `/usage` - 플랜 한도 확인
- Tab으로 thinking 토글 (sticky)
- Ctrl+R로 히스토리 검색
- **Claude Code SDK → Claude Agent SDK** 이름 변경

### v2.1.x 주요 변경
- `--from-pr` 플래그 (PR 번호/URL로 세션 재개)
- PR 생성 시 자동 세션 연결
- mTLS/프록시 지원 (기업 네트워크)
- OAuth 토큰 만료 수정
- 커스텀 스피너 동사 설정 (`spinnerVerbs`)
- Shift+Enter로 줄바꿈 (설정 없이 바로 사용)
- Hooks를 agents & skills frontmatter에 직접 추가
- Skills: forked context, hot reload, custom agent 지원
- `/` 로 skill 호출
- 도구 사용 거부 시에도 에이전트 계속 실행
- 응답 언어 설정 가능 (일본어, 스페인어 등)
- 도구 권한 와일드카드 지원: `Bash(*-h*)`
- `/teleport` - http://claude.ai/code 로 세션 이동

### v2.1.x 최신 (2026-02-05 기준)
- **`/debug` 명령어** - 세션 문제 해결용 새 명령어
- **PDF `pages` 파라미터** - 특정 페이지 범위 읽기 (`pages: "1-5"`)
- **대용량 PDF 처리 개선** - 10페이지 이상은 경량 참조로 반환
- **세션 재개 힌트** - 종료 시 재개 방법 표시
- **일본어 IME 개선** - 전각(全角) 스페이스 입력 지원
- **MCP OAuth 개선** - `--client-id`, `--client-secret` 옵션 추가
- **Claude in Chrome Beta** - Claude Code에서 브라우저 제어
- PDF 세션 잠금 버그 수정
- Sandbox 모드 "Read-only file system" 오류 수정

### 새 제품
- **Claude Cowork**: 비개발자용 GUI 버전 (2026-01 출시)
- **Claude Code Analytics API**: 생산성 지표, 도구 통계, 비용 데이터

---

## 플랫폼 URL 변경

| 이전 | 이후 | 날짜 |
|------|------|------|
| console.anthropic.com | **platform.claude.com** | 2026-01-12 |
| docs.anthropic.com | **platform.claude.com/docs** | 2025-11-19 |

---

## 문서화 작업 계획

### Phase 1 (완료)
1. [x] `05_Structured_Outputs_Guide.md` ✅ 2026-02-03 완료
2. [x] `06_Memory_Context_Guide.md` (Memory + Context Editing) ✅ 2026-02-03 완료

### Phase 2 (진행 중)
3. [x] `07_Effort_Parameter_Guide.md` ✅ 2026-02-05 완료
4. [ ] `08_New_Tools_Guide.md` (Web Fetch, Tool Search, Programmatic)
5. [ ] `09_Files_MCP_Guide.md` (Files API + MCP Connector)
6. [ ] `10_Claude_Code_v2_Guide.md`

### Phase 3 (신규 추가 - 2026-02-05)
7. [x] `12_Claude_Cowork_Plugins_Guide.md` ✅ 2026-02-05 완료
8. [ ] `13_Enterprise_Integrations_Guide.md` 🆕
9. [ ] `14_Claude_Constitution_Guide.md` 🆕

### Phase 4 (유지보수)
10. [ ] 기존 문서 업데이트 (모델 ID, URL 변경 반영)
11. [ ] README.md 업데이트
12. [ ] examples/ 폴더에 새 예제 추가

---

## 참고 링크

### 공식 문서
- [Claude API Release Notes](https://platform.claude.com/docs/en/release-notes/api)
- [Claude Code CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)
- [Anthropic News](https://www.anthropic.com/news)

### 커뮤니티
- [ClaudeLog](https://claudelog.com/)
- [Releasebot - Claude Updates](https://releasebot.io/updates/anthropic/claude)

---

## 내일 작업 시작 방법

```bash
# 1. Claude Code 실행
claude

# 2. 이 폴더 열기
cd D:\Claude_AI_Knowledge

# 3. Claude에게 요청
"NEW_FEATURES_TODO_2026.md 파일을 읽고 Structured Outputs 가이드 작성해줘"
```

또는:
```
"오늘 조사한 최신 기능 중에서 첫 번째 문서 작성 시작해줘"
```

---

> **마지막 업데이트**: 2026-02-06
> **다음 작업**: Enterprise Integrations 가이드 또는 New Tools 가이드 작성

*Made with Claude by Bella (OZKIZ)*
