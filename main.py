import os
from flask import Flask, render_template, request
app = Flask(__name__)
API_KEY = os.getenv('e462fdff526172f9ea5dc84f8cf5870f') 
API_URL = os.getenv('http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&appid={}')
import requests
def query_api(city):
        print(API_URL.format(city, API_KEY))
        data = requests.get(API_URL.format(city, API_KEY)).json()
        return data
@app.route('/')
def index():
    city= "Dubai"
    resp = query_api(city)
    print(resp)
    temp=resp['main']['temp']
    country=resp['sys']['country']
    weather=resp['weather'][0]['description']
    iconcode = resp['weather'][0]['icon']
    humidity=resp['main']['humidity']
    feels_like=resp['main']['feels_like']
    return render_template('index.html', city=city, temp=temp,country=country,weather=weather,
                           iconcode=iconcode,humidity= humidity,feels_like=feels_like)

if '__main__' == __name__:
    app.run()
    




