import requests
import json
key = '887aaff89bee4fd742287bfd4afa2483'
city = 'New York'
response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}')
ატრიბუტები = {'q': city, 'appid': key, 'units':'metric'}
response = requests.get('https://api.openweathermap.org/data/2.5/weather', params=ატრიბუტები)
print(response)
print('response.status_code')
print(response.headers)
print(response.text)
j_son = response.json()
print(json.dumps(j_son, indent=10))
print('მინიმალური ტემპერატურა', j_son['main'] ['temp_min'])

with open('weather.json', 'w') as file:
    json.dump(j_son, file, indent=4)


j_son = json.loads(response.text)
with open('weather.json', 'r') as file:
    j_son = json.load(file)
    print(j_son)