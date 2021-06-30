'''Создать csv файл с данными о ежедневной погоде. Структура: Дата,
Место, Градусы, Скорость ветра. Найти среднюю погоду(скорость ветра и
градусы) для Минск за последние 7 дней.'''

import requests
import json

response = requests.get("https://api.openweathermap.org/data/2.5/forecast?q=Minsk&cnt=40&units=metric&appid=ad9850d93aa3036db2fd25c4d3bc30af")
m, n = 0, 0
with open('whether.json', 'w+') as f:
    json.dump(response.text, f)
    slov = json.loads(response.text)
    for i in slov['list']:
        m += i['main']['temp']
        n += i['wind']['speed']
    print("Средняя скорость ветра =", n / 40, ', а средняя температура =', m / 40)



