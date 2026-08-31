# Python: Modules, File Handling & Exception Handling

> 🖼️ **Nguồn ảnh gốc (6 file):**
> 1. 1379_cheat-sheet-python-modules-packages-pip-venv.jpg
>
> 2. 1380_cheat-sheet-python-file-handling-doc-ghi-csv-json.jpg
>
> 3. 1381_cheat-sheet-python-exception-handling-try-except-r.jpg
>
> 4. 1435_ghi-chu-python-modules-va-packages.jpg
>
> 5. 1436_ghi-chu-python-xu-ly-ngoai-le-exception-handling.jpg
>
> 6. 1437_ghi-chu-python-xu-ly-file-file-handling-csv-json.jpg
>

### Modules & Packages

**Module** là một file Python (`.py`) chứa các định nghĩa hàm, class, biến. **Package** là một thư mục chứa nhiều module, kèm file `__init__.py` để Python nhận diện đó là package.

#### Import module

- `import module_name` → import toàn bộ, truy cập bằng `module_name.thanh_phan`.

- `from module_name import name1, name2` → import các thành phần cụ thể, dùng thẳng không cần tiền tố.

- `import module_name as alias` → đặt bí danh khi tên module dài.

- `from module_name import *` → import tất cả (không khuyến khích trong dự án lớn vì dễ xung đột tên).

```python
# mymodule.py
PI = 3.14159

def add(a, b):
    return a + b

class Calculator:
    def mul(self, a, b):
        return a * b
```

```python
# main.py
import mymodule
print(mymodule.PI)
result = mymodule.add(10, 20)
calc = mymodule.Calculator()

# Hoặc import cụ thể
from mymodule import add, PI
print(add(5, 7))
```

#### Module dựng sẵn (built-in) phổ biến

| Module | Mục đích | Ví dụ |
| --- | --- | --- |
| math | Hàm toán học | math.sqrt(16), math.ceil(2.3), math.floor(2.8) |
| random | Sinh số ngẫu nhiên | random.randint(1,10), random.choice(['a','b']) |
| datetime | Xử lý ngày giờ | [datetime.now](http://datetime.now/)() |
| os | Giao tiếp hệ điều hành | os.listdir('.') |
| sys | Tham số hệ thống | sys.version |
| json | Làm việc với dữ liệu JSON | json.load(), json.dump() |

#### Tạo package riêng

```javascript
mypackage/
    __init__.py
    module1.py
    module2.py
```

`__init__.py` giúp Python nhận diện thư mục đó là một package (có thể để trống). Các bước: (1) tạo thư mục, (2) thêm `__init__.py`, (3) thêm các file `.py` là module, (4) import bằng dấu chấm.

```python
# mypackage/module1.py
def hello():
    return "Hello from module1!"

# mypackage/module2.py
def square(x):
    return x * x

# main.py
from mypackage import module1, module2
print(module1.hello())      # Hello from module1!
print(module2.square(5))    # 25
```

#### pip và Virtual Environment (venv)

**pip** là trình quản lý package, cài từ PyPI. **venv** tạo môi trường ảo độc lập cho từng dự án, tránh xung đột phiên bản package giữa các dự án.

```bash
# Cài package bằng pip
pip install requests
pip install pandas==2.1.4    # cài phiên bản cụ thể
pip list                     # liệt kê package đã cài
pip freeze > requirements.txt

# Tạo virtual environment
python -m venv venv

# Kích hoạt (Windows)
venv\Scripts\activate

# Kích hoạt (Linux/Mac)
source venv/bin/activate

# Cài package từ requirements.txt
pip install -r requirements.txt
```

> ⚠️ **Lỗi thường gặp:** quên kích hoạt venv trước khi cài package; cài package toàn cục (global) thay vì trong venv; push thư mục `venv/` lên Git — nên thêm `venv/` vào `.gitignore`.

### Đọc/Ghi File (File Handling)

File handling cho phép chương trình Python đọc từ và ghi dữ liệu vào file lưu trên đĩa, giúp lưu trữ dữ liệu vĩnh viễn giữa các lần chạy chương trình.

#### Mở file với open()

```python
f = open(file, mode, encoding='utf-8')
```

| Mode | Mô tả | Con trỏ file | Tạo file nếu chưa có? |
| --- | --- | --- | --- |
| r | Đọc (mặc định) | Đầu file | Không |
| w | Ghi (ghi đè) | Đầu file | Có |
| a | Thêm vào cuối | Cuối file | Có |
| x | Tạo mới (lỗi nếu đã tồn tại) | Đầu file | Có |
| b | Chế độ nhị phân (binary) | - | - |
| t | Chế độ văn bản (mặc định) | - | - |
| + | Đọc và ghi | Đầu file | - |

#### with statement (best practice)

`with` tự động đóng file kể cả khi có lỗi xảy ra, nên luôn ưu tiên dùng thay vì gọi `close()` thủ công.

```python
with open('data.txt', 'r', encoding='utf-8') as f:
    content = f.read()          # đọc toàn bộ

with open('data.txt', 'r', encoding='utf-8') as f:
    for line in f:               # đọc từng dòng
        print(line.strip())

with open('output.txt', 'w', encoding='utf-8') as f:
    f.write('Hello QA!\n')
    f.write('Python!')

with open('log.txt', 'a', encoding='utf-8') as f:
    f.write('New entry\n')       # thêm vào cuối, không ghi đè
```

**Method file thường dùng:** `f.read()` (toàn bộ), `f.readline()` (1 dòng), `f.readlines()` (list các dòng), `f.write()`, `f.tell()` (vị trí con trỏ), `f.seek(offset)` (di chuyển con trỏ), `f.truncate()`, `f.close()`.

#### Đọc/Ghi CSV (module csv)

```python
import csv

# Ghi CSV
with open('data.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Name', 'Age', 'City'])
    writer.writerow(['Abhi', 20, 'Delhi'])
    writer.writerow(['Riya', 19, 'Mumbai'])

# Đọc CSV
with open('data.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
# ['Name', 'Age', 'City']
# ['Abhi', '20', 'Delhi']
# ['Riya', '19', 'Mumbai']

# Đọc dạng dictionary (mỗi dòng thành dict theo header)
with open('data.csv', 'r', encoding='utf-8') as f:
    for row in csv.DictReader(f):
        print(row['Name'], row['City'])
```

#### Đọc/Ghi JSON (module json)

```python
import json

data = {'name': 'Abhi', 'age': 20, 'city': 'Delhi'}

# Ghi JSON vào file
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4)

# Đọc JSON từ file
with open('data.json', 'r', encoding='utf-8') as f:
    data_read = json.load(f)
    print(data_read)   # {'name': 'Abhi', 'age': 20, 'city': 'Delhi'}

# Chuyển đổi qua lại giữa object Python và chuỗi JSON
json_str = json.dumps(data)   # dict -> string
back = json.loads(json_str)   # string -> dict
```

> 💡 **Mẹo:** luôn xử lý exception khi thao tác với file (`FileNotFoundError`, quyền truy cập...) bằng try-except để code chắc chắn hơn; luôn chỉ định `encoding='utf-8'` cho file text; chế độ nhị phân (`b`) hữu ích cho ảnh, PDF.

### Xử lý ngoại lệ (Exception Handling)

Exception là lỗi runtime làm gián đoạn luồng chạy bình thường của chương trình. Exception handling cho phép xử lý các lỗi đó một cách mềm dẻo mà không làm crash chương trình, cải thiện độ tin cậy và trải nghiệm người dùng.

#### try - except - else - finally

- `try`: chứa code có thể gây lỗi.

- `except`: xử lý lỗi cụ thể (có thể có nhiều khối `except` cho các loại lỗi khác nhau).

- `else`: chỉ chạy nếu **không** có lỗi xảy ra trong `try`.

- `finally`: luôn luôn chạy, dù có lỗi hay không — dùng để dọn dẹp (đóng file, giải phóng tài nguyên).

```python
try:
    x = 10 / int(input("Enter a number: "))
    print("Result:", x)
except ValueError:
    print("Invalid input!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print("Something went wrong!", e)
else:
    print("Execution successful.")
finally:
    print("Cleanup: This will run always.")
```

#### Từ khóa raise

Dùng để chủ động ném ra một exception (dựng sẵn hoặc tùy chỉnh) khi phát hiện điều kiện không hợp lệ.

```python
age = int(input("Enter age: "))
if age < 18:
    raise ValueError("Age must be 18 or above")
print("Access granted")
```

Khi `raise` thực thi, chương trình dừng lại và nhảy đến khối `except` gần nhất (nếu có).

#### Custom Exception (ngoại lệ tự định nghĩa)

Tạo class exception riêng bằng cách kế thừa từ `Exception`, hữu ích để xử lý lỗi đặc thù cho ứng dụng.

```python
class InvalidAgeError(Exception):
    """Raised when age is not valid."""
    pass

def check_age(age):
    if age < 0 or age > 120:
        raise InvalidAgeError("Age must be between 0 and 120")
    print("Age is valid:", age)

try:
    user_age = int(input("Enter your age: "))
    check_age(user_age)
except InvalidAgeError as e:
    print("Error:", e)
```

#### Các exception dựng sẵn phổ biến

| Exception | Khi nào xảy ra |
| --- | --- |
| ValueError | Giá trị/argument không hợp lệ cho một hàm |
| ZeroDivisionError | Chia cho số 0 |
| TypeError | Thao tác trên sai kiểu dữ liệu / kiểu không tương thích |
| FileNotFoundError | Không tìm thấy file hoặc đường dẫn |
| KeyError | Không tìm thấy key trong dictionary |
| IndexError | Chỉ số vượt ngoài phạm vi |
| ImportError | Câu lệnh import thất bại |

#### Luồng xử lý Exception (Flow)

| Tình huống | Luồng thực thi |
| --- | --- |
| Không có Exception | khối try chạy → khối else (nếu có) → khối finally |
| Có Exception xảy ra | khối try → khối except phù hợp → khối finally |
| Câu lệnh raise | raise thực thi → nhảy đến except → khối finally |
| Exception không khớp except nào | khối finally vẫn chạy → chương trình dừng (lỗi chưa xử lý) |

#### Đọc Traceback

Traceback hiển thị chuỗi gọi hàm dẫn đến lỗi — đọc từ dưới lên trên để tìm vị trí lỗi thực sự.

```javascript
Traceback (most recent call last):
  File "app.py", line 4, in <module>
    x = 10 / 0
ZeroDivisionError: division by zero
```

#### Best Practices

- Xử lý exception cụ thể, tránh dùng `except:` trần (bắt mọi lỗi mà không rõ nguyên nhân).

- Không bỏ qua exception âm thầm (`except: pass`).

- Thông báo lỗi thân thiện, dễ hiểu cho người dùng.

- Giữ khối `finally` để dọn dẹp resource (đóng file, kết nối...).

- Kiểm tra input, fail sớm bằng `raise` khi phát hiện dữ liệu không hợp lệ.

- Dùng `logging` thay vì `print()` trong dự án lớn.

> ⭐ **Ứng dụng thực tế:** Exception handling được dùng trong API, xử lý file, automation scripts, data pipelines và hệ thống production để tránh crash ngoài ý muốn.

> 📝 **Ghi chú bổ sung:** Nội dung trang này tổng hợp và hợp nhất từ 3 cheat sheet và 3 ghi chú chi tiết (6 ảnh gốc liệt kê ở đầu trang), có bổ sung thêm ví dụ minh họa (DictReader, json.dumps/loads, bảng Luồng xử lý Exception) để đầy đủ và dễ tra cứu hơn.
