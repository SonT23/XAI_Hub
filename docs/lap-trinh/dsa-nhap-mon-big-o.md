# DSA: Nhập môn & Độ phức tạp (Big-O)

> 🖼️ **Ảnh nguồn cần dán vào trang này** (8 ảnh ghi chú gốc, dán thủ công vào các mục tương ứng bên dưới):
> 1. `1319_cam-nang-dsa-gioi-thieu-data-structures-algorithms.jpg`
>
> 2. `1320_cam-nang-dsa-complexity-analysis-big-o-notation.jpg`
>
> 3. `1335_bia-cam-nang-cau-truc-du-lieu-giai-thuat-phong-van.jpg`
>
> 4. `1336_ghi-chu-dsa-trang-2-what-why-dsa.jpg`
>
> 5. `1337_ghi-chu-dsa-trang-3-big-o-complexity-chi-tiet.jpg`
>
> 6. `1404_trang-bia-ghi-chu-dsa-cau-truc-du-lieu-giai-thuat.jpg`
>
> 7. `1405_gioi-thieu-ve-cau-truc-du-lieu-va-giai-thuat-dsa.jpg`
>
> 8. `1406_do-phuc-tap-thoi-gian-va-bo-nho-ky-hieu-big-o.jpg`
>

Trang này tổng hợp lại 3 bộ ghi chú/cheat sheet tiếng Anh và tiếng Việt khác nhau về **Nhập môn DSA** và **Big-O Notation**, gộp thành một bài học liền mạch, không trùng lặp ý nhưng giữ đầy đủ chi tiết hữu ích từ mọi nguồn.

### 1. DSA là gì?

**DSA (Data Structures & Algorithms – Cấu trúc dữ liệu & Giải thuật)** = cách **tổ chức, lưu trữ dữ liệu** (Data Structure) kết hợp với cách **biến đổi/xử lý dữ liệu đó một cách hiệu quả** (Algorithm) để giải quyết vấn đề.

#### 1.1. Data Structure (Cấu trúc dữ liệu) là gì?

- Là cách tổ chức và lưu trữ dữ liệu trong máy tính sao cho có thể **truy cập và thao tác hiệu quả**.

- Giúp thực hiện tối ưu các thao tác cơ bản: **Insertion** (thêm), **Deletion** (xóa), **Searching** (tìm kiếm), **Sorting** (sắp xếp), **Traversal** (duyệt).

**Ví dụ trực quan:**

| **Cấu trúc** | **Mô tả nhanh** |
| --- | --- |
| Array (Mảng) | Dãy phần tử liền kề trong bộ nhớ, truy cập theo chỉ số (index), vd `[10, 20, 30, 40]` |
| Linked List (Danh sách liên kết) | Các node nối tiếp nhau bằng con trỏ: `10 → 20 → 30` |
| Stack (Ngăn xếp) | Vào sau ra trước (LIFO) |
| Queue (Hàng đợi) | Vào trước ra trước (FIFO) |

#### 1.2. Algorithm (Giải thuật) là gì?

- Là một **tập hợp các bước tuần tự, hữu hạn, rõ ràng** để giải quyết một vấn đề hoặc thực hiện một tác vụ.

- Mô tả **CÁCH (HOW)** để thực hiện, và **độc lập với ngôn ngữ lập trình** (có thể viết bằng Python, Java, C++... đều cho cùng kết quả).

**Ví dụ: Thuật toán tìm giá trị lớn nhất trong mảng**

1. Bắt đầu (Start)

2. Giả sử phần tử đầu tiên là lớn nhất

3. So sánh với các phần tử còn lại

4. Nếu có phần tử lớn hơn, cập nhật giá trị lớn nhất

5. Lặp lại đến hết mảng

6. Trả về giá trị lớn nhất

7. Kết thúc (Stop)

```python
def find_max(arr):
    max_val = arr[0]
    for x in arr[1:]:
        if x > max_val:
            max_val = x
    return max_val

print(find_max([10, 20, 30, 40]))  # 40
```

#### 1.3. Data Structure vs Algorithm — phân biệt

| **Data Structure** | **Algorithm** |
| --- | --- |
| Cách tổ chức và lưu trữ dữ liệu | Các bước hướng dẫn để giải quyết vấn đề |
| Tập trung vào biểu diễn dữ liệu | Tập trung vào logic và quy trình xử lý |
| Ví dụ: Array, Linked List, Stack, Tree, Graph | Ví dụ: Sorting, Searching, Traversal, Shortest Path |
| Giúp quản lý dữ liệu hiệu quả | Giúp giải quyết vấn đề hiệu quả |

#### 1.4. Ba tầng kiến thức của DSA

DSA thường được nhìn theo 3 tầng bổ trợ lẫn nhau:

1. **Data Structures** — các khối nền tảng (Array, Hash, Stack, Tree, Graph, DP table...)

2. **Algorithms** — kỹ thuật và chiến lược xử lý (Sorting, Searching, Graph traversal, Optimization...)

3. **Problem Patterns** — các khuôn mẫu bài toán lặp lại (Two Pointers, BFS/DFS, Heap, Dynamic Programming, Greedy...), giúp *nhận diện* dạng bài nhanh thay vì học thuộc lời giải.

> 💡 **Ghi nhớ quan trọng:** DSA = *patterns* + khả năng đánh giá Big-O — tức là khả năng **nhận diện, lựa chọn, triển khai và chứng minh** độ hiệu quả của giải pháp. Sai lầm phổ biến là **học thuộc lời giải mà không nhận diện được pattern** phía sau nó — pattern quan trọng hơn học thuộc.

### 2. Vì sao cần học DSA?

- **Cải thiện kỹ năng giải quyết vấn đề** (problem-solving) và tư duy logic.

- Giúp viết code **hiệu quả và tối ưu hơn** (giảm độ phức tạp thời gian & bộ nhớ).

- Được dùng trong **hầu hết ứng dụng thực tế** — từ web, mobile đến hệ thống lớn.

- Là yếu tố **cốt lõi của phỏng vấn kỹ thuật** (technical interview): giúp dự đoán khả năng mở rộng (scalability), tính đúng đắn, và các đánh đổi (trade-off) trong giới hạn thời gian.

- Là **nền tảng cho các chủ đề nâng cao** hơn (machine learning, hệ thống phân tán, cơ sở dữ liệu...).

#### Ứng dụng thực tế của DSA

| **Bài toán thực tế** | **Cấu trúc/thuật toán dùng** |
| --- | --- |
| Bản đồ, định vị GPS, tìm đường ngắn nhất | Graph (Dijkstra, BFS) |
| Undo / Redo trong ứng dụng, lịch sử trình duyệt | Stack |
| Hàng đợi máy in, danh sách phát nhạc | Queue |
| Tìm kiếm danh bạ, cache | Hashing / Hash Table |
| Hệ thống file, thư mục | Tree |
| Hệ thống đặt vé online, thương mại điện tử (tìm kiếm, sắp xếp sản phẩm) | Array, List, Sorting/Searching |
| Trò chơi: tìm đường đi, phát hiện va chạm, AI cho NPC | Graph, Tree, Heuristic search |

> 🔬 **Liên hệ với NCKH (Machine Learning / AI):** DSA là nền tảng bắt buộc khi làm nghiên cứu ML/AI — ví dụ: chọn cấu trúc dữ liệu phù hợp để xử lý tập dữ liệu lớn (mảng/ma trận cho tensor, hash table cho embedding lookup, heap cho top-k, tree/graph cho mô hình cây quyết định hoặc mạng nơ-ron đồ thị - GNN), đồng thời phân tích độ phức tạp thời gian/không gian giúp đánh giá khả năng **mở rộng (scalability)** của thuật toán khi dữ liệu tăng lên (rất quan trọng khi huấn luyện mô hình trên dữ liệu lớn) và tối ưu hóa pipeline xử lý dữ liệu, huấn luyện mô hình.

#### Vòng lặp học DSA hiệu quả

Mục tiêu cần theo đúng thứ tự ưu tiên: **tính đúng đắn** > **thời gian/không gian** > **sự tinh gọn của code**.

Quy trình học một dạng bài: `learn (học lý thuyết)` → `dry-run (chạy tay ví dụ nhỏ)` → `code (cài đặt)` → `complexity (phân tích Big-O)` → `variants (làm biến thể bài toán)`.

#### Quy trình giải một bài toán DSA cơ bản

1. **Problem** — đọc kỹ đề bài

2. **Understand** — xác định input, output và ràng buộc

3. **Choose DS** — chọn cấu trúc dữ liệu phù hợp

4. **Algorithm** — thiết kế giải pháp từng bước

5. **Code** — cài đặt giải pháp

6. **Test** — kiểm thử với nhiều input, sửa lỗi

7. **Optimize** — phân tích và cải thiện thời gian & bộ nhớ

### 3. Phân loại Data Structure & Algorithm

#### 3.1. Các loại Data Structure

- **Linear Data Structure** (cấu trúc tuyến tính — phần tử sắp xếp nối tiếp): Array, Linked List, Stack, Queue, Deque.

- **Non-Linear Data Structure** (cấu trúc phi tuyến — phần tử phân cấp/liên kết phức tạp): Tree, Graph, Heap, Hash Table.

#### 3.2. Các loại Algorithm phổ biến

- **Searching Algorithms**: Linear Search, Binary Search.

- **Sorting Algorithms**: Bubble Sort, Quick Sort, Merge Sort...

- **Graph Algorithms**: BFS, DFS, Dijkstra.

- **Optimization Algorithms**: Greedy, Dynamic Programming (DP), Backtracking.

- **Mathematical Algorithms**: GCD, kiểm tra số nguyên tố (Prime Check), v.v.

### 4. Độ phức tạp thuật toán (Complexity Analysis) là gì?

**Độ phức tạp thời gian (Time Complexity)** là lượng thời gian một giải thuật cần để chạy, tính theo hàm của **kích thước đầu vào n** — dùng để **đo tốc độ chạy** của giải thuật.

**Độ phức tạp bộ nhớ (Space Complexity)** là lượng bộ nhớ phụ trội một giải thuật sử dụng, cũng tính theo hàm của n — dùng để **đo lượng bộ nhớ cần thiết**.

#### Vì sao cần phân tích độ phức tạp trước khi code?

- Để **dự đoán** giải thuật sẽ hoạt động thế nào khi kích thước input (n) tăng lên.

- Giúp **so sánh** các cách tiếp cận khác nhau cho cùng một bài toán.

- Giúp viết code hiệu quả, **có khả năng mở rộng** (scalable).

- Là kỹ năng bắt buộc trong **phỏng vấn kỹ thuật**.

> ⚖️ **Đánh đổi Space vs Time (Space-Time Tradeoff):** dùng nhiều bộ nhớ hơn (cache, tính toán trước - precompute, hash table) đôi khi có thể giảm thời gian chạy — và ngược lại. Lựa chọn tuỳ theo ràng buộc thực tế của bài toán (ví dụ hệ thống giới hạn RAM thì ưu tiên tiết kiệm bộ nhớ dù chậm hơn một chút).

### 5. Ký hiệu tiệm cận: Big-O, Big-Omega, Big-Theta

Big-O không phải là thời gian chạy chính xác (tính bằng giây), mà là cách **mô tả tốc độ tăng trưởng** của thời gian chạy (hoặc bộ nhớ) khi kích thước input n tăng lên — bỏ qua các hằng số và yếu tố phần cứng.

| **Ký hiệu** | **Ý nghĩa** | **Công thức** |
| --- | --- | --- |
| Big O (O) | Chặn trên — độ phức tạp trường hợp **xấu nhất** (worst case). Cho biết thời gian *tối đa* giải thuật có thể mất. | f(n) ≤ c·g(n) với n ≥ n₀ |
| Big Ω (Omega) | Chặn dưới — độ phức tạp trường hợp **tốt nhất** (best case). Cho biết thời gian *tối thiểu* giải thuật có thể mất. | f(n) ≥ c·g(n) với n ≥ n₀ |
| Big Θ (Theta) | Chặn chặt — độ phức tạp trường hợp **trung bình**, cho biết tốc độ tăng chính xác (cả chặn trên và dưới cùng bậc). | c₁·g(n) ≤ f(n) ≤ c₂·g(n) |

Trong thực hành (đặc biệt khi phỏng vấn), người ta thường chỉ nói đến **Big-O** vì nó mô tả trường hợp xấu nhất — là cận an toàn nhất để đảm bảo hệ thống không bị chậm bất ngờ.

#### Best Case, Average Case, Worst Case

| **Trường hợp** | **Ý nghĩa** | **Ví dụ** |
| --- | --- | --- |
| Best Case | Thời gian tối thiểu cho một đầu vào | Binary Search khi phần tử giữa chính là target → O(1) |
| Average Case | Thời gian trung bình trên mọi đầu vào | Quick Sort trường hợp trung bình → O(n log n) |
| Worst Case | Thời gian tối đa cho một đầu vào | Quick Sort trường hợp xấu nhất (mảng đã sắp xếp sẵn) → O(n²) |

**Ví dụ minh hoạ — Linear Search trên mảng **`[10, 20, 30, 40, 50]`**:**

- Tìm `10` (đứng đầu) → best case, chỉ 1 lần so sánh → O(1)

- Tìm `30` (ở giữa) → average case, ~n/2 lần so sánh → O(n)

- Tìm `50` hoặc phần tử không tồn tại → worst case, n lần so sánh → O(n)

> 💡 **Mẹo khi phỏng vấn:** khi trình bày độ phức tạp, hãy nói rõ cả 3 khía cạnh — Best case, Average case (kỳ vọng), Worst case — và làm rõ giả định (ví dụ: "giả sử hash function tốt và load factor hợp lý").

### 6. Các độ phức tạp phổ biến (từ nhanh đến chậm)

| **Notation** | **Tên gọi** | **Ý nghĩa** | **Ví dụ điển hình** |
| --- | --- | --- | --- |
| O(1) | Constant (Hằng số) | Thời gian không đổi, không phụ thuộc n | Truy cập phần tử mảng theo index, lookup hash (trung bình) |
| O(log n) | Logarithmic | Giảm một nửa bài toán sau mỗi bước, tăng rất chậm | Binary Search, thao tác trên cây cân bằng (balanced tree) |
| O(n) | Linear (Tuyến tính) | Thời gian tăng tỉ lệ thuận với n | Linear Search, duyệt mảng (Traversal), tìm max |
| O(n log n) | Linearithmic | Phổ biến trong các thuật toán chia để trị / sắp xếp hiệu quả | Merge Sort, Heap Sort, Quick Sort (trung bình) |
| O(n²) | Quadratic (Bậc hai) | Hai vòng lặp lồng nhau, mỗi vòng ~n | Bubble Sort, Selection Sort, so sánh từng cặp phần tử |
| O(2ⁿ) | Exponential (Hàm mũ) | Tăng theo cấp số nhân với n — bùng nổ rất nhanh | Đệ quy ngây thơ tính Fibonacci, liệt kê tất cả tập con (subset) |
| O(n!) | Factorial (Giai thừa) | Tăng cực nhanh (n giai thừa) | Bài toán người du lịch (TSP) giải vét cạn, liệt kê hoán vị (Permutations) |

#### Ví dụ minh hoạ bằng Python cho từng độ phức tạp

```python
# O(1) - Constant: truy cập phần tử theo index
def get_first(arr):
    return arr[0]

# O(log n) - Logarithmic: Binary Search
def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

# O(n) - Linear: duyệt qua toàn bộ mảng
def linear_search(arr, target):
    for i, x in enumerate(arr):
        if x == target:
            return i
    return -1

# O(n log n) - Linearithmic: Merge Sort (chia để trị)
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    return result + left[i:] + right[j:]

# O(n^2) - Quadratic: Bubble Sort (2 vòng lặp lồng nhau)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# O(2^n) - Exponential: Fibonacci đệ quy ngây thơ (không nhớ kết quả)
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
```

#### Tốc độ tăng trưởng khi n lớn dần (minh hoạ bằng con số cụ thể)

| **Complexity** | **Tốc độ tăng** | **n = 10** | **n = 1.000** |
| --- | --- | --- | --- |
| O(1) | Constant | 1 | 1 |
| O(log n) | Logarithmic | ≈ 3 | ≈ 10 |
| O(n) | Linear | 10 | 1.000 |
| O(n log n) | Linearithmic | ≈ 33 | ≈ 9.970 |
| O(n²) | Quadratic | 100 | 1.000.000 |
| O(2ⁿ) | Exponential | 1.024 | ≈ 10³⁰¹ (siêu lớn!) |

Có thể thấy: với n = 1.000, O(n²) đã lên tới **1 triệu phép tính**, còn O(2ⁿ) thì gần như **không thể tính nổi** trên máy tính thông thường. Đây là lý do vì sao chọn đúng thuật toán/cấu trúc dữ liệu lại quan trọng đến vậy khi dữ liệu đầu vào lớn (ví dụ dữ liệu huấn luyện ML với hàng triệu mẫu).

### 7. Cách phân tích độ phức tạp của vòng lặp và đệ quy

#### 7.1. Vòng lặp (Loop)

- **Một vòng lặp chạy hết n phần tử** → O(n).

- **Hai vòng lặp lồng nhau, mỗi vòng chạy ~n** → O(n²).

- **Vòng lặp mà mỗi bước giảm một nửa kích thước bài toán** (vd chia đôi mảng) → O(log n).

> ⚠️ **Cạm bẫy thường gặp (Common Pitfalls):**
> - Vòng lặp lồng nhau **không phải lúc nào cũng là O(n²)**. Nếu vòng lặp bên trong co lại dần (ví dụ chạy từ `n` xuống `1`), tổng số phép tính có thể vẫn là O(n²), nhưng nếu vòng trong chỉ chạy hằng số bước hoặc giảm theo cấp số nhân thì có thể là O(n), O(n log n)...
>
> - **Hash table** có độ phức tạp trung bình O(1) cho tra cứu/thêm phần tử, nhưng **trường hợp xấu nhất là O(n)** (khi xảy ra nhiều đụng độ - collision).
>
> - Đừng chỉ khẳng định O(n) trong khi thực tế bạn đang **build lại/redo toàn bộ cấu trúc dữ liệu mỗi lần** — rebuild một cấu trúc ở mỗi truy vấn (query) thường khiến độ phức tạp tổng thể trở thành O(n²). Cần chú ý các thao tác ẩn bên trong vòng lặp và trong các lệnh gọi hàm (ví dụ gọi `list.index()` hay nối chuỗi trong vòng lặp cũng tốn O(n) mỗi lần gọi).
>

#### 7.2. Đệ quy (Recursion)

- Đệ quy **không nhớ kết quả trung gian** (như `fib(n)` ở trên) thường dẫn tới độ phức tạp **hàm mũ O(2ⁿ)** vì cùng một bài toán con bị tính lại nhiều lần.

- Đệ quy kiểu **chia để trị (divide & conquer)** như Merge Sort, mỗi lần chia bài toán làm 2 và tốn O(n) để gộp lại → tổng là O(n log n).

- Có thể tối ưu đệ quy hàm mũ bằng kỹ thuật **ghi nhớ (memoization)** hoặc **quy hoạch động (Dynamic Programming)** để giảm xuống O(n):

```python
# Fibonacci với memoization -> O(n) thay vì O(2^n)
def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]
```

#### 7.3. Amortized (Chi phí khấu hao) vs Worst Case

- **Amortized**: chi phí *trung bình* cho mỗi thao tác, tính trên cả một chuỗi thao tác (ví dụ: `append` vào một mảng động (dynamic array) trung bình là O(1) dù thỉnh thoảng phải resize tốn O(n)).

- **Worst case**: chi phí *tối đa* cho **một** thao tác bất kỳ.

- Cần biết rõ mình đang nói đến loại nào khi phân tích/trình bày độ phức tạp.

### 8. Bảng độ phức tạp của các thao tác trên cấu trúc dữ liệu phổ biến

| **Cấu trúc** | **Thao tác** | **Average** | **Worst Case** |
| --- | --- | --- | --- |
| Array | Truy cập theo index (Access by index) | O(1) | O(1) |
| Hash Table | Tra cứu / Thêm (Lookup / Insert) | O(1) | O(n) |
| Binary Heap | Thêm phần tử (Push) | O(log n) | O(log n) |

★ *Giả sử hash function tốt và hệ số tải (load factor) hợp lý.*

### 9. Ví dụ nhanh kiểu phỏng vấn

- Tìm 1 phần tử trong mảng **chưa sắp xếp**, kích thước n → Linear Search → **O(n)**

- Tìm 1 phần tử trong mảng **đã sắp xếp**, kích thước n → Binary Search → **O(log n)**

- Sắp xếp mảng bằng Bubble Sort → **O(n²)**

- Sắp xếp mảng bằng Merge Sort → **O(n log n)**

- In tất cả tập con (subset) của tập kích thước n → **O(2ⁿ)**

> 📝 **Ghi chú bổ sung**
> - **Big-O chỉ mô tả xu hướng tăng trưởng**, không phải thời gian chạy thực tế tính bằng giây — hai thuật toán cùng O(n) có thể khác nhau về tốc độ thực do hằng số ẩn (constant factor) hoặc đặc thù phần cứng, cache CPU... Big-O chỉ có ý nghĩa rõ rệt khi **n đủ lớn**.
>
> - Khi phân tích độ phức tạp, luôn nêu rõ đang xét **thời gian hay bộ nhớ**, và đang ở trường hợp **best/average/worst case** nào — tránh nhầm lẫn khi trao đổi hoặc khi viết báo cáo NCKH.
>
> - Mục tiêu học DSA nên đi theo thứ tự: **đúng đắn (correctness) → hiệu quả thời gian/bộ nhớ → độ tinh gọn/dễ đọc của code**. Đừng tối ưu quá sớm khi chưa chắc thuật toán đã đúng.
>
> - Trong nghiên cứu ML/AI, việc chọn đúng cấu trúc dữ liệu và hiểu độ phức tạp thuật toán ảnh hưởng trực tiếp đến khả năng mở rộng khi làm việc với dữ liệu lớn — ví dụ, dùng hash table/inverted index để tăng tốc truy vấn, hoặc chọn thuật toán O(n log n) thay vì O(n²) khi xử lý hàng triệu bản ghi.
>
