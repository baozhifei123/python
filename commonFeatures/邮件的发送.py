# 点击设置-》开启pop3/smtp服务；获取授权码
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr


def send_email():
    msg = MIMEText("武傻子，爹给你发邮件了", "html", "utf-8")
    msg["From"] = formataddr(["暴志飞", "13283553732@163.com"])
    msg["Subject"] = "邮件主题"

    server = smtplib.SMTP_SSL("smtp.163.com")
    server.login("13283553732@163.com", "PIIJUQMXKEFXLSEK")
    server.sendmail("13283553732@163.com", "1792409365@qq.com", msg.as_string())
    server.quit()


send_email()
