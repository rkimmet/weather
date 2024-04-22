import requests
import datetime
class getWeather():
    params={'q':'Indianapolis','units':'imperial'}

    #initialize the array
    def __init__(self,appid):
        self.array={'min':0,'max':0}
        self.params['appid']=appid
        self.weathercode=[]
        self.abnormal=[]
    #grabs the weather data from the NWS
    def getreq(self):
#        print(self.params)
        r=requests.get("https://api.weather.gov",params=self.params)
        if(r.status_code!=requests.codes.ok):
            print(r.status_code)
            print("something went wrong")
        else:
            s=r.json()
            Name=s['city']['name']
            today=s['list']
#           print(today[1])
            return today
    #takes the weather and parses he next weather for the next day grabbing the minimun and maximum tempurature
    def parseweather(self,weather):
        day=datetime.datetime.today()
        for part in weather:
#            print((part))
            if int(part['dt_txt'][5:7])==day.month:
                if int(part['dt_txt'][8:10])==day.day:
                    continue
                elif int(part['dt_txt'][8:10])-day.day==1:
                    #print(part['main']['temp'])
                    self.array['min']=getWeather._getWeather__mintemp(round(part['main']['temp']),self.array['min'])
                    self.array['max']=getWeather._getWeather__maxtemp(round(part['main']['temp']),self.array['max'])
                    self.weathercode.extend(part['weather'])
                else:
                    break
            else:
                if int(part['dt_txt'][8:10]) ==1:
                    self.array['min']=getWeather._getWeather__mintemp(round(part['main']['temp_min']),self.array['min'])
                    self.array['max']=getWeather._getWeather__maxtemp(round(part['main']['temp_max']),self.parray['max'])
                    self.weathercode.extend(part['weather'])
                else:
                    break

    @staticmethod
    def __maxtemp(forc,maxtempe):
        if ((forc>maxtempe)or(maxtempe==0)):
            return forc
        else:
            return maxtempe

    #grabs the min temp
    @staticmethod
    def __mintemp(forc,mintempe):
        #print(forc)
        if ((forc<mintempe) or (mintempe==0)):
            return forc
        else:
            return mintempe
    def getcode(self):
        for x in self.weathercode:
            if x['id']<800:
                if x['description'] not in self.abnormal:
                    print(self.abnormal)
                    self.abnormal.append(x['description'])

    def createtext(self):
        text='Tommorrow\'s weather has a low of '
        text=text+str(self.array['min'])+ ' degrees and a high of '
        text=text+str(self.array['max'])+ ' degrees with '
        if not self.abnormal:
            text=text+'no abnormal weather going on throughout the day'
        else:
            ab=''.join(self.abnormal)
            text=text+'abnormal weather such as '+ab
        return(text)
