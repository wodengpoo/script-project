# -*- coding: utf-8 -*-
import mimetypes
import mysmtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header

#global value
def sendMessage(reciever="azfzg0995@naver.com", content="testing..." , busCD="1"):
    host = "smtp.naver.com"  # naver STMP 서버 주소.
    port = "587"

    senderAddr = "azfzg0995@naver.com"  # 보내는 사람 email 주소.
    recipientAddr = reciever  # 받는 사람 email 주소.

    msg = MIMEMultipart()
    msg['Subject'] = "버스 정보 알림 도착!"
    msg['From'] = senderAddr
    msg['To'] = recipientAddr

    # MIME 문서를 생성합니다.
    text = MIMEText(content, _charset='UTF-8')

    # 만들었던 mime을 MIMEBase에 첨부 시킨다.
    msg.attach(text)

    # 메일을 발송한다.
    s = mysmtplib.MySMTP(host, port)
    #s.set_debuglevel(1)        # 디버깅이 필요할 경우 주석을 푼다.
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login("azfzg0995@naver.com", "nukk8945")
    s.sendmail(senderAddr, [recipientAddr], msg.as_string())
    s.close()








































