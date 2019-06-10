import requests
import datetime
class getWeather():
    params={'id':5188843,'appid':'1906cf72b3ad7716e9954c02b39eac6d','units':'imperial'}
    def __init__(self):
        self.array={'min':0,'max':0}
    def getreq(self):
        r=requests.get("https://api.openweathermap.org/data/2.5/forecast",params=self.params)
        if(r.status_code!=requests.codes.ok):
            print(r.status_code)
            print("something went wrong")
        else:
            s=r.json()
            Name=s['city']['name']
            today=s['list']
            print(today[1])
            return today
    def parseweather(self,weather):
        day=datetime.datetime.today()
        for part in weather:
            print(int(part['dt_txt'][8:10]))
            if int(part['dt_txt'][5:7])==day.month:
                if int(part['dt_txt'][8:10])==day.day:
                    continue
                elif int(part['dt_txt'][8:10])-day.day==1:
                    #print(part['main']['temp'])
                    self.array['min']=getWeather._getWeather__mintemp(round(part['main']['temp']),self.array['min'])
                    self.array['max']=getWeather._getWeather__maxtemp(round(part['main']['temp']),self.array['max'])

                else:
                    break
            else:
                if int(part['dt_txt'][8:10]) ==1:
                    self.array['min']=getWeather._getWeather__mintemp(round(part['main']['temp_min']),self.array['min'])
                    self.array['max']=getWeather._getWeather__maxtemp(round(part['main']['temp_max']),self.parray['max'])
                else:
                    break
    @staticmethod
    def __maxtemp(forc,maxtempe):
        if ((forc>maxtempe)or(maxtempe==0)):
            return forc
        else:
            return maxtempe
    @staticmethod
    def __mintemp(forc,mintempe):
        print(forc)
        if ((forc<mintempe) or (mintempe==0)):
            return forc
        else:
            return mintempe
    def weath(self,weather):
        for part in weather:
            print(int(part['dt_txt'][8:10]))
            if int(part['dt_txt'][5:7])==day.month:
                if int(part['dt_txt'][8:10])==day.day:
                    continue
                elif int(part['dt_txt'][8:10])-day.day==1:
                    x=1
weather=getWeather()
forcast=weather.getreq()
weather.parseweather(forcast)
