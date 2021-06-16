'''Создать csv файл с данными о ежедневной погоде. Структура: Дата,
Место, Градусы, Скорость ветра. Найти среднюю погоду(скорость ветра и
градусы) для Минск за последние 7 дней.'''

import requests
import json
import csv
response = requests.get("https://api.openweathermap.org/data/2.5/forecast?q=Minsk&cnt=5&appid=ad9850d93aa3036db2fd25c4d3bc30af")
#todos = json.loads(response.text)
#print(todos)
with open('whether.json', 'w+') as f:
    json.dump(response.text, f)
with open('whether.json') as am:
    print(json.loads(am.read()))