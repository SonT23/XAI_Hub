# Python: Nâng cao (Iterators, Generators, Decorators) & Thư viện

> 🖼️ **Tổng hợp từ 5 ảnh ghi chú gốc:**
> 1. 1383_cheat-sheet-python-nang-cao-iterators-generators-d.jpg
>
> 2. 1384_danh-sach-cac-thu-vien-python-can-biet-numpy-panda.jpg
>
> 3. 1440_ghi-chu-python-nang-cao-iterators-generators-decor.jpg
>
> 4. 1441_ghi-chu-python-cac-thu-vien-numpy-pandas-matplotli.jpg
>
> 5. 1442_ghi-chu-python-ket-noi-co-so-du-lieu-sqlite-sql.jpg
>

> Python nâng cao (iterators, generators, decorators) và các thư viện xử lý dữ liệu (NumPy, Pandas, Matplotlib) là nền tảng kỹ thuật trực tiếp phục vụ pipeline code thực nghiệm NCKH: đọc dữ liệu, tiền xử lý, huấn luyện mô hình ML/DL, và trực quan hóa kết quả.

### Iterators & Generators

#### Iterator là gì?

- **Iterable**: đối tượng có thể duyệt qua (list, tuple, str, dict...).

- **Iterator**: đối tượng thực hiện *iterator protocol* — bắt buộc có hai method `__iter__()` (trả về chính nó) và `__next__()` (trả về phần tử tiếp theo, `raise StopIteration` khi hết).

- Dùng `iter()` để lấy iterator từ một iterable, và `next()` để lấy phần tử kế tiếp.

```python
nums = [1, 2, 3]
it = iter(nums)
print(next(it))  # 1
print(next(it))  # 2
```

Tự viết một class Iterator theo đúng protocol:

```python
class CountDown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        val = self.current
        self.current -= 1
        return val

# Sử dụng iterator
for num in CountDown(3):
    print(num)  # 3 2 1 0
```

#### Generator là gì?

- Generator là cách **đơn giản hơn nhiều** để tạo iterator, dùng từ khóa `yield` thay vì `return`.

- Mỗi lần gọi `yield`, hàm tạm dừng và lưu lại trạng thái; lần gọi `next()` kế tiếp sẽ tiếp tục chạy từ đúng chỗ dừng.

- **Lazy evaluation**: giá trị chỉ được sinh ra khi cần, không tính toán/lưu trữ toàn bộ trước.

```python
def countdown(n):
    while n >= 0:
        yield n
        n -= 1

for num in countdown(3):
    print(num)  # 3 2 1 0
```

```python
# Ứng dụng thực tế: đọc file lớn theo từng dòng, không load hết vào RAM
def read_large_file(path):
    with open(path, "r") as f:
        for line in f:
            yield line.strip()

for line in read_large_file("data.csv"):
    process(line)
```

**Generator expression** — giống list comprehension nhưng dùng `()` thay vì `[]`:

```python
squares = (x * x for x in range(5))
for x in squares:
    print(x)  # 0 1 4 9 16
```

#### Lợi ích tiết kiệm bộ nhớ

| Iterator/Generator | List thông thường |
| --- | --- |
| Sinh từng giá trị một, không giữ toàn bộ dữ liệu trong RAM | Tạo và lưu toàn bộ phần tử cùng lúc |
| Phù hợp dữ liệu lớn / luồng vô hạn (stream API, đọc file lớn, dataset lớn) | Tốn bộ nhớ khi dữ liệu lớn |
| Chỉ duyệt được **một lần** | Duyệt lại nhiều lần được |

> 💡 Trong NCKH, khi xử lý dataset lớn (hàng triệu dòng) trước khi đưa vào Pandas/NumPy, dùng generator để đọc và tiền xử lý theo batch giúp tránh tràn bộ nhớ (out-of-memory) — rất hữu ích khi huấn luyện mô hình theo mini-batch trong Deep Learning.

### Decorators

- Decorator là một **hàm nhận vào hàm khác** và mở rộng hành vi của hàm đó **mà không sửa đổi code gốc** — tuân thủ nguyên tắc DRY (Don't Repeat Yourself).

- Cú pháp áp dụng: đặt `@ten_decorator` ngay phía trên định nghĩa hàm.

- Ứng dụng phổ biến: logging, đo thời gian chạy, xác thực (authentication), retry, caching.

#### Decorator cơ bản

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result
    return wrapper

@my_decorator
def say_hello():
    print("Hello, Python!")

say_hello()
# Before function call
# Hello, Python!
# After function call
```

#### Decorator đo thời gian chạy hàm

```python
import time
from functools import wraps

def log_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"{func.__name__} chạy trong {elapsed:.4f} giây")
        return result
    return wrapper

@log_time
def train_model(epochs):
    for _ in range(epochs):
        pass  # giả lập huấn luyện mô hình

train_model(1000)
# train_model chạy trong 0.0001 giây
```

#### Decorator có tham số

Muốn decorator nhận tham số riêng (ví dụ số lần lặp lại), cần thêm một lớp hàm bao bọc bên ngoài:

```python
def repeat(num):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(num):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet():
    print("Hi!")

greet()
# Hi!
# Hi!
# Hi!
```

> ⭐ Kiến thức phỏng vấn hay gặp: phân biệt rõ Iterator vs Generator, và giải thích cơ chế hoạt động của Decorator (hàm bậc cao, closure, `*args`/`**kwargs`).

### Các thư viện Python quan trọng cho NCKH

Trong pipeline nghiên cứu Machine Learning / Deep Learning, ba thư viện dưới đây gần như luôn xuất hiện cùng nhau: **NumPy** xử lý số liệu ở tầng thấp (mảng, phép toán tuyến tính), **Pandas** xử lý dữ liệu ở tầng bảng biểu (đọc file, làm sạch, tổng hợp), và **Matplotlib** trực quan hóa kết quả (loss curve, phân bố dữ liệu, so sánh mô hình).

#### NumPy (Numerical Python)

- Cung cấp đối tượng mảng đa chiều `ndarray`, mạnh hơn list Python nhờ **vectorization**: các phép toán áp dụng trực tiếp lên toàn bộ mảng mà không cần vòng lặp `for`, chạy nhanh hơn nhiều nhờ được cài đặt bằng C.

- Nền tảng bên dưới của hầu hết framework ML/DL (Pandas, scikit-learn, TensorFlow, PyTorch đều dùng hoặc tương thích với ndarray).

```python
import numpy as np

# Tạo mảng
arr = np.array([1, 2, 3, 4, 5])

# Ma trận 2D
mat = np.array([[1, 2, 3],
                 [4, 5, 6]])

# Vectorization: không cần vòng lặp for
print(arr + 10)        # [11 12 13 14 15]
print(arr * 2)         # [2 4 6 8 10]
print(np.sum(arr))     # 15
print(np.mean(arr))    # 3.0
print(arr.shape)       # (5,)
print(np.dot(mat, arr[:3]))  # nhân ma trận - vector
```

**Vai trò trong pipeline ML/DL:** chuẩn hóa dữ liệu (normalization/standardization), tính toán ma trận trọng số, biểu diễn tensor đầu vào/đầu ra của mô hình, tính các phép toán tuyến tính (dot product, ma trận nghịch đảo) dùng trong thuật toán học máy.

#### Pandas (Data Analysis Library)

- Cung cấp cấu trúc **DataFrame** (bảng 2 chiều, giống Excel/SQL) và **Series** (1 cột dữ liệu).

- Dùng để đọc, làm sạch, biến đổi và tổng hợp dữ liệu — bước **tiền xử lý dữ liệu** gần như bắt buộc trước khi đưa vào mô hình.

```python
import pandas as pd

# Đọc dữ liệu thực nghiệm từ file CSV
df = pd.read_csv("ket_qua_thi_nghiem.csv")

print(df.head())          # 5 dòng đầu
print(df.info())          # Thông tin kiểu dữ liệu từng cột
print(df.describe())      # Thống kê tóm tắt (mean, std, min, max...)

# Làm sạch dữ liệu
df = df.dropna()                          # Xóa dòng thiếu dữ liệu
df["age"] = df["age"].fillna(df["age"].mean())  # Điền giá trị thiếu

# Tổng hợp theo nhóm — ví dụ so sánh độ chính xác theo từng mô hình
summary = df.groupby("model_name")["accuracy"].mean()
print(summary)

# Sắp xếp và lọc
df_sorted = df.sort_values("accuracy", ascending=False)
```

**Vai trò trong pipeline ML/DL:** đọc dữ liệu thô (CSV/Excel/SQL/JSON), làm sạch dữ liệu thiếu/ngoại lai, tách tập train/test, tổng hợp và so sánh kết quả thực nghiệm giữa các lần chạy mô hình — thường là bước đầu tiên trong mọi notebook nghiên cứu.

#### Matplotlib (Data Visualization)

- Thư viện vẽ biểu đồ nền tảng nhất trong Python: biểu đồ tĩnh, động và tương tác.

- Trong NCKH, dùng để trực quan hóa **quá trình huấn luyện** (loss/accuracy theo epoch) và **kết quả so sánh** giữa các mô hình.

```python
import matplotlib.pyplot as plt

# Ví dụ: vẽ đường loss trong quá trình huấn luyện mô hình
epochs = list(range(1, 11))
train_loss = [0.9, 0.7, 0.55, 0.42, 0.35, 0.30, 0.26, 0.23, 0.21, 0.20]

plt.plot(epochs, train_loss, label="Train Loss", color="b")
plt.title("Loss theo Epoch")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend()
plt.grid(True)
plt.show()

# Biểu đồ cột so sánh độ chính xác giữa các mô hình
models = ["CNN", "RNN", "Transformer"]
accuracy = [0.91, 0.87, 0.95]
plt.bar(models, accuracy, color="orange")
plt.title("So sánh độ chính xác giữa các mô hình")
plt.show()
```

**Vai trò trong pipeline ML/DL:** theo dõi quá trình hội tụ của mô hình (learning curve), phát hiện overfitting/underfitting qua biểu đồ train/validation loss, minh họa kết quả để đưa vào báo cáo hoặc bài báo khoa học.

> 💡 **Tóm tắt pipeline dữ liệu NCKH:** Pandas đọc & làm sạch dữ liệu → NumPy biến đổi thành mảng số để đưa vào mô hình ML/DL → mô hình huấn luyện và sinh ra kết quả (loss, accuracy...) → Matplotlib trực quan hóa kết quả để phân tích và viết báo cáo.

#### Các thư viện chuẩn (Standard Library) hữu ích khác

Có sẵn khi cài Python, không cần cài thêm:

| Thư viện | Công dụng | Ví dụ |
| --- | --- | --- |
| `os` | Giao tiếp hệ điều hành, thao tác file & thư mục | `os.getcwd()`, `os.listdir()` |
| `sys` | Truy cập biến/hàm hệ thống | `sys.version`, `sys.exit(0)` |
| `pathlib` | Xử lý đường dẫn file hướng đối tượng | `Path("file.txt").exists()` |
| `json` | Đọc/ghi dữ liệu JSON | `json.dumps(data)`, `json.loads(s)` |
| `datetime` | Xử lý ngày giờ | `datetime.now()` |

Thư viện bên thứ ba khác đáng biết: `requests` (gọi HTTP API), `seaborn` (trực quan hóa thống kê nâng cao, xây trên Matplotlib).

Cài thư viện bên thứ ba bằng `pip install ten_thu_vien` — nên dùng virtual environment để tránh xung đột phiên bản giữa các dự án.

### Kết nối cơ sở dữ liệu (SQLite/SQL cơ bản)

- **SQLite**: database engine nhẹ, không cần server, không cần cấu hình — lưu toàn bộ dữ liệu trong một file `.db` duy nhất. Rất phù hợp để lưu kết quả thực nghiệm cục bộ.

- Module `sqlite3` có sẵn trong Python, dùng để thao tác với SQLite.

- **SQL (Structured Query Language)** là ngôn ngữ truy vấn dùng để quản lý cơ sở dữ liệu quan hệ, với 4 lệnh CRUD chính:

| Lệnh SQL | Mục đích |
| --- | --- |
| `SELECT` | Truy xuất dữ liệu |
| `INSERT` | Thêm dữ liệu |
| `UPDATE` | Sửa dữ liệu |
| `DELETE` | Xóa dữ liệu |
| `CREATE TABLE` | Tạo bảng |

#### Kết nối và tạo bảng

```python
import sqlite3

conn = sqlite3.connect("nckh_results.db")   # Mở (hoặc tạo mới) database
cur = conn.cursor()                          # Tạo cursor để chạy lệnh SQL

cur.execute("""
CREATE TABLE IF NOT EXISTS experiments (
    id INTEGER PRIMARY KEY,
    model_name TEXT,
    accuracy REAL,
    run_date TEXT
)
""")
conn.commit()
```

#### CRUD operations

```python
# Create - thêm dữ liệu (dùng dấu ? để tránh SQL injection)
cur.execute(
    "INSERT INTO experiments (model_name, accuracy, run_date) VALUES (?, ?, ?)",
    ("CNN", 0.91, "2026-08-30")
)
conn.commit()

# Read - đọc dữ liệu
cur.execute("SELECT * FROM experiments")
rows = cur.fetchall()
for row in rows:
    print(row)

# Update - cập nhật dữ liệu
cur.execute(
    "UPDATE experiments SET accuracy = ? WHERE model_name = ?",
    (0.93, "CNN")
)
conn.commit()

# Delete - xóa dữ liệu
cur.execute("DELETE FROM experiments WHERE model_name = ?", ("CNN",))
conn.commit()

conn.close()
```

#### Dùng context manager để an toàn hơn

```python
with sqlite3.connect("nckh_results.db") as conn:
    cur = conn.cursor()
    cur.execute("SELECT * FROM experiments")
    for row in cur.fetchall():
        print(row)
# Tự động commit/đóng kết nối khi ra khỏi block with
```

#### Đọc dữ liệu từ SQLite thẳng vào Pandas (kết hợp thực tế trong NCKH)

```python
import pandas as pd
import sqlite3

conn = sqlite3.connect("nckh_results.db")
df = pd.read_sql_query("SELECT * FROM experiments", conn)
conn.close()

print(df.describe())
```

**Best practices:** luôn dùng câu truy vấn có tham số (`?`) thay vì nối chuỗi trực tiếp để tránh SQL injection; luôn `commit()` sau các thao tác ghi (INSERT/UPDATE/DELETE); luôn đóng kết nối (`close()`) hoặc dùng context manager (`with`); xử lý ngoại lệ bằng `try/except` khi thao tác database.

> 📌 **Ghi chú bổ sung:** SQLite phù hợp lưu trữ kết quả thực nghiệm cục bộ (log các lần chạy mô hình, siêu tham số, độ chính xác) để sau này truy vấn/so sánh bằng SQL hoặc load thẳng vào Pandas — thay vì phải quản lý nhiều file CSV rời rạc. Với dữ liệu lớn hơn hoặc cần nhiều người truy cập đồng thời, có thể chuyển sang MySQL/PostgreSQL với cú pháp SQL tương tự.
