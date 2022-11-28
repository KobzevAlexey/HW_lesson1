# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

print('Введите координаты первой точки через пробел: ')
point_1 = [float(i) for i in input().split()]

print('Введите координаты второй точки: ')
point_2 = [float(i) for i in input().split()]

distance = ((point_2[0] - point_1[0]) ** 2 + (point_2[1] - point_1[1]) ** 2) ** (0.5)
print('Расстояние между точками равно: ''%.3f' % distance)
