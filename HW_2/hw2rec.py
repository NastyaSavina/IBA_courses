a=int (input("введите длину прямоугольника:\n"))
b=int (input("введите ширину прямоугольника:\n"))
#a = 9
#b = 7
s = a * b


def rec(a, b):
    if b==0 or a==0:
        return []

    else:
        if a > b:
            count = int(a / b)
            print("длина ребер получаемых квадратов: " + str(b))
            print("количество квадратов: " + str(count))
            c = rec(a - b * count, b)
            c.append({'count': count, 'side': b})
            return c
        if b > a:
            count = int(b / a)
            print("длина ребер получаемых квадратов: " + str(a))
            print("количество квадратов: " + str(count))
            c = rec(a, b - a * count)
            c.append({'count': count, 'side': a})
            return c

k = rec(a, b)
print(k)


