---
tags:
  - gpters
  - study
  - claude
  - remote-control
  - ppt
  - 사례
  - 2026
---

# [사례] 폰에서 명령 -> PC에서 PPT 생성! Claude Code Remote Control 써봤습니다

> **작성자**: Bella (OZKIZ)
> **스터디**: 지피터스 AI 활용 스터디
> **작성일**: 2026-02-26
> **게시 URL**: https://www.gpters.org/llm-service/post/command-phone-create-ppt-EwehPLHpNl3ygZD

---

## TL;DR (3줄 요약)

1. **Claude Code Remote Control** = 폰으로 PC의 AI 코딩 에이전트 원격 조종
2. **설정 10초**, QR 스캔하면 끝 — 생각보다 너무 쉬움
3. **Pro 플랜($20/월)**부터 사용 가능 — 실제로 폰에서 PPT 만들어봤는데 진짜 됩니다

---

## Remote Control이 뭔가요?

### 한 줄 요약

> 집 PC에서 돌아가는 Claude Code를 폰으로 조종하는 기능

2월 24일에 공개된 따끈따끈한 신기능이에요!

### Before vs After

| 기존 | Remote Control |
|------|---------------|
| 코딩하려면 PC 앞에 앉아야 함 | 폰에서 "이거 해줘" -> PC에서 실행됨 |
| 외출하면 작업 중단 | 카페에서, 지하철에서도 계속 작업 |
| PC 화면 봐야 진행상황 확인 | 폰에서 실시간 확인 |

---

## 설정 방법 (진짜 10초)

**Step 1**: PC에서 Claude Code 실행
```
claude
```

**Step 2**: 로그인 (이미 되어있으면 스킵)
```
/login
```

**Step 3**: Remote Control 시작
```
/rc
```
(또는 `/remote-control`)

**Step 4**: QR 코드 스캔
-> Claude 모바일 앱으로 스캔하면 끝!

> Tip: 스페이스바 누르면 QR 코드가 표시돼요!

---

## 실제 사례: 폰으로 PPT 만들기

### 상황

집에서 Claude Code 켜놓고 외출했는데, 갑자기 "Claude 생태계 정리 PPT" 만들어야겠다는 생각이 들었어요.

### 폰에서 보낸 메시지

> "Claude AI 생태계 가이드 PPT 만들어줘. Web, Code, Desktop, Cowork, OpenClaw 포함해서 깔끔하게 13장 정도로"

### 결과

- ✅ 집 PC에서 PPT 파일이 실제로 생성됨!
- ✅ 13장 슬라이드, 목차부터 비용 정리까지 완성
- ✅ 저는 카페에서 커피 마시고 있었음

### 만들어진 PPT 구성

| 슬라이드 | 내용 |
|----------|------|
| 1 | 표지 |
| 2 | 목차 |
| 3-4 | Claude 생태계 한눈에 보기 |
| 5 | Claude AI (Web) |
| 6 | Claude Code (CLI) |
| 7 | Claude Desktop & Cowork |
| 8 | Remote Control 소개 |
| 9 | 제품 비교표 |
| 10-11 | OpenClaw 연동 |
| 12 | 자동화 활용법 |
| 13 | 비용 & 시작 가이드 |

-> 이게 폰으로 된다고요?!

---

## 이럴 때 쓰면 좋아요

| 상황 | 활용 예시 |
|------|----------|
| 출퇴근 중 | "아까 그 버그 수정해줘" |
| 카페에서 | "새 기능 추가해줘" |
| 소파에 누워서 | "테스트 돌려봐" |
| 자기 전에 | "내일 아침까지 이거 정리해놔" |
| 산책하면서 | "빌드 상태 어때?" |

---

## 필수 조건

### 플랜 요구사항

| 플랜 | Remote Control | 비용 |
|------|---------------|------|
| Free | X | $0 |
| Pro | ✅ 사용 가능 | $20/월 |
| Max | ✅ 사용 가능 | $100~200/월 |
| Team | X 현재 미지원 | - |
| Enterprise | X 현재 미지원 | - |

> Pro 플랜($20/월)부터 바로 사용 가능합니다!

### 기타 조건

- PC가 켜져 있어야 함
- Claude Code가 실행 중이어야 함
- 터미널 창이 열려 있어야 함

---

## 보안 걱정되시나요?

걱정 마세요! 안전합니다.

| 항목 | 설명 |
|------|------|
| 포트 | 인바운드 포트 안 열어도 됨 (해킹 걱정 X) |
| 암호화 | 모든 통신 TLS 암호화 |
| 파일 처리 | 파일은 PC에서만 처리 (클라우드 X) |
| 공공 Wi-Fi | 안전하게 사용 가능 |

> 폰/브라우저는 그냥 "원격 창문" 역할만 해요. 실제 작업은 다 PC에서 일어납니다!

---

## 알아둘 제한사항

| 제한 | 설명 |
|------|------|
| 세션 수 | 동시에 1개 세션만 가능 |
| 터미널 | 터미널 닫으면 세션 종료 |
| 절전 모드 | PC 절전 -> 연결 끊김 (깨어나면 자동 재연결) |
| 네트워크 | 10분 이상 오프라인 -> 세션 타임아웃 |

---

## Remote Control vs Claude Code on the Web

둘 다 claude.ai/code 인터페이스를 사용하지만 다릅니다!

| 구분 | Remote Control | Claude Code on the Web |
|------|---------------|----------------------|
| 실행 위치 | **내 PC** | Anthropic 클라우드 |
| 로컬 파일 | ✅ 접근 가능 | X 불가 |
| MCP 서버 | ✅ 내 설정 그대로 | X 불가 |
| 용도 | 작업 중 이어서 하기 | 새로 빠르게 시작하기 |

---

## 마치며

### 솔직한 후기

- **설정**: 예상보다 너무 쉬움 (10초)
- **사용감**: PC 앞에 있는 것처럼 자연스러움
- **실용성**: 외출이 많은 분들한테 강추

### 이런 분께 추천!

- 이동이 많은 분
- 집에 작업용 PC 두고 다니는 분
- 폰으로 뭐든 해결하고 싶은 분
- "잠깐 카페 가는데 작업 멈추기 싫은" 분

---

## 참고 자료

- [Remote Control 공식 문서](https://code.claude.com/docs/en/remote-control)
- [Claude Code + Pro/Max 사용법](https://code.claude.com/docs/en/cli-reference)

---

*Made with Claude Code Remote Control by Bella (OZKIZ)*
*#지피터스 #Claude #RemoteControl #AI활용 #클로드코드*
