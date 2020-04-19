# Считать отдельными операторами целочисленные ширину и высоту прямоугольника, 
# создать функцию (def), принимающую в качестве параметров ширину и высоту фигуры.
# Внутри функции создать две вложенные функции (lambda) по подсчету площади и периметра фигуры. 
# Вывести одной строкой через пробел площадь и периметр, разделенные пробелом (например '20 18').

def printAreaAndPerimeter(width, height):
    getPerimeter = lambda a, b: (a + b) * 2
    getArea = lambda a, b: a * b

    print(getArea(width, height), getPerimeter(width, height))

a = int(input())
b = int(input())

printAreaAndPerimeter(a, b)