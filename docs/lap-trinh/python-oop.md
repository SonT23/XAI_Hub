# Python: Lập trình hướng đối tượng (OOP)

> 🖼️ **Tổng hợp từ 3 ảnh ghi chú gốc:**
> 1. 1382_cheat-sheet-python-oop-class-inheritance-polymorph.jpg
>
> 2. 1438_ghi-chu-python-lap-trinh-huong-doi-tuong-oop-co-ba.jpg
>
> 3. 1439_ghi-chu-python-cac-khai-niem-oop-ke-thua-da-hinh.jpg
>

OOP (Object-Oriented Programming – Lập trình hướng đối tượng) là mô hình lập trình mô hình hóa thực thể trong thế giới thực thành **class** và **object**, giúp code tái sử dụng được, dễ bảo trì và dễ mở rộng. OOP dựa trên 4 tính chất chính: **Encapsulation, Inheritance, Polymorphism, Abstraction**.

### Class & Object

**Class** là bản thiết kế (blueprint/template) dùng để tạo ra **object**. Class định nghĩa **attributes** (thuộc tính/dữ liệu) và **methods** (phương thức/hành vi) mà object sẽ có.

**Object** là một thực thể (instance) cụ thể được tạo ra từ class. Mỗi object có state (giá trị thuộc tính) và hành vi riêng của nó — giống như class là bản vẽ, object là vật thật được xây từ bản vẽ đó.

#### Constructor `__init__` và `self`

`__init__` là **constructor** — method đặc biệt được Python tự động gọi khi một object được tạo ra, dùng để khởi tạo thuộc tính cho object. `self` là tham số đầu tiên của mọi method trong class, đại diện cho chính object đang được thao tác, dùng để truy cập attributes/methods của object đó.

```python
class Student:
    school = "ABC School"  # class attribute — dùng chung cho mọi object

    def __init__(self, name, age):
        # instance attribute — riêng cho từng object
        self.name = name
        self.age = age

    def info(self):  # method
        return f"{self.name} is {self.age} years old."


# Tạo object (instance) từ class
s1 = Student("Abhi", 16)
s2 = Student("Riya", 15)

print(s1.school)   # ABC School (class attribute, dùng chung)
print(s1.info())   # Abhi is 16 years old.
print(s2.info())   # Riya is 15 years old.
```

Có hai loại thuộc tính: **Class attribute** (khai báo trực tiếp trong class, dùng chung cho mọi object — ví dụ `school`) và **Instance attribute** (gán qua `self` trong `__init__`, riêng cho từng object — ví dụ `name`, `age`). Truy cập attribute/method của object bằng toán tử dấu chấm (`.`).

---

### Kế thừa (Inheritance)

Inheritance cho phép một **class con (child/subclass)** kế thừa attributes và methods từ **class cha (parent/superclass)**, giúp tái sử dụng code và tổ chức phân cấp hợp lý.

#### Single inheritance & Override method

```python
class Animal:                     # Class cha (Parent)
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Animal speaks")


class Dog(Animal):                 # Dog kế thừa Animal
    def speak(self):                # Ghi đè (override) method của cha
        print("Dog barks")


d = Dog("Buddy")
d.speak()        # Dog barks (dùng method đã override)
print(d.name)    # Buddy (kế thừa attribute từ Animal)
```

Dùng `super()` để gọi lại constructor hoặc method của class cha bên trong class con — hữu ích khi class con muốn mở rộng thêm hành vi thay vì thay thế hoàn toàn:

```python
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)   # gọi __init__ của Animal
        self.color = color

    def speak(self):
        super().speak()          # vẫn chạy "Animal speaks"
        print("Cat meows")


c = Cat("Mimi", "White")
c.speak()
# Animal speaks
# Cat meows
```

#### Multiple inheritance (đa kế thừa)

Python cho phép một class con kế thừa từ **nhiều class cha cùng lúc**:

```python
class Flyable:
    def fly(self):
        print("Flying...")


class Swimmable:
    def swim(self):
        print("Swimming...")


class Duck(Flyable, Swimmable):   # kế thừa cả 2 class cha
    pass


duck = Duck()
duck.fly()    # Flying...
duck.swim()   # Swimming...
```

---

### Tính đa hình & Đóng gói

#### Polymorphism (Tính đa hình)

Polymorphism nghĩa là "nhiều hình dạng" — cùng một tên method nhưng hành vi thực thi khác nhau tùy theo object gọi nó. Có 2 loại: **Compile-time (Method Overloading)** — Python không hỗ trợ trực tiếp, và **Run-time (Method Overriding)** — được hỗ trợ (như ví dụ `Dog`/`Cat` override `speak()` ở trên).

```python
class Shape:
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, w, h):
        self.w, self.h = w, h

    def area(self):
        return self.w * self.h


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r


def print_area(shape):     # cùng 1 hàm dùng cho nhiều loại object
    print("Area:", shape.area())


print_area(Rectangle(4, 5))  # Area: 20
print_area(Circle(3))        # Area: 28.26
```

#### Encapsulation (Tính đóng gói)

Encapsulation là quá trình gói dữ liệu (biến) và code (method) lại thành một đơn vị (class), đồng thời hạn chế truy cập trực tiếp vào một số thành phần của object để bảo vệ dữ liệu. Python quy ước mức truy cập bằng dấu gạch dưới:

| **Quy ước** | **Mức truy cập** | **Ý nghĩa** |
| --- | --- | --- |
| `name` | Public | Truy cập tự do từ bên ngoài class |
| `_name` | Protected | Quy ước "không nên" truy cập trực tiếp từ ngoài, nhưng vẫn truy cập được |
| `__name` | Private | Bị "name-mangling" (đổi tên nội bộ), rất khó truy cập trực tiếp từ ngoài |

```python
class BankAccount:
    def __init__(self, owner, balance):
        self._owner = owner        # protected — quy ước
        self.__balance = balance   # private — name mangling

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):         # method public để truy cập dữ liệu private
        return self.__balance


acc = BankAccount("Abhi", 1000)
acc.deposit(500)
print(acc.get_balance())   # 1500
print(acc.__balance)       # AttributeError — không truy cập trực tiếp được
```

#### Abstraction (Tính trừu tượng)

Abstraction ẩn chi tiết triển khai bên trong và chỉ hiển thị những tính năng cốt lõi cần thiết — tập trung vào "object làm gì" thay vì "làm như thế nào". Trong Python, dùng module `abc` với `ABC` và `@abstractmethod`. Abstract class **không thể khởi tạo trực tiếp**; bất kỳ class con nào cũng bắt buộc phải override toàn bộ abstract method, nếu không sẽ không thể khởi tạo được.

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):            # Abstract Base Class
    @abstractmethod
    def start(self):
        pass


class Car(Vehicle):             # Concrete class — bắt buộc override start()
    def start(self):
        print("Car started")


class Bike(Vehicle):
    def start(self):
        print("Bike started")


c = Car()
c.start()   # Car started
b = Bike()
b.start()   # Bike started

# v = Vehicle()  # TypeError — không thể khởi tạo abstract class
```

---

### Bảng tóm tắt 4 tính chất OOP

| **Tính chất** | **Trọng tâm** | **Cách hiện thực trong Python** | **Lợi ích chính** |
| --- | --- | --- | --- |
| Encapsulation (Đóng gói) | Ẩn dữ liệu & method, gộp chung vào 1 class | Quy ước `_attr` (protected), `__attr` (private, name-mangling) | Bảo vệ dữ liệu, kiểm soát truy cập, bảo mật tốt hơn |
| Inheritance (Kế thừa) | Tái sử dụng code có sẵn từ class cha | `class Con(Cha):`, `super()`, hỗ trợ đa kế thừa `class C(A, B):` | Tái sử dụng code, tổ chức phân cấp rõ ràng |
| Polymorphism (Đa hình) | Nhiều hình thái của cùng một method | Method overriding (runtime); Python không hỗ trợ method overloading truyền thống | Code linh hoạt, dùng chung 1 giao diện cho nhiều loại object |
| Abstraction (Trừu tượng) | Ẩn chi tiết triển khai, chỉ lộ tính năng cần thiết | Module `abc`, `ABC`, `@abstractmethod` | Đơn giản hóa, hỗ trợ thiết kế hệ thống lớn |

> 📝 **Ghi chú bổ sung**
> - `self` không phải từ khóa bắt buộc về tên, nhưng là quy ước chuẩn của Python cho tham số đầu tiên tham chiếu đến chính object.
>
> - Private attribute (`__name`) thực chất vẫn truy cập được từ ngoài qua tên đã bị "mangled": `obj._ClassName__name`, nhưng đây không phải cách dùng khuyến khích.
>
> - Method Overloading (nhiều method cùng tên khác số tham số) không được Python hỗ trợ như Java/C++; muốn mô phỏng có thể dùng tham số mặc định (`def f(a, b=None)`) hoặc `*args`.
>
> - Abstract class (kế thừa từ `ABC`) không thể khởi tạo trực tiếp — nó chỉ định nghĩa "bản hợp đồng" (interface) mà các class con bắt buộc phải tuân theo.
>
