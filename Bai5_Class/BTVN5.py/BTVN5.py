class Book:
    def __init__(self,title, author):
        self.title = title
        self.author = author
        self._is_borrowed = False
        self.history = []

    def dercribe(self):
        return f"{self.title} - {self.author}"

    @property
    def is_borrowed(self):
        return self._is_borrowed

    def borrow(self):
        if(self._is_borrowed == False): 
            self._is_borrowed = True
            self.history.append("borrow")
            return True
        return False

    def return_book(self):
        if(self._is_borrowed):
            self._is_borrowed = False
            self.history.append("return")
            return True
        return False

     
a = Book("Python co ban", "Linh")
b = Book("Git thuc hanh","Ha")
print(a.dercribe())
print(b.dercribe())

print(a.borrow())
print(a.is_borrowed)
print(a.borrow())

print(a.borrow())
print(a.borrow())
print(b.is_borrowed)
print(a.return_book())
print(a.is_borrowed)
print(a.return_book())

print("\n Lich su thao tac: ")
print("Sach a: ",a.history)
print("Sach b: ", b.history)


        