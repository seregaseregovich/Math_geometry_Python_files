d = "да"
while d == "да":
    while True:
        a = input("Введите 1 сторону треугольника: ")
        try:
            a = int(a)
        except ValueError:
            print("ОШИБКА! Это не целое число, попробуйте снова! ")
        else:
            break
    while True:
        b = input("Введите 2 сторону треугольника: ")
        try:
            b = int(b)
        except ValueError:
            print("ОШИБКА! Это не целое число, попробуйте снова! ")
        else:
            break
    while True:
        c = input("Введите 3 сторону треугольника: ")
        try:
            c = int(c)
        except ValueError:
            print("ОШИБКА! Это не целое число, попробуйте снова! ")
        else:
            break
    if a + b <= c or a + c <= b or b + c <= a:
        print("Введена какая-то херня, попробуйте еще раз!!!")
    elif a == b and a == c and b == c:
        print("Это равносторонний треугольник.")
    elif a / b == 1 or a / c == 1 or b / c == 1:
        print("Это равнобедренный треугольник.")
    elif a * a + b * b == c * c or c * c + b * b == a * a or a * a + c * c == b * b:
        print("Это прямоугольный треугольник.")
    else:
        print("Это обычный треугольник.")
    d = input('Продолжить работу? \n(введите "да" или "нет") ')
    while d != "да" and d != "нет":
        print("Введены неверные данные, повторите ввод данных.")
        d = input('Продолжить проверку? Введите "да" или "нет" ')
if d == "нет":
    print("Ну тогда вали отсюда, \nиди делай свои уроки!!!")
    exit()
