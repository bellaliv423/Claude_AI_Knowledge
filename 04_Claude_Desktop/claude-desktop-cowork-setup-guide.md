---
tags:
  - claude
  - desktop
  - cowork
  - setup
  - windows
---

# Claude Desktop + Cowork 완전 설치 가이드 (Windows 11 Home)

> 2026-02-12 실제 설치 경험 기반. Windows 11 Home 환경에서 검증 완료.

---

## 1. 개요

**Cowork**는 Claude Desktop의 초기 연구 프리뷰 기능으로, Hyper-V 기반 Linux VM에서 코드 실행, 파일 관리, 스크린샷 정리 등을 수행합니다.

### 필수 환경 요건
| 항목 | 요구 사항 |
|------|-----------|
| OS | Windows 10/11 (Home도 가능하나 추가 설정 필요) |
| Hyper-V | 필수 (vmms + vmcompute 서비스) |
| 디스크 공간 | 최소 15GB 여유 (rootfs.vhdx ~9.4GB + initrd ~175MB 등) |
| NTFS 압축 | **반드시 해제** (vhdx 파일에 압축 적용 시 VM 시작 불가) |
| 메모리 | 최소 8GB RAM 권장 |

### 핵심 파일 경로
```
설치 경로 (앱):
  C:\Program Files\WindowsApps\Claude_<버전>_x64__pzs8sxrjxfjjc\app\resources\cowork-svc.exe

VM 번들 경로 (데이터):
  %APPDATA%\Claude\vm_bundles\claudevm.bundle\
    ├── rootfs.vhdx        (~9.4GB, 메인 디스크 이미지)
    ├── initrd             (~175MB, 초기 RAM 디스크)
    ├── vmlinuz            (~15MB, Linux 커널)
    ├── sessiondata.vhdx   (~4MB, 세션 데이터)
    ├── smol-bin.vhdx      (~37MB, 유틸리티)
    └── .*.origin          (해시 파일들)

서비스:
  CoworkVMService (cowork-svc.exe) - AUTO_START, LocalSystem
  vmms (Hyper-V Virtual Machine Management) - Automatic
  vmcompute (Hyper-V Host Compute Service) - Manual

Named Pipe:
  \\.\pipe\cowork-vm-service

로그:
  C:\Users\User\AppData\Local\Claude\Logs\
```

---

## 2. 설치 절차 (처음부터)

### Step 1: Claude Desktop 다운로드 및 설치
- https://claude.ai/download 에서 Windows 버전 다운로드
- 설치 실행 (Microsoft Store 앱 패키지 형태)

### Step 2: Hyper-V 활성화 (Windows Home 필수!)

**Windows Home에는 Hyper-V가 기본 미포함.** Pro/Enterprise는 이 단계 불필요.

#### 방법 A: Claude Code에게 요청하는 프롬프트
```
Windows 11 Home에 Hyper-V를 설치해 주세요.
enable-hyperv.bat 파일을 만들어서 관리자 CMD로 실행하게 해주세요.
설치 후 재부팅이 필요합니다.
```

#### 방법 B: 직접 bat 파일 생성 후 관리자 CMD에서 실행
파일명: `C:\Users\User\enable-hyperv.bat`
```bat
@echo off
pushd "%~dp0"
dir /b %SystemRoot%\servicing\Packages\*Hyper-V*.mum >hyper-v-pkgs.txt
for /f %%i in ('findstr /i . hyper-v-pkgs.txt 2^>nul') do dism /online /norestart /add-package:"%SystemRoot%\servicing\Packages\%%i"
del hyper-v-pkgs.txt
Dism /online /enable-feature /featurename:Microsoft-Hyper-V -All /LimitAccess /ALL
pause
```

**중요:**
- **반드시 "관리자 권한으로 실행"** (우클릭 > 관리자 권한으로 실행)
- Claude Code의 bash/powershell에서는 관리자 권한이 없어 DISM 실행 불가
- 설치 완료 후 **PC 재부팅 필수**

### Step 3: 재부팅 후 확인
```powershell
# 서비스 확인
sc query vmms
sc query vmcompute
sc query CoworkVMService
# 세 개 모두 RUNNING이면 정상
```

### Step 4: NTFS 압축 확인 및 해제
Claude Desktop 첫 실행 시 VM 번들이 자동 다운로드됨. 이후:
```powershell
# 압축 상태 확인
$vhdx = Join-Path $env:APPDATA "Claude\vm_bundles\claudevm.bundle\rootfs.vhdx"
(Get-Item $vhdx -Force).Attributes
# "Archive"만 표시되면 정상
# "Archive, Compressed" 등이면 압축 해제 필요
```

압축 해제가 필요한 경우:
```powershell
$bundlePath = Join-Path $env:APPDATA "Claude\vm_bundles\claudevm.bundle"
compact /U /S:"$bundlePath" /I
```

### Step 5: Claude Desktop에서 Cowork 사용
- Claude Desktop 실행
- "할 일을 처리해 볼까요?" 화면이 나타나면 성공!

---

## 3. 발생 가능한 오류와 해결법

### 오류 1: "VM service not running. The service failed to start."
**원인:** Hyper-V 미설치 (Windows Home)
**해결:** Step 2의 enable-hyperv.bat 실행 + 재부팅

**진단:**
```powershell
sc query vmms
# "서비스가 설치되지 않았습니다" → Hyper-V 미설치
```

### 오류 2: "가상 디스크 시스템 제한 오류 (0xC03A001A)"
**원인:** rootfs.vhdx에 NTFS 압축이 적용됨
**해결:** compact /U 명령으로 압축 해제

**진단:**
```powershell
$vhdx = Join-Path $env:APPDATA "Claude\vm_bundles\claudevm.bundle\rootfs.vhdx"
(Get-Item $vhdx -Force).Attributes
# "Archive, Compressed" → 압축 해제 필요
```

### 오류 3: Claude Code에서 PowerShell 명령 실행 오류
**원인:** Claude Code의 bash 환경(MINGW/Git Bash)에서 PowerShell의 `$_` 변수가
bash의 extglob으로 치환됨
**증상:** `extglob.Name`, `extglob.Message` 같은 오류

**해결/우회:**
- `$_` 를 사용하는 파이프라인 필터 대신, PowerShell 스크립트 파일(.ps1)을 만들어 실행
- 또는 `$_` 대신 `$PSItem` 사용 시도
- 또는 단순 명령어만 사용 (Where-Object 피하기)
```powershell
# 나쁜 예 (bash에서 $_ 치환됨):
powershell -Command "Get-Service | Where-Object { $_.Name -match 'cowork' }"

# 좋은 예 (ps1 파일로 저장 후 실행):
powershell -NoProfile -File C:\Users\User\check-service.ps1

# 또는 Where-Object 없이:
powershell -NoProfile -Command "Get-Service CoworkVMService"
```

### 오류 4: 관리자 권한 부족
**원인:** Claude Code는 일반 사용자 권한으로 실행됨
**증상:** DISM, Get-WindowsOptionalFeature, Get-VM 등에서 "권한 부족" 오류

**해결:**
- 관리자 권한이 필요한 작업은 **별도 관리자 CMD/PowerShell 창**에서 실행
- Claude Code에게 bat/ps1 파일을 **만들어 달라고 한 후**, 직접 관리자로 실행
```
Claude Code에게: "enable-hyperv.bat 파일을 만들어 주세요"
사용자가 직접: 파일 우클릭 > 관리자 권한으로 실행
```

### 오류 5: CMD/PowerShell/Claude Code 실행 불가 (충돌)
**원인:** Hyper-V 설치 과정에서 시스템 구성이 변경되며 셸 환경 불안정
**증상:** 터미널/Claude Code가 먹통이 됨

**해결:**
- PC 재부팅으로 해결
- 재부팅 후 Claude Code 재실행

---

## 4. Claude Code를 이용한 자동화 프롬프트

### 처음부터 한 번에 설치하고 싶을 때 (권장 프롬프트)

```
Claude Desktop의 Cowork 기능을 사용하려고 합니다.
내 환경은 Windows 11 Home입니다.

아래 순서로 진행해 주세요:
1. Hyper-V 설치 여부 확인 (sc query vmms)
2. 미설치 시: enable-hyperv.bat 파일 생성 (C:\Users\User\enable-hyperv.bat)
   - 단, 직접 실행하지 말고 파일만 만들어 주세요
   - 제가 관리자 CMD로 직접 실행하겠습니다
3. 설치 후 재부팅하면 다시 알려 주세요
4. 재부팅 후: vmms, vmcompute, CoworkVMService 서비스 상태 확인
5. rootfs.vhdx 파일 존재 여부 및 NTFS 압축 상태 확인
6. 압축이 적용되어 있으면 compact /U 명령으로 해제
7. 최종 점검 결과 알려주기
```

### Hyper-V만 설치하고 싶을 때
```
Windows 11 Home에 Hyper-V를 설치하는 bat 파일을 만들어 주세요.
경로: C:\Users\User\enable-hyperv.bat
저는 이 파일을 관리자 CMD로 직접 실행하겠습니다.
```

### 설치 후 점검만 하고 싶을 때
```
재부팅 완료! Hyper-V 설치 상태 확인하고 Cowork 작동되게 해주세요.
1. vmms 서비스 존재 여부 확인
2. CoworkVMService 상태 확인
3. rootfs.vhdx 압축 해제 재확인
4. Cowork 실행 테스트
```

### 충돌 방지 팁 (프롬프트에 포함)
```
주의사항:
- PowerShell에서 Where-Object { $_ } 구문은 bash와 충돌합니다.
  $_ 대신 직접 서비스명을 지정하거나 ps1 파일을 만들어 실행해 주세요.
- 관리자 권한이 필요한 명령(DISM, Get-VM 등)은 직접 실행하지 말고
  bat/ps1 파일로 만들어 주세요. 제가 관리자로 실행하겠습니다.
- Get-WmiObject에서 $_.Name 같은 구문도 bash에서 깨집니다.
```

---

## 5. 검증 체크리스트

설치 완료 후 아래 항목이 모두 충족되면 Cowork 정상 작동:

```powershell
# 1. Hyper-V 서비스 (RUNNING)
sc query vmms
sc query vmcompute

# 2. CoworkVMService (RUNNING)
sc query CoworkVMService

# 3. cowork-svc 프로세스 (실행 중)
tasklist /FI "IMAGENAME eq cowork-svc.exe"

# 4. rootfs.vhdx (존재 + Archive 속성만)
powershell -Command "Test-Path (Join-Path $env:APPDATA 'Claude\vm_bundles\claudevm.bundle\rootfs.vhdx')"
powershell -Command "(Get-Item (Join-Path $env:APPDATA 'Claude\vm_bundles\claudevm.bundle\rootfs.vhdx')).Attributes"

# 5. Named Pipe (존재)
powershell -Command "[IO.Directory]::GetFiles('//./pipe/') -match 'cowork'"

# 6. Claude Desktop (실행 중)
tasklist /FI "IMAGENAME eq claude.exe"
```

모든 항목 통과 → Claude Desktop에서 "할 일을 처리해 볼까요?" 화면 확인!

---

## 6. 아키텍처 요약

```
[Claude Desktop (Electron)]
       │
       ▼
[CoworkVMService (cowork-svc.exe)]
       │  Named Pipe: \\.\pipe\cowork-vm-service
       ▼
[Hyper-V (vmms + vmcompute)]
       │
       ▼
[cowork-vm (Linux VM)]
  ├── rootfs.vhdx (9.4GB - 루트 파일시스템)
  ├── initrd (175MB - 초기 RAM 디스크)
  ├── vmlinuz (15MB - Linux 커널)
  ├── sessiondata.vhdx (4MB - 세션 데이터)
  └── smol-bin.vhdx (37MB - 유틸리티 바이너리)
```

---

## 7. 주의사항 및 팁

1. **Windows Home 사용자**: Hyper-V 수동 설치가 반드시 필요. Pro/Enterprise는 설정에서 활성화만 하면 됨
2. **디스크 압축 주의**: C: 드라이브에 "내용 압축하여 디스크 공간 절약"이 켜져 있으면 rootfs.vhdx에도 자동 적용되어 VM 시작 불가
3. **관리자 권한**: Claude Code는 관리자 권한이 없으므로, DISM/Hyper-V 설정은 별도 관리자 셸에서 실행
4. **재부팅**: Hyper-V 설치 후 재부팅 없이는 서비스가 시작되지 않음
5. **VM 번들 다운로드**: Claude Desktop 첫 실행 시 자동으로 ~9.8GB 다운로드됨 (네트워크 환경 확인)
6. **bash vs PowerShell 충돌**: Claude Code의 bash에서 `$_`, `$PSItem` 등 PowerShell 변수가 bash에 의해 치환될 수 있음

---

*마지막 업데이트: 2026-02-12*
*환경: Windows 11 Home 10.0.26100, Claude Desktop v1.1.2685.0*
