---
tags:
  - claude
  - cowork
  - vm
  - troubleshooting
  - hyper-v
---

# Claude Desktop Cowork VM 문제 해결

> 종합 설치 가이드는 [claude-desktop-cowork-setup-guide.md](claude-desktop-cowork-setup-guide.md) 참조

---

## 문제 1: VM service not running (서비스 시작 실패)

### 증상
- Cowork 시작 시 "VM service not running. The service failed to start." 오류
- `CoworkVMService` 상태가 `Stopped`

### 원인
Windows **Home** 에디션에는 Hyper-V VM 관리 기능(`vmms` 서비스)이 포함되지 않음.
- `vmcompute`는 WSL2를 통해 설치되지만, 전체 Hyper-V는 Pro/Enterprise에만 기본 포함

### 진단 명령어

**1. 서비스 상태 확인:**
```powershell
sc query vmms
sc query vmcompute
sc query CoworkVMService
```
- `vmms`가 없으면 → Hyper-V 미설치

**2. Windows 에디션 확인:**
```powershell
powershell -Command "(Get-ComputerInfo -Property WindowsProductName).WindowsProductName"
```

### 해결 방법: Windows Home에서 Hyper-V 활성화

**관리자 권한 CMD에서 실행 (`enable-hyperv.bat`):**
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
- 반드시 **관리자 권한 CMD**에서 실행 (Claude Code에서는 불가)
- 설치 완료 후 **PC 재부팅 필수**
- 재부팅 후 `vmms` 서비스가 생성되고 `CoworkVMService` 정상 작동

---

## 문제 2: 가상 디스크 시스템 제한 오류 (0xC03A001A)

### 증상
- Cowork 시작 시 `cowork-vm` 가상 컴퓨터 시작 실패
- 에러 코드: `0xC03A001A`
- 에러 메시지: "가상 디스크 시스템 제한으로 인해 요청한 작업을 완료할 수 없습니다. 가상 하드 디스크 파일은 압축이 풀려 있는 상태이고 암호화되지 않아야 하며 스파스가 아니어야 합니다."

### 원인
`rootfs.vhdx` 파일에 **NTFS 압축**이 적용되어 Hyper-V가 VM을 시작할 수 없음.
- 드라이브 또는 상위 폴더에 "내용 압축하여 디스크 공간 절약" 옵션이 켜져 있을 때 발생

### 관련 파일 경로
```
%APPDATA%\Claude\vm_bundles\claudevm.bundle\rootfs.vhdx
```
전체 경로:
```
C:\Users\User\AppData\Roaming\Claude\vm_bundles\claudevm.bundle\rootfs.vhdx
```

### 진단 명령어

**파일 속성 확인 (압축/스파스/암호화 여부)**
```powershell
$vhdx = Join-Path $env:APPDATA "Claude\vm_bundles\claudevm.bundle\rootfs.vhdx"
(Get-Item $vhdx -Force).Attributes
```
- 정상: `Archive`
- 비정상: `Archive, Compressed` 또는 `Archive, SparseFile` 또는 `Archive, Encrypted`

### 해결 방법

**번들 폴더 전체 NTFS 압축 해제:**
```powershell
$bundlePath = Join-Path $env:APPDATA "Claude\vm_bundles\claudevm.bundle"
compact /U /S:"$bundlePath" /I
```

**해제 후 확인:**
```powershell
$vhdx = Join-Path $env:APPDATA "Claude\vm_bundles\claudevm.bundle\rootfs.vhdx"
(Get-Item $vhdx -Force).Attributes
# "Archive" 만 표시되면 정상
```

### 재발 방지
- `C:\Users\User\AppData\Roaming\Claude` 폴더 우클릭 > 속성 > 고급 > "내용을 압축하여 디스크 공간 절약" 체크 해제
- 드라이브 전체에 압축이 걸려 있는 경우, 해당 드라이브 속성에서도 압축 해제 필요

---

## 문제 3: Claude Code에서 PowerShell 명령 실행 시 `$_` 변수 오류

### 증상
- `extglob.Name`, `extglob.Message` 같은 엉뚱한 에러 발생
- `Where-Object { $_.Name -match ... }` 패턴이 동작하지 않음

### 원인
Claude Code의 bash 환경(MINGW/Git Bash)에서 `$_`가 bash 내장 변수로 해석되어
PowerShell에 전달되기 전에 치환됨

### 해결 방법
1. **`$_` 사용하는 복잡한 명령은 .ps1 파일로 저장 후 실행**
```powershell
# check-service.ps1 로 저장
Get-Service | Where-Object { $_.Name -match 'cowork' } | Format-Table Name, Status
```
```bash
powershell -NoProfile -File C:\Users\User\check-service.ps1
```

2. **단순 명령으로 대체** (Where-Object 파이프라인 피하기)
```bash
# 직접 서비스명 지정
sc query CoworkVMService
powershell -NoProfile -Command "Get-Service CoworkVMService"
```

3. **Get-WmiObject 대신 다른 방법 사용**
```bash
# 나쁜 예: Get-WmiObject win32_service | Where-Object { $_.Name -like '*cowork*' }
# 좋은 예:
sc qc CoworkVMService
```

---

## 문제 4: 관리자 권한 부족

### 증상
- DISM 실행 실패
- `Get-WindowsOptionalFeature` 실행 불가
- `Get-VM` 권한 오류

### 원인
Claude Code는 일반 사용자 권한으로 실행됨

### 해결 방법
- Claude Code에게 **bat/ps1 스크립트 파일을 만들도록** 요청
- 사용자가 해당 파일을 **관리자 권한으로 직접 실행**
- Claude Code에서 직접 관리자 명령 실행 시도하지 않기

---

## 문제 5: Hyper-V 설치 중 CMD/PowerShell/Claude Code 실행 불가

### 증상
- Hyper-V 설치(DISM) 실행 중 또는 직후 터미널이 먹통
- Claude Code 응답 없음

### 원인
- DISM이 시스템 구성을 변경하면서 셸 환경이 불안정해짐
- 특히 패키지 설치 중 시스템 파일 잠금 발생 가능

### 해결 방법
- **PC 재부팅**으로 해결
- 재부팅 후 모든 셸 환경 정상 복구

---

*마지막 업데이트: 2026-02-12*
*환경: Windows 11 Home 10.0.26100, Claude Desktop v1.1.2685.0*
