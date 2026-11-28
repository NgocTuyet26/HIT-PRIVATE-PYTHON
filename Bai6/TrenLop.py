# BAI2
class User:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"Toi la {self.name}"

class Student(User):
    def __init__(self, name,id):
        super().__init__(name)
        self.id = id
    def introduce(self):
        return super().introduce() + ", ID: " + f"{self.id}"
    
sv1 = Student("PANh", 111)
sv2 = Student ("Tuyet",222)
print(sv1.introduce())
print(sv2.introduce())

# BAI3
class Notification:
    def send(self, message):
        return f"Notice: {message}"

class EmailNotification(Notification):
    def send(self, message):
        return f"Email: {message}"

class AppNotification(Notification):
    def send(self, message):
        return f"App: {message}"

def notify_all(services, message):
    for service in services:
        print(service.send(message))

services = [
    EmailNotification(),AppNotification()
]
notify_all(services,"chao ban")

# BAI5
from abc import ABC, abstractmethod
class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass

class IncompleteNotification(Notification):
    def send(self, message):
        return f"InComp: {message}"

class SMSNotification(Notification):
    def send(self, message):
        return f"SMS: {message}"
print(SMSNotification().send("Xin chao"))
print(IncompleteNotification().send("Xin chao"))

# BAI6
class BankAccount:
    def __init__(self, balance=0):
        if balance < 0:
            raise ValueError("So du am")
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def withdraw(self, amount):
        if (amount < 0):
            raise ValueError("So tien phai duong")
        if amount > self._balance:
            return False
        self._balance -= amount
        return True
account = BankAccount(1000000)
print (account.withdraw(300000))
print(account.balance)
print (account.withdraw(800000))
print(account.balance)
print(account.withdraw(70000))
print(account.balance)

# * tuple  phai tu dinh nghia 
# ** dictionary