import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from dotenv import load_dotenv
from llm import generate_email_content
from datetime import datetime


#Load environment variables from .env file
load_dotenv()

# Set up email details from environment variables
sender_email = os.getenv("SENDER_EMAIL")
password = os.getenv("EMAIL_PASSWORD")
smtp_server = "smtp.gmail.com"
smtp_port = 587

def send_email(recipient_email, subject, body, attachment_path=None):
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, recipient_email, msg.as_string())
        print(f"Email sent to {recipient_email}")

    except Exception as e:
        print(f"Failed to send email to {recipient_email}: {e}")


if __name__ == "__main__":
    recipient = "conradkrantz@gmail.com"
    subject = f"AI Newsletter - {datetime.now().strftime('%Y-%m-%d')}"
    body = generate_email_content("the importance of AI in modern business")
    send_email(recipient, subject, body)