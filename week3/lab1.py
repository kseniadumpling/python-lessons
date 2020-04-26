# Ввести с клавиатуры строку латиницей (1-3 слова). Зашифровать ее с использованием гарантированных алгоритмов шифрования. 
# Сформировать словарь, где в качестве ключа используется название гарантированного алгоритма шифрования, 
# а в качестве значения - результат шифрования в шестнадцатеричном представлении { 'sha1': 'd0b…', 'md5', '1f3…',…}.
# Итог вывести отдельными операторами вывода в виде пар ключа и значения, отсортированных по возрастанию ключа

# Пример входных данных:
# apple

# Пример выходных данных:
# md5 1f3870be274f6c49b3e31a0c6728957f
# sha1 d0be2dc421be4fcd0172e5afceea3970e2f3d940
# sha224 b7bbfdf1a1012999b3c466fdeb906a629caa5e3e022428d1eb702281
# sha256 3a7bd3e2360a3d29eea436fcfb7e44c735d117c42d1c1835420b6b9942dd4f1b
# sha384 3d8786fcb588c93348756c6429717dc6c374a14f7029362281a3b21dc10250ddf0d0578052749822eb08bc0dc1e68b0f
# sha512 844d8779103b94c18f4aa4cc0c3b4474058580a991fba85d3ca698a0bc9e52c5940feb7a65a3a290e17e6b23ee943ecc4f73e7490327245b4fe5d5efb590feb2

import hashlib

input_str = input()

encoded_dict = {}

encoded_dict['md5'] = hashlib.md5(input_str.encode()).hexdigest()
encoded_dict['sha1'] = hashlib.sha1(input_str.encode()).hexdigest()
encoded_dict['sha224'] = hashlib.sha224(input_str.encode()).hexdigest()
encoded_dict['sha256'] = hashlib.sha256(input_str.encode()).hexdigest()
encoded_dict['sha384'] = hashlib.sha384(input_str.encode()).hexdigest()
encoded_dict['sha512'] = hashlib.sha512(input_str.encode()).hexdigest()

for i in sorted(encoded_dict):
    print(i, encoded_dict[i])