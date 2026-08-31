# DSA: Mảng, Chuỗi & Danh sách liên kết

> 🖼️ Trang này tổng hợp từ 8 ảnh ghi chú học tập gốc sau (dán ảnh tương ứng vào từng mục bên dưới khi cần):
> 1. `1321_cam-nang-dsa-arrays-khai-bao-insertion-deletion.jpg`
>
> 2. `1322_cam-nang-dsa-strings-operations-palindrome-anagram.jpg`
>
> 3. `1323_cam-nang-dsa-linked-list-insertion-deletion.jpg`
>
> 4. `1338_ghi-chu-dsa-arrays-strings-khong-lien-quan-ml.jpg`
>
> 5. `1342_ghi-chu-dsa-linked-lists.jpg`
>
> 6. `1407_ghi-chu-ve-cau-truc-du-lieu-mang-arrays.jpg`
>
> 7. `1408_ghi-chu-ve-cau-truc-du-lieu-chuoi-strings.jpg`
>
> 8. `1418_ghi-chu-danh-sach-lien-ket-linked-list.jpg`
>

### Mảng (Arrays)

> 📌 Ảnh thuộc mục này: `1321_cam-nang-dsa-arrays-khai-bao-insertion-deletion.jpg`, `1338_ghi-chu-dsa-arrays-strings-khong-lien-quan-ml.jpg`, `1407_ghi-chu-ve-cau-truc-du-lieu-mang-arrays.jpg`

#### Định nghĩa & biểu diễn bộ nhớ

Mảng (Array) là cấu trúc dữ liệu tuyến tính lưu trữ các phần tử **cùng kiểu dữ liệu** tại các vị trí bộ nhớ **liên tiếp (contiguous)**. Các phần tử được truy cập thông qua chỉ số (index), và ở hầu hết các ngôn ngữ lập trình, indexing bắt đầu từ 0.

Vì bộ nhớ liên tiếp, địa chỉ của phần tử `arr[i]` có thể tính trực tiếp:

```javascript
address(arr[i]) = base_address + (i × kích_thước_1_phần_tử)
```

Ví dụ: nếu `base = 1000` và mỗi số nguyên (int) chiếm 4 byte:

| Index | 0 | 1 | 2 | 3 |
| --- | --- | --- | --- | --- |
| Giá trị | 10 | 20 | 30 | 40 |
| Địa chỉ | 1000 | 1004 | 1008 | 1012 |

#### Khai báo & khởi tạo (ví dụ C++)

```c++
// Khai báo
int arr[5];              // array kích thước 5

// Khởi tạo
int arr1[5] = {1, 2, 3, 4, 5};
int arr2[] = {10, 20, 30, 40};   // size được suy ra
int arr3[5] = {5, 4, 3};         // các phần tử còn lại mặc định là 0
```

**Mảng 1D và 2D:**

```c++
// 1D
int arr[5] = {1, 2, 3, 4, 5};
// Truy cập: arr[0], arr[1], ..., arr[4]

// 2D (ma trận)
int mat[3][4] = {
    {1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}
};
// Truy cập: mat[i][j]  |  Rows = 3, Cols = 4
```

#### Duyệt (Traversal)

```c++
for (int i = 0; i < n; i++) {
    cout << arr[i] << " ";
}
// Time Complexity: O(n)
```

#### Chèn (Insertion)

Chèn phần tử `x` tại vị trí `k` (0 ≤ k ≤ n):

1. Kiểm tra capacity (kích thước mảng còn chỗ trống không).

2. Dịch các phần tử từ vị trí `k` đến `n-1` sang phải một ô.

3. Chèn `x` vào vị trí `k`.

Ví dụ: chèn 25 tại index 2 của `[10, 20, 30, 40, 50]`:

```javascript
Before: 10 20 30 40 50
After:  10 20 25 30 40 50
```

Time Complexity: **O(n)** (trường hợp chèn ở cuối và còn chỗ trống: O(1)).

#### Xóa (Deletion)

Xóa phần tử tại index `k` (0 ≤ k < n):

1. Lưu/xóa phần tử tại `k`.

2. Dịch các phần tử từ `k+1` đến `n-1` sang trái một ô.

3. Giảm kích thước (size) đi 1.

Ví dụ: xóa phần tử tại index 2 của `[10, 20, 30, 40, 50]`:

```javascript
Before: 10 20 30 40 50
After:  10 20 40 50
```

Time Complexity: **O(n)** (trường hợp xóa ở cuối: O(1)).

#### Cập nhật (Updating) & Tìm kiếm (Searching)

- Cập nhật: `arr[k] = newValue;` → **O(1)**

- Tìm kiếm tuyến tính (Linear Search): kiểm tra từng phần tử → hoạt động trên mảng chưa/đã sắp xếp → **O(n)**

- Tìm kiếm nhị phân (Binary Search): chỉ hoạt động trên mảng **đã sắp xếp (sorted)** → **O(log n)**

#### Ưu điểm & Nhược điểm

**Ưu điểm**

- Truy cập ngẫu nhiên (random access) trong O(1)

- Đơn giản để hiểu và cài đặt

- Thân thiện với cache (cache-friendly) do bộ nhớ liên tiếp

- Duyệt (traversal) dễ dàng

**Nhược điểm**

- Kích thước cố định (static ở nhiều ngôn ngữ), khó tăng/giảm

- Insertion/Deletion tốn kém — O(n)

- Yêu cầu một khối bộ nhớ liên tiếp

#### Ứng dụng thực tế

Lưu danh sách/mục điểm số · Ma trận và biểu diễn bảng · Triển khai các cấu trúc dữ liệu khác (Stack, Queue, Heap) · Tìm kiếm (Linear/Binary Search) · Đếm tần suất và băm (hashing)

#### Bảng độ phức tạp thời gian tổng hợp

| Thao tác | Tốt nhất | Trung bình | Xấu nhất | Bộ nhớ (space) |
| --- | --- | --- | --- | --- |
| Truy cập (access) | O(1) | O(1) | O(1) | O(n) |
| Tìm kiếm (chưa sắp xếp) | O(1)* | O(n) | O(n) | O(1) |
| Tìm kiếm (đã sắp xếp - binary) | O(1)* | O(log n) | O(log n) | O(1) |
| Chèn (insertion) | O(1) (ở cuối) | O(n) | O(n) | O(1) |
| Xóa (deletion) | O(1) (ở cuối) | O(n) | O(n) | O(1) |
| Duyệt (traversal) | O(n) | O(n) | O(n) | O(1) |

*Nếu phần tử mục tiêu là phần tử đầu tiên.

#### Các pattern thường gặp khi phỏng vấn với Array

- **Two Pointers** — dùng hai con trỏ duyệt mảng từ hai đầu hoặc cùng chiều để giảm độ phức tạp.

- **Prefix Sum / Cumulative Sum** — `prefix[i] = prefix[i-1] + a[i]`, dùng để tính tổng đoạn con nhanh chóng.
    - Ví dụ: `a = [2, 3, -1, 4]` → `prefix = [2, 5, 4, 8]`

- **Sliding Window** — duy trì một cửa sổ (window) trượt trên mảng để tính toán trên đoạn con liên tiếp.

- **Kadane's Algorithm** (Max Subarray) — tìm tổng đoạn con liên tiếp lớn nhất.

- **Frequency Counting** — đếm số lần xuất hiện của phần tử bằng hash map hoặc mảng đếm.

- **In-place vs Extra Space**: xử lý *in-place* (sửa trực tiếp trên mảng đầu vào, tiết kiệm bộ nhớ O(1)) so với dùng *extra space* (mảng/map phụ, đôi khi code đơn giản hơn).

> ⚠️ Lỗi thường gặp: off-by-one trên biên slice/subarray `arr[l...r]` — cần xác định rõ `l` và `r` là inclusive hay exclusive.

---

### Chuỗi (Strings)

> 📌 Ảnh thuộc mục này: `1322_cam-nang-dsa-strings-operations-palindrome-anagram.jpg`, `1338_ghi-chu-dsa-arrays-strings-khong-lien-quan-ml.jpg`, `1408_ghi-chu-ve-cau-truc-du-lieu-chuoi-strings.jpg`

#### Chuỗi là gì?

String là một dãy các ký tự (characters) dùng để biểu diễn văn bản (text). Về bản chất, trong hầu hết các ngôn ngữ, **string chính là một mảng ký tự**. Chỉ số (indexing) trong string cũng bắt đầu từ 0.

Ví dụ: `str = "HELLO"`

| Index | 0 | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- | --- |
| Ký tự | H | E | L | L | O |

Ở hầu hết ngôn ngữ (VD: Java, C++ `string`, Python), string mặc định là **immutable** (không thể thay đổi sau khi tạo) — mỗi lần "sửa" thực chất tạo ra một đối tượng string mới.

#### Duyệt chuỗi (Traversal)

```c++
string str = "HELLO";
for (int i = 0; i < str.length(); i++) {
    cout << str[i] << " ";
}
// Output: H E L L O
```

#### Các thao tác cơ bản với chuỗi

| Thao tác | Cách dùng (ví dụ C++) | Độ phức tạp |
| --- | --- | --- |
| Độ dài (length) | `str.length()` | O(1) |
| Truy cập ký tự tại index i | `str[i]` / `s.charAt(i)` | O(1) |
| Nối chuỗi (concatenation) | `str1 + str2` | O(n) |
| Chuỗi con (substring) | `str.substr(start, len)` | O(n) |
| So sánh (compare) | `str1 == str2` hoặc `str1.compare(str2)` | O(n) |
| Tìm 1 ký tự/chuỗi con | `str.find('x')` / `indexOf` | O(n) |
| Thay thế (replace) | `str.replace(pos, len, "new")` | O(n) |
| Tách chuỗi (split) | `str.split("delim")` | O(n) |
| Đổi kiểu chữ | `tolower()`, `toupper()` | O(n) |

**Các method String phổ biến trong C++ STL:**

| Method | Mô tả | Ví dụ |
| --- | --- | --- |
| `length()` | Trả về độ dài string | `str.length()` |
| `substr(pos,len)` | Trả về substring từ pos, độ dài len | `str.substr(1,3)` |
| `find(ch/str)` | Trả về index xuất hiện đầu tiên | `str.find('a')` |
| `rfind(ch/str)` | Trả về index xuất hiện cuối cùng | `str.rfind('a')` |
| `replace(pos,len,s)` | Thay thế len ký tự tại pos | `str.replace(2,1,"X")` |
| `erase(pos,len)` | Xóa len ký tự từ pos | `str.erase(1,2)` |
| `insert(pos,s)` | Chèn str tại vị trí pos | `str.insert(2,"XY")` |

#### Đảo ngược chuỗi (Reverse a String)

Ví dụ: `"HELLO"` → `"OLLEH"`

```c++
string rev = "";
for (int i = str.length() - 1; i >= 0; i--)
    rev += str[i];
// rev = "OLLEH"
```

#### Kiểm tra Palindrome

Một string là **palindrome** nếu đọc xuôi và đọc ngược giống nhau.

Ví dụ: `"MADAM"` → đọc xuôi `M-A-D-A-M`, đọc ngược cũng `M-A-D-A-M` → **Is Palindrome? → Yes**

```python
def is_palindrome(s: str) -> bool:
    s = s.lower()
    return s == s[::-1]

print(is_palindrome("MADAM"))  # True
print(is_palindrome("HELLO"))  # False
```

Cách khác dùng hai con trỏ (two pointers) — tối ưu hơn vì không cần tạo chuỗi đảo mới:

```python
def is_palindrome_two_pointers(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
```

Độ phức tạp: **O(n)** thời gian, O(1) hoặc O(n) bộ nhớ tùy cách làm.

#### Kiểm tra Anagram

Hai string là **anagram** của nhau nếu chứa cùng các ký tự với cùng tần suất (chỉ khác thứ tự).

Ví dụ: `"LISTEN"` và `"SILENT"` → **Are Anagrams? → Yes**

```python
def is_anagram(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    return sorted(s1.lower()) == sorted(s2.lower())

print(is_anagram("listen", "silent"))  # True
```

Cách tối ưu hơn dùng đếm tần suất (frequency counting), tránh chi phí sort O(n log n):

```python
from collections import Counter

def is_anagram_counting(s1: str, s2: str) -> bool:
    return Counter(s1.lower()) == Counter(s2.lower())
```

#### Đếm tần suất ký tự (Character Frequency Counting)

Ví dụ: `str = "aabac"` → tần suất: a=3, b=1, c=1

```c++
unordered_map<char, int> freq;
for (char ch : str) freq[ch]++;
```

```python
from collections import Counter
freq = Counter("aabac")   # Counter({'a': 3, 'b': 1, 'c': 1})
```

#### Mutable vs Immutable String

| Immutable String | Mutable String |
| --- | --- |
| Không thể thay đổi sau khi tạo. Mỗi lần "sửa" tạo ra 1 string mới. Ví dụ: `string` (C++), Java `String`. Thường được lưu trong String Pool (Java) để tối ưu bộ nhớ. | Có thể thay đổi sau khi tạo, hiệu quả hơn khi sửa đổi liên tục. Ví dụ: `StringBuilder` (Java). Thay đổi diễn ra trên cùng đối tượng, không lưu trong String Pool. |

```java
// Immutable
String s = "abc";
s = s + "d";  // tạo đối tượng mới "abcd"

// Mutable
StringBuilder sb = new StringBuilder("abc");
sb.append("d");  // sửa trực tiếp -> "abcd"
```

#### Bảng độ phức tạp thời gian các thao tác chuỗi

| Thao tác | Tốt nhất | Trung bình | Xấu nhất |
| --- | --- | --- | --- |
| Truy cập (charAt(i)) | O(1) | O(1) | O(1) |
| Độ dài (length()) | O(1) | O(1) | O(1) |
| Nối chuỗi (s1+s2) | O(n) | O(n) | O(n) |
| Chuỗi con (substring) | O(1)* | O(n) | O(n) |
| So sánh (equals) | O(1)* | O(n) | O(n) |
| Tìm kiếm (indexOf) | O(1)* | O(n) | O(n) |
| Thay thế (replace) | O(n) | O(n) | O(n) |
| Tách (split) | O(n) | O(n) | O(n) |

*Trường hợp tốt nhất khi ký tự đầu tiên khớp/được tìm thấy ngay vị trí đầu.

#### Các pattern thường gặp khi phỏng vấn với String

Check Palindrome · Check Anagram · Reverse a String · Find First Non-Repeating Character · Longest Substring Without Repeating Characters · String Compression · Tiền tố chung dài nhất (Longest Common Prefix) · Chuyển chuỗi thành số nguyên (atoi) · Đếm nguyên âm và phụ âm · Kiểm tra một chuỗi có phải là xoay vòng (rotation) của chuỗi khác

> 💡 Mẹo phỏng vấn: luôn làm rõ string là **mutable** hay **immutable** trong ngôn ngữ bạn dùng — điều này ảnh hưởng trực tiếp đến độ phức tạp khi sửa đổi chuỗi liên tục.

---

### Danh sách liên kết (Linked List)

> 📌 Ảnh thuộc mục này: `1323_cam-nang-dsa-linked-list-insertion-deletion.jpg`, `1342_ghi-chu-dsa-linked-lists.jpg`, `1418_ghi-chu-danh-sach-lien-ket-linked-list.jpg`

#### Linked List là gì?

Linked List là một cấu trúc dữ liệu tuyến tính (linear data structure), trong đó các phần tử được lưu trong các **node**. Mỗi node chứa dữ liệu (data) và con trỏ (pointer/address) tới node kế tiếp. Các node **không** được lưu ở các vị trí bộ nhớ liên tiếp (non-contiguous) — chúng được kết nối với nhau bằng con trỏ.

**Cấu trúc Node** (singly linked list):

```javascript
| data | next |
```

- **Head**: trỏ tới node đầu tiên.

- **Tail**: trỏ tới node cuối cùng; ở node cuối, `next = NULL`.

#### Singly Linked List

```javascript
HEAD → [10|•] → [20|•] → [30|•] → [40|NULL]
```

**Class Node cơ bản (Python):**

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next
```

#### Duyệt (Traversal)

```c++
Node* temp = head;
while (temp != NULL) {
    cout << temp->data << " ";
    temp = temp->next;
}
// Time Complexity: O(n)
```

#### Chèn (Insertion)

**a) Chèn ở đầu (Insert at Beginning)** — O(1)

- Tạo node mới → `newNode->next = head` → `head = newNode`

```python
def insert_at_beginning(self, value):
    new_node = Node(value)
    new_node.next = self.head
    self.head = new_node
```

**b) Chèn ở cuối (Insert at End)** — O(n) (O(1) nếu có sẵn con trỏ tail)

- Tạo node mới → duyệt tới node cuối → `last->next = newNode` → `newNode->next = NULL`

```python
def insert_at_end(self, value):
    new_node = Node(value)
    if not self.head:
        self.head = new_node
        return
    temp = self.head
    while temp.next:
        temp = temp.next
    temp.next = new_node
```

**c) Chèn tại một vị trí (pos)** — O(n)

- Duyệt tới node ở vị trí `pos-1` → `newNode->next = curr->next` → `curr->next = newNode`

Ví dụ: chèn 25 vào vị trí 2 của `10 → 20 → 30 → 40`:

```javascript
Sau khi chèn: 10 → 25 → 20 → 30 → 40
```

#### Xóa (Deletion)

**a) Xóa đầu (Delete from Beginning)** — O(1): `temp = head`, `head = head->next`, `delete temp`

**b) Xóa cuối (Delete from End)** — O(n): duyệt tới node kế cuối, `secondLast->next = NULL`, `delete lastNode`

**c) Xóa theo giá trị/vị trí (Delete by Value/Position)** — O(n): tìm node cần xóa (giữ `prev` và `curr`), `prev->next = curr->next`, `delete curr`

```python
def delete_by_value(self, value):
    if not self.head:
        return
    if self.head.data == value:
        self.head = self.head.next
        return
    prev, curr = self.head, self.head.next
    while curr and curr.data != value:
        prev, curr = curr, curr.next
    if curr:
        prev.next = curr.next
```

> ⚠️ Lỗi thường gặp: mất con trỏ tới phần còn lại của list khi thay đổi liên kết sai thứ tự (ví dụ gán `next = NULL` trước khi lưu lại phần còn lại) — sẽ làm mất quyền truy cập vào toàn bộ phần đuôi của danh sách. Luôn lưu `next` vào biến tạm trước khi thay đổi con trỏ.

#### Doubly Linked List

Mỗi node có 3 phần: `prev | data | next`. Có thể duyệt (traversal) theo cả hai chiều (thuận và ngược).

```javascript
NULL ← [•10•] ↔ [•20•] ↔ [•30•] → NULL
```

```python
class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
```

#### Circular Linked List

Node cuối trỏ ngược về node đầu (không có `NULL` ở cuối).

```javascript
HEAD → 10 → 20 → 30 → (quay lại 10)
```

#### Mẹo thực hành

- Dùng **dummy head / dummy node** để đơn giản hóa các trường hợp biên (danh sách rỗng, chèn/xóa tại head).

- Dùng tên biến rõ nghĩa; xử lý trường hợp biên (danh sách rỗng, chỉ có một node); giải phóng bộ nhớ trong C/C++ để tránh rò rỉ (memory leak).

> ⚠️ Lỗi thường gặp: quên cập nhật con trỏ `head`; mất tham chiếu tới node kế trong khi xóa; không kiểm tra điều kiện `NULL`.

#### So sánh Array vs Linked List

| Đặc điểm | Array | Linked List |
| --- | --- | --- |
| Bộ nhớ | Liên tiếp (contiguous) | Không liên tiếp (non-contiguous) |
| Kích thước | Cố định (fixed) | Động (dynamic) |
| Insertion/Deletion | Tốn kém — O(n) | Hiệu quả — O(1)* (nếu có sẵn con trỏ tới vị trí) |
| Truy cập (access) | Ngẫu nhiên (random) — O(1) | Tuần tự (sequential) — O(n) |
| Memory overhead | Ít hơn | Nhiều hơn (do lưu thêm con trỏ) |

*Tại vị trí đã biết (nếu node được cho sẵn).

#### Bảng độ phức tạp thời gian (Singly / Doubly / Circular)

| Thao tác | Đơn (Singly) | Đôi (Doubly) | Vòng (Circular) |
| --- | --- | --- | --- |
| Chèn đầu | O(1) | O(1) | O(1) |
| Chèn cuối | O(n) | O(n) | O(n)* |
| Chèn tại vị trí | O(n) | O(n) | O(n) |
| Xóa đầu | O(1) | O(1) | O(1) |
| Xóa cuối | O(n) | O(n) | O(n)* |
| Xóa tại vị trí | O(n) | O(n) | O(n) |
| Tìm kiếm | O(n) | O(n) | O(n) |

*O(1) nếu giữ con trỏ tail (đặc biệt hữu ích cho Circular Linked List).

#### Các pattern thường gặp khi phỏng vấn với Linked List

- **Đảo ngược một Linked List** (Reverse a Linked List)

- **Phát hiện chu trình / vòng lặp** (Floyd's Tortoise & Hare / Cycle Detection)

- **Tìm node ở giữa** bằng Slow & Fast Pointers

- **Merge hai linked list đã sắp xếp** (Merge Two Sorted Lists)

```python
# Ví dụ: đảo ngược singly linked list
def reverse(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev  # head mới
```

---

> 📝 **Ghi chú bổ sung**
> - Ba bộ ghi chú gốc dùng ký hiệu và ngôn ngữ code hơi khác nhau (C++ trong hai bộ đầu, một số ví dụ Python được bổ sung ở đây để minh họa thêm) — về bản chất khái niệm và độ phức tạp là nhất quán giữa các nguồn.
>
> - Với Linked List, "O(1)" cho insertion/deletion chỉ đúng **khi đã có sẵn con trỏ tới vị trí cần thao tác**; nếu phải tìm vị trí trước thì tổng chi phí vẫn là O(n) do bước duyệt tìm kiếm.
>
> - Nên luyện tập cài đặt tay cả ba cấu trúc (Array, String, Linked List) bằng ít nhất một ngôn ngữ để nắm vững thao tác con trỏ/index trước khi làm bài tập nâng cao (Stack, Queue, Tree...).
>
