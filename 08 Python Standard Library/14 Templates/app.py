from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib
from pathlib import Path
from string import Template

template = Template(Path('template.html').read_text())


message = MIMEMultipart()
message["from"] = "Mosh Hamedani"
message["to"] = "test@yopmail.com"
message["subject"] = "This is a test"
# body = template.substitute({"name": "Jeetu"})
# alternative of above step instead of passing dictionary we can pass keyword arguments
body = template.substitute(name="Jeetu")
message.attach(MIMEText(body, "plain"))
message.attach(MIMEImage(Path("jeetu.png").read_bytes()))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("jeetukumar.jk367@gmail.com", "12345678")
    smtp.send_message(message)
    print("Sent....")
