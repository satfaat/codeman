movies_table = [
    ['Побег из Шоушенка', 'США', 1994, 'драма', 142, 9.111],
    ['Крёстный отец', 'США', 1972, 'драма, криминал', 175, 8.730]
]

movies_table_sorted = sorted(movies_table, key=lambda row: row[5])

print(movies_table_sorted)


def filter_by_timing(data, target_duration=140): # target_duration — параметр со значением по умолчанию
    res = []
    for row in data:
        if row[4] > target_duration:
            res.append(row)
    return res 


def print_movie_table(data):
    for movie in data:
        for elem in movie:
            print(f'{elem:<45}', end='')
        print()


movies_table = [
    ['Побег из Шоушенка', 'США', 1994, 'драма', 142, 9.111],
    ['Крёстный отец', 'США', 1972, 'драма, криминал', 175, 8.730],
    ['Тёмный рыцарь', 'США', 2008, 'фантастика, боевик, триллер', 152, 8.499],
    ['Список Шиндлера', 'США', 1993, 'драма', 195, 8.818],
    ['Властелин колец: Возвращение Короля', 'Новая Зеландия', 2003, 'фэнтези, приключения, драма', 201, 8.625],
    ['Криминальное чтиво', 'США', 1994, 'триллер, комедия, криминал', 154, 8.619],
    ['Хороший, плохой, злой', 'Италия', 1966, 'вестерн', 178, 8.521],
    ['Бойцовский клуб', 'США', 1999, 'триллер, драма, криминал', 139, 8.644],
    ['Харакири', 'Япония', 1962, 'драма, боевик, история', 133, 8.106],
    ['Сталкер', 'СССР', 1979, 'фантастика, драма, детектив', 163, 8.083],
    ['Иди и смотри', 'СССР', 1985, 'драма, военный', 136, 8.094]
]

movies_table_filtered = filter_by_timing(movies_table, 170)
print_movie_table(movies_table_filtered)

def get_minutes_and_seconds(time_string):
    time_list = time_string.split(':')
    m = int(time_list[0])
    s = int(time_list[1])
    return m, s


def check_song_duration(time_string):
    minutes, seconds = get_minutes_and_seconds(time_string)
    seconds = minutes * 60 + seconds
    return seconds <= 210


tracks = ['2:25', '2:35', '3:45', '2:00', '5:10']

#напишите ваш код здесь
for track in tracks:
    print(check_song_duration(track))

def replace_wrong_values(wrong_values, correct_value): # на вход функции подаются список неправильных значений и строка с правильным значением
    for wrong_value in wrong_values: # перебираем неправильные имена
        tennis['name'] = tennis['name'].replace(wrong_value, correct_value) # и для каждого неправильного имени вызываем метод replace()

duplicates = ['Roger Fderer', 'Roger Fdrer', 'Roger Federer'] # список неправильных имён
name = 'Роджер Федерер' # правильное имя
replace_wrong_values(duplicates, name) # вызов функции, replace() внутри будет вызван 3 раза
print(tennis) # датафрейм изменился, неявные дубликаты устранены 