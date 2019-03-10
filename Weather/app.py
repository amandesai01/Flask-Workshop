import requests
from flask import Flask, render_template, request
app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
        if request.method == 'GET':
                city = request.args.get('city')
        if city == None or city == '':
                city = 'Mumbai'

        req = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+ city +'&units=celsius&appid=271d1234d3f497eed5b1d80a07b3fcd1').json()
        print(req)

        description = req['weather'][0]['description'].upper()
        temperature = req['main']['temp'] - 273.15
        temperature = round(temperature,1)
        #temperature = (temperature - 32)*5/9
        icon = req['weather'][0]['icon']
        icon = 'https://openweathermap.org/img/w/'+ icon +'.png'

        return render_template('index.html', city = city, description = description, temperature = temperature, icon = icon)
if __name__ == '__main__':
   app.run()