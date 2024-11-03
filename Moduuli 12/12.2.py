import json
import requests

print("Syötä haluamasi kaupungin nimi niin kerron tämän maan sään.")
kaupunki = input(str("Anna paikkakunnan nimi: "))

api_key = "cab44e382b48cc9d1997ed2fe65d1226"
lat = 0
lon = 0
pyynto1 = f"https://api.openweathermap.org/geo/1.0/direct?q={kaupunki}&limit=1&appid={api_key}"
try:
    vastaus = requests.get(pyynto1)
    if vastaus.status_code==200:
        json_vastaus = vastaus.json()
        lat = json_vastaus[0]["lat"]
        lon = json_vastaus[0]["lon"]
except requests.exceptions.RequestException as e:
    print ("Hakua ei voitu suorittaa.")

pyynto2 = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"

try:
    vastaus = requests.get(pyynto2)
    if vastaus.status_code==200:
        json_vastaus = vastaus.json()
        kuvaus = json_vastaus["weather"][0]["description"]
        saa = json_vastaus["main"]["temp"]-273.15
        print(f"Sään kuvaus: {kuvaus}")
        print(f"Lämpotila: {saa:.2f} celsiusastetta")
except requests.exceptions.RequestException as e:
    print ("Hakua ei voitu suorittaa.")
