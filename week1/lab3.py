# Считать единой строкой без пробелов набор целых чисел (28745623873465386), 
# удалить все дубликаты, вывести отдельными операторами вывода в порядке возрастания 
# и в порядке убывания в виде кортежей целых чисел (2, 3, 4, 5, 6, 7, 8) и (8, 7, 6, 5, 4, 3, 2).

inputStr = str(input())

inputStr = "".join(sorted(inputStr))

result = (int(inputStr[0]),)
for i in range(1, len(inputStr)):
    if (inputStr[i-1] != inputStr[i]):
        result = result + (int(inputStr[i]),)

print(result)
print(result[::-1])