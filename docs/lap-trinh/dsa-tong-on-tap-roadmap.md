# DSA: Tổng ôn tập & Lộ trình học (Roadmap)

> 🖼️ Trang này tổng hợp nội dung từ 3 ảnh cheat sheet / ghi chú tổng ôn tập DSA gốc:
> - `1334_cam-nang-dsa-cheat-sheet-on-tap-phong-van-cuoi-cun.jpg`
>
> - `1354_ghi-chu-dsa-roadmap-recap-tong-ket.jpg`
>
> - `1422_cam-nang-on-tap-dsa-tong-hop-mang-chuoi-tim-kiem.jpg`
>

### Bảng tổng hợp độ phức tạp các cấu trúc dữ liệu & giải thuật

#### Big-O Complexity (bảng nhanh)

| **Complexity** | **Tên** | **Tốc độ** | **Khi nào xảy ra** | **Ví dụ** |
| --- | --- | --- | --- | --- |
| O(1) | Hằng số | Tốt nhất | Truy cập phần tử mảng, thao tác hash | arr[i], stack push/pop, hashMap.get() |
| O(log n) | Logarit | Rất tốt | Binary Search, thao tác trên cây cân bằng/heap | Binary Search, AVL/Red-Black Tree |
| O(n) | Tuyến tính | Tốt | Vòng lặp đơn qua n phần tử | Linear Search, duyệt list/array |
| O(n log n) | Tuyến tính-log | Khá tốt | Sắp xếp hiệu quả dựa trên so sánh | Merge Sort, Quick Sort, Heap Sort |
| O(n²) | Bậc hai | Kém | Vòng lặp lồng trên n phần tử | Bubble Sort, Selection Sort, brute force |
| O(2ⁿ) | Mũ | Rất kém | Đệ quy sinh 2 nhánh mỗi bước | Subset/Recursion |
| O(n!) | Giai thừa | Cực kém | Thử mọi hoán vị | Permutations |

**Thứ tự tăng dần cần nhớ:** O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ) < O(n!)

#### So sánh các thuật toán Sắp xếp

| **Algorithm** | **Best** | **Average** | **Worst** | **Space** | **Stable** |
| --- | --- | --- | --- | --- | --- |
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | No |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | No |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) | No |

#### Array vs Linked List

|   | **Array** | **Linked List** |
| --- | --- | --- |
| Bộ nhớ | Liên tiếp | Không liên tiếp |
| Random access | O(1) | Không hỗ trợ, O(n) |
| Insert/Delete | O(n) | O(1) (nếu có sẵn nút) |
| Kích thước | Cố định | Động |

*Dùng Array cho truy cập nhanh. Dùng Linked List cho insert/delete thường xuyên.*

#### Stack vs Queue

|   | **Stack (LIFO)** | **Queue (FIFO)** |
| --- | --- | --- |
| Nguyên tắc | Last In First Out — thao tác ở TOP | First In First Out |
| Thao tác | push() / pop() / peek() | enqueue() / dequeue() |
| Ứng dụng | Undo/Backtracking, đệ quy, parsing, quay lui | Scheduling, BFS, lập lịch, bộ đệm |

#### BFS vs DFS

|   | **BFS** | **DFS** |
| --- | --- | --- |
| Bộ nhớ | Tốn ít hơn (theo level) | Tốn nhiều hơn (đi sâu) |
| Cấu trúc dùng | Queue | Stack/Recursion |
| Ứng dụng | Tìm shortest path (Unweighted Graph), level order traversal | Đi sâu trước, Backtracking, Topo Sort |

#### Các cấu trúc dữ liệu & kỹ thuật cốt lõi khác

| **Chủ đề** | **Tóm tắt** |
| --- | --- |
| Mảng (Array) | Kích thước cố định, bộ nhớ liên tục. Truy cập ngẫu nhiên O(1). Chèn/Xóa ở giữa tốn kém O(n). |
| Chuỗi (String) | Dãy ký tự, bất biến trong nhiều ngôn ngữ. Thao tác phổ biến: so sánh, tìm kiếm, chuỗi con. |
| Đệ quy (Recursion) | Hàm tự gọi chính nó, cần trường hợp cơ sở (base case), dùng call stack. Phổ biến trong Trees, Backtracking, DP. |
| Hai con trỏ (Two Pointers) | Dùng hai chỉ số, thường trên mảng đã sắp xếp. Giải trong O(n). |
| Sliding Window | Duy trì một cửa sổ/khoảng, cố định hoặc biến đổi. Hữu ích cho bài toán mảng/chuỗi con. |
| Prefix Sum | Tính trước tổng tiền tố. Truy vấn tổng khoảng O(1). Tuyệt vời cho nhiều truy vấn khoảng. |
| Băm (Hashing) | Ánh xạ giá trị vào chỉ số (Hash). HashMap, HashSet. Thao tác trung bình O(1). |
| Tìm kiếm nhị phân | Chia để trị trên dữ liệu đã sắp xếp. Time O(log n). Tìm lần xuất hiện đầu/cuối, cận trên/dưới. |
| Thao tác Bit | Làm việc trực tiếp với bit: &, |, ^, ~, <<, >>. Hữu ích trong tối ưu hóa, mẹo XOR, mặt nạ bit. |
| Tree Traversals | Preorder (N-L-R), Inorder (L-N-R), Postorder (L-R-N), Level Order (BFS dùng Queue). |
| BST (Binary Search Tree) | Left < Root < Right. Inorder traversal cho ra thứ tự đã sorted. Search/Insert/Delete trong O(h). |
| Heap & Priority Queue | Complete Binary Tree. Min Heap: parent ≤ child; Max Heap: parent ≥ child. Insert/Delete O(log n), Peek O(1). Dùng trong Priority Queue (CPU scheduling, Dijkstra). |

#### Bản đồ mẫu nhanh (Pattern → Ứng dụng)

| **Pattern** | **Ứng dụng điển hình** |
| --- | --- |
| Hai con trỏ | Cặp/Bộ ba/Bài toán mảng đã sắp |
| Sliding Window | Ràng buộc mảng con/chuỗi con |
| Prefix Sum | Truy vấn tổng khoảng |
| Hashing | Tần suất/Tính duy nhất/Tra cứu |
| Stack | Phần tử lớn hơn/Ngoặc/Đảo ngược |
| BFS (Queue) | Đường đi ngắn nhất trên đồ thị không trọng số |
| Binary Search | Tìm kiếm trong khoảng đã sắp xếp |

### Lộ trình học đề xuất (Roadmap)

Cả 2 nguồn ghi chú roadmap đều thống nhất một trình tự học từ nền tảng → cấu trúc dữ liệu → giải thuật → pattern → luyện tập có hệ thống. Áp dụng vào các trang DSA đã có trong hub **Lập trình**, thứ tự học đề xuất như sau:

1. **DSA: Nhập môn & Độ phức tạp (Big-O)** — *Foundations*: nắm Big-O, phân tích độ phức tạp thời gian/không gian.

2. **DSA: Mảng, Chuỗi & Danh sách liên kết** — *Core Structures* (phần 1): Array, String, Linked List.

3. **DSA: Stack, Queue & Hashing** — *Core Structures* (phần 2): Stack, Queue, HashMap/HashSet.

4. **DSA: Đệ quy, Tìm kiếm & Sắp xếp** — *Core Algorithms*: Recursion, Searching (Linear/Binary Search), Sorting.

5. **DSA: Trees, Heap & Graphs** — *Core Structures* (phần 3) + *Core Algorithms*: Tree Traversals, BST, Heap/Priority Queue, BFS/DFS trên đồ thị.

6. **DSA: Quy hoạch động (DP) & Greedy** — *Patterns* (phần 1): tư duy chia bài toán con, tối ưu.

7. **DSA: Kỹ thuật giải bài tập** — *Patterns* (phần 2) + *Luyện tập có hệ thống*: Two Pointers, Sliding Window, Prefix Sum, Backtracking, Divide & Conquer, cộng với luyện đề có tính giờ (timed mocks).

> 🧭 **Sơ đồ tổng quát (theo ghi chú Roadmap & Recap):**
> Foundations (Big-O, arrays) → Core Structures (hash, stack, list, tree, heap, graph) → Core Algorithms (search, sort, BFS/DFS) → Patterns (window, backtrack, DP, greedy) → Luyện tập có hệ thống + Timed Mocks
>
> Một lộ trình khác (theo cẩm nang cuối cùng) tóm gọn: Arrays → Strings → Linked List → Stack/Queue → Hashing → Recursion → Searching → Sorting → Trees → Heap → Graphs → Patterns
>

### Checklist ôn tập phỏng vấn / tổng kết

#### Quy trình giải bài (Interview Problem-Solving Checklist)

- [ ] Hiểu rõ đề bài

- [ ] Phân tích với ví dụ cụ thể

- [ ] Xác định constraints & edge case

- [ ] Chọn đúng pattern & data structure

- [ ] Viết brute force solution trước

- [ ] Tối ưu (time & space)

- [ ] Test với sample & edge case

- [ ] Phân tích độ phức tạp

- [ ] Trình bày rõ ràng cách tiếp cận

#### Recap Checklist (khi giải một bài DSA)

- [ ] 

- [ ] 

- [ ] 

- [ ] 

- [ ] 

> ⭐ **Điểm chính**
> - Luyện mẫu, không chỉ bài toán
>
> - Hiểu Time & Space Complexity
>
> - Chạy thử trước khi code
>
> - Chỉ tối ưu sau khi có giải pháp đúng
>

> ⚠️ **Lỗi thường gặp**
> - Bỏ qua trường hợp biên
>
> - Lỗi lệch chỉ số (off-by-one)
>
> - Không phân tích độ phức tạp
>
> - Làm phức tạp hóa bài toán đơn giản
>

> 💡 **Ghi nhớ**
> Mỗi bài toán đều có mẫu.
>
> Xác định → Chọn cách tiếp cận đúng → Triển khai → Kiểm thử → Tối ưu
>

> 🎯 **Mẹo phỏng vấn:** Giải thích cách tiếp cận rõ ràng. Nói rõ tư duy, xử lý trường hợp biên và viết code đúng, sạch!

> 📌 **Ghi nhớ cốt lõi:** DSA là tư duy có thể tái sử dụng — không phải một kho lời giải.

### Ghi chú bổ sung

> 📝 
> - Trang này là bản tổng hợp cuối cùng (capstone) cho toàn bộ chủ đề DSA trong hub **Lập trình**, gộp nội dung từ 3 bộ cheat sheet/ghi chú khác nhau — dùng để ôn tập nhanh trước phỏng vấn hoặc để tra cứu nhanh khi cần nhớ lại một khái niệm.
>
> - Với nội dung chi tiết hơn về từng chủ đề (giải thích, ví dụ code, bài tập), tham khảo các trang con tương ứng trong lộ trình học ở trên.
>
