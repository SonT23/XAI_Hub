# Python: Cú pháp cơ bản (Biến, Kiểu dữ liệu, I/O)

> 🖼️ **Tổng hợp từ 7 ảnh ghi chú gốc (2 bộ khác nhau):**
> 1. 1369_bia-ghi-chu-python-co-ban-den-nang-cao.jpg
>
> 2. 1370_ghi-chu-python-gioi-thieu-ve-python.jpg
>
> 3. 1371_ghi-chu-python-variables-data-types.jpg
>
> 4. 1372_ghi-chu-python-input-output-operators.jpg
>
> 5. 1425_ghi-chu-python-co-ban-cu-phap-bien-tu-khoa.jpg
>
> 6. 1426_ghi-chu-python-cac-kieu-du-lieu-so-chuoi-boolean.jpg
>
> 7. 1427_ghi-chu-python-input-output-va-cac-toan-tu.jpg
>

### Giới thiệu về Python

> 🖼️ Ảnh thuộc mục này: 1370, 1425

**Python là gì?** Python là ngôn ngữ lập trình bậc cao, thông dịch (interpreted), đa mục đích (general-purpose), do **Guido van Rossum** tạo ra và phát hành năm **1991**. Python chú trọng tính dễ đọc của code, cú pháp đơn giản, rõ ràng, gần giống tiếng Anh. Ngôn ngữ hỗ trợ nhiều mô hình lập trình: thủ tục (procedural), hướng đối tượng (OOP) và hàm (functional).

**Tính năng & ưu điểm nổi bật:**

- ✓ Dễ học, dễ đọc — cú pháp đơn giản, gần giống tiếng Anh

- ✓ Ngôn ngữ thông dịch — không cần biên dịch, chạy từng dòng

- ✓ Ngôn ngữ bậc cao — tập trung vào logic, không lo chi tiết cấp thấp

- ✓ Kiểu dữ liệu động (dynamically typed) — không cần khai báo kiểu tường minh

- ✓ Đa nền tảng / khả chuyển — chạy trên Windows, macOS, Linux; viết một lần chạy mọi nơi

- ✓ Thư viện chuẩn phong phú — module dựng sẵn cho hầu hết mọi việc

- ✓ Mã nguồn mở, miễn phí, có thể mở rộng bằng C/C++

- ✓ Cộng đồng hỗ trợ lớn và năng động

**Ứng dụng:** Phát triển Web, Data Science & Analytics, Machine Learning, Automation & Scripting, DevOps & Infrastructure, Cybersecurity, Phát triển Game.

**Cú pháp cơ bản:** Python dùng **thụt lề (indentation)** — dấu cách hoặc tab — để xác định khối code (thay vì dấu ngoặc `{}` như nhiều ngôn ngữ khác). Python phân biệt hoa - thường (case-sensitive).

```python
if True:
    print("Hello, Python!")
else:
    print("Goodbye!")
```

> ⚠️ Thụt lề rất quan trọng trong Python — nó xác định phạm vi (scope) của khối code. Thụt lề sai sẽ gây lỗi `IndentationError`.

**Comment (chú thích):** dùng để giải thích code, bị trình thông dịch bỏ qua khi chạy.

```python
# Đây là comment một dòng

'''
Đây là comment
nhiều dòng.
Có thể trải dài nhiều dòng.
'''
```

**Cài đặt Python:**

1. Truy cập [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. Tải phiên bản Python 3.x mới nhất

3. Khi cài đặt, **tick chọn "Add Python to PATH"**

4. Nhấn "Install Now" và hoàn tất

5. Kiểm tra bằng terminal:

```bash
$ python --version
Python 3.12.3
```

**Chạy chương trình đầu tiên:**

```python
# hello.py
print("Hello, Python!")
```

```bash
$ python hello.py
Hello, Python!
```

**Luồng thực thi Python:** Viết code (file `.py`) → Interpreter đọc code từng dòng → Thực thi từng dòng code → Output hiển thị trên màn hình.

> 💡 **Mẹo:** File Python có đuôi `.py`. Nên đặt tên file có ý nghĩa, luôn cập nhật Python và pip để có hiệu năng và bảo mật tốt hơn.

### Biến & Từ khoá

> 🖼️ Ảnh thuộc mục này: 1371, 1425

**Biến (Variable)** là tên được đặt cho một vị trí bộ nhớ để lưu giá trị. Trong Python, biến được tạo ra ngay khi bạn gán một giá trị cho nó — Python **không có lệnh khai báo biến riêng** như `var`/`int` ở các ngôn ngữ khác.

```python
name = "QA Insights"   # String
age = 25                # Integer
price = 19.99           # Float
is_active = True        # Boolean
```

**Dynamic typing (kiểu dữ liệu động):** Python không yêu cầu khai báo kiểu dữ liệu tường minh — kiểu được xác định lúc chạy (runtime), dựa vào giá trị được gán. Một biến có thể được gán lại với kiểu dữ liệu khác.

**Quy tắc đặt tên biến / định danh (identifier):**

- ✓ Phải bắt đầu bằng chữ cái (a-z, A-Z) hoặc dấu gạch dưới (`_`)

- ✓ Có thể chứa chữ cái, số (0-9) và dấu gạch dưới

- ✓ Không được bắt đầu bằng chữ số

- ✓ Phân biệt hoa - thường (`myVar` khác `myvar`, `age` khác `Age`)

- ✗ Không được dùng từ khoá (keyword) của Python

- ✗ Không được chứa khoảng trắng hay ký tự đặc biệt (`!,@,#,$,%,...`)

| ✓ Hợp lệ | ✗ Không hợp lệ |
| --- | --- |
| my_var, userName, _count, total2 | 2value, user-name, my var, class |

**Từ khoá (Keywords):** là các từ được Python dành riêng, có ý nghĩa đặc biệt và **không thể** dùng làm định danh (tên biến, hàm, lớp...).

```python
False None True and as assert break
class continue def del elif else
except finally for from global if
import in is lambda nonlocal not or
pass raise return try while with
yield
```

### Kiểu dữ liệu

> 🖼️ Ảnh thuộc mục này: 1371, 1426

**Các kiểu dữ liệu phổ biến trong Python:**

| Data Type | Mô tả | Ví dụ |
| --- | --- | --- |
| int | Số nguyên (âm hoặc dương) | 10, -25, 0 |
| float | Số thập phân | 3.14, -0.001, 2.0 |
| complex | Số có phần thực và phần ảo | 2 + 3j |
| str | Chuỗi ký tự nằm trong dấu ngoặc | 'Hello', "Python" |
| bool | Biểu diễn True hoặc False | True, False |
| NoneType | Đại diện cho sự vắng mặt giá trị | None |
| list | Tập hợp có thứ tự, có thể thay đổi | [1,2,3], ['a','b'] |
| tuple | Tập hợp có thứ tự, không thể thay đổi | (1,2,3), ('a','b') |
| set | Tập hợp không thứ tự, phần tử duy nhất | {1,2,3} |
| dict | Cặp key-value | {'name':'QA','age':25} |

**Số (Numbers):** Python hỗ trợ `int`, `float`, `complex`.

```python
a = 10       # int
b = 3.14     # float
c = 2 + 3j   # complex
```

**Chuỗi (Strings):** đặt trong dấu nháy đơn, kép hoặc ba dấu nháy (multi-line). String là **bất biến (immutable)** — không thể thay đổi sau khi tạo.

```python
s1 = "Hello"
s2 = 'Python'
s3 = """Multi
line
string"""

# Thao tác thường dùng
len(s1)              # 5
s1[0]                 # 'H'
s1 + " World"          # "Hello World"
s1.upper()             # "HELLO"
s1.lower()             # "hello"
s1.replace('l', 'x')   # "Hexxo"
```

**Boolean:** chỉ có 2 giá trị `True` hoặc `False`, dùng trong điều kiện và phép toán logic.

```python
a = True
b = False
print(a, b)   # True False
```

**None:** đại diện cho sự vắng mặt của giá trị — là kiểu dữ liệu đặc biệt riêng (`NoneType`), thường dùng để khởi tạo biến.

```python
x = None
print(x)   # None
```

> ⭐ `None` **không phải** là `0`, `False` hay rỗng — nó có nghĩa là "không có gì".

**Truthy và Falsy values:**

- Giá trị Truthy: `True, 1, -1, "hello", [1,2], {1:'a'}, (1,), 3.14,...`

- Giá trị Falsy: `False, 0, None, "", [], (), {}` (các tập rỗng),...

**Ép kiểu (Type Casting):**

- *Ngầm định (Implicit)*: Python tự động chuyển kiểu nhỏ hơn thành kiểu lớn hơn.

```python
a = 5      # int
b = 2.5    # float
c = a + b  # 7.5 (float) — tự động ép kiểu
```

- *Tường minh (Explicit)*: dùng hàm dựng sẵn `int()`, `float()`, `str()`, `bool()`.

```python
int('10')     # 10
float('3.14') # 3.14
str(100)      # '100'
bool(0)       # False
bool(1)       # True
```

**Kiểm tra kiểu dữ liệu:** dùng hàm `type()`.

```python
x = 25
y = "Python"
z = 3.14
print(type(x))   # <class 'int'>
print(type(y))   # <class 'str'>
print(type(z))   # <class 'float'>
```

### Input/Output & Toán tử

> 🖼️ Ảnh thuộc mục này: 1372, 1427

#### Input / Output

**Hàm **`input()`**:** dùng để nhận dữ liệu nhập từ người dùng. **Luôn trả về kiểu String** — cần ép kiểu (type casting) nếu muốn dùng làm số.

```python
name = input("Enter your name: ")
age = int(input("Enter age: "))
print("Hello", name)
print("Age is", age)
```

**Hàm **`print()`**:** hiển thị output ra màn hình, hỗ trợ nhiều giá trị cùng lúc và các tham số `sep` (ký tự phân cách), `end` (ký tự kết thúc), cùng f-string để định dạng.

```python
print("Python is awesome!")
print("A", "B", "C", sep="-", end="\n")   # A-B-C
x = 10
print(f"Value of x is {x}")               # Value of x is 10
print(1, 2, sep=" | ")                     # 1 | 2
```

#### Các nhóm toán tử (Operators)

**1. Toán tử số học (Arithmetic):**

| Toán tử | Ý nghĩa | Ví dụ |
| --- | --- | --- |
| + | Cộng | 5+3=8 |
| - | Trừ | 5-3=2 |
| * | Nhân | 5*3=15 |
| / | Chia (kết quả float) | 5/2=2.5 |
| // | Chia lấy nguyên | 5//2=2 |
| % | Chia lấy dư | 5%2=1 |
|   | Luỹ thừa | 53=125 |

**2. Toán tử so sánh (Comparison):** `==` bằng, `!=` khác, `>` lớn hơn, `<` nhỏ hơn, `>=` lớn hơn hoặc bằng, `<=` nhỏ hơn hoặc bằng. Luôn trả về `True`/`False`.

```python
a, b = 5, 3
print(a > b)    # True
print(a == b)   # False
```

**3. Toán tử logic (Logical):** `and` (cả hai True), `or` (một trong hai True), `not` (đảo ngược kết quả). Luôn trả về giá trị boolean.

```python
a, b = True, False
print(a and b)   # False
print(a or b)    # True
print(not a)     # False
```

**4. Toán tử gán (Assignment):** `=`, `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=`.

```python
x = 10
x += 5    # x = 15
x **= 2   # x = 225
```

**5. Toán tử bitwise:** hoạt động ở cấp độ bit — `&` AND, `|` OR, `^` XOR, `~` NOT, `<<` dịch trái, `>>` dịch phải.

```python
a, b = 5, 3       # 0101, 0011
print(a & b)      # 1
print(a | b)      # 7
print(a ^ b)      # 6
print(~a)         # -6
print(a << 1)     # 10
print(a >> 1)     # 2
```

**6. Toán tử membership:** `in`, `not in` — kiểm tra một phần tử có tồn tại trong dãy (string, list, tuple, set, dict) hay không.

```python
lst = [1, 2, 3, 4]
print(2 in lst)       # True
print(5 not in lst)   # True
```

**7. Toán tử identity:** `is`, `is not` — so sánh **vị trí bộ nhớ (identity)** của hai đối tượng, khác với `==` (so sánh **giá trị**).

```python
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a is b)       # True  (cùng object)
print(a is c)       # False (khác object, dù giá trị giống nhau)
print(a is not c)   # True
```

> 💡 **Phân biệt quan trọng:** `is` kiểm tra identity (địa chỉ bộ nhớ); `==` kiểm tra equality (giá trị). Thứ tự ưu tiên toán tử (độ ưu tiên giảm dần): Arithmetic > Comparison > Logical > Assignment.

<callout icon="📌" color="orange_bg">**Ghi chú bổ sung — Trường hợp sử dụng thực tế:**

- Nhận input từ người dùng trong ứng dụng CLI

- Thực hiện tính toán trong automation scripts

- Kiểm tra điều kiện và quyết định trong test scripts

- Kiểm tra sự tồn tại dữ liệu trong collections (membership operators)

- So sánh objects và references trong frameworks (identity operators)

</callout>
