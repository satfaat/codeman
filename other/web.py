import urllib.parse


strings = [
    'что такое backend',
    'Привет!',
    ' ',  # просто пробел
    'letiště',  # аэропорт по-чешски
    'München',  # крупнейший город Баварии
    'Champs-Élysées',  # Елисейские поля
    '東京',  # а это Токио, столица Японии  :)
]

for s in strings:
    encoded = urllib.parse.quote(s)  # зашифрованная строка
    decoded = urllib.parse.unquote(encoded)  # расшифрованная обратно строка
    print(decoded, '-', encoded)

import urllib.parse

url = 'https://yandex.ru/search/?text=%D0%BA%D0%B0%D0%BA%20%D0%B1%D0%B5%D1%81%D0%BF%D0%BB%D0%B0%D1%82%D0%BD%D0%BE%20%D0%B5%D0%B7%D0%B4%D0%B8%D1%82%D1%8C%20%D0%BD%D0%B0%20%D1%82%D0%B0%D0%BA%D1%81%D0%B8'

# чтобы вычленить текст вопроса
# разбейте строку по знаку =, и возьмите
# второй элемент получившегося списка 
q_list = url.split('=')

question = q_list[1] # сохраните его в переменной question
# напечатайте на экран запрос в расшифрованном виде

print(urllib.parse.unquote(question))  # ваш код здесь


import requests

response = requests.get('https://ya.ru/white')

print(response.text)  # печатаем текст запрошенной страницы



url = 'http://wttr.in/?0T'

response = requests.get(url)  # выполните HTTP-запрос

print(response.text)  # напечатайте текст HTTP-ответа

import requests

search_parameters = {
    'text': 'что такое backend',
    'lr': 213
}
url = 'https://yandex.ru/search/'
# Функция get() приняла на вход URL и параметры поиска,
# а дальше она знает, что делать
response = requests.get(url, params=search_parameters)

print(response.status_code)
print(response.url)

import requests

parameters = {
    'u': '',
    'T': ''
}
url = 'http://wttr.in'

# параметры передаются через аргумент params
response = requests.get(url, params=parameters)

print(response.text)

import requests

response = requests.get('https://ya.ru/white')

# вот мы узнали, что код ответа 200 и заполучили это число в свой код:
code = response.status_code
print(f'Код ответа = {code}')

# а вот мы и заголовки читаем, и выводим их форматированной строкой
# с примечанием, каким захочется, на любом языке
headers = response.headers
print(f'Тип содержимого: {headers["content-type"]}')
print(f'Время ответа: {headers["date"]}')

import requests

request_headers = {
    'Accept-Language': 'ru'  # попросим материал на русском языке
}

# сходим почитать блоги про IT, строкой передаём URL платформы habr
response = requests.get('https://habr.com', headers=request_headers)

print(response.text)