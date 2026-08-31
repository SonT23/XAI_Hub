# Python: Cấu trúc điều khiển (If/Else & Vòng lặp)

> 🖼️ **Tổng hợp từ 3 ảnh ghi chú gốc:**
> 1. `1373_ghi-chu-python-decision-making-if-elif-else.jpg`
>
> 2. `1374_cheat-sheet-python-vong-lap-loops-while-for-break.jpg`
>
> 3. `1428_ghi-chu-python-cau-lenh-dieu-kien-va-vong-lap.jpg`
>

## Câu lệnh điều kiện

### 1. Câu lệnh if

Thực thi một khối code nếu điều kiện là `True`. Nếu điều kiện là `False`, khối bị bỏ qua.

```python
age = 18
if age >= 18:
    print("You are eligible to vote.")
```

### 2. Câu lệnh if - else

Thực thi khối `if` nếu điều kiện `True`, ngược lại thực thi khối `else`.

```python
x = 3
if x % 2 == 0:
    print("Even")
else:
    print("Odd")
```

### 3. Chuỗi if - elif - else

`elif` (viết tắt của "else if") dùng để kiểm tra nhiều điều kiện theo thứ tự, từ trên xuống dưới. Điều kiện đúng đầu tiên sẽ được thực thi.

```python
marks = 75
if marks >= 90:
    grade = 'A'
elif marks >= 60:
    grade = 'B'
else:
    grade = 'C'
print("Grade:", grade)
```

### 4. If lồng nhau (Nested if)

Một khối `if`/`else` nằm bên trong khối `if`/`else` khác — dùng để xử lý các điều kiện phức tạp, phụ thuộc lẫn nhau.

```python
age = 20
has_id = True
if age >= 18:
    if has_id:
        print("Entry Allowed")
    else:
        print("ID is required")
else:
    print("Not eligible")
```

### 5. Toán tử điều kiện ba ngôi (Ternary / Conditional Expression)

Cú pháp rút gọn để gán giá trị dựa trên một điều kiện, viết trên một dòng: `giá_trị_nếu_true if điều_kiện else giá_trị_nếu_false`.

```python
age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)  # Adult

# Có thể dùng trực tiếp trong biểu thức khác
num = 7
result = "Even" if num % 2 == 0 else "Odd"
print(result)  # Odd
```

### 6. match-case (Python 3.10+)

Chọn một khối code để chạy dựa trên giá trị của biểu thức, tương tự `switch-case` ở các ngôn ngữ khác. Ký hiệu `_` là trường hợp mặc định (giống `else`).

```python
day = 3
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case _:
        print("Weekend")
```

### 7. Ví dụ thực tế — Hệ thống Login

Kết hợp if lồng nhau để xác thực username và password qua nhiều điều kiện.

```python
username = input("Enter username: ")
password = input("Enter password: ")
if username == "admin":
    if password == "1234":
        print("Login Successful")
    else:
        print("Incorrect Password")
else:
    print("Invalid Username")
```

> 💡 **Mẹo hay**
> - Dùng điều kiện có ý nghĩa rõ ràng, dễ đọc.
>
> - Sắp xếp điều kiện từ cụ thể đến tổng quát.
>
> - Dùng `match-case` cho code sạch, gọn khi so khớp giá trị cố định.
>
> - Dùng biểu thức ternary khi logic đơn giản, tránh lạm dụng khi điều kiện phức tạp (sẽ khó đọc).
>

---

## Vòng lặp

### 1. Vòng lặp for

Dùng để lặp qua một dãy (list, tuple, string, `range()`,...).

```python
for variable in sequence:
    # khối code
    pass

for i in range(1, 6):
    print(i)
# Output: 1 2 3 4 5
```

### 2. Vòng lặp while

Lặp lại một khối code trong khi điều kiện còn `True`.

```python
i = 1
while i <= 5:
    print(f"Count: {i}")
    i += 1
# Output:
# Count: 1
# Count: 2
# Count: 3
# Count: 4
# Count: 5
```

### 3. Hàm range()

Sinh ra một dãy số. Cú pháp: `range(start, stop, step)`.

| Ví dụ | Output |
| --- | --- |
| range(5) | 0, 1, 2, 3, 4 |
| range(1, 5) | 1, 2, 3, 4 |
| range(2, 10, 2) | 2, 4, 6, 8 |

```python
for i in range(1, 6):
    print(i, end=' ')
# Output: 1 2 3 4 5
```

### 4. Câu lệnh break

Dừng vòng lặp hoàn toàn ngay lập tức, bất kể điều kiện lặp còn đúng hay không.

```python
for i in range(1, 6):
    if i == 3:
        break
    print(i)
# Output: 1 2
```

### 5. Câu lệnh continue

Bỏ qua lần lặp hiện tại và tiếp tục với lần lặp kế tiếp.

```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
# Output: 1 2 4 5
```

### 6. Câu lệnh pass

Không làm gì cả — dùng như placeholder để tránh lỗi cú pháp khi khối code chưa được viết.

```python
for i in range(1, 4):
    if i == 2:
        pass
    print(i)
# Output: 1 2 3
```

### 7. Mệnh đề else trong vòng lặp (for...else / while...else)

Khối `else` của vòng lặp chạy khi vòng lặp kết thúc **bình thường** (không bị ngắt bởi `break`). Thường dùng để kiểm tra xem vòng lặp có tìm thấy gì hay không.

```python
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} = {x} * {n // x}")
            break
    else:
        # chỉ chạy nếu vòng lặp trong không gặp break -> n là số nguyên tố
        print(f"{n} là số nguyên tố")
```

### 8. Vòng lặp lồng nhau (Nested Loops)

Một vòng lặp nằm bên trong vòng lặp khác — hữu ích cho các bài toán về ma trận, pattern, tổ hợp.

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(i * j, end=" ")
    print()
# Output:
# 1 2 3
# 2 4 6
# 3 6 9
```

> ⭐ **Trường hợp sử dụng thực tế**
> - Duyệt qua các tập hợp dữ liệu (list, dict, set...)
>
> - Đọc từng dòng từ file
>
> - Cơ chế retry trong automation scripts
>
> - Polling API cho đến khi đạt điều kiện
>
> - Sinh report, bảng biểu hoặc pattern
>

> 📌 **Ghi chú bổ sung**
> - Câu lệnh điều kiện giúp chương trình đưa ra quyết định và chọn đúng luồng xử lý; vòng lặp giúp giảm lặp code, tiết kiệm thời gian và công sức.
>
> - `break` chỉ thoát vòng lặp gần nhất chứa nó (trong vòng lặp lồng nhau, không thoát toàn bộ các vòng ngoài).
>
> - Nên chọn đúng câu lệnh điều khiển (`break`, `continue`, `pass`) để tối ưu luồng và hiệu năng code.
>
