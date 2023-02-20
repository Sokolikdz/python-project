class Greeting:
    def __init__(self, name = 'Віталій Ігорович'):
        self.name = name

    def info_name(self):
        print(f'{self.name}!')

    def sayHi(self):
        print(f'Вітаю! Сподіваюся що цього разу файл коректно заапдейтеться:)')

print('~~'*30)
robot1 = Greeting()
robot1.info_name()
robot1.sayHi()
print('~~'*30)















