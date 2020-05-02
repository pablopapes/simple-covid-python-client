import requests
import json


resp = requests.get('https://corona.lmao.ninja/v2/countries/ARG')
resp_json = resp.json()
print('...........ARGENTINA................')
print('Casos: ' + str(resp_json['cases']))
print('Muertes: ' + str(resp_json['deaths']))
print('Curados: ' + str(resp_json['recovered']))
print('#QuedateEnCasa')