from django.shortcuts import render
import requests

def index(request):
    city = request.GET.get('city',"London")
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=37b1a5f4df9ba5a136a94ec2c2c792f4'
    data = requests.get(url).json()
    

    payload = {
        'city': data['name'],
        'weather': data['weather'][0]['main'],
        'icon': data['weather'][0]['icon'],    
        'kelvin_temprature':data['main']['temp'],
        'celcius_temprature':int(data['main']['temp'] - 273),
        'pressure':data['main']['pressure'],
        'humidity':data['main']['humidity'],
        'description':data['weather'][0]['description'],
        'wind':data['wind']['speed'],
        'cloud':data['clouds']['all'],
        #'rains':data['rain']['1h']
    }
    context = {'data':payload}
    print(context)
    return render(request,"index.html",context)