from random import random

class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def to_string(self):
        return f'x: {self.__x} y: {self.__y}'

    def change_x(self):
        self.__x = random() * 10

    def change_y(self):
        self.__y = random() * 10

class Triangle:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.p1 = Point(x1, y1)
        self.p2 = Point(x2, y2)
        self.p3 = Point(x3, y3)

    def print_triangle(self):
        print(f'p1: {self.p1.to_string()}')
        print(f'p2: {self.p2.to_string()}')
        print(f'p3: {self.p3.to_string()}')

    def get_perimeter(self):
        self.side1 = ((self.p1.get_x() - self.p3.get_x()) ** 2 + (self.p1.get_y() - self.p3.get_y()) ** 2) ** 1 / 2
        self.side2 = ((self.p2.get_x() - self.p1.get_x()) ** 2 + (self.p2.get_y() - self.p1.get_y()) ** 2) ** 1 / 2
        self.side3 = ((self.p3.get_x() - self.p2.get_x()) ** 2 + (self.p3.get_y() - self.p2.get_y()) ** 2) ** 1 / 2

        self.p = self.side1 + self.side2 + self.side3
        return self.p

    def get_form(self):
        self.side1 = ((self.p1.get_x() - self.p3.get_x()) ** 2 + (self.p1.get_y() - self.p3.get_y()) ** 2) ** 1 / 2
        self.side2 = ((self.p2.get_x() - self.p1.get_x()) ** 2 + (self.p2.get_y() - self.p1.get_y()) ** 2) ** 1 / 2
        self.side3 = ((self.p3.get_x() - self.p2.get_x()) ** 2 + (self.p3.get_y() - self.p2.get_y()) ** 2) ** 1 / 2
        if self.side1 == self.side2 and self.side1 == self.side3 and self.side2 == self.side3:
            return "равносторонний"
        if self.side1 == self.side2 or self.side1 == self.side3 or self.side2 == self.side3:
            return "равнобедренный"
        else:
            return "произвольный"

    def change_p1(self):
        self.p1.change_x()
        self.p1.change_y()

    def change_p2(self):
        self.p2.change_x()
        self.p2.change_y()

    def change_p3(self):
        self.p3.change_x()
        self.p3.change_y()

    def print_coordinates(self):
        return f'p1_x: {self.p1.get_x()} p1_y: {self.p1.get_y()} p2_x:{self.p2.get_x()} p2_y: {self.p2.get_y()} p3_x: {self.p3.get_x()} p3_y: {self.p3.get_y()}'
def main():
    count_ravn = 0
    count_ravnb = 0
    count_proizv = 0

    RS = []
    RB = []
    PR = []
    T = []

    triangle1 = Triangle(x1=0, y1=0, x2=2, y2=0, x3=1, y3=1)
    triangle2 = Triangle(x1=2, y1=5, x2=6, y2=7, x3=4, y3=0)
    triangle3 = Triangle(x1=7, y1=0, x2=6, y2=2, x3=7, y3=3)
    triangle4 = Triangle(x1=1, y1=9, x2=3, y2=8, x3=3, y3=10)
    triangle5 = Triangle(x1=8, y1=4, x2=12, y2=4, x3=10, y3=7)
    triangle6 = Triangle(x1=6, y1=5, x2=1, y2=7, x3=4, y3=0)

    print(f'координаты точек : {triangle1.print_coordinates()}')

    triangle1.change_p1()
    triangle1.change_p2()
    triangle1.change_p3()

    print(f'координаты точек : {triangle1.print_coordinates()}')

    T.append(triangle1)
    T.append(triangle2)
    T.append(triangle3)
    T.append(triangle4)
    T.append(triangle5)
    T.append(triangle6)

    for triangle in T:
        if triangle.get_form() == "равносторонний":
            count_ravn += 1
            RS.append({'объект': triangle, 'периметр': triangle.get_perimeter()})
        if triangle.get_form() == "произвольный":
            count_proizv += 1
            PR.append({'объект': triangle, 'периметр': triangle.get_perimeter()})
        if triangle.get_form() == "равнобедренный":
            count_ravnb += 1
            RB.append({'объект': triangle, 'периметр': triangle.get_perimeter()})

    print(f'вид треугольника 1: {triangle1.get_form()}' "\n" f'периметр: {triangle1.get_perimeter()}'"\n")
    print(f'вид треугольника 2: {triangle2.get_form()}' "\n" f'периметр: {triangle2.get_perimeter()}'"\n")
    print(f'вид треугольника 3: {triangle3.get_form()}' "\n" f'периметр: {triangle3.get_perimeter()}'"\n")
    print(f'вид треугольника 4: {triangle4.get_form()}' "\n" f'периметр: {triangle4.get_perimeter()}'"\n")
    print(f'вид треугольника 5: {triangle5.get_form()}' "\n" f'периметр: {triangle5.get_perimeter()}'"\n")
    print(f'вид треугольника 6: {triangle6.get_form()}' "\n" f'периметр: {triangle6.get_perimeter()}'"\n")

    print(f'количество равносторонних треугольников: {count_ravn}')
    print(f'количество равнобедренных треугольников: {count_ravnb}')
    print(f'количество произвольных треугольников: {count_proizv}')


    def vstavka_RB(RB):
        for i in range(1, len(RB)):
            t = RB[i]
            j = i
            while j > 0 and RB[j - 1]['периметр'] > t['периметр']:
                RB[j]['периметр'] = RB[j - 1]['периметр']
                j -= 1
            RB[j] = t

    vstavka_RB(RB)
    if len(RB) != 0:
        print('Самый большой равнобедренный треугольник:')
        print(RB[-1]['объект'].print_coordinates())
        print(RB[-1]['периметр'])
    else:
        print("нет равнобедренных треугольников")

    def vstavka_PR(PR):
        for i in range(1, len(PR)):
            t = PR[i]['периметр']
            j = i
            while j > 0 and PR[j - 1]['периметр'] > t:
                PR[j]['периметр'] = PR[j - 1]['периметр']
                j -= 1
            PR[j]['периметр'] = t

    vstavka_PR(PR)
    if len(PR) != 0:
        print('Самый большой произвольный треугольник:')
        print(PR[-1]['объект'].print_coordinates())
        print(PR[-1]['периметр'])
    else:
        print("нет произвольных треугольников")

    def vstavka_RS(RS):
        for i in range(1, len(RS)):
            t = RS[i]['периметр']
            j = i
            while j > 0 and RS[j - 1]['периметр'] > t:
                RS[j]['периметр'] = RS[j - 1]['периметр']
                j -= 1
            RS[j]['периметр'] = t

    vstavka_RS(RS)
    if len(RS) != 0:
        print('Самый большой равносторонний треугольник:')
        print(RS[-1]['объект'].print_coordinates())
        print(RS[-1]['периметр'])
    else:
        print("нет равносторонних треугольников")

if __name__ == "__main__":
    main()
