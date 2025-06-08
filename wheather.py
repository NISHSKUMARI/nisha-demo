import requests
import json
import win32com.client as wincom
city=input("enter the name of the city\n")
url=f"https://api.weatherapi.com/v1/current.json?key=255ddd924e26444c9b6175853242111&q={city}"
r = requests.get(url)
#print(r.text)
#print(type(r.text))
wdic = json.loads(r.text)
w=wdic["current"]["temp_c"]
speak = wincom.Dispatch("SAPI.SpVoice")
text = (f"say'the current weather in {city} is {w} degree'")
speak.Speak(text)
