# Создайте класс, осуществляющий подсчет и изменение числа книг. 
# Названия книг, их количество считываются одной строкой вида 'Boogeyman 66 Battleground 50', число книг - произвольное.
# В классе должен быть реализован конструктор, деструктор, методы просмотра числа, взятия и возвращения книг.
# Реализовать вывод начальных значений, взятие по 1 книге, возвращение по 1 книге с выводом текущего числа после вызова каждого из методов, меняющих значение книг.
# Типичный ответ одной строкой: 'Boogeyman 66 65 66 Battleground 50 49 50'.

class BookCounter(object):
    def __init__(self, name, number):
        self.name = name
        self.number = number

    # def __del__(self):
    #     print (' ')

    def get_name(self):
        return self.name

    def get_number(self):
        return self.number

    def increment_number(self):
        self.number = self.number + 1
        return self.number
    
    def decrement_number(self):
        if (self.number > 0):
            self.number = self.number - 1
        return self.number


books = str.split(input())
result = ''

for i in range(int(len(books)/2)):
    newBook = BookCounter(books[i*2], int(books[i*2+1]))
    result += newBook.get_name() + ' ' + str(newBook.get_number()) + ' ' + str(newBook.decrement_number()) + ' ' + str(newBook.increment_number()) + ' '

print(result)