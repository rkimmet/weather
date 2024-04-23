import SendEmail,weather

def main():
        data=open('keys.txt','r').readlines()
        sdata=[]
        for x in data:
            sdata.append(x.rstrip('\n'))
        weathr=weather.getWeather()
        forcast=weathr.getreq()
        text=forcast['name']+'\n'+forcast['detailedForecast']
        print(text)
        password=sdata[0]
        eserver=SendEmail.SendEmail(text,password,sdata[1])
#        print('ok')
        eserver.sendmsg()

main()
