"""
Claude Code 파일 자동 발송 도구
- 이메일 (Gmail SMTP)
- OpenClaw (WhatsApp)

사용법 (Claude Code에서):
  python D:/Claude_AI_Knowledge/tools/auto_deliver.py --file "파일경로" --to work
  python D:/Claude_AI_Knowledge/tools/auto_deliver.py --file "파일경로" --to personal
  python D:/Claude_AI_Knowledge/tools/auto_deliver.py --file "파일경로" --to both
  python D:/Claude_AI_Knowledge/tools/auto_deliver.py --file "파일경로" --to whatsapp
  python D:/Claude_AI_Knowledge/tools/auto_deliver.py --file "파일경로" --to all
"""

import smtplib
import argparse
import os
import subprocess
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
from datetime import datetime

# ─── 설정 ───
GMAIL_USER = "kndli.210@gmail.com"
GMAIL_APP_PASSWORD = "lkwemxsyxgzjtige"

EMAIL_TARGETS = {
    "work": {
        "address": "bella@ozkiz.com",
        "label": "OZKIZ 업무",
    },
    "personal": {
        "address": "kndli.210@gmail.com",
        "label": "개인 프로젝트",
    },
}

WHATSAPP_NUMBER = "+821097805690"


def send_email(file_path, target_key):
    """Gmail SMTP로 파일 이메일 발송"""
    target = EMAIL_TARGETS[target_key]
    file_name = os.path.basename(file_path)
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    msg = MIMEMultipart()
    msg["From"] = GMAIL_USER
    msg["To"] = target["address"]
    msg["Subject"] = f"[Claude Auto] {file_name} ({now})"

    body = f"""안녕하세요!

Claude Code에서 자동 발송된 파일입니다.

파일명: {file_name}
발송 시간: {now}
대상: {target['label']}
PC 경로: {os.path.abspath(file_path)}

---
Sent by Claude Auto Mail
"""
    msg.attach(MIMEText(body, "plain", "utf-8"))

    with open(file_path, "rb") as f:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(f.read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", f"attachment; filename={file_name}")
        msg.attach(part)

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(GMAIL_USER, GMAIL_APP_PASSWORD)
        server.send_message(msg)
        server.quit()
        print(f"  [EMAIL] {target['label']} ({target['address']}) -> 발송 완료!")
        return True
    except Exception as e:
        print(f"  [EMAIL] 발송 실패: {e}")
        return False


def send_via_whatsapp(file_path):
    """OpenClaw을 통해 WhatsApp으로 알림 전송"""
    file_name = os.path.basename(file_path)
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    message = f"[Claude Auto] 파일 완성!\n\n파일: {file_name}\n시간: {now}\nPC 경로: {os.path.abspath(file_path)}\n\n이메일로도 발송되었습니다."

    try:
        result = subprocess.run(
            ["wsl", "-e", "bash", "-c",
             f"source ~/.bashrc && npx openclaw message send --target '{WHATSAPP_NUMBER}' --message '{message}'"],
            capture_output=True, text=True, timeout=30
        )
        if result.returncode == 0:
            print(f"  [WHATSAPP] {WHATSAPP_NUMBER} -> 알림 발송 완료!")
            return True
        else:
            print(f"  [WHATSAPP] 발송 실패: {result.stderr}")
            return False
    except Exception as e:
        print(f"  [WHATSAPP] 발송 실패: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(description="Claude Code 파일 자동 발송")
    parser.add_argument("--file", required=True, help="발송할 파일 경로")
    parser.add_argument("--to", required=True,
                        choices=["work", "personal", "both", "whatsapp", "all"],
                        help="발송 대상: work/personal/both/whatsapp/all")
    parser.add_argument("--subject", default=None, help="이메일 제목 (선택)")
    args = parser.parse_args()

    if not os.path.exists(args.file):
        print(f"파일을 찾을 수 없습니다: {args.file}")
        return

    file_name = os.path.basename(args.file)
    file_size = os.path.getsize(args.file)
    print(f"\n{'='*50}")
    print(f"  Claude Auto Deliver")
    print(f"  파일: {file_name} ({file_size:,} bytes)")
    print(f"  대상: {args.to}")
    print(f"{'='*50}\n")

    results = []

    if args.to in ["work", "both", "all"]:
        results.append(("업무 이메일", send_email(args.file, "work")))

    if args.to in ["personal", "both", "all"]:
        results.append(("개인 이메일", send_email(args.file, "personal")))

    if args.to in ["whatsapp", "all"]:
        results.append(("WhatsApp", send_via_whatsapp(args.file)))

    print(f"\n{'='*50}")
    print(f"  발송 결과:")
    for name, success in results:
        status = "성공" if success else "실패"
        print(f"    {name}: {status}")
    print(f"{'='*50}\n")


if __name__ == "__main__":
    main()
