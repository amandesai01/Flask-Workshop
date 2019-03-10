from flask import Flask, render_template, request, jsonify
from flask_simple_geoip import SimpleGeoIP
import requests

app = Flask(__name__)
app.debug = True

@app.route('/')
def location():
    data = requests.get('https://geoipify.whoisxmlapi.com/api/v1?apiKey=at_tO6ReNldmeViKxs7xF6Vo8bwgU1tG&ipAddress=').json()
    city = data['location']['city']

    req = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+ city +'&units=celsius&appid=271d1234d3f497eed5b1d80a07b3fcd1').json()
    description = req['weather'][0]['description'].upper()
    temperature = req['main']['temp'] - 273.15
    temperature = round(temperature,1)
    icon = req['weather'][0]['icon']
    icon = 'https://openweathermap.org/img/w/'+ icon +'.png'
    return render_template('location.html', city = city, description = description, temperature = temperature, icon = icon)

if __name__ == '__main__':
    app.run()
