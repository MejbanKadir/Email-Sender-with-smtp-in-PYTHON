import smtplib
from email.mime.text import MIMETex
SMTP_SERVER = "smtp.outlook.com"#add you email provider instead of "outlook"
#All Capital = Constant
SMTP_PORT = 587
USERNAME = "yourEmail@outlook.com"
PASSWORD = "password"

SUBJECT = "Hello from SMH"
BODY = "This is a test email from SMH"
RECIPIENT = "email@example.com"

# text message
msg = MIMEText(BODY)
msg['Subject'] ="Hello from SMH"
msg['From'] = USERNAME
msg['To'] = RECIPIENT
# Connect to server
server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
server.starttls()
server.login(USERNAME, PASSWORD)
# Send email
server.sendmail(USERNAME, RECIPIENT, msg.as_string())
server.quit()
