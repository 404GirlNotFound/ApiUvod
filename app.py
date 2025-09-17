#API klici(spletni klici)

import requests 
import pprint #lepše izpiše rezultate


baseUrl = "https://www.google.com/"
#klic = requests.get(baseUrl)

#print(klic) #koda odgovora
#print(klic.text) #raw odgovor - t
"""
#API klic z JASON odgovorom
baseUrl = "https://api.chucknorris.io/jokes/random"
for i in range(10):
    klic = requests.get(baseUrl)
    #preverimo .text, da je 100% JSON
    js = klic.json() #pretvorimo v dict
    #pprint.pprint(js)
    print(js.get("value"))
"""

baseUrl = "https://api.nationalize.io/?name="
ime="luka"

klic= requests.get(baseUrl+ime).json()
#print(klic.url)
#print(klic)

print(f"{klic.get("count")}")
print(f"{klic.get("name")}")

drzave=klic.get("country")
for d in drzave:
    print(d.get("country_id"))
    print(d.get("probability"))
#popravite izpise, da bo lepši in v %