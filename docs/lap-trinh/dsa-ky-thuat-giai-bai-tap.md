# DSA: Kỹ thuật giải bài tập (Two Pointers, Sliding Window, Prefix Sum...)

> 🖼️ **Nguồn ảnh gốc tổng hợp trong trang này (8 ảnh):**
> 1. `1333_cam-nang-dsa-cac-pattern-giai-bai-toan-pho-bien.jpg`
>
> 2. `1339_ghi-chu-dsa-two-pointers-sliding-window.jpg`
>
> 3. `1353_ghi-chu-dsa-cheat-sheet-pattern-map.jpg`
>
> 4. `1412_ghi-chu-ky-thuat-hai-con-tro-two-pointers-trong-ds.jpg`
>
> 5. `1413_ghi-chu-ky-thuat-cua-so-truot-sliding-window.jpg`
>
> 6. `1414_ghi-chu-tong-tien-to-va-mang-hieu-prefix-sum.jpg`
>
> 7. `1420_ghi-chu-co-ban-ve-thao-tac-bit-bitwise-operations.jpg`
>
> 8. `1421_ghi-chu-cac-mau-giai-quyet-van-de-lap-trinh-proble.jpg`
>

Trang này tổng hợp các **kỹ thuật (pattern) giải bài tập DSA phổ biến nhất**: Two Pointers, Sliding Window, Prefix Sum/Difference Array, một số thao tác Bit nâng cao, và một bản đồ pattern tổng quát giúp nhận diện nhanh nên dùng kỹ thuật nào khi gặp một bài toán mới.

---

### Two Pointers (Kỹ thuật hai con trỏ)

> 📌 Ảnh thuộc mục này: `1339_...jpg`, `1412_...jpg`

#### Khái niệm

Two Pointers dùng **hai chỉ số (con trỏ)** di chuyển qua một cấu trúc dữ liệu (thường là mảng/chuỗi đã sắp xếp) để giải bài toán mà không cần vòng lặp lồng nhau — giúp giảm độ phức tạp thời gian từ **O(n²) xuống O(n)**.

#### Hai dạng con trỏ chính

| **Dạng** | **Cách hoạt động** | **Dùng khi** |
| --- | --- | --- |
| Đối xứng (trái/phải hội tụ) | `left = 0`, `right = n-1`, hai con trỏ tiến về nhau | Mảng **đã sắp xếp**, tìm cặp/bộ ba thỏa điều kiện |
| Cùng chiều (fast & slow) | Hai con trỏ cùng xuất phát, di chuyển tốc độ khác nhau | Linked List Cycle, loại bỏ trùng lặp, Happy Number |

#### Cách hoạt động (dạng đối xứng — Pair Sum)

- Sắp xếp mảng nếu chưa sắp xếp.

- `left = 0`, `right = n - 1`.

- Lặp `while left < right`:
    - `sum = a[left] + a[right]`

    - Nếu `sum == target` → tìm thấy.

    - Nếu `sum < target` → `left += 1` (cần tăng tổng).

    - Nếu `sum > target` → `right -= 1` (cần giảm tổng).

| 2 | 4 | 7 | 11 | 15 | 20 | 24 |
| --- | --- | --- | --- | --- | --- | --- |

`left` bắt đầu từ đầu (0), `right` bắt đầu từ cuối (n-1). Hai đầu hội tụ về phía nhau cho tới khi gặp nhau hoặc tìm ra đáp án.

#### Khi nào dùng

- Tìm cặp/bộ ba (pair/triplet) có tổng cho trước, trên mảng **đã sắp xếp** (Two Sum II, 3Sum).

- Xóa phần tử trùng lặp trong mảng đã sắp xếp (Remove Duplicates from Sorted Array).

- Kiểm tra palindrome trong chuỗi (Valid Palindrome).

- Container With Most Water và các biến thể Trapping Rain Water.

#### Độ phức tạp

| Cách tiếp cận | Time | Space | Ghi chú |
| --- | --- | --- | --- |
| Hai con trỏ | O(n) | O(1) | Mỗi con trỏ di chuyển tối đa n lần |
| Brute Force | O(n²) | O(1) | Dùng vòng lặp lồng nhau |

> ⚠️ **Lỗi thường gặp:** quên di chuyển con trỏ trong một số trường hợp; di chuyển sai hướng (bỏ sót phần tử); không xử lý trường hợp biên (mảng rỗng, một phần tử); di chuyển cả hai con trỏ cùng lúc khi chỉ nên di chuyển một.

#### Code mẫu (Python) — Two Sum trên mảng đã sắp xếp

```python
def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        s = arr[left] + arr[right]
        if s == target:
            return [left, right]
        elif s < target:
            left += 1
        else:
            right -= 1
    return [-1, -1]
```

#### Code mẫu (Python) — Kiểm tra Palindrome

```python
def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
```

---

### Sliding Window (Cửa sổ trượt)

> 📌 Ảnh thuộc mục này: `1339_...jpg`, `1413_...jpg`

#### Khái niệm

Sliding Window duy trì một **cửa sổ **`[left, right]` trên mảng/chuỗi, trượt qua dữ liệu để thỏa mãn một ràng buộc nào đó — tránh việc phải quét lại từ đầu cho mỗi vị trí, đưa độ phức tạp về **O(n)**.

#### Cửa sổ cố định (Fixed-size Window)

- Kích thước cửa sổ **k cố định**.

- Trượt cửa sổ từng bước một: thêm phần tử mới bên phải, bỏ phần tử cũ bên trái.

- Hữu ích khi cần mảng con/chuỗi con có kích thước đúng bằng k.

Ví dụ: `Array = [1, 3, 2, 6, 4, 1, 8]`, `k = 3` → các cửa sổ liên tiếp có tổng lần lượt: `[1,3,2]=6 → [3,2,6]=11 → [2,6,4]=12 → [6,4,1]=11 → [4,1,8]=13`.

#### Cửa sổ biến đổi (Variable-size Window)

- Kích thước cửa sổ **không cố định**, co giãn theo điều kiện.

- **Mở rộng phải (+):** đưa `a[right]` vào cửa sổ để tăng tổng/kích thước.

- **Thu hẹp trái (−):** trong khi ràng buộc bị vi phạm, dịch `left` tới để thu hẹp cửa sổ.

- Hữu ích để tìm mảng con/chuỗi con **nhỏ nhất/dài nhất** thỏa điều kiện.

Ví dụ ràng buộc: `Max sum ≤ k`; `Longest substring có tối đa K ký tự khác nhau`.

#### Quy trình chung

1. Thêm phần tử mới với `right`.

2. Kiểm tra điều kiện; nếu vi phạm thì thu hẹp từ `left`.

3. Theo dõi/cập nhật kết quả (max/min/count...) trong mỗi cửa sổ hợp lệ.

#### Khi nào dùng

Bài toán về **subarray/substring liên tục (contiguous)** — không dùng được nếu phần tử không liền kề nhau.

#### Các bài toán thường gặp

1. Maximum Sum Subarray kích thước K (fixed window).

2. Smallest Subarray với Sum ≥ K (variable window).

3. Longest Substring không lặp ký tự.

4. Longest Substring với tối đa K ký tự khác nhau.

5. Fruit Into Baskets (tối đa 2 loại quả).

6. Minimum Window Substring.

7. Max Consecutive Ones III (đổi tối đa K số 0).

#### Độ phức tạp

Mỗi phần tử được duyệt tối đa 2 lần (một lần bởi `left`, một lần bởi `right`) → độ phức tạp tổng thể là **tuyến tính O(n)**, bộ nhớ **O(1)**.

> ⚠️ **Lỗi thường gặp:** quên di chuyển `left` khi điều kiện bị vi phạm; không xử lý trường hợp biên (mảng rỗng, `k > n`); lỗi lệch chỉ số (off-by-one) khi xác định biên cửa sổ; không cập nhật window state (sum/count).

#### Code mẫu (Python) — Max Subarray Sum kích thước K (fixed window)

```python
def max_sum_fixed_k(arr, k):
    window_sum = sum(arr[:k])
    best = window_sum
    for right in range(k, len(arr)):
        window_sum += arr[right] - arr[right - k]
        best = max(best, window_sum)
    return best
```

#### Code mẫu (Python) — Longest Substring không lặp ký tự (variable window)

```python
def longest_unique_substring(s):
    seen = set()
    left = 0
    best = 0
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        best = max(best, right - left + 1)
    return best
```

---

### Prefix Sum & Difference Array (Tổng tiền tố & Mảng hiệu)

> 📌 Ảnh thuộc mục này: `1333_...jpg` (Range Query, Subarray Sum = K), `1414_...jpg`

#### Prefix Sum (Tổng tiền tố)

Prefix Sum lưu **tổng tích lũy** các phần tử từ đầu đến chỉ số hiện tại: `Prefix[i] = Tổng của A[0..i]`. Sau khi tiền xử lý O(n), có thể trả lời **truy vấn tổng đoạn con bất kỳ trong O(1)**.

Ví dụ: `A = [3, 1, 4, 2, 5]`

| Chỉ số | 0 | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- | --- |
| A[i] | 3 | 1 | 4 | 2 | 5 |
| Prefix[i] | 3 | 4 | 8 | 10 | 15 |

**Công thức truy vấn tổng khoảng **`[L, R]`**:**

`Sum(L, R) = Prefix[R] - Prefix[L-1]` (nếu `L > 0`, ngược lại `Sum(L,R) = Prefix[R]`)

Ví dụ: `Prefix = [3,4,8,10,15]`, truy vấn tổng từ `L=1` đến `R=3` → `Prefix[3] - Prefix[0] = 10 - 3 = 7`.

#### Difference Array (Mảng hiệu)

Difference Array lưu **hiệu giữa các phần tử liền kề** của mảng gốc: `Diff[0] = A[0]`; `Diff[i] = A[i] - A[i-1]` (`i > 0`). Hữu ích để **cập nhật theo khoảng hiệu quả trong O(1)**; sau khi cập nhật xong, dựng lại mảng gốc bằng chính kỹ thuật Prefix Sum trên mảng Diff.

Ví dụ: `A = [3, 1, 4, 2, 5]` → `Diff = [3, -2, 3, -2, 3]`.

**Cập nhật khoảng:** để cộng `+v` vào mọi phần tử trong khoảng `[l, r]`:

- `Diff[l] += v`

- `Diff[r+1] -= v` (nếu `r+1` còn trong mảng)

Ví dụ: thêm `+5` vào khoảng `[1,3]` của `A = [3,1,4,2,5]`:

- `Diff[1] += 5`, `Diff[4] -= 5` → `Diff = [3, 3, 3, -2, -2]`

- Dựng lại bằng Prefix Sum trên Diff → `A = [3, 6, 9, 7, 5]`

#### Ứng dụng

- Truy vấn tổng khoảng nhanh, lặp lại nhiều lần.

- Đếm tần suất trong mảng con; bài toán `Subarray Sum = K` (kết hợp Prefix Sum + HashMap).

- Cập nhật khoảng + truy vấn điểm (Difference Array).

- Cập nhật khoảng + truy vấn khoảng (Prefix Sum áp lên Difference Array).

- Truy vấn tổng khoảng 2D (dùng Prefix Sum 2D).

#### Độ phức tạp

| Thao tác | Prefix Sum | Diff Array (cập nhật khoảng + truy vấn điểm) | Diff Array (cập nhật khoảng + truy vấn khoảng) |
| --- | --- | --- | --- |
| Tiền xử lý | O(n) | – | O(n) |
| Truy vấn tổng khoảng | O(1) | O(n) | O(1) |
| Cập nhật khoảng | – | O(1) | O(1) |
| Bộ nhớ | O(n) | O(n) | O(n) |

> ⚠️ **Lỗi thường gặp:** lệch chỉ số trong Prefix Sum; quên xử lý trường hợp `L = 0`; quên cập nhật `Diff[R+1]` khi cập nhật khoảng; quên dựng lại mảng gốc bằng Prefix Sum sau khi cập nhật Difference Array.

> 💡 **Mẹo phỏng vấn:** nếu bài toán có nhiều truy vấn khoảng hoặc nhiều cập nhật khoảng, đó thường là dấu hiệu cho thấy Prefix Sum hoặc Difference Array là cách tiếp cận tối ưu. Prefix Sum tốt nhất cho truy vấn tổng nhanh; Difference Array tốt nhất cho cập nhật khoảng nhanh.

#### Code mẫu (Python)

```python
# Prefix Sum: tiền xử lý O(n), truy vấn O(1)
def build_prefix(arr):
    prefix = [0] * len(arr)
    prefix[0] = arr[0]
    for i in range(1, len(arr)):
        prefix[i] = prefix[i - 1] + arr[i]
    return prefix

def range_sum(prefix, l, r):
    return prefix[r] - (prefix[l - 1] if l > 0 else 0)

# Difference Array: cập nhật khoảng O(1)
def build_diff(arr):
    diff = [0] * (len(arr) + 1)
    diff[0] = arr[0]
    for i in range(1, len(arr)):
        diff[i] = arr[i] - arr[i - 1]
    return diff

def range_update(diff, l, r, val):
    diff[l] += val
    if r + 1 < len(diff):
        diff[r + 1] -= val

def rebuild_from_diff(diff, n):
    arr = [0] * n
    arr[0] = diff[0]
    for i in range(1, n):
        arr[i] = arr[i - 1] + diff[i]
    return arr
```

---

### Bit Manipulation (tóm tắt — tránh trùng lặp)

> 📌 Ảnh thuộc mục này: `1420_...jpg`

> ℹ️ Các thao tác bit **cơ bản** (AND/OR/XOR/NOT/dịch trái-phải, biểu diễn nhị phân, kiểm tra số chẵn/lẻ, kiểm tra lũy thừa của 2, dùng XOR để tìm số bị thiếu, kỹ thuật bitmask cho tập con/subset) **đã được trình bày chi tiết** ở trang **"DSA: Quy hoạch động & Greedy"** — xem trang đó để tránh trùng lặp. Phần dưới đây chỉ liệt kê thêm các **mẹo bit nâng cao** xuất hiện trong ảnh `1420` mà chưa có ở trang kia.

#### Các mẹo bit bổ sung

| **Mẹo** | **Công thức / Cách dùng** | **Giải thích** |
| --- | --- | --- |
| Đảo ngược mọi bit (NOT) | `~A` | 0→1, 1→0. Trên số có dấu: `~A = -(A + 1)` (bù hai). VD: `A=12` → `~A = -13`. |
| Tắt bit set thấp nhất | `n & (n - 1)` | Xóa bit 1 thấp nhất của n. Dùng trong thuật toán Brian Kernighan để đếm bit set. |
| Tách (cô lập) bit set thấp nhất | `n & (-n)` | Trả về riêng bit 1 thấp nhất (dựa trên biểu diễn bù hai). |
| Đếm số bit set (Brian Kernighan) | Lặp `n = n & (n-1)` cho đến khi `n == 0`, đếm số lần lặp | Nhanh hơn duyệt từng bit khi số bit set ít. |
| Hoán đổi hai số không dùng biến tạm | `a = a^b; b = a^b; a = a^b;` | Dùng tính chất XOR để swap tại chỗ. |
| Kiểm tra bit thứ k | `(n >> k) & 1` | Trả về giá trị bit thứ k (0 hoặc 1). |
| Bật (set) bit thứ k | `n \| (1 << k)` | Đặt bit thứ k thành 1. |
| Tắt (clear) bit thứ k | `n & ~(1 << k)` | Đặt bit thứ k thành 0. |
| Đảo (toggle) bit thứ k | `n ^ (1 << k)` | Đảo giá trị bit thứ k. |

#### Dịch bit — lưu ý về số có dấu

- **Dịch trái **`<<`: dịch bit sang trái k vị trí, thêm 0 vào bên phải; tương đương nhân với `2^k`. VD: `5 << 1 = 10`, `5 << 2 = 20`.

- **Dịch phải **`>>`: dịch bit sang phải k vị trí; **không dấu** thì thêm 0 bên trái, **có dấu** thì thêm bit dấu (dịch số học); tương đương chia cho `2^k`. VD: `20 >> 1 = 10`, `20 >> 2 = 5`.

> ⚠️ **Lỗi thường gặp:** quên xử lý số âm (biểu diễn bù hai); nhầm lẫn hành vi `<<`/`>>` giữa số có dấu và không dấu (đặc biệt khi chuyển đổi giữa các ngôn ngữ lập trình).

> 💡 **Điểm chính:** Thao tác bit chạy rất nhanh (O(1) phần cứng), cải thiện hiệu năng và giúp giải nhiều bài toán khó một cách tinh gọn — thường gặp trong lập trình thi đấu và các bài toán hệ thống. Nên luyện tập để nhận diện nhanh các mẫu (pattern) bit phổ biến.

---

### Tổng hợp các Pattern giải bài tập phổ biến

> 📌 Ảnh thuộc mục này: `1333_...jpg`, `1353_...jpg`, `1421_...jpg`

> ⭐ **Điểm chính:** Nắm vững **pattern** (mẫu giải quyết vấn đề) quan trọng hơn việc học thuộc từng bài toán riêng lẻ. Khi gặp bài mới, hãy nhận diện nó thuộc pattern nào thay vì cố nhớ lời giải cụ thể.

#### 1. Làm sao để nhận diện đúng pattern?

1. Hiểu rõ đề bài.

2. Ghi chú lại các ràng buộc (constraints: n, giá trị, giới hạn thời gian...).

3. Tìm các từ khóa và đặc điểm của đề bài.

4. So khớp với các pattern đã biết.

5. Chọn cấu trúc dữ liệu (data structure) + thuật toán (algorithm) phù hợp.

6. Tối ưu và xử lý edge case.

#### 2. Bảng ánh xạ Pattern (Pattern Map) — "Nếu bạn thấy X → Hãy thử Y"

| **Dấu hiệu / Loại bài toán** | **Pattern nên dùng** | **Ví dụ bài toán** |
| --- | --- | --- |
| Contiguous segment (đoạn liên tục) | Sliding Window | Max Sum Subarray kích thước K, Longest Substring không lặp |
| Pair/Triplet có tổng = target | Two Pointers hoặc Hashing | Two Sum, 3Sum, Pair Sum |
| Range Query (truy vấn tổng đoạn) | Prefix Sum | Range Sum Query, Subarray Sum = K |
| Order/Nesting (thứ tự, lồng nhau) | Stack | Valid Parentheses, kiểm tra dấu ngoặc |
| Hierarchy (cấu trúc phân cấp) | Tree Recursion | Duyệt cây: f(node) → f(children) |
| Relations/Paths (quan hệ, đường đi) | Graph BFS/DFS | Duyệt đồ thị theo chiều rộng/sâu |
| Extreme/Top-K (giá trị cực trị) | Heap | Max/Min Heap, Top K Elements |
| Sorted/Monotonic answer (đáp án đơn điệu) | Binary Search | Koko Eating Bananas, Search in Rotated Array |
| Uniqueness (tính duy nhất) | Hashing | Kiểm tra trùng lặp, đếm tần suất |
| Optimal overlapping structure (bài toán con chồng lấp) | Dynamic Programming | Fibonacci, 0/1 Knapsack — định nghĩa state + transition |
| Choice/All ways (tất cả lựa chọn/tổ hợp) | Recursion & Backtracking | N-Queens, Subset/Permutations |
| Local optimal with proof (lựa chọn tối ưu cục bộ, có thể chứng minh exchange argument) | Greedy | Activity Selection, Fractional Knapsack |
| Bài toán chia nhỏ thành các bài toán con độc lập | Divide & Conquer | Merge Sort, Binary Search |

#### 3. Complexity Strip — Độ phức tạp của các thao tác phổ biến

| Thao tác | Độ phức tạp |
| --- | --- |
| Array access (truy cập mảng) | O(1) |
| Push/Pop (stack) | O(1) |
| Enqueue/Dequeue (queue) | O(1) |
| Hash map get/put | trung bình O(1) |
| Heap push/pop | O(log n) |
| Sort (sắp xếp) | O(n log n) |

#### 4. Ký hiệu độ phức tạp thường gặp

| Ký hiệu | Tên | Ví dụ |
| --- | --- | --- |
| O(1) | Hằng số | Truy cập mảng |
| O(log n) | Logarit | Binary Search |
| O(n) | Tuyến tính | Vòng lặp đơn |
| O(n log n) | Tuyến tính-log | Merge Sort |
| O(n²) | Bậc hai | Vòng lặp lồng nhau |

#### 5. Ví dụ nhận diện pattern nhanh

- Sum/Subarray → **Sliding Window**

- Pair/Triplet → **Two Pointers**

- Range Query → **Prefix Sum**

- Uniqueness → **Hashing**

- Choice/All ways → **Backtracking**

- Optimal choice → **Greedy**

#### 6. Chiến lược Brute Force → Optimize

- Bắt đầu với brute force (thử trực tiếp tất cả khả năng — đơn giản, dễ triển khai, nhưng không hiệu quả với đầu vào lớn).

- Phân tích bottleneck (điểm nghẽn hiệu năng).

- Tìm pattern phù hợp (ánh xạ bài toán vào các mẫu đã biết: Two Pointer, Sliding Window, Prefix Sum, Fast & Slow Pointer, DFS/BFS, Binary Search...).

- Chọn cách tiếp cận tốt hơn (dùng cấu trúc dữ liệu/thuật toán phù hợp hơn, VD: dùng HashMap thay vì vòng lặp lồng nhau để giảm từ O(n²) xuống O(n)).

- Tối ưu time & space.

#### 7. Quy trình tổng quát giải một bài toán DSA

`Problem → Constraints → Identify Pattern → Choose Data Structure → Design Algorithm → Test & Edge Cases → Optimize`

Diễn giải chi tiết hơn theo 5 bước: **Hiểu** (đọc kỹ đề bài) → **Lên kế hoạch** (nghĩ các cách tiếp cận) → **Áp dụng** (triển khai giải pháp tốt nhất) → **Kiểm thử** (chạy test case & dry run) → **Tối ưu** (cải thiện nếu cần).

#### 8. Chạy thử (Dry Run) — ví dụ minh họa Two Pointers

Với `Array = [2, 7, 11, 15]`, `Target = 9`:

| i | j | Sum | Hành động |
| --- | --- | --- | --- |
| 0 | 3 | 17 | Sum > 9 → j-- |
| 0 | 2 | 13 | Sum > 9 → j-- |
| 0 | 1 | 9 | Tìm thấy! |

#### 9. Trường hợp biên (Edge Cases) cần luôn kiểm tra

- Mảng/chuỗi rỗng.

- Một phần tử duy nhất.

- Mọi phần tử giống nhau.

- Đầu vào đã sắp xếp / sắp xếp ngược.

- Giá trị nguyên lớn nhất/nhỏ nhất, số âm, kích thước đầu vào lớn.

#### 10. Mẹo viết code & mẹo phỏng vấn

- Viết code sạch, dễ đọc; dùng tên biến rõ nghĩa; chia giải pháp thành các hàm nhỏ.

- Kiểm thử với nhiều test case; đừng tối ưu quá sớm; ghi chú logic quan trọng; xử lý lỗi & trường hợp biên.

- Luyện tập thường xuyên; luôn phân tích Time & Space; tập trung vào trường hợp xấu nhất.

- Khi phỏng vấn: giao tiếp rõ ràng cách tiếp cận, giải thích tư duy, gọi tên pattern đang dùng thành tiếng trước khi code.

> ⚠️ **Lỗi thường gặp:** đọc đề không kỹ; code ngay không lên kế hoạch; bỏ qua trường hợp biên.

---

> 📝 **Ghi chú bổ sung**
> - 5 pattern cốt lõi trong trang này (Two Pointers, Sliding Window, Prefix Sum/Difference Array) đều có thể kết hợp với Hashing để mở rộng khả năng áp dụng (VD: Subarray Sum = K dùng Prefix Sum + HashMap thay vì yêu cầu mảng đã sắp xếp).
>
> - Phần Bit Manipulation cơ bản (AND/OR/XOR/shift, kiểm tra lũy thừa 2, XOR tìm số thiếu, bitmask subset) xem chi tiết tại trang **"DSA: Quy hoạch động & Greedy"**.
>
> - Bảng Pattern Map ở mục cuối là công cụ tra cứu nhanh rất hữu ích khi luyện tập — nên học thuộc để phản xạ nhanh khi đọc đề bài mới.
>
