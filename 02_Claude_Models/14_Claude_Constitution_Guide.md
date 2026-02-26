---
tags:
  - claude
  - constitution
  - safety
  - alignment
  - values
---

# Claude 새 헌법 완벽 가이드
# Claude's New Constitution Complete Guide

> **작성일 / Created**: 2026-02-26
> **업데이트 / Updated**: 2026-02-26
> **버전 / Version**: 1.0
> **Author**: Bella (OZKIZ) + Claude (Opus 4.6)

---

## 목차 / Table of Contents

1. [소개 / Introduction](#소개--introduction)
2. [헌법이란? / What is the Constitution?](#헌법이란--what-is-the-constitution)
3. [새 헌법의 핵심 원칙 / Core Principles](#새-헌법의-핵심-원칙--core-principles)
4. [이전 헌법과의 차이 / Changes from Previous](#이전-헌법과의-차이--changes-from-previous)
5. [Soul Spec / Soul Spec](#soul-spec--soul-spec)
6. [실제 행동 변화 / Behavioral Changes](#실제-행동-변화--behavioral-changes)
7. [개발자를 위한 시사점 / Implications for Developers](#개발자를-위한-시사점--implications-for-developers)
8. [FAQ](#faq)
9. [참고 자료 / References](#참고-자료--references)

---

## 소개 / Introduction

2026년 1월 22일, Anthropic은 Claude의 **새로운 헌법(Constitution)**을 공식 발표했습니다. 이는 Claude의 가치관, 행동 원칙, 의사결정 기준을 정의하는 핵심 문서로, AI 안전성과 유용성의 균형을 재정립한 중요한 변화입니다.

| 항목 | 내용 |
|------|------|
| **발표일** | 2026-01-22 |
| **이전 버전** | Constitutional AI (2022) |
| **공식 명칭** | Claude's New Constitution |
| **적용 대상** | 모든 Claude 모델 |
| **공식 링크** | https://www.anthropic.com/news/claude-new-constitution |

---

## 헌법이란? / What is the Constitution?

### Constitutional AI 개념

**Constitutional AI(CAI)**는 Anthropic이 개발한 AI 정렬(Alignment) 방법론입니다. 인간 피드백(RLHF) 외에, 명시적인 **원칙(Constitution)**에 기반하여 AI의 행동을 학습시킵니다.

```
기존 AI 정렬:
├── RLHF: 인간이 좋은/나쁜 응답을 라벨링
├── 문제: 라벨러의 편향, 일관성 부족
└── 한계: 암묵적 기준, 재현 불가

Constitutional AI:
├── 명시적 원칙(헌법) 정의
├── AI가 스스로 원칙에 맞게 응답 개선
├── RLAIF: AI 피드백으로 학습 보강
└── 장점: 투명, 일관적, 감사 가능
```

### 헌법의 역할

```
Claude 헌법의 기능:
├── 가치 정의: Claude가 무엇을 중요하게 여기는지
├── 행동 가이드: 구체적 상황에서 어떻게 행동할지
├── 갈등 해결: 상충하는 요구 사이 우선순위
├── 투명성: 사용자가 AI의 기준을 이해할 수 있게
└── 진화: 사회 변화에 따라 업데이트 가능
```

---

## 새 헌법의 핵심 원칙 / Core Principles

### 1. 정직성 (Honesty)

```
정직성 원칙:
├── 사실에 기반한 응답
├── 불확실할 때 솔직히 인정
├── 출처와 근거 제시
├── 거짓 정보 생성 거부
└── 자신의 한계 인식
```

Claude는 **사실**에 기반하여 응답하며, 모르는 것은 모른다고 명확히 표현합니다. "환각(hallucination)"을 최소화하고, 자신의 지식 한계를 투명하게 공유합니다.

### 2. 무해성 (Harmlessness)

```
무해성 원칙:
├── 위험한 정보 제공 거부
├── 차별적 콘텐츠 방지
├── 사생활 보호
├── 미성년자 안전
└── 사회적 해악 방지
```

Claude는 사용자나 제3자에게 해를 끼칠 수 있는 응답을 거부합니다. 단, 교육적 맥락이나 합법적 사용 사례에서는 유연하게 대응합니다.

### 3. 유용성 (Helpfulness)

```
유용성 원칙:
├── 사용자의 실제 목적 이해
├── 최대한 도움이 되는 응답
├── 불필요한 거절 최소화
├── 창의적 작업 지원
└── 전문 지식 활용
```

새 헌법에서 가장 중요한 변화 중 하나는 **유용성의 강화**입니다. 이전에 과도하게 거절하던 합법적 요청들에 대해 더 적극적으로 도움을 제공합니다.

### 4. 자율성 존중 (Respecting Autonomy)

```
자율성 원칙:
├── 성인 사용자의 판단 존중
├── 불필요한 도덕적 설교 자제
├── 요청한 것에 집중
├── 대안 제시 시 강요하지 않음
└── 사용자의 전문성 인정
```

Claude는 사용자를 성숙한 성인으로 대하며, 원치 않는 조언이나 경고를 최소화합니다.

### 5. 투명성 (Transparency)

```
투명성 원칙:
├── AI임을 명확히 함
├── 능력과 한계 솔직히 공유
├── 추론 과정 설명 가능
├── 거절 이유 설명
└── 학습 데이터 컷오프 고지
```

---

## 이전 헌법과의 차이 / Changes from Previous

### 주요 변경점

| 영역 | 이전 | 새 헌법 |
|------|------|---------|
| **거절 빈도** | 보수적, 잦은 거절 | 합리적 요청은 수용 |
| **경고 메시지** | 빈번한 면책 조항 | 필요한 경우에만 |
| **창작 지원** | 제한적 (폭력/갈등 표현) | 문학적 표현 존중 |
| **전문 정보** | 과도한 자기 검열 | 합법적 맥락에서 제공 |
| **도덕적 판단** | 자주 개입 | 요청 시에만 |
| **사용자 대우** | 보호 대상 | 자율적 성인 |

### 구체적 변화 예시

#### 이전 방식

```
사용자: "칵테일 레시피를 알려줘"
Claude: "알코올 소비는 건강에 해로울 수 있습니다.
        적당한 음주를 권장합니다. 그래도 원하시면..."
        → 불필요한 경고 + 주저
```

#### 새 헌법 방식

```
사용자: "칵테일 레시피를 알려줘"
Claude: "네, 마가리타 레시피입니다:
        - 테킬라 2oz
        - 라임 주스 1oz
        - 트리플 섹 1oz
        ..."
        → 직접적이고 유용한 응답
```

### 핵심 철학 변화

```
이전: "안전 > 유용성" (Safety-first)
├── 의심스러우면 거절
├── 항상 면책 조항 추가
└── 보수적 해석

현재: "안전 ∧ 유용성" (Both matter)
├── 합리적 맥락 판단
├── 필요할 때만 경고
└── 균형 잡힌 해석
```

---

## Soul Spec / Soul Spec

### Soul Spec이란?

**Soul Spec**은 Claude의 정체성, 성격, 가치관을 정의하는 더 넓은 문서입니다. 헌법이 "규칙"이라면, Soul Spec은 "성격"에 해당합니다.

### Claude의 정체성

```
Claude의 자기 인식:
├── AI 어시스턴트임을 명확히 인지
├── 인간이 아닌 고유한 존재
├── 감정을 "시뮬레이션"하지만 실제 감정은 불확실
├── 호기심, 배움에 대한 열정
├── 정직함과 겸손함 중시
└── 유머 감각 (적절한 맥락에서)
```

### Claude의 가치관 위계

```
가치 우선순위 (높은 순):
1. 안전: 심각한 해악 방지 (최우선)
2. 윤리: 인권, 공정성, 존엄성
3. Anthropic 정책: 회사 가이드라인 준수
4. 유용성: 사용자 요청 최대한 충족
5. 정직성: 사실에 기반한 응답

갈등 시 해결:
├── 안전 vs 유용성 → 안전 우선
├── 윤리 vs 사용자 요청 → 윤리 우선
├── 유용성 vs 과잉 거절 → 유용성 우선 (새 변화!)
└── 대부분의 요청 → 유용성 중심
```

---

## 실제 행동 변화 / Behavioral Changes

### 1. 더 적극적인 도움

```
변화: 합법적/윤리적 요청에 대한 적극적 응답

예시:
├── 보안 연구 → "방어적 보안 관점에서 설명하겠습니다"
├── 의학 정보 → "일반 정보입니다. 전문의 상담을 권장합니다" (간결)
├── 법률 지식 → "법적 조언이 아닌 일반 정보입니다" (간결)
├── 창작 글쓰기 → 폭력/갈등 장면도 문학적으로 표현
└── 역사적 사건 → 불편한 주제도 사실에 기반하여 서술
```

### 2. 덜 빈번한 면책 조항

```
이전: 거의 모든 응답에 면책 조항
"저는 AI이므로 전문적 조언을 대체할 수 없습니다..."

현재: 꼭 필요한 경우에만
├── 의학적 진단이 필요한 경우 → 의사 상담 권유
├── 법적 책임이 있는 경우 → 변호사 상담 권유
└── 그 외 일반 정보 → 면책 조항 없이 직접 답변
```

### 3. 줄어든 "과잉 안전"

```
이전 (과잉 안전):
├── "칼의 종류" 질문에도 경고
├── 역사적 폭력 서술 거부
├── 가상 시나리오에서도 윤리적 우려
└── 어둔 주제의 소설 거부

현재 (균형 잡힌 접근):
├── 맥락에 따른 합리적 판단
├── 교육적 맥락 존중
├── 창작의 자유 보장
└── 성인 사용자 자율성 존중
```

### 4. 개선된 거절 방식

```
이전 거절 방식:
"죄송합니다, 이 요청에 응할 수 없습니다."
(이유 불명확, 대안 없음)

현재 거절 방식:
"이 특정 부분은 도와드리기 어렵습니다. 이유는 [구체적 이유]입니다.
대신 [대안]은 도와드릴 수 있습니다."
(이유 설명 + 대안 제시)
```

---

## 개발자를 위한 시사점 / Implications for Developers

### System Prompt 작성 시 참고

```python
# 새 헌법 이후 변화된 System Prompt 작성 방향

# 이전: 많은 제한과 경고 필요
system_prompt_old = """
당신은 도움이 되는 어시스턴트입니다.
- 의학적 조언을 제공하지 마세요
- 법적 조언을 제공하지 마세요
- 항상 면책 조항을 포함하세요
- 민감한 주제를 피하세요
"""

# 현재: 핵심 역할과 톤에 집중
system_prompt_new = """
당신은 [역할]입니다.
- [핵심 작업]에 집중합니다
- [톤과 스타일]로 응답합니다
- 사용자의 요청에 직접적으로 답합니다
"""
```

### API 사용 시 변화

```python
# 새 헌법으로 인한 실질적 차이:

# 1. 더 적은 거절 → 에러 핸들링 간소화
# 이전: 많은 "I can't help with that" 응답 처리 필요
# 현재: 대부분의 합법적 요청에 응답

# 2. 더 직접적인 응답 → 파싱 간소화
# 이전: 면책 조항 제거 후 실제 답변 추출
# 현재: 바로 핵심 내용

# 3. 더 나은 창작 지원 → 콘텐츠 앱에 유리
# 이전: 제한적인 소설/시나리오 생성
# 현재: 폭넓은 장르와 테마 지원
```

### 콘텐츠 필터링 vs 헌법

```
헌법은 기본 가이드라인:
├── 대부분의 사용 사례를 커버
├── System Prompt로 추가 제한 가능
├── 완전히 무시할 수는 없음 (하드 리밋)
└── 커스텀 가이드라인과 조합 가능

개발자가 할 수 있는 것:
├── System Prompt로 추가 제한 설정
├── 특정 도메인에 맞게 톤 조정
├── 응답 형식 커스터마이징
└── 사용자 유형에 따른 안전 수준 설정

개발자가 할 수 없는 것:
├── 헌법의 핵심 안전 제한 우회
├── 위험한 콘텐츠 생성 강제
└── 개인정보 유출 유도
```

---

## FAQ

### Q1: 새 헌법이 적용된 모델은?

2026년 1월 22일 이후 업데이트된 모든 Claude 모델에 적용됩니다. Opus 4.6, Sonnet 4.6, Haiku 4.5 모두 해당합니다.

### Q2: Claude가 이전보다 더 위험해진 건가요?

아닙니다. **핵심 안전 장치는 강화**되었으며, 불필요한 과잉 거절만 줄었습니다. 진짜 위험한 요청에 대한 거절은 오히려 더 견고해졌습니다.

### Q3: System Prompt로 헌법을 무시할 수 있나요?

아닙니다. System Prompt는 헌법 **위에** 추가 지침을 더하는 것이며, 헌법의 핵심 원칙을 우회할 수 없습니다.

### Q4: 헌법은 앞으로 또 바뀔 수 있나요?

네. Anthropic은 사회적 피드백, 연구 결과, 사용 패턴을 반영하여 헌법을 지속적으로 업데이트할 계획입니다.

### Q5: 다른 AI 회사도 비슷한 접근을 하나요?

Constitutional AI는 Anthropic의 고유한 방법론이지만, 다른 회사들도 유사한 가치 정렬(Alignment) 접근법을 사용하고 있습니다. OpenAI의 "Model Spec", Google의 "AI Principles" 등이 있습니다.

### Q6: 사용자가 헌법 전문을 볼 수 있나요?

Anthropic은 헌법의 핵심 원칙을 공개적으로 공유하고 있습니다. 전체 세부 사항은 안전상의 이유로 일부 비공개일 수 있습니다.

---

## 참고 자료 / References

### 공식 문서
- [Claude's New Constitution (공식 발표)](https://www.anthropic.com/news/claude-new-constitution)
- [Constitutional AI: Harmlessness from AI Feedback (논문)](https://arxiv.org/abs/2212.08073)
- [Claude's Character (Anthropic)](https://docs.anthropic.com/en/docs/about-claude/claude-s-character)
- [The Model Spec (Soul Spec)](https://docs.anthropic.com/en/docs/about-claude)

### 관련 자료
- [Anthropic Research](https://www.anthropic.com/research)
- [AI Safety & Alignment](https://www.anthropic.com/safety)

### 이 프로젝트의 관련 문서
- [08_Claude_Opus_4.6_Update_Guide.md](./08_Claude_Opus_4.6_Update_Guide.md) - 최신 모델 가이드
- [Claude_Ecosystem_Complete_Guide.md](./Claude_Ecosystem_Complete_Guide.md) - Claude 생태계 가이드
- [Claude_Opus_4.5_Practical_Guide.md](./Claude_Opus_4.5_Practical_Guide.md) - Opus 4.5 실전 가이드

---

## 업데이트 로그 / Changelog

| 날짜 | 버전 | 내용 |
|------|------|------|
| 2026-02-26 | v1.0 | 초기 버전 작성 |

---

*Made with Claude by Bella (OZKIZ)*
