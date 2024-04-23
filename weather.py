import requests
class getWeather():
    params={'User-Agent':'littleproless@gmail.com'}

    def getreq(self):
        
#        print(self.params)
        r=requests.get("https://api.weather.gov/points/39.8650,-86.1419")
        if(r.status_code!=requests.codes.ok):
            print(r.status_code)
            print("something went wrong")
        else:
            s=r.json()
            forecastRequest=s['properties']['forecast']
            forecast =requests.get(forecastRequest)
            detailedforcast=forecast.json()
            return detailedforcast['properties']['periods'][1]