from dotenv import load_dotenv
import yagmail
import os

load_dotenv()
def send_email(to, subject , body):
    "Sends an email ONLY to an email address like user@gmail.com. Do NOT use this for Slack. Example: send_email('user@gmail.com', 'Subject', 'Body')"
    try:
        if isinstance(body, list):
            body = "\n\n".join([f"{r['agent']}: {r['result']}" for r in body])
        
        yag = yagmail.SMTP(os.getenv("EMAIL"), os.getenv("EMAIL_PASS"))
        yag.send(to = to , subject = subject, contents = body)
        return f"> Email sent to {to}"
    except Exception as e :
        print(f"> Failed to send email : {e}")

