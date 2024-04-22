import emaill,weatheronecall

def main():
        data=open('keys','r').readlines()
        sdata=[]
        for x in data:
            sdata.append(x.rstrip('\n'))
#        print(sdata)
#sdata 0 is the weather token, sdata 1 is password, sdata 2 email to send to
        weathr=weatheronecall.getWeather(sdata[0])
        weathr.getreq()
        text=weathr.createtext()
        password=sdata[1]
        eserver=emaill.emaill(text,password,sdata[2])
#        print('ok')
        eserver.sendmsg()

main()
