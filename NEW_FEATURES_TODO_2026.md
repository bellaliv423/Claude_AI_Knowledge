# Claude 최신 기능 업데이트 대기 목록
# Claude Latest Features Update Queue

> **조사일 / Research Date:** 2026-02-02
> **상태 / Status:** 문서화 대기 중
> **GitHub**: https://github.com/bellaliv423/Claude_AI_Knowledge

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

### Phase 1 (즉시)
1. [ ] `05_Structured_Outputs_Guide.md`
2. [ ] `06_Memory_Context_Guide.md` (Memory + Context Editing)
3. [ ] `07_Effort_Parameter_Guide.md`

### Phase 2 (1주일 내)
4. [ ] `08_New_Tools_Guide.md` (Web Fetch, Tool Search, Programmatic)
5. [ ] `09_Files_MCP_Guide.md` (Files API + MCP Connector)
6. [ ] `10_Claude_Code_v2_Guide.md`

### Phase 3 (2주일 내)
7. [ ] 기존 문서 업데이트 (모델 ID, URL 변경 반영)
8. [ ] README.md 업데이트
9. [ ] examples/ 폴더에 새 예제 추가

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

> **마지막 업데이트**: 2026-02-02
> **다음 작업**: Structured Outputs 가이드 작성

*Made with Claude by Bella (OZKIZ)*
