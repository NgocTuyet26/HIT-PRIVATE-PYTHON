from abc import ABC, abstractmethod
import math

class Shape(ABC):
    def __init__(self,size):
        if size <= 0:
            raise ValueError("Kich thuoc phai > 0")
        self.__size = size

    @ abstractmethod
    def area(self):
        pass

    @property
    def size(self):
        return self.__size

class Square(Shape):
    def __init__(self, side):
        super().__init__(side)

    def area(self):
        return self.size **2

    
class Circle(Shape):
    def __init__(self, radius):
        super().__init__(radius)

    def area(self):
        return self.size ** 2 * math.pi


def total_area(shapes):
    tong = 0
    for shape in shapes:
        tong += shape.area()
    return tong


print(Square(3).size)
print("Dien tich hinh vuong:", Square(3).area())
print(f"Dien tich hinh tron: {Circle(2).area():.2f}")

shapes = [Square(3), Circle(2)]
print(f"Tong dien tich: {total_area(shapes):.2f}")
print("Danh sach rong:", total_area([]))
# print(Circle(0).area())




