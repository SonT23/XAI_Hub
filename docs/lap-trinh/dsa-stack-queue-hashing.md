# DSA: Stack, Queue & Hashing

> 🖼️ Trang này tổng hợp từ 7 ảnh ghi chú học tập gốc:
> 1. 1324_cam-nang-dsa-stack-queue-lifo-fifo.jpg
>
> 2. 1325_cam-nang-dsa-hashing-hash-tables-collision.jpg
>
> 3. 1340_ghi-chu-dsa-hashing-hash-maps.jpg
>
> 4. 1341_ghi-chu-dsa-stacks-queues.jpg
>
> 5. 1415_ghi-chu-ve-bam-hashing-hashmap-hashset.jpg
>
> 6. 1416_ghi-chu-cau-truc-du-lieu-ngan-xep-stack.jpg
>
> 7. 1417_ghi-chu-hang-doi-va-deque-queue-deque.jpg
>

Bài viết hợp nhất nội dung của 3 bộ ghi chú (Cẩm nang DSA, DSA Notes, ghi chú viết tay) về chủ đề **Stack, Queue và Hashing**, loại bỏ trùng lặp và giữ lại đầy đủ ý.

### Stack (LIFO)

> 📌 Ảnh thuộc mục này: 1324_cam-nang-dsa-stack-queue-lifo-fifo.jpg, 1341_ghi-chu-dsa-stacks-queues.jpg, 1416_ghi-chu-cau-truc-du-lieu-ngan-xep-stack.jpg

#### Khái niệm

Stack (Ngăn xếp) là một **cấu trúc dữ liệu tuyến tính (linear data structure)** tuân theo nguyên lý **LIFO — Last In First Out** (vào sau, ra trước). Mọi thao tác thêm/xoá đều diễn ra tại một đầu duy nhất gọi là **top** (đỉnh).

Ví dụ trực quan: `push(10) → push(20) → push(30) → pop() → pop()` cho ra thứ tự lấy ra là 30, 20 — phần tử vào sau cùng bị lấy ra trước tiên.

#### Các thao tác cơ bản (đều O(1))

| Thao tác | Mô tả | Time |
| --- | --- | --- |
| push(x) | Thêm phần tử x lên đỉnh (top) | O(1) |
| pop() | Xoá và trả về phần tử ở đỉnh | O(1) |
| peek() / top() | Xem (không xoá) phần tử ở đỉnh | O(1) |
| isEmpty() | Kiểm tra stack có rỗng không | O(1) |
| isFull() | Kiểm tra stack đã đầy chưa (khi cài đặt bằng mảng cố định) | O(1) |

Không gian lưu trữ: O(n) với n là số phần tử trong stack.

#### Cách triển khai

- **Dùng mảng (Array):** kích thước cố định, dùng chỉ số `top` để theo dõi đỉnh.

- **Dùng danh sách liên kết (Linked List):** kích thước động, node mới luôn được thêm vào đầu danh sách.

```c
int stack[MAX], top = -1;

// push(x)
if (top == MAX - 1) {
 // Overflow
} else {
 stack[++top] = x;
}

// pop()
if (top == -1) {
 // Underflow
} else {
 return stack[top--];
}
```

Minh hoạ bằng Python (dùng list làm stack):

```python
stack = []

# push
stack.append(10)
stack.append(20)
stack.append(30)

# peek
top_value = stack[-1] # 30

# pop
value = stack.pop() # 30, stack còn [10, 20]

# isEmpty
is_empty = len(stack) == 0
```

#### Ứng dụng thực tế

- Quản lý lời gọi hàm / đệ quy (Call Stack, function call recursion)

- Undo/Redo trong trình soạn thảo

- Nút Back của trình duyệt

- Đánh giá biểu thức (infix, postfix, prefix — expression evaluation)

- Kiểm tra cú pháp / khớp dấu ngoặc cân bằng `()[]{}`

- Quay lui (backtracking: DFS, N-Queens, Maze)

- Đảo ngược chuỗi hoặc dữ liệu

- Bài toán **Monotonic Stack** (ví dụ: Next Greater Element)

<details markdown="1">
<summary>Mẹo: Monotonic Stack cho bài toán Next Greater Element (NGE)</summary>

1. Duyệt từ phải sang trái.

2. Duy trì một stack giảm dần.

3. Pop trong khi `stack.top <= current`.

4. NGE là `stack.top` (nếu có), sau đó push current.

Ví dụ: `nums = [2, 1, 2, 4, 3]` → `NGE = [4, 2, 4, -1, -1]`

</details>

#### Các bài toán phỏng vấn thường gặp

1. Valid Parentheses

2. Min Stack

3. Evaluate Reverse Polish Notation

4. Daily Temperatures

5. Next Greater Element (I & II)

6. Largest Rectangle in Histogram

7. Basic Calculator

8. Remove K Digits

> ⚠️ **Lỗi thường gặp:** Pop khi stack rỗng; không kiểm tra điều kiện biên; dùng sai cấu trúc dữ liệu cho bài toán cần LIFO.
>
>
> **Thực hành tốt:** Luôn kiểm tra stack rỗng trước khi pop; giữ code sạch, mô-đun; dùng tên biến rõ nghĩa (`top`).
>

---

### Queue & Deque (FIFO)

> 📌 Ảnh thuộc mục này: 1324_cam-nang-dsa-stack-queue-lifo-fifo.jpg, 1341_ghi-chu-dsa-stacks-queues.jpg, 1417_ghi-chu-hang-doi-va-deque-queue-deque.jpg

#### Khái niệm

Queue (Hàng đợi) là cấu trúc dữ liệu tuyến tính tuân theo nguyên lý **FIFO — First In First Out** (vào trước, ra trước). Việc chèn diễn ra ở **rear** (cuối), việc xoá diễn ra ở **front** (đầu).

Ví dụ: `enqueue(10) → enqueue(20) → enqueue(30) → dequeue() → dequeue()` — phần tử vào trước tiên (10) bị lấy ra trước tiên.

#### Các thao tác cơ bản (đều O(1))

| Thao tác | Mô tả |
| --- | --- |
| enqueue(x) | Thêm phần tử vào cuối (rear) |
| dequeue() | Xoá và trả về phần tử ở đầu (front) |
| front() / peek() | Xem phần tử ở đầu |
| rear() | Xem phần tử ở cuối |
| isEmpty() | Kiểm tra queue có rỗng không |

```c
int queue[MAX], front = -1, rear = -1;

// enqueue(x)
if (rear == MAX - 1) {
 // Overflow
} else {
 if (front == -1) front = 0;
 queue[++rear] = x;
}

// dequeue()
if (front == -1 || front > rear) {
 // Underflow
} else {
 return queue[front++];
}
```

```python
from collections import deque

q = deque()
q.append(10) # enqueue, O(1)
q.append(20)
q.append(30)

front_value = q[0] # peek/front
value = q.popleft() # dequeue, O(1)
```

> ⚠️ Lỗi thường gặp: dùng `list.pop(0)` để làm dequeue trong Python. Đây là **O(n)** vì phải dịch chuyển toàn bộ phần tử còn lại — nên dùng `collections.deque` thay vì `list`.

#### Các loại hàng đợi nâng cao (Advanced Variants)

**A. Circular Queue (Hàng đợi vòng)**

- Vị trí cuối được nối ngược về vị trí đầu, tận dụng không gian mảng hiệu quả.

- Cập nhật chỉ số theo modulo: `front = (front + 1) % N`, `rear = (rear + 1) % N`.

**B. Deque (Double-Ended Queue — hàng đợi hai đầu)**

- Cho phép insert/delete ở **cả hai đầu** (front và rear) trong O(1): `appendleft/append`, `popleft/pop`.

- Ứng dụng: Undo/Redo, kiểm tra palindrome, **Sliding Window Maximum** (duy trì các ứng viên trong deque).

```python
from collections import deque

dq = deque([10, 20, 30])
dq.appendleft(5) # thêm vào đầu
dq.append(40) # thêm vào cuối
dq.popleft() # xoá ở đầu
dq.pop() # xoá ở cuối
```

**C. Priority Queue (Hàng đợi ưu tiên)**

- Mỗi phần tử có 1 độ ưu tiên; phần tử ưu tiên cao nhất (Max-Heap) hoặc thấp nhất (Min-Heap) được phục vụ trước, không theo thứ tự chèn.

- Thường cài đặt bằng **Heap** → insert/delete/peek có độ phức tạp **O(log n)**.

```python
import heapq

min_heap = []
heapq.heappush(min_heap, 5)
heapq.heappush(min_heap, 1)
heapq.heappush(min_heap, 3)
smallest = heapq.heappop(min_heap) # 1
```

#### Độ phức tạp

| Cấu trúc dữ liệu | Thao tác | Time | Space | Ghi chú |
| --- | --- | --- | --- | --- |
| Hàng đợi đơn (mảng) | Enqueue/Dequeue/Peek | O(1) | O(n) | Có thể cần dịch chuyển trong trường hợp xấu nhất |
| Hàng đợi vòng (mảng) | Enqueue/Dequeue/Peek | O(1) | O(n) | Tận dụng bộ nhớ tốt hơn nhờ modulo |
| Deque (mảng) | Chèn/xoá cả 2 đầu | O(1) | O(n) | Cần quản lý chỉ số cẩn thận |
| Priority Queue (Heap) | Insert/Delete/Peek | O(log n) | O(n) | Triển khai bằng Binary Heap |

#### So sánh nhanh Stack vs Queue

| Đặc điểm | Stack | Queue |
| --- | --- | --- |
| Nguyên lý | LIFO (Last In First Out) | FIFO (First In First Out) |
| Chèn | Tại top | Tại rear |
| Xoá | Tại top | Tại front |

#### Ứng dụng thực tế

- CPU scheduling (Round Robin)

- Printer spooling / bộ đệm I/O

- Breadth First Search (BFS)

- Task Scheduling / Fairness, Rate Limiting / Buffering

- In hàng đợi trong hệ điều hành

- Lập lịch dựa trên độ ưu tiên (Priority Queue)

#### Bài toán phỏng vấn thường gặp

1. Triển khai Queue bằng 2 Stack

2. Triển khai Stack bằng 2 Queue

3. Thiết kế Circular Queue

4. Sliding Window Maximum (dùng Deque)

5. Kth Largest Element trong luồng dữ liệu (dùng Priority Queue)

> ⚠️ **Lỗi thường gặp:** nhầm lẫn front và rear; không xử lý hàng đợi đầy/rỗng; quên phép modulo khi cài Circular Queue.
>
>
> **Thực hành tốt:** luôn xử lý trường hợp biên; dùng Circular Queue khi cài bằng mảng; dùng Deque cho bài toán sliding window tối ưu.
>

---

### Hashing (Hash Table / Hash Map / Hash Set)

> 📌 Ảnh thuộc mục này: 1325_cam-nang-dsa-hashing-hash-tables-collision.jpg, 1340_ghi-chu-dsa-hashing-hash-maps.jpg, 1415_ghi-chu-ve-bam-hashing-hashmap-hashset.jpg

#### Hashing là gì?

Hashing là kỹ thuật **ánh xạ (map)** một **key** thành một số nguyên nhỏ (**index**) bằng một **hash function**. Index này dùng để lưu và truy xuất dữ liệu nhanh chóng từ hash table.

`Key → Hash Function h(key) → Index`

#### Hash Function

- Nhận vào 1 key, trả về 1 index trong khoảng `[0, m-1]` với m là kích thước bảng.

- Hash function tốt phân bố các key đều nhau để giảm thiểu collision (đụng độ).

- Ví dụ đơn giản: `h(key) = key % m`

Ví dụ với `m = 7`: keys `25, 40, 55, 12` → index tương ứng `4, 5, 6, 5` (55 và 12 cùng có `key % 7 = 5`... minh hoạ collision xảy ra khi hai key khác nhau map về cùng index).

#### Hash Table là gì?

Hash table là một **array gồm các bucket/slot**, mỗi bucket lưu trữ (các) phần tử — thường là cặp **(key, value)**.

**Basic Operations** (average time O(1)):

- **Insert(k, v):** tính `index = h(k)`, lưu `v` tại index đó.

- **Search(k):** tính `index = h(k)`, tìm `k` tại index đó.

- **Delete(k):** tính `index = h(k)`, xoá `k` khỏi index đó.

#### Collision (Đụng độ) và cách xử lý

Khi 2 key khác nhau cho cùng một index, đó gọi là **collision**. Ví dụ với `h(key) = key % 5`: các key `10, 15, 20, 25` đều map về index `0` → collision xảy ra.

Hai kỹ thuật xử lý collision chính:

**A. Chaining (Separate Chaining — Nối chuỗi)**

- Mỗi index của bảng trỏ tới 1 danh sách liên kết (linked list/vector) chứa các key hash về đó.

- Ưu điểm: dễ cài đặt, xử lý xoá dễ dàng.

- Nhược điểm: tốn thêm bộ nhớ cho pointer.

**B. Open Addressing (Địa chỉ mở)**

- Tất cả phần tử được lưu ngay trong bảng; nếu slot đầy thì dò (probe) slot trống tiếp theo.

- **Linear Probing:** nếu index i đầy, thử i+1, i+2, ... (vòng lại khi hết bảng). Đơn giản nhưng có thể gây hiện tượng **clustering**.

- Nhược điểm: xoá phần tử khó, cần xử lý đặc biệt (tombstone).

#### So sánh Chaining vs Open Addressing

| Đặc điểm | Chaining | Open Addressing |
| --- | --- | --- |
| Lưu trữ | Phần tử lưu trong linked list | Tất cả phần tử lưu ngay trong bảng |
| Bộ nhớ | Tốn thêm bộ nhớ cho pointer | Không tốn thêm bộ nhớ |
| Xoá | Dễ | Khó (cần xử lý đặc biệt) |
| Clustering | Không bị clustering | Có thể bị clustering |

#### Load Factor (Hệ số tải)

`Load Factor (α) = Số phần tử (n) / Kích thước bảng (m)`

- Load factor càng cao → càng nhiều collision.

- Nên giữ `α ≤ 0.7` để hiệu năng tốt.

- Khi α vượt ngưỡng (ví dụ 0.75), cần thay đổi kích thước bảng (**resize / rehashing**) để duy trì O(1).

> ⚖️ **Trade-off cốt lõi:** Hashing đánh đổi **SPACE lấy TIME** — dùng thêm bộ nhớ để đạt tốc độ truy cập trung bình O(1).

#### Hash Map vs Hash Set

- **HashMap (Khoá → Giá trị):** lưu các cặp key-value duy nhất theo key; thêm/xoá/tìm kiếm nhanh trung bình; được triển khai bằng Hash Table.

- **HashSet (Giá trị duy nhất):** chỉ lưu các phần tử duy nhất; về bản chất là HashMap chỉ có khoá (không có value); dùng để kiểm tra tồn tại/tồn tại phần tử (membership).

- Trong Java, `HashMap` dùng hashing nội bộ, xử lý collision bằng chaining, cho phép 1 null key.

```python
# HashMap / dict trong Python
map_ = {}
map_[101] = "Alice"
map_[102] = "Bob"

print(map_.get(101)) # "Alice"
print(102 in map_) # True (containsKey)
del map_[101] # xoá key
<empty-block/>
# HashSet / set trong Python
s = set()
s.add(10)
s.add(20)
print(20 in s) # True
s.remove(10)
```

#### Độ phức tạp trung bình

| Thao tác | HashMap | HashSet | Ghi chú |
| --- | --- | --- | --- |
| Chèn (Insert) | O(1) | O(1) | Amortized O(1) |
| Tìm kiếm (Search) | O(1) | O(1) | Tra cứu nhanh |
| Xoá (Delete) | O(1) | O(1) | Nếu khoá/phần tử tồn tại |
| Bộ nhớ (Space) | O(n) | O(n) | n = số phần tử |

Với hash function tốt và load factor thấp → O(1). Ở **worst case** (nhiều collision, ví dụ hash function kém) → có thể suy biến thành **O(n)**.

#### Ứng dụng thực tế của Hashing

- Dictionary / Map (key-value pairs), Database indexing

- Caching / Memoization

- Đếm tần suất phần tử (frequency count)

- Phát hiện trùng lặp (duplicate detection), kiểm tra tồn tại (set membership)

- Nhóm anagram (group anagrams)

- Bảng ký hiệu trong trình biên dịch (symbol table)

- Two Sum (dùng cặp (a) + (b))

#### Các bài toán phỏng vấn thường gặp

1. Two Sum

2. Subarray Sum Equals K

3. Longest Consecutive Sequence

4. Group Anagrams

5. Top K Frequent Elements

> 🎤 **Mẹo phỏng vấn:** Làm rõ kiểu key (string/int/object). Hỏi về kỳ vọng collision và ràng buộc (n, phạm vi giá trị). Đề cập trường hợp xấu nhất có thể là O(n) nếu có nhiều collision.

> ⚠️ **Lỗi thường gặp:** chọn hash function không tốt; bỏ qua hệ số tải; không xử lý collision; quên rehashing khi thay đổi kích thước bảng; thay đổi (mutate) key sau khi đã insert (làm sai lệch hash).

---

> 📝 **Ghi chú bổ sung**
> - Stack và Queue đều có thể triển khai lẫn nhau (Queue bằng 2 Stack, Stack bằng 2 Queue) — đây là dạng bài phỏng vấn phổ biến.
>
> - Deque là cấu trúc "tổng quát hoá" của cả Stack và Queue vì hỗ trợ thao tác O(1) ở cả hai đầu; trong Python nên dùng `collections.deque` thay vì `list` để tránh độ phức tạp O(n) khi thao tác ở đầu danh sách.
>
> - Hashing là nền tảng của `dict`/`set` trong Python, `HashMap`/`HashSet` trong Java — độ phức tạp trung bình O(1) nhưng phụ thuộc mạnh vào chất lượng hash function và việc kiểm soát load factor.
>
