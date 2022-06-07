from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendEmail(fromAddr, toAddr, msg):
    import smtplib
    s = smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()

    emailmsg = MIMEMultipart('alternative')
    emailmsg['Subject'] = '요구하신 정보를 보내드립니다'
    emailmsg['From'] = fromAddr
    emailmsg['To'] = toAddr

    sendingStr = ' '
    for item in msg:
        sendingStr += item
        sendingStr += '\n'

    HtmlPart = MIMEText(sendingStr)
    emailmsg.attach(HtmlPart)

    #앱 패스워드
    s.login('manutd1st@gmail.com', 'tsatnapylgzmoztr')
    s.sendmail(fromAddr,[toAddr],emailmsg.as_string())
    s.close()

