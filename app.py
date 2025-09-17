#API klici(spletni klici)

import requests 
import pprint #lepše izpiše rezultate


baseUrl = "https://www.google.com/"
#klic = requests.get(baseUrl)

#print(klic) #koda odgovora
#print(klic.text) #raw odgovor - t

#API klic z JASON odgovorom
baseUrl = "https://api.chucknorris.io/jokes/random"
klic = requests.get(baseUrl)
#preverimo .text, da je 100% JSON
js = klic.json() #pretvorimo v dict
#pprint.pprint(js)
print(js.get("value"))