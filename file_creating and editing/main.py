import urequests
import utime
import os
import ujson

#response = urequests.get("http://www.randomnumberapi.com/api/v1.0/random?min=100&max=1000&count=5")
response = urequests.get("http://dataservice.accuweather.com/locations/v1/countries/asia?apikey=bIvA4XowQwkDGkkf73Dasb5tgxcA7Oqo")

f = open("testapi.txt", "w")
f.write(response.text)

f = open("testapi.txt")
saveData = f.read()
#print(saveData)
jsonData = ujson.loads(str(saveData))
print(jsonData[0])


