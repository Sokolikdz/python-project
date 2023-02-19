class Phone:
    def __init__(self, number, model, weight):
        self.number = number
        self.model = model
        self.weight = weight

    def info(self):
        return f'Номер: {self.number}\n'\
               f'Модель: {self.model}\n'\
               f'Вага: {self.weight}'

    def receiveCall(self, name):
        return f'Телефонує {name}'

    def getNumber(self):
        return self.number

    def sendMsg(self,text, *number):
        return f'Повідомлення з текстом:\n'\
               f'"{text}" \n'\
               f'відправлено на номери: {number}'

user = Phone(80979259576, 'Xiaomi', 150)
print('~~'*15)
print(user.info())
print('~~'*15)
print(user.receiveCall('Сергій'))
print(user.getNumber())
print('~~'*15)
print(user.sendMsg('Треба вчити Пайтон', 80979259576, 80968347141))
print('~~'*15)

