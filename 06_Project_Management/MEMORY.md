---
tags:
  - project
  - memory
  - index
  - file-map
---

# Memory Index

## Claude Desktop + Cowork (Windows 11 Home)
- [완전 설치 가이드](claude-desktop-cowork-setup-guide.md) - 설치, 환경 설정, 프롬프트, 오류 해결
- [Cowork VM 문제 해결](cowork-vm-troubleshooting.md) - 개별 오류별 진단/해결
- [Cowork 플러그인 가이드](12_Claude_Cowork_Plugins_Guide.md)

## Claude 도구 & API 가이드
- [Claude 도구 완전 가이드 v3](claude_tools_complete_guide_v3.md) - 최신 종합
- [Claude 도구 완전 가이드 v1](01_Claude_Tools_Complete_Guide.md)
- [코드 실행 설정 가이드](02_Code_Execution_Setup_Guide.md)
- [MCP 사용 가이드](03_MCP_Usage_Guide.md)
- [Claude 스킬 가이드](04_Claude_Skills_Guide.md)
- [구조화된 출력 가이드](05_Structured_Outputs_Guide.md)
- [메모리 & 컨텍스트 가이드](06_Memory_Context_Guide.md)
- [Effort 파라미터 가이드](07_Effort_Parameter_Guide.md)

## Claude 모델 & 생태계
- [Claude Opus 4.6 업데이트 가이드](08_Claude_Opus_4.6_Update_Guide.md)
- [Claude Opus 4.5 실전 가이드](Claude_Opus_4.5_Practical_Guide.md)
- [Claude 생태계 완전 가이드](Claude_Ecosystem_Complete_Guide.md)
- [Claude Code 베스트 프랙티스 (Boris Cherny)](Boris_Cherny_Claude_Code_Best_Practices.md)

## OpenClaw
- [OpenClaw 완전 가이드](11_OpenClaw_Complete_Guide.md)
- [OpenClaw 빠른 명령어](OpenClaw_Quick_Commands.md)
- [OpenClaw 설정 로그 (2026-02-03)](OpenClaw_Setup_Log_2026-02-03.md)

## 프로젝트 관리
- [CLAUDE.md (프로젝트 설정)](CLAUDE.md)
- [init.md (초기 설정)](init.md)
- [AI 협업 로그](AI_Collaboration_Log.md)
- [2026 신기능 TODO](NEW_FEATURES_TODO_2026.md)

## 코드 예제 (examples/)
- batch_api.py, code_execution_basic.py, container_reuse.py
- extended_thinking.py, mcp_client.py, memory_context.py
- programmatic_tool_calling.py, structured_outputs.py

## Environment
- Windows 11 Home 10.0.26100
- Claude Desktop v1.1.2685.0 (WindowsApps 패키지)
- Hyper-V: 수동 설치 완료 (Home 에디션용 bat 스크립트)

## Claude Code 사용 시 주의
- PowerShell `$_` 변수가 bash extglob으로 치환됨 → ps1 파일로 저장 후 실행 권장
- 관리자 권한 필요 명령 → bat/ps1 파일 생성 후 사용자가 직접 관리자 실행
- `Get-VM`, `DISM`, `Get-WindowsOptionalFeature` 등은 관리자 권한 필수
