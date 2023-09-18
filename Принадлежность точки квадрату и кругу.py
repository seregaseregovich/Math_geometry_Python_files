def IsPointInSquare(x1, y1, x2, y2, x3, y3):
    if x1 > x2:
        x1, x2 = x2, x1
    if y1 > y2:
        y1, y2 = y2, y1
    return x1 <= x3 <= x2 and y1 <= y3 <= y2


print(IsPointInSquare(2, -2, -2, 2, -3, 1))


def IsPointInCircle(r, x, y):
    return r >= (((x ** 2) + (y ** 2)) ** (1 / 2))


print(IsPointInCircle(4, 3, 2))


#  from timeit import default_timer as timer
#  start = timer()


#  end = timer()
#  print("Control time taken:", end-start)
