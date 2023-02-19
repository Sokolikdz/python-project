class Robots:
    popularity = 0                                                 # Атрибут класу, яка отримує кількість роботів
    def __init__(self, name):
        self.name = name                                           # При створенні робота, робот добавляється
        Robots.popularity += 1                                     # до атрибуту population

    def info_name(self):                                           # Виводимо ім'я робота
        print(f'(Ініціалізація {self.name})')

    def sayHi(self):                                               # Виводимо вітання робота
        print(f'Вітаю! Мої господарі називають мене {self.name}')

    @classmethod                                                   # За допомогою classmethod виводимо
    def howRobots(cls):                                            # кількість роботів (оновлюємо значення)
        print(f'У нас {Robots.popularity} роботів')

class BotCoins:                                                    # Клас коінів. Задаємо початкове значення
    def __init__(self, startcoins = 100):                          # коіну, і далі до початкового
        self.__startcoins = startcoins                             # значення додаємо задане значення коіну

    def __call__(self, coins = 0):
        return self.__startcoins + coins

print('~~'*21)
robot1 = Robots('R2-D2')
robot1.info_name()
robot1.sayHi()
robot1.howRobots()
robotCoins = BotCoins()
print(f'У робота {robotCoins()} коінів.')

print('~~'*21)
robot2 = Robots('C-3PO')
robot2.info_name()
robot2.sayHi()
robot2.howRobots()
robotCoins = BotCoins()
print(f'У робота {robotCoins(50)} коінів.')
print('~~'*21)













