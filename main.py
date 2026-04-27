import os
import requests
from flask import Flask, render_template, request

app = Flask(__name__)

# Correct way to use getenv: os.getenv('VARIABLE_NAME', 'DEFAULT_VALUE')
API_KEY = os.getenv('WEATHER_API_KEY', 'e462fdff526172f9ea5dc84f8cf5870f') 
API_URL = "http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&appid={}"

def query_api(city):
    # We use the variable names here
    url = API_URL.format(city, API_KEY)
    print(f"Querying: {url}")
    response = requests.get(url)
    return response.json()

@app.route('/')
def index():
    city = "Dubai"
    resp = query_api(city)
    
    # It's good to check if the API actually returned data
    if resp.get('cod') != 200:
        return f"Error: {resp.get('message', 'Could not connect to API')}"

    temp = resp['main']['temp']
    country = resp['sys']['country']
    weather = resp['weather'][0]['description']
    iconcode = resp['weather'][0]['icon']
    humidity = resp['main']['humidity']
    feels_like = resp['main']['feels_like']
    
    return render_template('index.html', 
                           city=city, temp=temp, country=country, 
                           weather=weather, iconcode=iconcode, 
                           humidity=humidity, feels_like=feels_like)

if __name__ == '__main__':
    # Render requires the app to listen on 0.0.0.0 and a dynamic port
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    




