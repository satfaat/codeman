import datetime as dt


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        '''To record data from calculator.'''
        self.records.append(record)

    def get_today_stats(self):
        '''How much money/calories spent today.'''
        spent = 0
        today = dt.date.today()
        for record in self.records:
            if today == record.date:
                spent += record.amount
        return spent

    def get_week_stats(self):
        '''How much money/calories spent for a week.'''
        spent_in_week = 0
        week_ago = dt.date.today() - dt.timedelta(days=6)
        today = dt.date.today()
        for record in self.records:
            if week_ago <= record.date <= today:
                spent_in_week += record.amount
        return spent_in_week


class Record:
    def __init__(self, amount, comment, date=None):
        self.amount = amount  # will keep calories or money
        self.comment = comment
        if date is None:
            self.date = dt.date.today()
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        calories = self.limit - self.get_today_stats()
        if calories > 0:
            return f'Сегодня можно съесть что-нибудь ещё,'\
                f' но с общей калорийностью не более {calories} кКал'
        else:
            return 'Хватит есть!'


class CashCalculator(Calculator):
    EXCHANGE_RATES = {'rub': [1, 'руб'], 'usd': [60.00, 'USD'],
                      'eur': [70.00, 'Euro']}
    USD_RATE = float(60)
    EURO_RATE = float(70)

    def get_today_cash_remained(self, currency):
        '''To see how much calories/ money I can spent today'''
        default_remained = self.limit - self.get_today_stats()
        cash_remained = round(default_remained /
                              self.EXCHANGE_RATES[currency][0], 2)
        currency_name = self.EXCHANGE_RATES[currency][1]
        if cash_remained > 0:
            return f'На сегодня осталось {cash_remained} {currency_name}'
        elif cash_remained < 0:
            return f'Денег нет, держись: твой долг -'\
                   f' {-cash_remained} {currency_name}'
        else:
            return 'Денег нет, держись'

if __name__ == '__main__':
    # для CashCalculator.
    r1 = Record(amount=145, comment='Безудержный шопинг', date='08.03.2019')
    r2 = Record(amount=1568, comment='Наполнение потребительской корзины',
                date='09.03.2019')
    r3 = Record(amount=691, comment='Катание на такси', date='08.03.2019')

    # для CaloriesCalculator.
    r4 = Record(amount=1186, comment='Кусок тортика. И ещё один.',
                date='24.02.2019')
    r5 = Record(amount=84, comment='Йогурт.', date='23.02.2019')
    r6 = Record(amount=1140, comment='Баночка чипсов.', date='24.02.2019')

    # создадим калькулятор денег с дневным лимитом 1000.
    cash_calculator = CashCalculator(1000)

    # дата в параметрах не указана,
    # по умолчанию к записи должна автоматически добавиться сегодняшняя дата.
    cash_calculator.add_record(Record(amount=145, comment='кофе'))

    # и к этой записи тоже дата должна добавиться автоматически.
    cash_calculator.add_record(Record(amount=300, comment='Серёге за обед'))

    # with date.
    cash_calculator.add_record(Record(amount=3000, comment='бар в Танин др',
                                      date='08.11.2019'))

    print(cash_calculator.get_today_cash_remained('rub'))
    # должно напечататься
    # На сегодня осталось 555 руб
