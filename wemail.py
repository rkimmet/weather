import emaill,weather

def main():
        data=open('keys','r').readlines()
        sdata=[]
        for x in data:
            sdata.append(x.rstrip('\n'))
#        print(sdata)
        weathr=weather.getWeather(sdata[0])
        forcast=weathr.getreq()
        weathr.parseweather(forcast)
        weathr.getcode()
        text=weathr.createtext()
        password=sdata[1]
        eserver=emaill.emaill(text,password,sdata[2])
#        print('ok')
        eserver.sendmsg()

main()
