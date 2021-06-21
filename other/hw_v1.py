import datetime as dt

class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record): #Сохранять новую запись о расходах
        self.records.append(record)

    def get_today_stats(self): # Считать, сколько денег потрачено сегодня
        spent = 0
        today = dt.date.today()
        for index in range(len(self.records)):
            if today == self.records[index].date:
                spent += self.records[index].amount
        return spent
    
    def get_week_stats(self): # Считать, сколько денег потрачено за последние 7 дней
        spent_in_week = 0
        one_day = dt.timedelta(days=1)
        today = dt.date.today()
        days = 7
        while days > 0:
            for index in range(len(self.records)):
                if today == self.records[index].date:
                    spent_in_week += self.records[index].amount
            today = today - one_day
            days -= 1
        return spent_in_week

class Record:
    def __init__(self, amount, comment, date = None):
        self.amount = amount # денежная сумма или количество килокалорий
        self.comment = comment
        if date is None:
            self.date = dt.date.today()
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()

class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        calories = self.limit - self.get_today_stats()
        if calories > 0:
            return f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {calories} кКал'
        else:
            return 'Хватит есть!'

class CashCalculator(Calculator):
    USD_RATE = float(60)
    EURO_RATE = float(70)

    def get_today_cash_remained(self, currency): # Определять, сколько ещё денег можно потратить сегодня в рублях, долларах или евро
        result = self.limit - self.get_today_stats()
        if result > 0:
            if currency == 'usd':
                result = round(result / self.USD_RATE, 2)
                return f'На сегодня осталось {result} USD'
            elif currency == 'eur':
                result = round(result / self.EURO_RATE, 2)
                return f'На сегодня осталось {result} Euro'
            else:
                return f'На сегодня осталось {result} руб'
        elif result == 0:
            return 'Денег нет, держись'
        else:
            if currency == 'usd':
                result = round(abs(result) / self.USD_RATE, 2)
                return f'Денег нет, держись: твой долг - {result} USD'
            elif currency == 'eur':
                result = round(abs(result) / self.EURO_RATE, 2)
                return f'Денег нет, держись: твой долг - {result} Euro'
            else:
                result = abs(result)
                return f'Денег нет, держись: твой долг - {result} руб'


# для CashCalculator 
r1 = Record(amount=145, comment='Безудержный шопинг', date='08.03.2019')
r2 = Record(amount=1568, comment='Наполнение потребительской корзины', date='09.03.2019')
r3 = Record(amount=691, comment='Катание на такси', date='08.03.2019')

# для CaloriesCalculator
r4 = Record(amount=1186, comment='Кусок тортика. И ещё один.', date='24.02.2019')
r5 = Record(amount=84, comment='Йогурт.', date='23.02.2019')
r6 = Record(amount=1140, comment='Баночка чипсов.', date='24.02.2019')

# создадим калькулятор денег с дневным лимитом 1000
cash_calculator = CashCalculator(1000)

# дата в параметрах не указана, 
# так что по умолчанию к записи должна автоматически добавиться сегодняшняя дата
cash_calculator.add_record(Record(amount=145, comment='кофе'))

# и к этой записи тоже дата должна добавиться автоматически
cash_calculator.add_record(Record(amount=300, comment='Серёге за обед'))

# а тут пользователь указал дату, сохраняем её
cash_calculator.add_record(Record(amount=3000, comment='бар в Танин др', date='08.11.2019'))
                
print(cash_calculator.get_today_cash_remained('rub'))
# должно напечататься
# На сегодня осталось 555 руб