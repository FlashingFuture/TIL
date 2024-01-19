import requests
import pprint

api_key = 'cd17dbaa9b5f2cd5fd9bf8b427dd08ea'
#location of seoul
lat = 37.56
lon = 126.97

url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}'
data = requests.get(url).json()
pprint.pprint(data['weather'][0]['description'])

# 추가 공부 과제
# data.get()과 data['']의 차이점??
