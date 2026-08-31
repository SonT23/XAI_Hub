# Python: Automation, Best Practices & Ôn tập tổng hợp

> 🖼️ **Tổng hợp từ 5 ảnh ghi chú gốc (bộ CamNangPython & Ghi chú Python):**
> 1. 1385_automation-python-file-organizer-csv-processor-api.jpg
>
> 2. 1386_python-best-practices-pep8-cau-truc-du-an-dat-ten-.jpg
>
> 3. 1387_python-ultimate-cheat-sheet-on-tap-phong-van-tong-.jpg
>
> 4. 1443_ghi-chu-python-giai-quyet-van-de-searching-sorting.jpg
>
> 5. 1444_ghi-chu-python-bai-tap-thuc-hanh-va-cau-hoi-phong-.jpg
>

### Automation với Python

Python giúp tự động hóa các tác vụ lặp lại, xử lý dữ liệu, tương tác API và quản lý hệ thống hiệu quả — rất phổ biến trong DevOps/SRE (cấp phát server, Docker, CI/CD, giám sát log, bảo trì hạ tầng).

#### 1. File Organizer — sắp xếp file tự động theo phần mở rộng

```python
import os, shutil

for file in os.listdir('src'):
    ext = file.split('.')[-1]
    os.makedirs(ext, exist_ok=True)
    shutil.move(f'src/{file}', f'{ext}/')
```

**Ứng dụng:** giữ thư mục downloads/reports gọn gàng tự động.

#### 2. CSV Processor — đọc, lọc, biến đổi và ghi lại dữ liệu CSV

```python
import csv

with open('input.csv') as f:
    reader = csv.DictReader(f)
    with open('output.csv', 'w') as o:
        writer = csv.DictWriter(o, fieldnames=reader.fieldnames)
        writer.writeheader()
        for row in reader:
            if row['status'] == 'active':   # ví dụ lọc thêm
                writer.writerow(row)
```

**Ứng dụng:** xử lý báo cáo, lọc dữ liệu, tạo tóm tắt.

#### 3. Log Analyzer — trích lỗi/sự kiện quan trọng từ file log

```python
errors = []
with open('app.log') as f:
    for line in f:
        if 'ERROR' in line:
            errors.append(line.strip())
print(f"Total: {len(errors)}")
```

**Ứng dụng:** giám sát ứng dụng, theo dõi sự cố.

#### 4. REST API Caller — gọi API bằng module `requests`

```python
import requests

url = "https://api.example.com/users"
res = requests.get(url, timeout=5)
res.raise_for_status()
data = res.json()
print(data['name'])
```

**Ví dụ bổ sung — POST dữ liệu lên API:**

```python
payload = {"name": "Alice", "role": "admin"}
res = requests.post("https://api.example.com/users", json=payload, timeout=5)
print(res.status_code, res.json())
```

**Ứng dụng:** kiểm tra API, lấy dữ liệu, tích hợp hệ thống.

#### 5. Folder Backup — tạo bản backup có timestamp

```python
import shutil, datetime

src = 'important_data/'
backup = f"backup_{datetime.datetime.now():%Y%m%d}.zip"
shutil.make_archive(backup.replace('.zip', ''), 'zip', src)
```

**Ứng dụng:** backup hằng ngày, an toàn dữ liệu, khôi phục sự cố.

#### 6. Automation Scripts — kết hợp nhiều bước thành pipeline

`Đọc File → Xử lý → Sinh Report`

**Ứng dụng:** tự động hóa quy trình nghiệp vụ từ đầu đến cuối (ví dụ: đọc CSV → làm sạch dữ liệu → gọi API cập nhật → gửi báo cáo qua email).

#### Ứng dụng trong DevOps

- Tự động cấp phát server (AWS, Azure, GCP)

- Tự động hóa Docker

- Trigger Jenkins jobs (CI/CD)

- Upload log/artifact lên cloud storage

- Giám sát và cảnh báo hệ thống

- Bảo trì hạ tầng & dọn dẹp

**💡 Mẹo hay**

- Dùng `logging` thay vì `print` để dễ theo dõi hơn.

- Xử lý exception mềm dẻo (try/except cụ thể).

- Lập lịch tác vụ bằng cron/Task Scheduler.

**⭐ Best Practices**

- Viết code module hóa, tái sử dụng.

- Dùng config file cho cài đặt (không hardcode).

- Thêm log và validation đầy đủ.

**⚠️ Lỗi thường gặp**

- Hardcode đường dẫn và credentials.

- Bỏ qua exception handling (`except: pass`).

- Chạy tác vụ nặng trên main thread.

---

### Best Practices

Viết code Python sạch, dễ đọc và dễ bảo trì bằng cách tuân theo chuẩn, cấu trúc dự án rõ ràng và tránh các lỗi thường gặp.

#### PEP 8 — chuẩn viết code

- Tuân theo style guide chính thức của Python.

- Dùng 4 dấu cách để thụt lề (không dùng tab).

- Giới hạn độ dài dòng ở 79–99 kí tự.

- Dùng tên có ý nghĩa cho biến và hàm.

- Thêm khoảng trắng quanh toán tử và sau dấu phẩy.

- Giữ code nhất quán và sạch sẽ.

> Mẹo: dùng công cụ như `flake8`, `black`, `pylint` để tự động kiểm tra và format code.

#### Cấu trúc dự án

```javascript
my_project/
  src/
    my_package/
      __init__.py
      core.py
  tests/
    test_core.py
  requirements.txt
  README.md
  .gitignore
```

- Giữ source code trong `src/`

- Tách riêng test trong `tests/`

- Thêm `README.md`

- Bỏ qua file không cần thiết bằng `.gitignore`

#### Quy tắc đặt tên

| Loại | Quy tắc | Ví dụ |
| --- | --- | --- |
| variable_name | snake_case | `user_name` |
| function_name() | snake_case | `calculate_total()` |
| ClassName | PascalCase | `CustomerManager` |
| CONSTANT_NAME | UPPER_SNAKE_CASE | `MAX_RETRY_COUNT` |
| module_[name.py](http://name.py/) | snake_case | `data_utils.py` |

#### Virtual Environments — cách ly dependencies

```bash
# Tạo
python -m venv venv
# Kích hoạt (Windows)
venv\Scripts\activate
# Kích hoạt (Linux/Mac)
source venv/bin/activate
```

Giúp tránh xung đột phiên bản và giữ các package gọn gàng.

#### requirements.txt

```javascript
requests==2.31.0
numpy==1.26.4
pandas==2.2.2
pytest==8.2.0
```

Cài đặt bằng: `pip install -r requirements.txt`

#### Tính dễ đọc của code & docstring

- Viết hàm nhỏ, tập trung một việc.

- Dùng tên có ý nghĩa.

- Thêm comment và **docstring**.

- Tránh lồng nhiều tầng quá sâu.

- Tuân theo nguyên tắc **DRY** (Don't Repeat Yourself).

```python
def add(a, b):
    """Trả về tổng của hai số."""
    return a + b
```

#### Lỗi thường gặp cần tránh

| Lỗi | Ví dụ sai |
| --- | --- |
| Dùng mutable default argument | `def fun(lst=[]):` |
| Không đóng file | `f = open('file.txt')` (nên dùng `with`) |
| Copy-paste code | dẫn đến lỗi và khó bảo trì |
| Bỏ qua exception | `except: pass` |
| Dùng biến global | `global count` |
| Không viết test | luôn kiểm thử code của bạn |
| Hardcode giá trị | `API_KEY = "12345"` |
| Làm code phức tạp quá mức | dùng giải pháp đơn giản, đúng chuẩn Python |

> ⭐ Ghi nhớ: Thói quen tốt hôm nay, code tuyệt vời ngày mai!

---

### Giải quyết vấn đề với Python (Problem Solving)

Rèn tư duy logic và khả năng nhận diện mẫu (pattern) — hỗ trợ phỏng vấn coding và ứng dụng thực tế. **Quy trình:** Xác định pattern → Chọn đúng cách tiếp cận → Chia nhỏ vấn đề → Giải → Tối ưu → Kiểm thử.

#### 1. Searching (Tìm kiếm)

**Linear Search** — O(n), hoạt động trên dữ liệu chưa sắp xếp hoặc đã sắp xếp:

```python
def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1  # Không tìm thấy
```

**Binary Search** — O(log n), chỉ hoạt động trên dữ liệu đã sắp xếp:

```python
def binary_search(arr, target):
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1
```

Ví dụ: `arr = [1,3,5,7,9,11,13]`, `target=7` → Output: `3`

**Khi nào dùng:** Linear cho dữ liệu nhỏ/chưa sắp xếp; Binary cho dữ liệu đã sắp xếp (lớn, nhanh hơn nhiều).

#### 2. Sorting (Sắp xếp)

| Thuật toán | Độ phức tạp | Ghi chú |
| --- | --- | --- |
| Bubble Sort | O(n²) | Hoán đổi liên tục các phần tử liền kề nếu sai thứ tự |
| Selection Sort | O(n²) | Tìm phần tử nhỏ nhất, đặt vào đúng vị trí |
| Merge Sort | O(n log n) | Chia mảng thành hai nửa, sắp xếp rồi trộn lại |

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)  # merge() gộp 2 mảng đã sort
```

**Khi nào dùng:** Bubble/Selection cho dữ liệu nhỏ; Merge Sort cho dữ liệu lớn (ổn định, nhanh). Mẹo: ưu tiên `sorted()`/`.sort()` dựng sẵn trong Python.

#### 3. Two Pointers (Hai con trỏ)

Dùng hai con trỏ (trái & phải) để giải bài toán trong O(n) — phù hợp với mảng đã sắp xếp, cặp đôi, đối xứng (palindrome).

```python
def pair_with_sum(arr, target):
    l, r = 0, len(arr) - 1
    while l < r:
        s = arr[l] + arr[r]
        if s == target:
            return (arr[l], arr[r])
        elif s < target:
            l += 1
        else:
            r -= 1
    return None
```

Ví dụ: `arr = [2,4,6,8,10,14]`, `target=16` → tìm thấy `(2, 14)`.

#### 4. Sliding Window (Cửa sổ trượt)

Duy trì một "cửa sổ" trượt trên mảng/chuỗi để có kết quả trong O(n).

```python
def max_sum_k(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i-k]
        max_sum = max(max_sum, window_sum)
    return max_sum
```

Ví dụ: `arr = [2,1,5,1,3,2]`, `k=3` → cửa sổ `[5,1,3]`, tổng lớn nhất = 9.

**Ứng dụng phổ biến:** mảng con Max/Min kích thước K, chuỗi con dài nhất không lặp ký tự, đếm anagram trong chuỗi.

#### So sánh nhanh

| Kỹ thuật | Phù hợp nhất cho | Time | Space |
| --- | --- | --- | --- |
| Linear Search | Dữ liệu bất kỳ | O(n) | O(1) |
| Binary Search | Dữ liệu đã sort | O(log n) | O(1) |
| Bubble/Selection Sort | Dữ liệu nhỏ | O(n²) | O(1) |
| Merge Sort | Dữ liệu lớn | O(n log n) | O(n) |
| Two Pointers | Đã sort / Cặp đôi | O(n) | O(1) |
| Sliding Window | Mảng con / Chuỗi con | O(n) | O(1) |

> Ghi chú liên hệ: các kỹ thuật Two Pointers, Sliding Window và độ phức tạp thời gian (Big-O) ở trên cũng là nền tảng chung cho các trang Cấu trúc dữ liệu & Giải thuật (DSA) khác trong hub kiến thức — nên tham khảo chéo khi ôn tập LeetCode/HackerRank.

---

### Tổng ôn tập & Câu hỏi phỏng vấn

#### Cheat sheet — các khái niệm cốt lõi

| Chủ đề | Tóm tắt nhanh |
| --- | --- |
| Variables | Không cần khai báo kiểu, dynamic typing (`name = "Alice"`) |
| Data Types | str, int, float, bool, list, dict... |
| Operators | Arithmetic (+ - * / // % **), Comparison, Logical (and/or/not), Membership (in/not in), Identity (is/is not) |
| Conditions | if / elif / else |
| Loops | for, while |
| Functions | `def add(a, b): return a + b` |
| Collections | List (mutable), Tuple (immutable), Set (unique), Dict (key-value) |
| File Handling | `with open('data.txt') as f: content = f.read()` |
| Exceptions | try / except / finally |
| OOP | Class, Object, Inheritance, Encapsulation, Polymorphism |
| Hàm built-in | print, len, type, range, min, max, sum, sorted, enumerate, zip, map, filter, round |
| Module thường dùng | os, sys, math, datetime, json, re |

#### Câu hỏi phỏng vấn lý thuyết (kèm gợi ý trả lời ngắn gọn)

| # | Câu hỏi | Trả lời ngắn gọn |
| --- | --- | --- |
| 1 | Python là gì? | Ngôn ngữ lập trình bậc cao, thông dịch (interpreted), đa mục đích. |
| 2 | Khác nhau giữa list và tuple? | List có thể thay đổi (mutable), tuple thì không (immutable). |
| 3 | Khác nhau giữa `==` và `is`? | `==` so sánh giá trị, `is` so sánh vị trí bộ nhớ (identity). |
| 4 | Dictionary trong Python là gì? | Tập hợp các cặp key-value, không có thứ tự cố định, có thể thay đổi. |
| 5 | `self` dùng để làm gì? | Tham chiếu đến instance hiện tại của class. |
| 6 | Hàm lambda là gì? | Hàm ẩn danh viết trong một dòng, ví dụ `lambda x: x*2`. |
| 7 | Khác nhau giữa `append()` và `extend()`? | `append()` thêm một phần tử; `extend()` thêm từng phần tử từ một iterable. |
| 8 | Recursion (đệ quy) là gì? | Hàm tự gọi lại chính nó để giải bài toán nhỏ hơn. |
| 9 | Module là gì? | File Python chứa hàm, class, biến để tái sử dụng. |
| 10 | PEP 8 là gì? | Python Enhancement Proposal 8 — hướng dẫn phong cách viết code Python chuẩn. |

#### Câu hỏi phỏng vấn dạng coding

| # | Câu hỏi | Hướng tiếp cận |
| --- | --- | --- |
| 1 | Viết chương trình tìm giai thừa của một số. | Dùng vòng lặp hoặc đệ quy. |
| 2 | Viết chương trình kiểm tra số nguyên tố. | Kiểm tra chia hết từ 2 đến sqrt(n). |
| 3 | Viết chương trình đảo ngược một chuỗi. | Dùng slicing `s[::-1]` hoặc vòng lặp. |
| 4 | Tìm phần tử lớn nhất trong list. | Khởi tạo max, duyệt qua list (hoặc dùng `max()`). |
| 5 | Xóa phần tử trùng lặp trong list. | Chuyển list thành set rồi chuyển lại. |
| 6 | Đếm nguyên âm trong chuỗi. | Kiểm tra từng ký tự trong `'aeiouAEIOU'`. |
| 7 | Tìm số lớn thứ hai trong list. | Xóa max, tìm max lần nữa (hoặc sort rồi lấy phần tử áp chót). |

#### Bài tập thực hành đề xuất

- [ ] In bảng cửu chương của n

- [ ] Nhập n số và in tổng của chúng

- [ ] Kiểm tra một chuỗi có phải palindrome không

- [ ] In các phần tử chung của hai list

- [ ] Gộp hai list đã sắp xếp

- [ ] Đếm tần suất mỗi phần tử trong list

- [ ] Chuyển thập phân sang nhị phân

- [ ] Đếm số từ trong câu

- [ ] Sắp xếp list mà không dùng `sort()`

- [ ] Tìm số còn thiếu trong dãy 1 đến n

#### Bài toán thử thách (nâng cao)

- [ ] Cài đặt tìm kiếm nhị phân (binary search)

- [ ] Giải bài toán Tháp Hà Nội (Tower of Hanoi)

- [ ] Kiểm tra hai chuỗi có phải anagram không

- [ ] Tìm tiền tố chung dài nhất (longest common prefix)

- [ ] Cài đặt LRU Cache (cơ bản)

- [ ] Xoay ma trận 90 độ

- [ ] Tìm tất cả chuỗi con của một chuỗi

- [ ] Giải bài toán N-Queens

#### Bảng độ phức tạp thời gian (Big-O)

| Ký hiệu | Tên gọi |
| --- | --- |
| O(1) | Hằng số (Constant) |
| O(log n) | Logarit (Logarithmic) |
| O(n) | Tuyến tính (Linear) |
| O(n log n) | Linearithmic |
| O(n²) | Bậc hai (Quadratic) |
| O(2ⁿ) | Hàm mũ (Exponential) |

#### Mẹo cải thiện & nền tảng luyện tập

- Giải bài hàng ngày (ít nhất 1–2 bài).

- Hiểu rõ trước khi học thuộc.

- Tự viết code, đừng chỉ đọc.

- Kiểm thử các trường hợp biên (edge case).

- Xem lại và phân tích lời giải của mình.

- Nền tảng luyện tập: LeetCode, HackerRank, Codeforces, GeeksforGeeks, InterviewBit, Coding Ninjas, Exercism.

> Tư duy thông minh. Code tốt hơn. Tối ưu mọi lúc!

---

> 📝 **Ghi chú bổ sung:** Trang này tổng hợp và diễn giải lại nội dung từ 5 ảnh ghi chú gốc (đã liệt kê ở đầu trang), có bổ sung một số ví dụ code riêng (POST API, bảng so sánh, liên hệ DSA) để nội dung liền mạch và dễ tra cứu hơn. Khi cần xem lại chi tiết hình ảnh gốc, tham khảo đường dẫn file trong callout đầu trang.
