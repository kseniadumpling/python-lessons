# Считать отдельными операторами целочисленные ширину и высоту прямоугольника, 
# создать список из лямбда функций подсчета площади и периметра фигуры.
# Вывести первым оператором индекс лямбда функции подсчета площади и ее результат (например:0 20);
# вторым оператором индекс лямбда функции подсчета периметра и ее результат (например:1 18);
# вывести третьим оператором список полученным значений (например: [20, 18]);
# вывести четвертым оператором итоговые значения, сведенные в одну строк через пробел (например: '20 18').

# just my humble opinion: this task is bullshit

width = int(input())
height = int(input())

lambdaList = [lambda a, b: a * b, lambda a, b: (a + b) * 2]

getAreaIndex = 0
getPerimeterIndex = 1

print(getAreaIndex, lambdaList[getAreaIndex](width, height))
print(getPerimeterIndex, lambdaList[getPerimeterIndex](width, height))

result = [lambdaList[getAreaIndex](width, height), lambdaList[getPerimeterIndex](width, height)]
print(result)
print(result[0], result[1])

