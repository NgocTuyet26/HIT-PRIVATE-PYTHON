# Buổi 06 · Luyện tập OOP II trên lớp

Luyện theo thứ tự trong slide: **đóng gói → kế thừa → ghi đè và đa hình → trừu tượng → vận dụng**. Mỗi bài làm trong một file Python riêng. Các ví dụ thông báo chỉ tạo chuỗi, không gửi email hay SMS thật.

## Chuẩn bị

Tạo thư mục `buoi_06`, mở bằng VS Code và chọn Python trong môi trường `.venv`. Bài học chỉ dùng thư viện có sẵn, không cần cài thêm gói.

- Nếu đã kích hoạt môi trường: `python bai_01_account.py`.
- Windows, chạy trực tiếp bằng môi trường: `.venv\Scripts\python.exe bai_01_account.py`.
- macOS/Linux: `.venv/bin/python bai_01_account.py`.

Đổi tên file trong lệnh để chạy bài tương ứng. Các chỗ `TODO` hoặc `pass` trong khung là phần cần hoàn thành. Thêm lời gọi thử ở cuối mỗi file để nhìn thấy kết quả.

## Bài 1 · Đóng gói: rút tiền theo quy tắc

**Theo mục 1 trong slide. File:** `bai_01_account.py`.

Một tài khoản có số dư ban đầu. Người dùng được đọc số dư qua `balance`; thao tác rút tiền đi qua `withdraw()`.

### Khung ban đầu

```python
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

```

### Việc cần làm

Hoàn thành `withdraw(amount)` theo các quy tắc sau. Giả định `balance` và `amount` đều là số.

1. Nếu `amount <= 0`, báo `ValueError` bằng `raise ValueError("So tien phai duong")`.
2. Nếu số tiền rút lớn hơn số dư, trả `False` và giữ nguyên số dư.
3. Nếu đủ tiền, trừ số dư và trả `True`. Rút đúng số dư vẫn hợp lệ.

### Kết quả đối chiếu

Tạo `account = BankAccount(100000)`, rồi gọi **theo thứ tự**:

| Lời gọi                   | Giá trị trả về | Số dư sau lời gọi |
| ------------------------- | -------------- | ----------------: |
| `account.withdraw(30000)` | `True`         |             70000 |
| `account.withdraw(80000)` | `False`        |             70000 |
| `account.withdraw(70000)` | `True`         |                 0 |

Thử `withdraw(0)` và `withdraw(-1000)` ở các lần chạy riêng, hoặc bắt `ValueError` ở nơi gọi, để lỗi đầu tiên không chặn lần thử sau.

**Suy nghĩ:** Vì sao thêm dấu `_` trước tên biến vẫn chưa đủ để giữ số dư hợp lệ? Nếu gán thẳng `account._balance = -1`, điều gì xảy ra?

## Bài 2 · Kế thừa: mở rộng thông tin người dùng

**Theo mục 2 trong slide. File:** `bai_02_student.py`.

`User` lưu tên. `Student` là một `User` có thêm mã học viên.

### Khung ban đầu

````python
class User:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"Toi la {self.name}"


class Student(User):
    def __init__(self,name,id):
        super().__init__(name)
        self.id = id
sv1 = Student("Lan","SV01")
sv2 = Student("Minh","SV02")
print(sv1.name)
print(sv1.id)
print(sv1.introduce())
print(sv2.name)
print(sv2.id)
print(sv2.introduce())


### Việc cần làm

1. Trong `Student.__init__`, dùng `super().__init__(name)` để khởi tạo tên, rồi lưu `student_id` vào đối tượng.
2. Tạo `Student("Lan", "SV01")`. In tên, mã và kết quả `introduce()`.
3. Tạo thêm `Student("Minh", "SV02")` và kiểm tra hai học viên giữ thông tin riêng. Không cần viết lại `introduce()` trong `Student`.

### Kết quả đối chiếu

```python
s = Student("Lan", "SV01")
print(s.name)         # Lan
print(s.student_id)   # SV01
print(s.introduce())  # Toi la Lan
````

**Suy nghĩ:** Nếu bỏ lời gọi `super().__init__(name)` mà chỉ gán `student_id`, vì sao đọc `s.name` lại lỗi?

**Thử thêm:** Sau khi tạo `s`, chạy `leader = s`, rồi `leader.name = "An"`. Dự đoán `s.name` trước khi in. Phép gán `leader = s` có tạo một học viên mới không?

## Bài 3 · Ghi đè và đa hình: các kênh thông báo

**Theo mục 3 trong slide. File:** `bai_03_notifications.py`.

Các kênh thông báo cùng nhận một nội dung nhưng tạo kết quả khác nhau.

### Khung ban đầu

````python
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
    EmailNotification(), AppNotification(),ConsoleNotification()
]
notify_all(services,"Chao Lan")


### Việc cần làm

1. `EmailNotification.send(message)` **trả** chuỗi có tiền tố `"Email: "`; `AppNotification.send(message)` trả chuỗi có tiền tố `"App: "`.
2. Viết `notify_all(services, message)` duyệt danh sách và gọi `send(message)` của từng đối tượng. Không dùng `if` theo tên lớp để chọn nội dung.
3. Tự viết `ConsoleNotification` có `send(message)` trả chuỗi với tiền tố `"Console: "`. Lớp này **không kế thừa** `Notification`. Thêm object của lớp vào danh sách và giữ nguyên `notify_all()`.

### Kết quả đối chiếu

```python
services = [EmailNotification(), AppNotification()]
notify_all(services, "Chao Lan")
````

```text
Email: Chao Lan
App: Chao Lan
```

Khi thêm `ConsoleNotification()` ở cuối danh sách, chương trình in thêm `Console: Chao Lan`. Với danh sách rỗng, hàm không in dòng nào.

**Suy nghĩ:** Dòng nào thể hiện ghi đè? Dòng nào thể hiện đa hình? Vì sao `ConsoleNotification` vẫn dùng được dù không chung lớp cha?

## Bài 4 · Trừu tượng: lớp nào được tạo object?

**Theo mục 4 trong slide. File:** `bai_04_abstract.py`.

Bài này độc lập với bài 3. Lớp `Notification` dưới đây yêu cầu lớp cụ thể có `send(message)`.

### Khung ban đầu

```python
from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass


class IncompleteNotification(Notification):
    pass


class SMSNotification(Notification):
    def send(self,message):
        return f"SMS: {message}"

sms = SMSNotification()

print(sms.send("Chao Lan"))


### Việc cần làm

1. Giữ nguyên `IncompleteNotification`. Thử tạo `Notification()` và `IncompleteNotification()` ở các lần chạy riêng. Đọc thông báo lỗi để biết method nào còn thiếu.
2. Hoàn thành `SMSNotification.send(message)` để trả chuỗi có tiền tố `"SMS: "`.
3. Tạo một object SMS và gọi `send("Chao Lan")`. Không xóa `@abstractmethod` để làm mất lỗi.

### Kết quả đối chiếu

| Thao tác sau khi làm bài | Kết quả |
|---|---|
| `Notification()` | `TypeError`, còn method abstract |
| `IncompleteNotification()` | `TypeError`, còn thiếu `send` |
| `SMSNotification().send("Chao Lan")` | `"SMS: Chao Lan"` |

**Suy nghĩ:** Lỗi abstract xuất hiện lúc tạo object hay lúc gọi `send()`? ABC giúp phát hiện thiếu sót nào so với lớp cha thông thường ở bài 3?

## Bài 5 · Vận dụng: tính tổng đơn hàng

**Theo mục 5 trong slide. File:** `bai_05_delivery.py`.

Một đơn hàng gồm giá hàng và phí giao. Các công thức dưới đây là dữ liệu minh họa, đơn vị **đồng**; khoảng cách tính bằng **km**. Giả định giá và khoảng cách đã là số hợp lệ, không âm.

### Dữ liệu và khung ban đầu

class StandardDelivery:
    def fee(self, distance):
        return 15000 + 3000 * distance


class ExpressDelivery:
    def fee(self,distance):
        return 2500 + 5000*distance


class Order:
    def __init__(self, price, service):
        self.price = price
        self.service = service

    def total(self, distance):
        return self.price + self.service.fee()

standard = StandardDelivery()
express = ExpressDelivery()

order1 = Order(100000, standard)
order2 = Order(100000, express)

print(order1.total(4))
print(order2.total(4))


### Việc cần làm

1. Viết `ExpressDelivery.fee(distance)` theo công thức `25000 + 5000 * distance`.
2. Hoàn thành `Order.total(distance)`. Gọi `fee()` qua `self.service`, không phân nhánh theo loại dịch vụ.
3. Tạo hai đơn có cùng giá hàng 100000 đồng, cùng khoảng cách 4 km, nhưng dùng hai dịch vụ khác nhau. In tổng tiền của mỗi đơn.

### Kết quả đối chiếu

| Dịch vụ | Khoảng cách | Phí giao | Tổng đơn 100000 đồng |
|---|---:|---:|---:|
| `StandardDelivery()` | 4 | 27000 | 127000 |
| `ExpressDelivery()` | 4 | 45000 | 145000 |
| `StandardDelivery()` | 0 | 15000 | 115000 |

**Suy nghĩ:** Vì sao `Order` giữ một object dịch vụ thay vì kế thừa dịch vụ đó? Nếu thêm `FreeDelivery` có `fee(distance)` luôn trả 0, có cần sửa `Order.total()` không?

## Bài thêm · Minh họa bằng nhân vật game

Nếu đã xong các bài chính, tự viết trong `bai_them_characters.py`:

- `Character(ABC)` nhận `name`, HP ban đầu là số dương; cung cấp property `health` chỉ đọc và method abstract `attack()`.
- `take_damage(amount)` nhận sát thương là số không âm, giảm HP nhưng không thấp hơn 0. HP ban đầu không dương hoặc sát thương âm thì báo `ValueError`.
- `Warrior(name)` dùng `super()` để khởi tạo 120 HP; `attack()` trả `"Tên: dung kiem"`.
- `Mage(name)` khởi tạo 80 HP; `attack()` trả `"Tên: dung phep"`.

Tạo `Warrior("Lan")` và `Mage("Minh")`, cho Lan nhận 200 sát thương rồi in HP của cả hai. **Đối chiếu:** Lan còn 0, Minh vẫn 80. Duyệt hai object và gọi cùng `attack()` để thấy hai chuỗi khác nhau. Trong bài này `attack()` chỉ mô tả hành động, chưa gây sát thương cho đối thủ.

## Chốt lại trên chính bài làm

Chọn một đoạn code để chỉ ra kế thừa, một lời gọi đa hình và một quy tắc cập nhật trạng thái. Giải thích vì sao lớp trừu tượng ở bài 4 chưa thể tạo object khi còn thiếu `send()`.

Giữ các file `.py` đã làm trong `buoi_06/`; không đưa thư mục `.venv/` lên GitHub.
```
