# Python: Functions, Comprehension & Lambda

> 🖼️ Tổng hợp từ 5 ảnh ghi chú/cheat sheet gốc:
> 1. 1375_cheat-sheet-python-functions-parameters-args-kwarg.jpg
>
> 2. 1378_cheat-sheet-python-comprehensions-va-lambda-functi.jpg
>
> 3. 1432_ghi-chu-python-dictionary-nang-cao-va-comprehensio.jpg
>
> 4. 1433_ghi-chu-python-comprehensions-va-functions.jpg
>
> 5. 1434_ghi-chu-python-advanced-functions-lambda-map-filte.jpg
>

### Functions

Function là một khối code có thể tái sử dụng, giúp tổ chức và module hóa chương trình. Được định nghĩa bằng từ khóa `def`.

#### 1. Định nghĩa và gọi hàm

```python
def greet(name):
    """Function này chào người dùng."""
    print(f"Hello, {name}!")

# Gọi hàm
greet("QA Insights")   # Hello, QA Insights!
```

#### 2. Parameters vs Arguments

**Parameter** là biến được liệt kê trong định nghĩa hàm. **Argument** là giá trị thực tế được truyền vào khi gọi hàm.

```python
def add(a, b):      # a, b là parameters
    return a + b

result = add(10, 20) # 10, 20 là arguments
print(result)         # 30
```

#### 3. Return values

Câu lệnh `return` gửi kết quả về nơi gọi hàm. Nếu hàm không có `return`, nó mặc định trả về `None`.

```python
def multiply(x, y):
    return x * y

res = multiply(4, 5)
print(res)  # 20
```

#### 4. Default arguments (Giá trị mặc định)

Giá trị mặc định được dùng khi không có giá trị nào được truyền vào khi gọi hàm. **Lưu ý:** default arguments phải nằm sau các non-default arguments.

```python
def greet(name, msg="Welcome!"):
    print(f"Hi {name}, {msg}")

greet("Alice")                  # Hi Alice, Welcome!
greet("Alice", "Good morning!") # Hi Alice, Good morning!
```

#### 5. *args — Arbitrary Positional Arguments

Cho phép hàm nhận số lượng bất kỳ đối số vị trí (positional). Bên trong hàm, `*args` là một **tuple**.

```python
def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_all(1, 2, 3, 4, 5))  # 15
```

#### 6. kwargs — Arbitrary Keyword Arguments

Cho phép hàm nhận số lượng bất kỳ đối số từ khóa (keyword). Bên trong hàm, `**kwargs` là một **dictionary**.

```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25)
# name: Alice
# age: 25
```

#### 7. Variable Scope (Phạm vi biến)

Scope xác định nơi một biến có thể được truy cập: biến **global** (khai báo ngoài hàm) truy cập được từ mọi nơi để đọc, còn biến **local** (khai báo trong hàm) chỉ tồn tại bên trong hàm đó.

```python
x = "Global"

def show():
    y = "Local"
    print("Inside function ->", x, y)

show()                              # Inside function -> Global Local
print("Outside function ->", x)     # Outside function -> Global
# print(y)  # Lỗi: y không tồn tại ngoài function
```

> ⭐ **Điểm cần nhớ**
> - Dùng function để tổ chức và tái sử dụng code.
>
> - Return values giúp lấy kết quả ra khỏi function; không có `return` → trả về `None`.
>
> - `*args` và `**kwargs` xử lý input có số lượng thay đổi (tuple / dict).
>
> - Hiểu rõ scope để tránh xung đột biến local/global.
>

### List/Dict/Set Comprehension

Comprehension cung cấp cách ngắn gọn để tạo list, dict, set chỉ trong một dòng — dễ đọc hơn và thường nhanh hơn vòng lặp `for` truyền thống.

#### 1. List Comprehension

Cú pháp: `[expression for item in iterable if condition]`

```python
# Cách viết thông thường (vòng lặp for)
squares = []
for x in range(1, 6):
    squares.append(x * x)

# Viết lại bằng list comprehension — ngắn gọn hơn
squares = [x*x for x in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]

# Có điều kiện lọc (if)
evens = [x for x in range(1, 11) if x % 2 == 0]
print(evens)  # [2, 4, 6, 8, 10]

# Dùng if-else trong expression
result = ['Even' if x % 2 == 0 else 'Odd' for x in range(1, 6)]
print(result)  # ['Odd','Even','Odd','Even','Odd']
```

#### 2. Dictionary Comprehension

Cú pháp: `{key_expr: value_expr for item in iterable}`

```python
# Number : Square mapping
num_sq = {x: x*x for x in range(1, 6)}
print(num_sq)  # {1:1, 2:4, 3:9, 4:16, 5:25}

# Ký tự : mã ASCII
char_code = {ch: ord(ch) for ch in 'ABC'}
print(char_code)  # {'A':65, 'B':66, 'C':67}

# Dictionary comprehension có điều kiện
even_sq = {x: x*x for x in range(1, 11) if x % 2 == 0}
print(even_sq)  # {2:4, 4:16, 6:36, 8:64, 10:100}
```

#### 3. Set Comprehension

Cú pháp: `{expression for item in iterable}`. Kết quả luôn là các phần tử **duy nhất** (không trùng lặp).

```python
# Unique even numbers from 1 to 10
evens = {x for x in range(1, 11) if x % 2 == 0}
print(evens)  # {2, 4, 6, 8, 10}

# Ký tự duy nhất trong chuỗi
unique_chars = {ch for ch in 'abracadabra'}
print(unique_chars)  # {'a','b','r','c','d'}

vowels = {ch for ch in 'education' if ch in 'aeiou'}
print(vowels)  # {'e','u','a','i','o'}
```

#### 4. Nested Comprehension

Comprehension có thể lồng nhau để xử lý dữ liệu nhiều chiều, ví dụ làm phẳng (flatten) một ma trận:

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Nested list comprehension: duyệt từng hàng rồi từng phần tử trong hàng
flat = [num for row in matrix for num in row]
print(flat)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Tạo bảng cửu chương bằng nested comprehension
table = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(table)  # [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
```

| **Tính năng** | **List Comp** | **Dict Comp** | **Set Comp** |
| --- | --- | --- | --- |
| Trả về | List | Dictionary | Set |
| Công dụng | Biến đổi & lọc dữ liệu trong list | Tạo dict từ dữ liệu | Giá trị duy nhất từ dữ liệu |

> ⚠️ **Lỗi thường gặp:** Dùng list khi cần loại trùng lặp (nên dùng set); lạm dụng comprehension cho logic quá phức tạp làm giảm khả năng đọc code — khi đó nên quay lại vòng lặp `for` thông thường.

### Lambda & Higher-order functions

#### 1. Lambda là gì?

Lambda tạo ra hàm ẩn danh (không tên) nhỏ gọn, hữu ích cho các hàm ngắn, dùng một lần. Cú pháp: `lambda arguments: expression`. Lambda chỉ giới hạn trong **một biểu thức duy nhất** (không có nhiều dòng lệnh, không có `return` tường minh).

```python
add = lambda a, b: a + b
print(add(5, 3))     # 8

square = lambda x: x * x
print(square(4))      # 16

# Lambda nhiều đối số
mul = lambda x, y, z: x * y * z
print(mul(2, 3, 4))   # 24
```

#### 2. map() — áp dụng hàm cho mọi phần tử

`map(function, iterable)` áp dụng một hàm cho tất cả phần tử trong iterable, trả về một `map object` (dùng `list()` để chuyển đổi).

```python
nums = [1, 2, 3, 4]
doubled = list(map(lambda x: x * 2, nums))
print(doubled)  # [2, 4, 6, 8]

words = ['py', 'pthon', 'rocks']
upper = list(map(str.upper, words))
print(upper)  # ['PY', 'PTHON', 'ROCKS']
```

#### 3. filter() — lọc phần tử theo điều kiện

`filter(function, iterable)` lọc các phần tử mà hàm trả về `True`.

```python
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  # [2, 4, 6, 8, 10]

words = ['hi', 'python', 'is', 'awesome', 'code']
long_words = list(filter(lambda w: len(w) > 3, words))
print(long_words)  # ['python', 'awesome', 'code']
```

#### 4. reduce() — dồn tích lũy về một giá trị

`reduce(function, iterable[, initializer])` nằm trong module `functools`, áp dụng hàm dồn tích lũy lên các phần tử, trả về **một** kết quả tổng hợp duy nhất.

```python
from functools import reduce

nums = [1, 2, 3, 4]

# Tổng tất cả
sum_all = reduce(lambda x, y: x + y, nums)
print(sum_all)   # 10

# Tích tất cả
prod_all = reduce(lambda x, y: x * y, nums, 1)
print(prod_all)  # 24
```

#### 5. Khi nào nên dùng lambda?

- Dùng lambda cho các hàm **ngắn, dùng một lần**, đặc biệt làm callback truyền vào `map()`, `filter()`, `reduce()`, `sorted(key=...)`.

- **Không** nên lạm dụng lambda cho logic phức tạp nhiều bước — khi đó nên định nghĩa hàm bằng `def` có tên rõ ràng để dễ đọc và debug.

- `map()` và `filter()` trả về **iterator** trong Python 3 (không phải list), nên cần bọc `list(...)` nếu muốn xem/khai thác toàn bộ kết quả ngay.

```python
# Ví dụ thực tế: sắp xếp danh sách theo một tiêu chí
students = [("An", 8.5), ("Binh", 7.2), ("Chi", 9.1)]

# lambda làm key function cho sorted() — phù hợp vì logic rất ngắn
sorted_students = sorted(students, key=lambda s: s[1], reverse=True)
print(sorted_students)  # [('Chi', 9.1), ('An', 8.5), ('Binh', 7.2)]
```

> 💡 **Ứng dụng thực tế:** List Comp → biến đổi dữ liệu, tạo báo cáo. Dict Comp → tạo bảng tra cứu. Set Comp → loại bỏ trùng lặp. `map()` → áp dụng tính toán hàng loạt. `filter()` → kiểm tra/lọc dữ liệu. `lambda` → callback ngắn gọn, key function. `reduce()` → rút gọn toàn bộ iterable về một giá trị duy nhất.

> 📝 **Ghi chú bổ sung:** Nội dung về Dictionary nâng cao (creation, accessing, updating, deleting, looping) trong ảnh 1432 không thuộc phạm vi "Functions, Comprehension & Lambda" nên chỉ phần Comprehension của ảnh này được tổng hợp ở trên. Chủ đề Recursion (đệ quy, factorial, Fibonacci) xuất hiện trong ảnh 1434 nhưng thuộc phạm vi khác, không được đưa vào bài này.
