import requests
import datetime as dt
user_contry_chosie = input("Enter a contry: ")
BASE_URI = 'https://api.openweathermap.org/data/2.5/weather?'
API_KEY = 'be851a28dce34f4238bb7d722f3a341f'
CITY = user_contry_chosie

url = BASE_URI + "appid=" + API_KEY + "&q=" + CITY
res = requests.get(url).json()

def kel_to_cel_fah(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) * 32
    return celsius, fahrenheit

temp_kelvin = res['main']['temp']
temp_celsius, temp_fahrenheit = kel_to_cel_fah(temp_kelvin)

feels_like = res['main']['feels_like']
feels_like_cel, feels_like_fah = kel_to_cel_fah(feels_like)


humidity = res['main']['humidity']
description = res['weather'][0]['description']
wind_speed = res['wind']['speed']

sunrise_time = dt.datetime.utcfromtimestamp( res['sys']['sunrise'] + res['timezone'])
sunset_time = dt.datetime.utcfromtimestamp( res['sys']['sunset'] + res['timezone'])

print(f"The Contry {CITY} Here is details weather about it".capitalize())
print(f"The sunrise is {sunrise_time} and sunset: {sunset_time}")
print(f"The temperature in celsius: {round(temp_celsius)} kelvin: {temp_kelvin} fahrenheit: {round(temp_fahrenheit)} ".capitalize())
print(f"The humidity is: {humidity} the weather descpription: {description}")
print(f"The wind speed is: {wind_speed}")

