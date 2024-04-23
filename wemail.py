import emaill,weatheronecall

def main():
        data=open('keys.txt','r').readlines()
        sdata=[]
        for x in data:
            sdata.append(x.rstrip('\n'))
#        print(sdata)
#sdata 0 is the weather token, sdata 1 is password, sdata 2 email to send to
        weathr=weatheronecall.getWeather(sdata[0])
        weathr.getreq()
        text=weathr.createtext()
        password=sdata[0]
        eserver=SendEmail.SendEmail(text,password,sdata[1])
#        print('ok')
        #eserver.sendmsg()
main()
