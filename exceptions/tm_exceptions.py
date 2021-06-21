try:
    a = float(input('Enter a number: '))
except ValueError:
    print("You entered an invalid number")

try:
    a = Fraction(input('Enter a fraction: '))
except ZeroDivisionError:
    print('Invalid fraction')


try:
    # Здесь написан код.
    # Это код может содержать ошибки времени выполнения.
    # Разработчики говорят, что код может "выбросить" исключение.
except TypeError1:
    # Здесь описываем, что следует делать,
    # если будет "выброшено" исключение типа TypeError1.
except TypeError2:
      # А здесь разработчики говорят, как быть, если мы
    # "ловим" или "перехватываем" исключения типа TypeError2.



# вот функция, которая может выбросить исключение
def calc_share(apples, friends):
    # от строки откусываем число и приводим к типу int
    friends_number = int(friends.split()[0])
    return apples / friends_number

# есть 17 яблок
apples = 17

# будем считать, сколько достанется каждому другу
# вызовем функцию calc_share() для разных наших знакомых,
# с различным числом друзей
for friends in ['7 друзей', '2 друга', '0 друзей', 'один враг']:
    try:
        print('Каждому достанется по', calc_share(apples, friends), 'яблока')
    except ZeroDivisionError:
        print('На ноль делить нельзя.')
    except ValueError:
        print(f'Из строки "{friends}" не получилось достать число.')


import requests

cities = [
    'Омск',
    'Калининград',
    'Челябинск',
    'Владивосток',
    'Красноярск',
    'Москва',
    'Екатеринбург'
]


def make_url(city):
    # в URL задаём город, в котором узнаем погоду
    return f'http://wttr.in/{city}'


def make_parameters():
    params = {
        'format': 2,  # погода одной строкой
        'M': ''  # скорость ветра в "м/с"
    }
    return params


def what_weather(city):
    # Напишите тело этой функции.
    # Не изменяйте остальной код!
    
    try:
        response = requests.get(make_url(city), params=make_parameters())
        if response.status_code == 200:
            return response.text
        else:
            print('<ошибка на сервере погоды>')
    except requests.ConnectionError:
        return '<сетевая ошибка>'

print('Погода в городах:')
for city in cities:
    print(city, what_weather(city))