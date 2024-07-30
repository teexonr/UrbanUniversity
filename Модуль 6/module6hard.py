import math


class Figure:
    sides_count = 0

    def __init__(self, *args):
        color, *sides = args
        self.__color = []
        self.__sides = []
        self.set_color(*color)
        self.set_sides(*sides)
        self.filled = bool(self.__color)

    def __is_valid_color(self, r, g, b):
        return all(0 <= c <= 255 for c in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = list((r, g, b))

    def get_color(self):
        return self.__color

    def __is_valid_sides(self, sides):
        return all(s > 0 for s in sides)

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            if self.__is_valid_sides(new_sides):
                self.__sides = list(new_sides)
            else:
                self.__sides = [1 for _ in range(self.sides_count)]

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def __str__(self):
        return f'{self.__dict__}, perimeter: {self.__len__()}'


class Circle(Figure):
    sides_count = 1

    def __init__(self, *args):
        super().__init__(*args)
        self.__radius = round(self.get_sides()[0] / (2 * math.pi), 2)

    def get_square(self):
        return round(2 * math.pi * (self.__radius ** 2), 2)

    def __str__(self):
        return super().__str__() + f', square: {self.get_square()}'


class Triangle(Figure):
    sides_count = 3

    def __init__(self, *args):
        super().__init__(*args)
        self.__height = 'К какой стороне проведена высота?'

    def get_square(self):
        a, b, c = self.get_sides()
        p = self.__len__() / 2
        return round((p * (p - a) * (p - b) * (p - c)) ** 0.5, 2)

    def __str__(self):
        return super().__str__() + f', square: {self.get_square()}'


class Cube(Figure):
    sides_count = 12

    def __init__(self, *args):
        super().__init__(*args)
        _, sides = args
        self.__sides = None
        self.set_sides(sides)

    def set_sides(self, *new_sides):
        if len(new_sides) == 1:
            self.__sides = [new_sides[0] for _ in range(self.sides_count)]

    def get_sides(self):
        return self.__sides

    def get_volume(self):
        return self.__sides[0] ** 3

    def __str__(self):
        return super().__str__() + f', square: {self.get_volume()}'


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
triangle1 = Triangle((100, 200, 100), 3, 4, 5)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
