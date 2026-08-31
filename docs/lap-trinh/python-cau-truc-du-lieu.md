# Python: Cấu trúc dữ liệu (String, List, Tuple, Set, Dict)

> 🖼️ Trang này tổng hợp từ 5 ảnh ghi chú/cheat sheet gốc:
> 1. 1376_cheat-sheet-python-strings-indexing-slicing-format.jpg
>
> 2. 1377_cheat-sheet-python-collections-list-tuple-set-dict.jpg
>
> 3. 1429_ghi-chu-python-chuoi-strings-va-danh-sach-lists.jpg
>
> 4. 1430_ghi-chu-python-tuple-creation-indexing-methods.jpg
>
> 5. 1431_ghi-chu-python-sets-va-dictionaries.jpg
>

### Strings

String là chuỗi ký tự đặt trong `'...'`, `"..."` hoặc `"""..."""`. **String là immutable** (không thể thay đổi sau khi tạo).

```python
s1 = 'Hello'          # single quoted
s2 = "Python"         # double quoted
s3 = """Multi
line string"""        # triple quoted
```

#### Indexing & Slicing

Chỉ số bắt đầu từ 0; chỉ số âm đếm từ cuối (`-1` là ký tự cuối cùng).

```python
s = "Python"
s[0]    # 'P'
s[3]    # 'h'
s[-1]   # 'n'
s[-2]   # 'o'

s = "Hello, World!"
s[0:5]    # 'Hello'      -> slicing: s[start:end:step], end bị loại trừ
s[7:]     # 'World!'
s[:5]     # 'Hello'
s[::2]    # 'Hlo ol!'    -> cách nhau 2 ký tự
s[::-1]   # '!dlroW ,olleH'  -> đảo ngược chuỗi
```

Lưu ý: `start` mặc định = 0, `end` mặc định = `len(s)`, `step` mặc định = 1.

#### Formatting: f-string, `.format()`, `%`

```python
name, age = "Alice", 25

# % formatting (cũ)
'Name: %s, tuổi %d' % (name, age)

# str.format()
'Name: {}, tuổi {}'.format(name, age)

# f-string (Python 3.6+, khuyến nghị)
f"Name: {name}, tuổi {age}"
# 'Name: Alice, tuổi 25'
```

f-string cho phép nhúng cả biểu thức: `f"{age * 2}"`.

#### Các thao tác & method phổ biến

| Thao tác/Method | Ví dụ | Kết quả |
| --- | --- | --- |
| Nối chuỗi | `'Hello'+' '+'Python'` | `'Hello Python'` |
| Lặp chuỗi | `'Hi'*3` | `'HiHiHi'` |
| Độ dài | `len('Python')` | `6` |
| Kiểm tra tồn tại | `'Py' in 'Python'` | `True` |
| `.upper()` | `'py'.upper()` | `'PY'` |
| `.lower()` | `'PY'.lower()` | `'py'` |
| `.capitalize()` | `'python'.capitalize()` | `'Python'` |
| `.title()` | `'hello world'.title()` | `'Hello World'` |
| `.strip()` | `' hi '.strip()` | `'hi'` |
| `.replace(old,new)` | `'a_b_c'.replace('_','-')` | `'a-b-c'` |
| `.find(x)` | `'hello'.find('e')` | `1` |
| `.split(sep)` | `'a,b,c'.split(',')` | `['a','b','c']` |
| `.join(list)` | `'-'.join(['a','b','c'])` | `'a-b-c'` |
| `.count(x)` | `'banana'.count('a')` | `3` |

⚠️ **Lỗi thường gặp**: string là immutable, không thể gán trực tiếp `s[0] = 'H'` (lỗi). Phải tạo chuỗi mới: `s = 'H' + s[1:]`.

### List

List là tập hợp **có thứ tự**, **mutable** (thay đổi được), **cho phép trùng lặp**, hỗ trợ index/slicing như string.

```python
empty_list = []
nums = [1, 2, 3, 4, 5]
mixed = [1, 'hi', 3.5, True]     # chứa nhiều kiểu dữ liệu
nested = [1, [2, 3], 'abc']      # list lồng nhau
```

#### Indexing & Slicing

```python
nums = [10, 20, 30, 40, 50]
nums[0]     # 10
nums[2]     # 30
nums[-1]    # 50
nums[-2]    # 40

nums[1:4]   # [20, 30, 40]
nums[:3]    # [10, 20, 30]
nums[2:]    # [30, 40, 50]
nums[::2]   # [10, 30, 50]
nums[::-1]  # [50, 40, 30, 20, 10]
```

#### List Methods (mutable → có thể thay đổi tại chỗ)

| Method | Mô tả | Ví dụ | Kết quả |
| --- | --- | --- | --- |
| `append(x)` | Thêm phần tử vào cuối | `lst.append(5)` | `[1,2,3,5]` |
| `insert(i, x)` | Chèn tại vị trí i | `lst.insert(1, 9)` | `[1,9,2,3,5]` |
| `extend(iter)` | Thêm tất cả phần tử từ iterable | `lst.extend([4,5])` | `[1,2,3,4,5]` |
| `remove(x)` | Xóa lần xuất hiện đầu tiên | `lst.remove(2)` | `[1,3]` |
| `pop([i])` | Xóa & trả về phần tử | `lst.pop()` | `3` |
| `index(x)` | Trả về vị trí của x | `lst.index(2)` | `1` |
| `count(x)` | Đếm số lần xuất hiện | `lst.count(1)` | `2` |
| `sort()` | Sắp xếp list | `lst.sort()` | `[1,2,3]` |
| `reverse()` | Đảo ngược list | `lst.reverse()` | `[3,2,1]` |
| `clear()` | Xóa tất cả phần tử | `lst.clear()` | `[]` |

#### Nested list (list lồng nhau)

```python
matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix[0]      # [1, 2, 3]
matrix[1][2]   # 6
matrix[2][0]   # 7
```

**List là mutable**: có thể thay đổi trực tiếp một phần tử mà không tạo object mới.

```python
lst = [1, 2, 3]
lst[0] = 100
print(lst)   # [100, 2, 3]  -> cùng một object, chỉ giá trị thay đổi
```

### Tuple

Tuple là tập hợp **có thứ tự**, **immutable** (không đổi được sau khi tạo), **cho phép trùng lặp**. Tuple nhanh hơn list vì bất biến.

```python
empty_tuple = ()
numbers = (1, 2, 3, 4)
mixed = (1, "hi", 3.14, True)
single = (5,)          # chú ý dấu phẩy để tạo tuple 1 phần tử
nested = (1, (2, 3), 'abc')
```

#### Indexing & Slicing (giống list)

```python
t = ('p', 'y', 't', 'h', 'o', 'n')
t[0]    # 'p'
t[3]    # 'h'
t[-1]   # 'n'

t = (10, 20, 30, 40, 50, 60)
t[1:4]    # (20, 30, 40)
t[::2]    # (10, 30, 50)
t[::-1]   # (60, 50, 40, 30, 20, 10)
```

#### Tuple methods

Tuple chỉ có **2 method** dựng sẵn (không có `append`, `remove`, `pop`... vì immutable):

| Method | Mô tả | Ví dụ | Kết quả |
| --- | --- | --- | --- |
| `count(x)` | Số lần xuất hiện của x | `(1,2,2,3,2).count(2)` | `3` |
| `index(x)` | Vị trí xuất hiện đầu tiên của x | `(10,20,30,20).index(20)` | `1` |

#### Packing & Unpacking

```python
# Packing: gộp nhiều giá trị vào 1 tuple
t = 1, 2, 3, 4, 5
print(t)          # (1, 2, 3, 4, 5)

# Unpacking: gán các phần tử ra nhiều biến
a, b, c = (10, 20, 30)
print(a, b, c)    # 10 20 30

# Unpacking mở rộng (Python 3+) dùng *
t = (1, 2, 3, 4, 5, 6)
a, b, *rest, last = t
print(a, b, rest, last)   # 1 2 [3, 4, 5] 6
```

#### Khi nào dùng Tuple thay vì List?

- Dữ liệu **không nên bị thay đổi** trong suốt vòng đời chương trình (ví dụ: tọa độ, hằng số, cấu hình).

- Cần **hiệu năng cao hơn** list (tuple nhẹ và nhanh hơn).

- Cần dùng làm **key của dictionary** hoặc phần tử trong `set` (list không hashable nên không dùng được).

- Hàm cần **trả về nhiều giá trị** cùng lúc (dùng tuple packing).

### Set & Dictionary

#### Set

Set là tập hợp **không có thứ tự**, các phần tử **duy nhất** (không trùng lặp), phần tử phải là kiểu bất biến (không thể là list/dict/set). Set **không hỗ trợ index**.

```python
empty_set = set()             # set rỗng, KHÔNG dùng {}
numbers = {1, 2, 3, 4, 5}
letters = set('python')       # {'p','y','t','h','o','n'}
```

Set methods

| Method | Mô tả | Ví dụ | Kết quả |
| --- | --- | --- | --- |
| `add(x)` | Thêm một phần tử | `s.add(3)` | thêm 3 vào s |
| `update(iter)` | Thêm nhiều phần tử | `s.update([3,4])` | gộp thêm 3,4 |
| `remove(x)` | Xóa x, lỗi nếu không có | `s.remove(2)` | xóa 2 |
| `discard(x)` | Xóa x, không lỗi nếu không có | `s.discard(5)` | an toàn hơn remove |
| `pop()` | Xóa & trả về phần tử ngẫu nhiên | `s.pop()` | phần tử bất kỳ |
| `clear()` | Xóa tất cả | `s.clear()` | `set()` |

Các phép toán tập hợp

```python
a = {1, 2, 3, 4}
b = {3, 4, 5}

a | b   # union         -> {1, 2, 3, 4, 5}   (a.union(b))
a & b   # intersection  -> {3, 4}            (a.intersection(b))
a - b   # difference    -> {1, 2}            (a.difference(b))
b - a   # difference    -> {5}
```

#### Dictionary

Dictionary lưu dữ liệu theo cặp **key : value**. Key phải duy nhất và bất biến (immutable); value có thể là bất kỳ kiểu nào.

```python
empty_dict = {}
student = {'name': 'Abhi', 'age': 20, 'grade': 'A'}
marks = dict(math=95, eng=88, sci=90)

student['name']   # 'Abhi'
student['age']    # 20
```

Dictionary methods

| Method | Mô tả | Ví dụ | Kết quả |
| --- | --- | --- | --- |
| `keys()` | Trả về tất cả key | `d.keys()` | `dict_keys(['a','b'])` |
| `values()` | Trả về tất cả value | `d.values()` | `dict_values([1,2])` |
| `items()` | Trả về cặp key-value | `d.items()` | `dict_items([('a',1),('b',2)])` |
| `get(key, default)` | Lấy giá trị, tránh KeyError | `d.get('x', 0)` | `0` nếu không có key |
| `update(other)` | Cập nhật key-value mới | `d.update({'b':3})` | ghi đè/thêm key |
| `pop(key, default)` | Xóa key & trả về giá trị | `d.pop('a')` | giá trị đã xóa |
| `popitem()` | Xóa cặp chèn cuối cùng (3.7+) | `d.popitem()` | `('b', 2)` |
| `clear()` | Xóa tất cả phần tử | `d.clear()` | `{}` |

```python
d = {'a': 1, 'b': 2}
d['c'] = 3
d.update({'b': 20})
print(d)             # {'a': 1, 'b': 20, 'c': 3}
print(d.get('z', 0)) # 0 -> tránh KeyError khi key không tồn tại
```

Nested dictionary

```python
student = {
    'name': 'Abhi',
    'age': 20,
    'marks': {'math': 95, 'eng': 88, 'sci': 90},
    'address': {'city': 'Delhi', 'pin': 110001}
}
student['marks']['math']       # 95
student['address']['city']     # 'Delhi'
```

#### Khi nào dùng Set / Dictionary?

- **Set**: cần loại bỏ trùng lặp, kiểm tra thành viên (`in`) rất nhanh, hoặc thực hiện các phép toán tập hợp (union, intersection...).

- **Dictionary**: cần tra cứu nhanh theo key, lưu dữ liệu có cấu trúc dạng JSON, cấu hình, hồ sơ người dùng, caching.

### Bảng so sánh 4 cấu trúc dữ liệu

| Đặc điểm | List | Tuple | Set | Dictionary |
| --- | --- | --- | --- | --- |
| Mutable (thay đổi được)? | Có | Không | Có (nhưng phần tử phải bất biến) | Có |
| Có thứ tự? | Có | Có | Không | Có (từ Python 3.7+, theo thứ tự chèn) |
| Cho phép phần tử trùng? | Có | Có | Không | Key: không / Value: có |
| Cú pháp khởi tạo | `[1, 2, 3]` | `(1, 2, 3)` | `{1, 2, 3}` | `{'k': 'v'}` |
| Hỗ trợ indexing? | Có | Có | Không | Không (truy cập theo key) |

> 📝 **Ghi chú bổ sung**
> - Cả 4 cấu trúc đều có thể lồng nhau (list trong list, dict trong dict...) để biểu diễn dữ liệu phức tạp như ma trận hay JSON.
>
> - Chỉ tuple và các kiểu bất biến khác (string, số, tuple) mới có thể dùng làm key của dictionary hoặc phần tử của set.
>
> - Ưu tiên dùng `get()` với dictionary và `discard()` với set để tránh lỗi khi key/phần tử không tồn tại.
>
