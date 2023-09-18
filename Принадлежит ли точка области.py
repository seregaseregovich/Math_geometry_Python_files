# Принадлежит ли точка области (смотри задачу №3795)


def CycIn(x, y, r=1, xo=0, yo=0):
    return r ** 2 >= ((x - xo) ** 2) + ((y - yo) ** 2)


def CycOut(x, y, r=1, xo=0, yo=0):
    return r ** 2 <= ((x - xo) ** 2) + ((y - yo) ** 2)


def LP(x, y, a=1, b=0):
    return b >= y - a * x


def LM(x, y, a=1, b=0):
    return b <= y - a * x


x = -2
y = 2
print((LM(x, y, -1, 0) and LM(x, y, 2, 2) and
       CycIn(x, y, 2, -1, 1)) or (LP(x, y, -1, 0)
        and LP(x, y, 2, 2) and CycOut(x, y, 2, -1, 1)))
