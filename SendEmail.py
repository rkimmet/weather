import ssl, smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
class SendEmail():
    context= ssl.create_default_context()
    def __init__(self,wtext,passw,sender):
        self.text=wtext
        self.password=passw
        self.serverr="weathertomorrrow1@gmail.com"
        self.send=sender
    def sendmsg(self):
        with smtplib.SMTP_SSL("smtp.gmail.com",465) as server:
            server.login(self.serverr,self.password)
            msg=MIMEMultipart()
#            print("ok")
            msg['Subject']='Tomorrow\'s weather'
            msg.attach(MIMEText(self.text,'plain'))
            server.sendmail(self.serverr,self.send,msg.as_string())


