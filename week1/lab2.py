# Считать несколько имен людей одной строкой, записанных латиницей, через пробел, например:
# «Anna Maria Peter».
# Вывести их одной строкой в порядке возрастания «Anna Maria Peter».
# Вывести их одной строкой в порядке убывания «Peter Maria Anna».

inputStr = str(input())

arr = inputStr.split()

arr.sort()
output = " ".join(str(name) for name in arr)
print(output)

arr.reverse()
output = " ".join(str(name) for name in arr)
print(output)