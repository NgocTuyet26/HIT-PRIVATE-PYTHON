class User:
    def __init__(self, age):
        self.age = age

class Account:
    def __init__(self, name,age):
        super().__init__(age)
        self.name = name
        self.__p = None

    # getter
    @ property
    def p(self): 
        return self.__p

    # setter
    @p.setter
    def p(self,p):
        if p > 0 and p < 100:
            self.__p = p
a = Account("Nam",20)
print(a.p)
a.p = 10
print(a.p)
print(a.age)

    