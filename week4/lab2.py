# Считать одной строкой произвольное количество пар элементов "Название книги Число экземпляров", 
# второй строкой название алгоритма хеширования md5
# Aibolit 66 Barmaley 67
# md5

# Создать 2 класса:
# 1-й преобразует строку вида 'Aibolit 66 Babmaley 67', где название книги уникально, в словарь.
# 2-й осуществляет хеширования названия книги алгоритмом md5.
# Вывести отдельными операторами вывода:
# - элементы словаря, отсортированные по возрастанию ключа, например:
# Aibolit 66
# Barmaley 67
# - результаты хеширования в виде пар названия алгоритма и результатов хеширования ключей, отсортированных по возрастанию, 
# представленных в шестнадцатеричном виде, сведенных в одну строку через пробел вида
# md5 c47.... md5 5d....' (без пробелов в начале и конце строки).

import hashlib

class Dictionary: 
    def __init__(self, input_str = ''):
        self.dict = {}

        books = str.split(input_str)
        for i in range(int(len(books)/2)):
            self.dict.update({books[i*2]: int(books[i*2+1])})

    def sort_dict(self):
        return sorted(self.dict)

    def print_dict(self):
        for i in self.sort_dict():
            print(i, self.dict[i])

    def __iter__(self):
        return iter(self.dict)

    def __getitem__(self, index):
        return self.dict[index]

    def __del__(self):
        del self.dict

class EncodeDictionary:
    def __init__(self, dictionary = {}, encode_method = ''):
        self.initial_dict = dictionary
        self.encode_method = encode_method
        self.encoded_dict = self.__encode_dict(dictionary)

    def __encode_dict(self, initial_dict):
        result_dict = {}
        for i in sorted(initial_dict): 
            result_dict.update({self.__encode(i): initial_dict[i]})
        return result_dict

    def __encode(self, key):
        type = self.encode_method
        if (type == 'md5'):
            return hashlib.md5(key.encode()).hexdigest()
        if (type == 'sha1'):
            return hashlib.sha1(key.encode()).hexdigest()
        if (type == 'sha224'):
            return hashlib.sha224(key.encode()).hexdigest()
        if (type == 'sha256'):
            return hashlib.sha256(key.encode()).hexdigest()
        if (type == 'sha384'):
            return hashlib.sha384(key.encode()).hexdigest()
        if (type == 'sha512'):
            return hashlib.sha512(key.encode()).hexdigest()

    def print_encode_dictionary(self):
        result = ''
        for i in self.encoded_dict:
            result += self.encode_method + ' ' + i + ' '
        print(result.rstrip())

    def __del__(self):
        del self.initial_dict
        del self.encoded_dict


input_str_books = str(input())
input_str_encode = str(input())

new_dict = Dictionary(input_str_books)
new_dict.print_dict()

new_encoded_dict = EncodeDictionary(new_dict, input_str_encode)
new_encoded_dict.print_encode_dictionary()