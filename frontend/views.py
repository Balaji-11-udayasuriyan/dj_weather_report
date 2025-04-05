# from django.shortcuts import render

import os
from django.shortcuts import render
from dotenv import load_dotenv
import requests
import json

load_dotenv()  # take environment variables

# Access the variables
API_KEY = os.getenv('API_KEY')

def home(request):

    if request.method == 'POST':

        location = request.POST['location']

        print(location)

        url = f"http://api.weatherstack.com/current?access_key={API_KEY}&query=" + location

        weather_request = requests.get(url)
        weather_api = json.loads(weather_request.text)

        print(weather_api)
        return render(request, "frontend/home.html", {'weather_api': weather_api})

    else:

        url = f"http://api.weatherstack.com/current?access_key={API_KEY}&query=New%20York"

        weather_request = requests.get(url)
        weather_api = json.loads(weather_request.text)

        return render(request, "frontend/home.html", {'weather_api': weather_api})