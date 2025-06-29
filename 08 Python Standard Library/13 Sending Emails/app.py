from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib
from pathlib import Path

message = MIMEMultipart()
message["from"] = "Mosh Hamedani"
message["to"] = "test@yopmail.com"
message["subject"] = "This is a test"
message.attach(MIMEText("Body"))
message.attach(MIMEImage(Path("jeetu.png").read_bytes()))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("jeetukumar.jk367@gmail.com", "12345678")
    smtp.send_message(message)
    print("Sent....")
