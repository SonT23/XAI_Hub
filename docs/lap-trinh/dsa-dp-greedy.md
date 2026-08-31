# DSA: Quy hoạch động (DP) & Greedy

> 🖼️ **3 ảnh gốc cho trang này (dán theo đúng thứ tự vào 2 mục bên dưới):**
> 1350_ghi-chu-dsa-dynamic-programming-intro.jpg
>
> 1351_ghi-chu-dsa-classic-dp-patterns.jpg
>
> 1352_ghi-chu-dsa-greedy-bit-tricks.jpg
>

### 1. Quy hoạch động (Dynamic Programming)

> 🖼️ Ảnh thuộc mục này: 1350_ghi-chu-dsa-dynamic-programming-intro.jpg, 1351_ghi-chu-dsa-classic-dp-patterns.jpg

#### 1.1. Nguyên lý cốt lõi

> DP = Overlapping subproblems + Optimal substructure

- **Overlapping subproblems (bài toán con lặp lại):** cùng một subproblem được gọi lại nhiều lần trong quá trình đệ quy (ví dụ: `fib(2)` xuất hiện lặp đi lặp lại khi tính `fib(5)` bằng đệ quy thuần).

- **Optimal substructure (cấu trúc con tối ưu):** lời giải tối ưu của bài toán lớn có thể xây dựng từ lời giải tối ưu của các bài toán con nhỏ hơn.

#### 1.2. Memoization (Top-down) vs Tabulation (Bottom-up)

|   | Top-down (Memoization) | Bottom-up (Tabulation) |
| --- | --- | --- |
| Cách làm | Giải bằng đệ quy, cache kết quả | Xây bảng lặp dần từ nhỏ → lớn |
| Đặc điểm | Chỉ tính phần thực sự cần thiết | Mọi state đều được tính theo đúng thứ tự |
| Ghi nhớ | Cache (dict/array) trong lúc đệ quy | Bảng (array/table) xây tuần tự |

💡 Cùng một ý tưởng, chỉ khác thứ tự tính toán!

#### 1.3. Công thức DP (DP Recipe) — 4 bước

1. **Define state** — Ta đang biểu diễn cái gì?

2. **Transition** — Đi từ state nhỏ hơn như thế nào?

3. **Base case(s)** — State nhỏ nhất / câu trả lời đã biết trước.

4. **Order** — Thứ tự tính toán (cần cho tabulation).

#### 1.4. Ví dụ minh hoạ: Fibonacci

- Transition: `fib[n] = fib[n-1] + fib[n-2]`

- Base case: `fib[0] = 0`, `fib[1] = 1`

- Cây đệ quy top-down cho thấy rõ **overlapping subproblems**: `fib(2)` và `fib(3)` bị tính lại nhiều lần nếu không nhớ kết quả.

- Bảng bottom-up: build trái → phải theo thứ tự n = 0,1,2,3,4,5 → fib[n] = 0,1,1,2,3,5.

```python
# Top-down: Memoization
from functools import lru_cache

@lru_cache(maxsize=None)
def fib_memo(n):
    if n <= 1:
        return n
    return fib_memo(n - 1) + fib_memo(n - 2)

# Bottom-up: Tabulation
def fib_tab(n):
    dp = [0, 1] + [0] * (n - 1)
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
```

> ⏱️ **Độ phức tạp DP:**
> Time = (số state) × (chi phí mỗi transition)
>
> Space = (số state) × (bộ nhớ mỗi state)
>
> Mẹo: đếm số state của bạn, ước lượng chi phí transition → đó chính là độ phức tạp!
>

#### 1.5. Khi nào dùng DP / Greedy / đệ quy thuần?

- **DP:** có overlapping subproblems, có optimal substructure, có thể định nghĩa được state + transition rõ ràng.

- **Greedy:** lựa chọn local là tối ưu toàn cục (cần chứng minh).

- **Đệ quy thuần (Plain recursion):** không có overlap (hiếm gặp) hoặc input quá nhỏ — nếu không cẩn thận sẽ có độ phức tạp hàm mũ 🙁.

⚠️ **Lỗi thường gặp:** Định nghĩa state không rõ ràng hoặc sai → dẫn đến sai recurrence, sai đáp án. Hãy tự hỏi: "Mình đang thực sự giải cái gì?"

#### 1.6. Các pattern DP kinh điển

**Pattern 1 — 1D Climb / House Robber**

- Tại vị trí i, đáp án tốt nhất dùng i phần tử đầu (chọn hoặc bỏ qua phần tử hiện tại).

- State: `dp[i]`

**Pattern 2 — Knapsack (0/1)**

- Chọn hoặc bỏ item i, trong giới hạn capacity W.

- State: `dp[i][w]`

```python
def knapsack_01(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            dp[i][w] = dp[i - 1][w]  # bỏ item i-1
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    dp[i][w],
                    dp[i - 1][w - weights[i - 1]] + values[i - 1],  # lấy item i-1
                )
    return dp[n][capacity]
```

**Pattern 3 — Unbounded Knapsack / Coin Change**

- Dùng một item bất kỳ số lần (không giới hạn, ∞).

- State: `dp[i][w]`

**Pattern 4 — LCS / Edit Distance**

- Ví dụ: A = "ACAGT", B = "A_G_T" → match/skip/replace để căn chỉnh hai chuỗi.

- State: `dp[i][j]`

**Pattern 5 — LIS (Longest Increasing Subsequence)**

- Ví dụ dãy: `3 1 5 2 6 4 9` → dãy con tăng dài nhất: `1 2 4 9`.

- Định nghĩa: dãy con tăng tốt nhất kết thúc tại i.

- State: `dp[i]`

**Pattern 6 — Interval DP (teaser)**

- Giải subproblem trên các interval [i, j].

- State: `dp[i][j]`

- ⭐ Nghĩ tới: partition / merge / burst balloons / matrix chain...

**Pattern 7 — DP on Trees / Paths**

- Tổng hợp kết quả từ node con, hoặc dọc theo đường đi.

- State: `dp[u]` hoặc `dp[u][k]`

#### 1.7. Tối ưu bộ nhớ (Space Optimize)

Dùng rolling array để giảm bộ nhớ khi có thể:

- 1D DP → chỉ giữ `prev`, `curr`

- 2D DP → chỉ giữ prev row/column (tái sử dụng bộ nhớ giữa `dp[i-1][*]` và `dp[i][*]`)

🎯 **Mẹo phỏng vấn:** Trước khi code, xác định PATTERN FAMILY trước: Sequence DP, Knapsack DP, Interval DP, Tree DP, ... others.

⚠️ **Lỗi thường gặp:** Ép dùng DP cho bài toán giải được bằng greedy. Luôn kiểm tra xem greedy có hoạt động trước!

### 2. Giải thuật Tham lam (Greedy) & Bit Manipulation Tricks

> 🖼️ Ảnh thuộc mục này: 1352_ghi-chu-dsa-greedy-bit-tricks.jpg

#### 2.1. Greedy Algorithm

> Lựa chọn **local** → tối ưu **global**, khi tính chất exchange/greedy được thoả mãn.

**Các bài toán kinh điển (Classics):**

- Interval scheduling (lập lịch khoảng thời gian)

- Huffman coding (teaser)

- Jump game intuition

**Ví dụ: Interval Scheduling (earliest finish first)**

Cho các khoảng: [1,3], [4,6], [7,9] (không chồng nhau) và [0,5], [3,8] (chồng nhau, chọn khoảng kết thúc sớm nhất trước).

→ Greedy chọn 3 interval không chồng nhau: [1,3], [4,6], [7,9] ✓

```python
def interval_scheduling(intervals):
    # intervals: list of (start, end)
    intervals.sort(key=lambda x: x[1])  # sắp xếp theo thời gian kết thúc sớm nhất
    selected = []
    last_end = float("-inf")
    for start, end in intervals:
        if start >= last_end:
            selected.append((start, end))
            last_end = end
    return selected
```

> ⚠️ **Lưu ý quan trọng:** Lựa chọn greedy PHẢI được biện minh — chứng minh (exchange argument/matroid...) hoặc đưa ra phản ví dụ.
> MISTAKE thường gặp: giả định greedy hoạt động mà không chứng minh. Counterexample > lời giải sai.
>

#### 2.2. Bit Manipulation Tricks

Các phép toán bit cơ bản: `&` (AND), `|` (OR), `^` (XOR), `<<` (left shift), `>>` (right shift).

**Kiểm tra luỹ thừa của 2:**

```python
def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

# Ví dụ: 8 = 1000(2)
# 1000 & 0111 = 0000 -> True
```

**XOR cho phần tử thiếu/duy nhất:**

Tính chất: `a^a = 0`, `a^0 = a`, `a^a^b = b`

```python
# Tìm số bị thiếu trong dãy 1..n
def missing_number(nums, n):
    ans = 0
    for i in range(1, n + 1):
        ans ^= i
    for x in nums:
        ans ^= x
    return ans

# Ví dụ: 1^2^3^4^5 ^ 3^1^2^5 = 4 (số 4 bị thiếu)
```

**Bitmask cho subset với n nhỏ:**

```python
# n = 3 -> 2^3 = 8 subsets
def all_subsets(elements):
    n = len(elements)
    result = []
    for mask in range(1 << n):  # mask từ 0 tới (1<<n)-1
        subset = [elements[i] for i in range(n) if mask & (1 << i)]
        result.append(subset)
    return result

# mask (bin): 000 001 010 011 100 101 110 111
# subset:     {}  {0} {1} {0,1} {2} {0,2} {1,2} {0,1,2}
```
