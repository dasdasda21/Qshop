import smtplib
from email.mime.text import MIMEText
subject ="学习邮件"
content ="""
hello world"""
sender = "1194420780@qq.com"
recver = """
2533636371@qq.com"""
password = "smxvabrhvnqajeed"
message = MIMEText(content,"plain","utf-8")
message["Subject"] = subject
message["From"] = sender
message["To"] = recver
smtp = smtplib.SMTP_SSL("smtp.qq.com",465)
smtp.login(sender,password)
smtp.sendmail(sender,recver.split(",\n"),message.as_string())
smtp.close()