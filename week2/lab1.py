# Считать отдельными операторами целочисленные ширину и высоту прямоугольника. 
# Создать функцию (def), принимающую в качестве параметров ширину и высоту фигуры 
# и название функции, которую необходимо выполнить. 
# Имя вложенной функции передавать явным образом (например: (a,b,name='perim')).
# Внутри функции создать две вложенные функции (def) по подсчету площади и периметра фигуры. 
# Вывести одной строкой через пробел площадь и периметр, разделенные пробелом (например, '20 18').

def calculator(width, height, name):
    def calculatePerimeter(width, height):
        return (width + height) * 2

    def calculateArea(width, height):
        return width * height

    if name == 'perimeter':
        return calculatePerimeter(width, height)
    if name == 'area':
        return calculateArea(width, height)

a = int(input())
b = int(input())

print(calculator(a, b, 'area'), calculator(a, b, 'perimeter'))