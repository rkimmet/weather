import SendEmail,weather

def main():
        data=open('keys.txt','r').readlines()
        data=open('keys.txt','r').readlines()
        sdata=[]
        for x in data:
            sdata.append(x.rstrip('\n'))
#        print(sdata)
        weathr=weather.getWeather()
        forcast=weathr.getreq()
        weathr.getcode()
        text=weathr.createtext()
        password=sdata[0]
        eserver=SendEmail.SendEmail(text,password,sdata[1])
#        print('ok')
        #eserver.sendmsg()

main()
