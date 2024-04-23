import requests
class getWeather():
    params={'q':'Indianapolis','units':'imperial'}

    #initialize the array
    def __init__(self):
        self.array={'min':0,'max':0}
        self.weathercode=[]
        self.abnormal=[]
    #grabs the weather data from the open weather api **future implementation** add feature to add own city by ID?
    def getreq(self):

#        print(self.params)
        r=requests.get("https://api.weather.gov",params=self.params)
        if(r.status_code!=requests.codes.ok):
            print(r.status_code)
            print("something went wrong")
        else:
            s=r.json()
            for period in s['properties']['periods']:
                print(period['detailedForecast'])
            return s 
    #takes the weather and parses he next weather for the next day grabbing the minimun and maximum tempurature
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
                self.abnormal.extend(x['description'])

    def createtext(self):
        text='tommorrow\'s weather has a low of '
        text=text+str(self.array['min'])+ ' degrees and a high of '
        text=text+str(self.array['max'])+ ' degrees with '
        if not self.abnormal:
            text=text+'no abnormal weather going on throughout the day'
        else:
            ab=''.join(self.abnormal)
            text=text+'abnormal weather such as '+ab
        return(text)
