# Треугольник паскаля
#  
#             1
#           1   1
#         1   2   1
#       1   3   3   1
#     1   4   6   4   1
#
# Каждое нижнее число является результатом суммы 
# двух близлежащих чисел в верхнем ряду.


# ВАРИАНТ 1:
# ======================


n = int(input("Введите уровень треугольника Паскаля: ")) - 1
triangle = [] # Создание пустого списка
for i in range(0, n+1):
    triangle.append([1]+[0]*(n)) # Создание матрицы размером n*n с заполнением
    # первых слева ячеек единицами, а остальных ячеек - нулями
for i in range(1, n+1):
    for j in range(1, i+1): 
        triangle[i][j] = triangle[i-1][j] + triangle[i-1][j-1] # Заполнение списка
        # содержимым - суммирование двух соседних верхних ячеек с занесением
        # результата в нижние ячейки
print("Печать матрицы-таблицы результата вычислений:")
for i in triangle:
    print(i)

    
# Получаем результат в виде матрицы такого вида (размер зависит от степени):
# [1, 0, 0, 0, 0]
# [1, 1, 0, 0, 0]
# [1, 2, 1, 0, 0]
# [1, 3, 3, 1, 0]
# [1, 4, 6, 4, 1]

# Еще вариант (почти такой же):
# m = int(input('Enter number: '))
# n = []
# for i in range(m):
#     n.append([1] + [0] * (m - 1))
# for i in range(1, m):  # (1.2.3.4)
#     for j in range(1, m):  # (1.2.3.4)
#         n[i][j] = n[i-1][j-1] + n[i-1][j]
# for i in n:
#     print(i)


    
# ГДЕ МОЖНО ПРИМЕНИТЬ:
# ======================
# В решении задач типа: (a + b)**n, где n - степень.
# Например - возведение суммы чисел (а + в) во вторую степень производится так:
# (a+b)**2 = 1 * (a**2*b**0) + 2 * (a**1*b**1) + 1 * (a**0*b**2)
# .,  где:  ---               ---               --- - числа из треугольника Паскаля
# Пример ниже - возведение в третью степень:
# (a+b)**3 = 1 * (a**3*b**0) + 3 * (a**2*b**1) + 3 * (a**1*b**2) + 1 * (a**0*b**3)
#           ---               ---               ---               ---    - числа 
# .. и так далее.


# Функция для вычисления произведения типа (a**n) * (b**m) ниже.
# (a+b)**2 = 1 * (a**2*b**0) + 2 * (a**1*b**1) + 1 * (a**0*b**2)
#                ----=----=-       ----=----=-       ----=----=-
# где в каждом произведении (см.подчеркнутое выше) степень n 
# меняется от n до нуля, а м - наоборот, от нуля до степени n - 
# - в зависимости от величины этой степени.


def fP():
    x = (a**(n-i)) * (b**(n-(n-i)))
    return x


# Основной модуль программы:


a = int(input("Введите число A: "))
b = int(input("Введите число В: "))
s = 0
for i in range(0, n+1):
    s = s + (fP()) * triangle[n][i] # Вычисление результата по формуле
print(s)

# ГОТОВО! ======================================================================




# ВАРИАНТ 2.1:
# ====================== (Программа для графического вывода на печать) 

def pascal_triangle(n):
    r = [1]
    y = [0]
    for x in range(max(n, 0)):  # не пойму, зачем здесь max(n, 0)
        print(x)
        print(r) # Результат - вывод на печать
        r = [left + right for left, right in zip(r + y, y + r)]
# В строке выше производится создание списка r, который
# является поэлементным сложением двух списков:
# списка (r + y) (который создается сложением
# списков r = [1] и y = [0], результат == [1, 0]),
# и списка (y + r) (который создается сложением
# списков y = [0] и r = [1], результат == [0, 1])).
# Результат поэлементного сложения этих списков в генераторе
# списков == [1, 1].
# Во втором цикле (r + y) = [1, 1, 0], а (y + r) = [0, 1, 1].
# Результат поэлементного сложения этих списков == [1, 2, 1].
# ... и так далее.

pascal_triangle(5)


# ВАРИАНТ 2.2:
# ====== То же самое, что выше, но выводит список res

def Pascal_Triangle(n):
    r = [1]
    y = [0]
    x = []
    for i in range(n):
        nn = r[:]
        if len(nn) < n:
            nn = nn[:] + [0] * (n - 1 - len(nn))
            print(nn)
            x = x[:] + [nn[:]]
        r = [ll + rr for ll, rr in zip(r + y, y + r)]
    return x


res = Pascal_Triangle(6)
print(res)



##from timeit import default_timer as timer
##start = timer()


##end = timer()
##print("Control time taken:", end-start)

