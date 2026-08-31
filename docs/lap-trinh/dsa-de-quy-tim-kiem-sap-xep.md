# DSA: Đệ quy, Tìm kiếm & Sắp xếp

> 🖼️ **Nguồn ảnh gốc (10 ảnh, 3 bộ ghi chú DSA):**
> 1. 1326_cam-nang-dsa-recursion-base-case-factorial-fibonac.jpg
>
> 2. 1327_cam-nang-dsa-searching-algorithms-linear-binary-se.jpg
>
> 3. 1328_cam-nang-dsa-sorting-algorithms-bubble-merge-quick.jpg
>
> 4. 1343_ghi-chu-dsa-recursion-backtracking.jpg
>
> 5. 1344_ghi-chu-dsa-binary-search.jpg
>
> 6. 1345_ghi-chu-dsa-sorting-essentials.jpg
>
> 7. 1409_ghi-chu-giai-thuat-tim-kiem-tuyen-tinh-va-nhi-phan.jpg
>
> 8. 1410_ghi-chu-giai-thuat-sap-xep-bubble-selection-merge-.jpg
>
> 9. 1411_ghi-chu-ve-de-quy-recursion-trong-lap-trinh.jpg
>
> 10. 1419_ghi-chu-tim-kiem-nhi-phan-binary-search-chi-tiet.jpg
>

### Đệ quy (Recursion & Backtracking)

> 📎 Ảnh thuộc mục này: #1, #4, #9

#### Đệ quy là gì?

Đệ quy (Recursion) là kỹ thuật một hàm **tự gọi lại chính nó** để giải một phiên bản nhỏ hơn của cùng một bài toán, cho đến khi đạt tới điều kiện dừng. Nó chia một bài toán phức tạp thành các bài toán con đơn giản hơn.

**Công thức:** Đệ quy = **Base Case** (trường hợp cơ sở) + **Recursive Case** (trường hợp đệ quy)

- **Base Case:** điều kiện dừng vòng đệ quy. Không có base case → đệ quy chạy vô hạn (Stack Overflow).

- **Recursive Case:** phần hàm tự gọi lại chính nó với đầu vào **nhỏ hơn**, đưa lời giải tiến dần về base case.

```python
def solve(n):
    if base_case(n):      # Base Case
        return ...
    return solve(smaller(n))  # Recursive Case
```

#### Call Stack (ngăn xếp lời gọi)

Mỗi lời gọi đệ quy được đẩy (push) vào Call Stack và phải chờ lời gọi bên dưới hoàn tất mới trả kết quả (LIFO). Khi đạt base case, các lời gọi lần lượt trả về (pop) theo thứ tự ngược lại.

```javascript
fact(4)  Waiting...
fact(3)  Waiting...
fact(2)  Waiting...
fact(1)  Waiting...
fact(0)  Return 1   ← base case
         Return ngược lên trên
```

#### Ví dụ 1: Factorial (Giai thừa)

Bài toán: `fact(n) = n * fact(n-1)`, `fact(0) = fact(1) = 1` (base case)

```python
def fact(n):
    if n == 0 or n == 1:
        return 1          # Base Case
    return n * fact(n - 1)  # Recursive Case
```

Cây gọi đệ quy của `fact(4)`:

```javascript
fact(4) = 4 * fact(3)
        = 4 * (3 * fact(2))
        = 4 * (3 * (2 * fact(1)))
        = 4 * (3 * (2 * (1 * fact(0))))
        = 4 * (3 * (2 * (1 * 1)))
        = 4 * 6 = 24
```

#### Ví dụ 2: Fibonacci

Bài toán: `fib(n) = fib(n-1) + fib(n-2)`, với `fib(0)=0`, `fib(1)=1` (2 base case)

```python
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)
```

> ⚠️ Fibonacci đệ quy thuần có nhiều **overlapping subproblems** (bài toán con lặp lại) → kém hiệu quả, độ phức tạp thời gian dạng hàm mũ O(2ⁿ). Nên nói rõ điều này khi phỏng vấn — có thể cải thiện bằng memoization/DP.

#### Ví dụ 3: Tổng N số đầu tiên

```python
def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n - 1)
```

#### Đệ quy vs Lặp (Iteration)

| **Tiêu chí** | **Đệ quy (Recursion)** | **Lặp (Iteration)** |
| --- | --- | --- |
| Cách tiếp cận | Hàm tự gọi lại | Dùng vòng lặp for/while |
| Bộ nhớ | Dùng Call Stack, O(log n) hoặc O(n) tùy bài toán | Bộ nhớ hằng số O(1) |
| Hiệu năng | Thường chậm hơn (chi phí gọi hàm) | Thường nhanh hơn |
| Code | Ngắn gọn, thanh lịch, trực quan cho chia để trị | Dài hơn nhưng hiệu quả |
| Rủi ro | Có thể Stack Overflow nếu đệ quy quá sâu | Không bị Stack Overflow |

> 💡 Đệ quy dùng thêm bộ nhớ ngăn xếp; đệ quy quá sâu (quá nhiều lời gọi lồng nhau) có thể vượt giới hạn call stack và gây **Stack Overflow** (crash chương trình, ví dụ `StackOverflowError` trong Java). Luôn đảm bảo có base case đúng.

**Lỗi thường gặp (Common Interview Mistakes):**

```python
# Ví dụ SAI: thiếu base case → đệ quy vô hạn
def fun(n):
    return fun(n + 1)  # không có điều kiện dừng!
```

**Khi nào dùng đệ quy?** Khi bài toán có thể chia thành các bài toán con tương tự (subproblems) — ví dụ duyệt cây/đồ thị, chia để trị (Divide & Conquer), quay lui (backtracking).

#### Ưu điểm & Nhược điểm

| **Ưu điểm** | **Nhược điểm** |
| --- | --- |
| Đơn giản hóa bài toán phức tạp | Sử dụng nhiều bộ nhớ (ngăn xếp lời gọi) |
| Dễ viết và dễ hiểu | Chậm hơn do chi phí gọi hàm |
| Tự nhiên cho bài toán có cấu trúc lặp lại | Có thể gây Tràn Ngăn Xếp (Stack Overflow) với đệ quy sâu |
| Hữu ích cho duyệt cây/đồ thị, quay lui, chia để trị | - |

#### Backtracking (Quay lui)

Backtracking là kỹ thuật đệ quy dùng để thử tất cả khả năng, và **hủy bỏ (quay lui)** lựa chọn khi nó không dẫn đến lời giải hợp lệ.

**Backtracking Template — 3 bước:**

1. **CHOOSE** — thực hiện một lựa chọn

2. **EXPLORE** — đệ quy để đi sâu hơn với lựa chọn đó

3. **UNCHOOSE** — hoàn tác lựa chọn, khôi phục trạng thái (đây là điều then chốt giúp backtracking hoạt động đúng)

**Các bài toán kinh điển dùng Backtracking:** Subsets (tập con), Permutations (hoán vị), N-Queens, Combination Sum.

> 🔻 **Pruning (cắt tỉa):** dùng các ràng buộc của bài toán để cắt sớm các nhánh đệ quy chắc chắn không dẫn tới lời giải hợp lệ, giúp giảm số nhánh cần duyệt.

**Lỗi thường gặp khi dùng Backtracking:**

- Thiếu base case → đệ quy vô hạn.

- Không khôi phục trạng thái (không thực hiện bước UNCHOOSE) → phá hỏng quá trình tìm kiếm ở các nhánh khác.

> ⚠️ Độ phức tạp của backtracking thường là **hàm mũ** (exponential) — nên nói rõ điều này khi phân tích/trình bày thuật toán.

---

### Tìm kiếm (Linear Search & Binary Search)

> 📎 Ảnh thuộc mục này: #2, #5, #7, #10

Searching là quá trình tìm một phần tử **target** trong một tập hợp phần tử. Chọn đúng thuật toán tìm kiếm giúp cải thiện hiệu năng chương trình.

#### 1. Linear Search (Tìm kiếm tuyến tính)

Kiểm tra **từng phần tử một**, từ đầu tới cuối, cho đến khi tìm thấy target hoặc hết mảng. Hoạt động được trên cả dữ liệu **đã sắp xếp và chưa sắp xếp**.

Ví dụ: `arr = [7, 2, 9, 4, 3, 6]`, `target = 4` → so sánh lần lượt 7≠4, 2≠4, 9≠4, 4=4 → tìm thấy tại index 3.

```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1  # không tìm thấy
```

**Độ phức tạp:** Best O(1) (phần tử đầu tiên là target) · Average O(n/2) ≈ O(n) · Worst O(n) (phần tử không tồn tại) · Space O(1).

#### 2. Binary Search (Tìm kiếm nhị phân) — yêu cầu dữ liệu đã sắp xếp

Liên tục **chia đôi** không gian tìm kiếm: so sánh phần tử ở giữa (mid) với target, nếu nhỏ hơn thì bỏ nửa trái, nếu lớn hơn thì bỏ nửa phải, lặp lại cho tới khi `low > high`.

**Điều kiện tiên quyết:** Mảng phải đã được sắp xếp (tăng dần); cấu trúc dữ liệu phải truy cập ngẫu nhiên được (array, vector — Binary Search trên Linked List không hiệu quả, vẫn là O(n)).

Ví dụ: `arr = [2,4,6,8,10,12,14,16]`, `target = 10` → mid chia dần cho tới khi `arr[mid] = 10`, tìm thấy tại index 4.

```python
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2   # tránh tràn số nguyên (overflow)
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1  # không tìm thấy
```

**Độ phức tạp:** Time O(log n) · Space O(1) khi cài đặt lặp (iterative); O(log n) nếu cài đặt đệ quy (do call stack).

> 💡 Dùng `low + (high - low) // 2` thay vì `(low + high) // 2` để tránh **tràn số nguyên (integer overflow)** khi low, high rất lớn.

**Lặp (Iterative) vs Đệ quy (Recursive) khi cài Binary Search:**

| **Tiêu chí** | **Lặp** | **Đệ quy** |
| --- | --- | --- |
| Cách làm | Dùng vòng lặp | Dùng lời gọi hàm |
| Bộ nhớ | O(1) | O(log n) do call stack |
| Thực tế | Thường được ưu dùng, nhanh hơn | Trực quan hơn cho tư duy chia để trị |

**Các biến thể thường gặp trong phỏng vấn:**

- **First Occurrence** (lower bound): tiếp tục tìm ở nửa trái ngay cả khi đã tìm thấy target, để lấy vị trí xuất hiện đầu tiên.

- **Last Occurrence** (upper bound): tương tự nhưng tiếp tục ở nửa phải, lấy vị trí xuất hiện cuối cùng.

- **Search Insert Position**: nếu không tìm thấy target, trả về vị trí cần chèn để giữ mảng có thứ tự (chỉ số đầu tiên mà `a[i] ≥ x`).

- **Search in Rotated Sorted Array.**

- **Binary Search trên Answer Space** (Predicate/`isOk(mid)`): dùng khi có thể định nghĩa một hàm kiểm tra boolean **đơn điệu** (monotonic: False...False, True...True) trên không gian đáp án, ví dụ bài toán min capacity / max speed.

#### So sánh Linear Search vs Binary Search

| **Tiêu chí** | **Linear Search** | **Binary Search** |
| --- | --- | --- |
| Yêu cầu dữ liệu | Chưa/đã sắp xếp đều được | Chỉ hoạt động trên dữ liệu đã sắp xếp |
| Cách tiếp cận | Kiểm tra từng phần tử | Chia để trị (chia đôi) |
| Best case | O(1) | O(1) |
| Average case | O(n/2) ≈ O(n) | O(log n) |
| Worst case | O(n) | O(log n) |
| Bộ nhớ | O(1) | O(1) |

**Khi nào dùng loại nào?**

- Dùng **Linear Search** khi: dữ liệu chưa sắp xếp, kích thước tập dữ liệu nhỏ, hoặc sự đơn giản quan trọng hơn.

- Dùng **Binary Search** khi: dữ liệu đã được sắp xếp, kích thước tập dữ liệu lớn, cần tốc độ nhanh hơn O(log n).

> ⚠️ **Lỗi thường gặp khi cài Binary Search:**
> - Dùng `(low + high) / 2` → có thể gây tràn số nguyên.
>
> - Cập nhật `low`/`high` sai (off-by-one), ví dụ gán `low = mid` thay vì `mid + 1`, hoặc `high = mid` thay vì `mid - 1` → vòng lặp vô hạn.
>
> - Áp dụng trên dữ liệu chưa sắp xếp → kết quả sai.
>
> - Nhầm chỉ số (index) với giá trị → trả về sai chỉ số, không phải phần tử.
>
> - Dùng Binary Search trên Linked List → không hiệu quả (vẫn là O(n) vì không truy cập ngẫu nhiên được).
>

**Mẹo phỏng vấn:** luôn kiểm tra mảng đã sắp xếp chưa. Nếu chưa → dùng Linear Search (hoặc sắp xếp trước, tốn thêm O(n log n)). Nếu đã sắp xếp → dùng Binary Search.

---

### Sắp xếp (Bubble / Selection / Insertion / Merge / Quick Sort)

> 📎 Ảnh thuộc mục này: #3, #6, #8

**Vì sao cần sắp xếp (Sorting)?** Sắp xếp giúp dữ liệu theo thứ tự có ý nghĩa: tìm kiếm dễ dàng hơn (cho phép Binary Search), tổ chức dữ liệu, cải thiện hiệu năng cho các thuật toán khác (Two Pointers, DP, Greedy), và dùng trong thực tế: bảng xếp hạng, báo cáo, lịch trình, indexing...

#### Bubble Sort

So sánh các **phần tử liền kề**, hoán đổi nếu sai thứ tự. Sau mỗi lượt, phần tử lớn nhất được đẩy về cuối.

Ví dụ `[5,1,4,2,8]` → Lượt 1: `[1,4,2,5,8]` → Lượt 2: `[1,2,4,5,8]` → Lượt 3: đã sắp xong.

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
```

**Complexity:** Best O(n) · Average O(n²) · Worst O(n²) · Space O(1) · **Stable**.

#### Selection Sort

Tìm **phần tử nhỏ nhất** trong phần chưa sắp và đưa nó lên đầu (đổi chỗ với vị trí đầu). Lặp lại cho phần còn lại.

Ví dụ `[64,25,12,22,11]` → Lượt 1: 11 là min → `[11,25,12,22,64]` → ... → `[11,12,22,25,64]`.

```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
```

**Complexity:** Best/Average/Worst O(n²) · Space O(1) · **Not Stable**.

#### Insertion Sort

Xây dựng dần một mảng đã sắp: lấy từng phần tử và **chèn vào đúng vị trí** trong phần đã sắp phía trước.

Ví dụ `[12,11,13,5,6]` → chèn 11 sang trái: `[11,12,13,5,6]` → 13 đã đúng chỗ → chèn 5 lên đầu: `[5,11,12,13,6]` → ...

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
```

**Complexity:** Best O(n) · Average O(n²) · Worst O(n²) · Space O(1) · **Stable**. Rất hiệu quả với dữ liệu nhỏ hoặc gần như đã sắp xếp.

#### Merge Sort (Divide & Conquer)

Chia mảng thành 2 nửa, đệ quy sắp xếp mỗi nửa, rồi **trộn (merge)** hai nửa đã sắp lại với nhau.

Ví dụ: `[38,27,43,3,9,82,10]` → chia đôi liên tục tới từng phần tử đơn → trộn dần: `[27,38],[3,43]` → `[3,27,38,43]`; `[9,82],[10]` → `[9,10,82]` → kết quả `[3,9,10,27,38,43,82]`.

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

**Complexity:** Time O(n log n) mọi trường hợp · Space O(n) · **Stable**. Hoạt động tốt với linked list và dữ liệu lớn; không sắp xếp tại chỗ (not in-place).

#### Quick Sort (Divide & Conquer)

Chọn một phần tử làm **pivot**, phân hoạch (partition) mảng: phần tử nhỏ hơn pivot ở trái, lớn hơn ở phải, rồi áp dụng đệ quy cho cả hai phía.

Ví dụ: `[10,7,8,9,1,5]`, chọn pivot = 10 (phần tử cuối) → `[7,8,9,1,5 | 10]` (tất cả đều nhỏ hơn 10) → sort tiếp phần còn lại.

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x < pivot]
    right = [x for x in arr[:-1] if x >= pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)
```

**Complexity:** Average O(n log n) · Worst O(n²) (khi pivot chọn xấu, ví dụ mảng đã sắp và luôn chọn phần tử đầu/cuối) · Space O(log n) trung bình (ngăn xếp đệ quy) · **Not Stable**. Sắp xếp tại chỗ (in-place), hiệu năng trung bình rất tốt.

#### Stable vs Unstable Sorting

- **Stable Sort:** các phần tử có giá trị bằng nhau **giữ nguyên thứ tự tương đối** ban đầu sau khi sắp xếp.

- **Unstable Sort:** thứ tự tương đối của các phần tử bằng nhau **có thể bị thay đổi**.

- Ví dụ input `(5,A),(3,B),(5,C),(3,D)` sắp theo khóa số: stable sort giữ `(3,B),(3,D),(5,A),(5,C)`.

- Tính ổn định (stability) quan trọng khi **sắp xếp đa khóa** (ví dụ sort theo age, rồi theo name).

#### Bảng so sánh tổng hợp các thuật toán sắp xếp

| **Thuật toán** | **Kỹ thuật** | **Best** | **Average** | **Worst** | **Space** | **Stable?** | **Tại chỗ (In-place)?** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Bubble Sort | So sánh liền kề | O(n) | O(n²) | O(n²) | O(1) | Có | Có |
| Selection Sort | Chọn min | O(n²) | O(n²) | O(n²) | O(1) | Không | Có |
| Insertion Sort | Chèn | O(n) | O(n²) | O(n²) | O(1) | Có | Có |
| Merge Sort | Divide & Conquer | O(n log n) | O(n log n) | O(n log n) | O(n) | Có | Không |
| Quick Sort | Divide & Conquer | O(n log n) | O(n log n) | O(n²) | O(log n)* | Không | Có |

*Bộ nhớ Quick Sort là ngăn xếp đệ quy trong trường hợp trung bình.

**Sắp xếp không so sánh (Non-comparison Sorts):** Counting Sort, Radix Sort — dùng khi key nằm trong một phạm vi giới hạn, có thể chạy tuyến tính, ví dụ Counting Sort là O(n + k) thay vì bị chặn dưới O(n log n) như comparison sort.

#### Khi nào dùng thuật toán nào?

- **Insertion Sort:** dữ liệu nhỏ hoặc gần như đã sắp xếp.

- **Merge Sort:** cần sắp xếp ổn định (stable) và cho dữ liệu lớn; tốt với linked list.

- **Quick Sort:** cần sắp xếp tại chỗ (in-place) với hiệu năng trung bình tốt nhất.

- Sắp xếp trước dữ liệu còn cho phép dùng **Two Pointers** và **Binary Search** ở các bước sau.

> 🛠️ **Mẹo phỏng vấn:** Biết khi nào dùng hàm sort có sẵn (built-in, ví dụ `sort()` trong Python) so với tự cài đặt thuật toán (chỉ khi được yêu cầu cụ thể). Luôn đề cập độ phức tạp tốt nhất, trung bình và xấu nhất khi phỏng vấn.

> ⚠️ **Lỗi thường gặp:** đi sắp xếp (tốn O(n log n)) trong khi dùng hash map có thể giải quyết bài toán trong O(n) — luôn tự hỏi "mình có thực sự cần SORT không?"

---

> 📝 **Ghi chú bổ sung**
> - Recursion, Searching và Sorting là ba nền tảng liên kết chặt chẽ: nhiều thuật toán sắp xếp (Merge Sort, Quick Sort) dùng chính kỹ thuật đệ quy/chia để trị; và dữ liệu cần được sắp xếp trước khi áp dụng Binary Search.
>
> - Khi phân tích độ phức tạp thuật toán đệ quy có nhiều overlapping subproblems (như Fibonacci đệ quy thuần hoặc Backtracking không pruning), nên chỉ rõ độ phức tạp hàm mũ và đề xuất tối ưu (memoization/DP, pruning).
>
> - Ba bộ tài liệu gốc dùng ký hiệu và ví dụ hơi khác nhau (C/Java-style code trong bộ "Cẩm Nang DSA", Python-style trong "DSA Notes", và bảng chi tiết trong "Ghi chú giải thuật") nhưng nội dung cốt lõi đã được hợp nhất, không trùng lặp ở trang này.
>
