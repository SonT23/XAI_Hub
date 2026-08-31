# DSA: Trees, Heap & Graphs

> 🖼️ Trang này tổng hợp nội dung từ 8 ảnh ghi chú học tập gốc:
> 1. 1329_cam-nang-dsa-trees-binary-tree-bst-traversal.jpg
>
> 2. 1330_cam-nang-dsa-heap-priority-queue.jpg
>
> 3. 1331_cam-nang-dsa-graphs-bfs-dfs-adjacency-matrix.jpg
>
> 4. 1332_cam-nang-dsa-graphs-tiep-theo-bfs-dfs-chi-tiet.jpg
>
> 5. 1346_ghi-chu-dsa-trees-bst.jpg
>
> 6. 1347_ghi-chu-dsa-heaps-priority-queue.jpg
>
> 7. 1348_ghi-chu-dsa-graphs-bfs-dfs.jpg
>
> 8. 1349_ghi-chu-dsa-graphs-paths-order-dijkstra-topo-sort.jpg
>

### Cây (Trees & Binary Search Tree)

> 📌 Ảnh thuộc mục này: 1329_cam-nang-dsa-trees-binary-tree-bst-traversal.jpg, 1346_ghi-chu-dsa-trees-bst.jpg

#### Tree là gì?

- **Tree** là một **non-linear data structure**, biểu diễn các mối quan hệ phân cấp (hierarchical) một cách gọn gàng, hiệu quả.

- Gồm các **node** được kết nối bằng **edge**.

- Chỉ có duy nhất **1 đường đi** từ root tới bất kỳ node nào.

- Một tree với **n node** có **(n-1) edge**.

#### Thuật ngữ cơ bản

- **Root**: Node trên cùng (không có parent)

- **Parent**: Node có children

- **Child**: Node được kết nối trực tiếp bên dưới

- **Leaf Node**: Node không có children

- **Edge**: Kết nối giữa 2 node

- **Siblings**: Các node có cùng parent

- **Depth of Node**: Số edge từ root tới node đó

- **Height of Tree**: Depth lớn nhất của bất kỳ node nào (tính từ root) = số cạnh trên đường dài nhất từ root tới một leaf

Ví dụ Binary Tree:

```javascript
     1 (Root)
    /  \
2(Edge) 3
 /\     /\
4  5   6  7
|
8 (Leaf)
```

Depth(1)=0, Depth(2)=1, Depth(3)=1, Depth(4)=2, Depth(5)=2, Depth(6)=2, Depth(7)=2, Depth(8)=3. Height của Tree = 3 (max depth).

#### Binary Search Tree (BST) và tính chất

Ví dụ BST:

```javascript
     50
    /  \
  30    70
  /\    /\
20 40 60 80
```

**Tính chất BST** — với mọi node: `left < root < right`

- Left subtree values < Node

- Right subtree values > Node

- Left & Right subtree cũng phải là BST

- Duyệt **inorder** của BST cho kết quả theo thứ tự **đã sort**

**Balanced Tree**: với mọi node, |height(left) − height(right)| ≤ 1 → giữ các thao tác ở mức ~O(log n).

> ⚠️ Lỗi thường gặp: nhầm lẫn giữa BST với Heap.
> - BST → sắp theo **giá trị** (left < root < right)
>
> - Heap → sắp theo **độ ưu tiên** (parent ≥ children hoặc ≤ children)
>

#### Insert và Search trong BST

Ví dụ Insert 45, 65, 10 vào BST (bắt đầu từ cây trên):

- Insert 45: 50>45 → trái, 30<45 → phải, 40<45 → phải

- Insert 65: 50<65 → phải, 70>65 → trái, 60<65 → phải

- Insert 10: 50>10 → trái, 30>10 → trái, 20>10 → trái

Ví dụ Search 65 trong BST:

- 50: 65>50 → đi phải

- 70: 65<70 → đi trái

- 60: 65>60 → đi phải

- 65: Found!

#### Các loại duyệt cây (Tree Traversals)

Ví dụ minh hoạ (ghi chú 2):

```javascript
     10
   /    \
  5      15
 / \    /  \
3   7  12   18
```

| **Loại duyệt** | **Thứ tự** | **Kết quả ví dụ** |
| --- | --- | --- |
| Preorder | Root, Left, Right | [10, 5, 3, 7, 15, 12, 18] |
| Inorder | Left, Root, Right | [3, 5, 7, 10, 12, 15, 18] (đã sort) |
| Postorder | Left, Right, Root | [3, 7, 5, 12, 18, 15, 10] |
| Level-order (BFS) | Theo từng tầng, dùng Queue | [10, 5, 15, 3, 7, 12, 18] |

**Ý tưởng đệ quy của traversal**: Preorder, Inorder, Postorder đều theo ý tưởng đệ quy tương tự nhau — base case là node null, xử lý + đệ quy trên left & right.

```python
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder(root):
    if root is None:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)

def preorder(root):
    if root is None:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)

def postorder(root):
    if root is None:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]

def level_order(root):
    if root is None:
        return []
    result, queue = [], [root]
    while queue:
        node = queue.pop(0)
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result

def bst_search(root, target):
    if root is None or root.val == target:
        return root
    if target < root.val:
        return bst_search(root.left, target)
    return bst_search(root.right, target)

def bst_insert(root, val):
    if root is None:
        return Node(val)
    if val < root.val:
        root.left = bst_insert(root.left, val)
    else:
        root.right = bst_insert(root.right, val)
    return root
```

#### Độ phức tạp thao tác trên BST

| Operation | Average | Worst (cây lệch) |
| --- | --- | --- |
| Search | O(log n) | O(n) |
| Insert | O(log n) | O(n) |
| Delete | O(log n) | O(n) |

#### Bài toán kinh điển về Tree/BST

- Lowest Common Ancestor (LCA)

- Diameter of Binary Tree

- Validate BST

- Path Sum (Root to Leaf)

- ... và nhiều hơn nữa!

---

### Heap & Priority Queue

> 📌 Ảnh thuộc mục này: 1330_cam-nang-dsa-heap-priority-queue.jpg, 1347_ghi-chu-dsa-heaps-priority-queue.jpg

#### Heap là gì?

- **Heap** là một **complete binary tree** (cây nhị phân hoàn chỉnh — mọi tầng được lấp đầy, trừ có thể tầng cuối được lấp từ trái sang phải) thoả mãn **heap property**.

- **Priority Queue** được xây dựng dựa trên Heap.

- Root luôn là phần tử **min** (Min-Heap) hoặc **max** (Max-Heap).

#### Min-Heap vs Max-Heap

| Đặc điểm | Min-Heap | Max-Heap |
| --- | --- | --- |
| Quan hệ Parent-Child | Parent ≤ Child | Parent ≥ Child |
| Root | Nhỏ nhất | Lớn nhất |
| Dùng khi | Cần giá trị nhỏ nhất | Cần giá trị lớn nhất |

Ví dụ Min-Heap:

```javascript
     1
   /   \
  3     4
 / \   / \
5   9 6   7
```

Array dạng level-order: `[1, 3, 4, 5, 9, 6, 7]`

**Quan hệ chỉ số (cho phần tử tại index i, i > 0)**

- Left Child Index = 2*i + 1

- Right Child Index = 2*i + 2

- Parent Index = (i-1)/2

#### Heapify, Insert, Delete/Extract

**Heapify (Down-Heap)** — độ phức tạp O(log n):

```python
def heapify(arr, n, i):
    smallest = i
    left, right = 2*i + 1, 2*i + 2
    if left < n and arr[left] < arr[smallest]:
        smallest = left
    if right < n and arr[right] < arr[smallest]:
        smallest = right
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify(arr, n, smallest)
```

**Insert vào Heap**: (1) Thêm phần tử ở cuối (làm leaf kế tiếp). (2) Heapify Up — so sánh với parent và swap nếu cần.

Ví dụ (Min-Heap): `[4,7,9]` —insert 3→ `[3,7,9,4]` → heapify up → `[3,4,9,7]`

**Delete/Extract**: Xoá root (min hoặc max) → thay root bằng phần tử cuối → Heapify Down.

Ví dụ (Min-Heap): `[1,3,6,5]` —deleteMin→ `[3,5,6]` → heapify down → `[3,5,6]`

**Peek**: lấy phần tử root trong O(1) — `peek() → arr[0]`

#### Các thao tác và độ phức tạp

| Operation | Min-Heap | Max-Heap |
| --- | --- | --- |
| Insert (push) | O(log n) | O(log n) |
| Delete (pop/extract) | O(log n) | O(log n) |
| Peek (top) | O(1) | O(1) |

#### Heap Sort

Ý tưởng: Dùng Max Heap (thứ tự tăng dần) / Min Heap (thứ tự giảm dần).

1. Build Heap.

2. Extract root và đặt ở cuối.

3. Lặp lại cho n phần tử.

Time Complexity: **O(n log n)**

#### Priority Queue và ứng dụng

Priority Queue là một data structure phục vụ phần tử có priority cao nhất/thấp nhất trước, được cài đặt dùng Heap.

**Ứng dụng thực tế:**

- Top-K elements (K phần tử lớn/nhỏ nhất)

- Merge K sorted lists

- Dijkstra's shortest path

- Median in a stream (dùng hai heap)

- Priority Queues (CPU scheduling)

- Huffman Coding

- Event simulation

#### Heap vs BST — so sánh nhanh

| Feature | Heap | BST |
| --- | --- | --- |
| Type | Complete Binary Tree | Binary Search Tree |
| Ordering | Partial (Heap Order) | Total Order |
| Insert/Delete | O(log n) | O(log n) |
| Search | O(n) (không tối ưu cho search) | O(log n) |

#### Code Python dùng heapq

```python
import heapq

# Min-Heap mặc định trong Python
min_heap = []
heapq.heappush(min_heap, 5)
heapq.heappush(min_heap, 3)
heapq.heappush(min_heap, 8)

print(heapq.heappop(min_heap))  # 3 (nhỏ nhất)
print(min_heap[0])              # peek: phần tử nhỏ nhất hiện có

# Max-Heap: đảo dấu giá trị khi push/pop
max_heap = []
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -3)
heapq.heappush(max_heap, -8)
print(-heapq.heappop(max_heap))  # 8 (lớn nhất)

# Priority Queue với heapq: dùng tuple (priority, item)
pq = []
heapq.heappush(pq, (2, "task B"))
heapq.heappush(pq, (1, "task A"))
heapq.heappush(pq, (3, "task C"))
while pq:
    priority, task = heapq.heappop(pq)
    print(priority, task)

# Heapify một list có sẵn: O(n)
arr = [9, 4, 7, 1, 3]
heapq.heapify(arr)
```

> 👤 **Góc phỏng vấn** — Vì sao heap tốt hơn sorted array cho streaming data?
> Heap hỗ trợ insert & extract trong O(log n); sorted array cần O(n) insert (phải dịch chuyển); heap luôn giữ sẵn giá trị cực trị (min/max).
>

> ⚠️ **Lỗi thường gặp**: dùng heap khi bạn chỉ cần sort **một lần**. Nếu có sẵn toàn bộ dữ liệu, sort một lần → O(n log n) đơn giản & nhanh hơn heapify + nhiều thao tác. Dùng heap cho dữ liệu động/streaming, không phải cho sort một lần.

---

### Đồ thị (Graphs)

> 📌 Ảnh thuộc mục này: 1331_cam-nang-dsa-graphs-bfs-dfs-adjacency-matrix.jpg, 1332_cam-nang-dsa-graphs-tiep-theo-bfs-dfs-chi-tiet.jpg, 1348_ghi-chu-dsa-graphs-bfs-dfs.jpg, 1349_ghi-chu-dsa-graphs-paths-order-dijkstra-topo-sort.jpg

#### Graph là gì?

Một **Graph G = (V, E)**, trong đó:

- V = tập các **vertices** (node)

- E = tập các **edges** (kết nối)

Graph dùng để biểu diễn các mối quan hệ, mạng lưới và kết nối giữa các object. Có thể là **directed/undirected**, **weighted/unweighted**.

Ví dụ Graph (Undirected): V = {A,B,C,D,E,F}, E = {(A,B),(A,C),(B,D),(C,E),(D,F),(C,F)}

#### Vertex, Edge & phân loại Graph

- **Vertex (Node)**: một điểm trong graph.

- **Edge**: kết nối giữa 2 vertex.

- **Directed Graph**: edge có hướng (A→B khác B→A).

- **Undirected Graph**: không có hướng (A—B giống B—A).

- **Weighted Graph**: edge có weight (giá trị cost, distance...).

- **Unweighted Graph**: mọi edge coi như bằng nhau (thường =1).

#### Degree của một Vertex

- Degree = số edge liên thuộc với vertex đó (ở undirected graph, degree ≥ 0).

- Ở directed graph: **In-degree** = số edge đi vào; **Out-degree** = số edge đi ra.

#### Connected Graph

Một graph là **connected** nếu tồn tại đường đi giữa mọi cặp vertex. Nếu 1 vertex bất kỳ không thể tới được từ các vertex khác → Not Connected.

#### Biểu diễn đồ thị: Adjacency Matrix & Adjacency List

**Adjacency Matrix**: mảng 2D kích thước V×V. `mat[i][j] = 1` (hoặc weight) nếu có edge giữa i và j, ngược lại là 0 (hoặc ∞ nếu weighted). Space: **O(V²)**.

|   | A | B | C | D | E | F |
| --- | --- | --- | --- | --- | --- | --- |
| A | 0 | 1 | 1 | 0 | 0 | 0 |
| B | 1 | 0 | 0 | 1 | 0 | 1 |
| C | 1 | 0 | 0 | 0 | 1 | 1 |
| D | 0 | 1 | 0 | 0 | 1 | 0 |
| E | 0 | 0 | 1 | 1 | 0 | 0 |
| F | 0 | 1 | 1 | 0 | 0 | 0 |

**Adjacency List**: với mỗi vertex, lưu list các vertex kề (adjacent). Space: **O(V+E)** (tốt hơn matrix cho sparse graph).

```javascript
A → B → C
B → A → D → F
C → A → E → F
D → B → E
E → C → D
F → B → C
```

**So sánh độ phức tạp:**

| Operation | Adjacency Matrix | Adjacency List |
| --- | --- | --- |
| Add Edge | O(1) | O(1) |
| Remove Edge | O(1) | O(deg(v)) |
| Check Edge (u,v) | O(1) | O(deg(u)) |
| BFS / DFS | O(V²) | O(V+E) |
| Space | O(V²) | O(V+E) |

#### BFS (Breadth First Search)

- Duyệt theo từng **level** (đi càng rộng càng tốt trước).

- Dùng **Queue (FIFO)**.

- Time Complexity: **O(V+E)**, Space: **O(V)**.

- Queue = tìm **đường đi ngắn nhất không trọng số** / duyệt theo các level.

- Use case: Shortest path (đồ thị unweighted).

Ví dụ (adjacency list: 1:[2,3,4], 2:[1,3,6], 3:[1,2,5,6], 4:[1,5], 5:[3,4,6], 6:[2,3,5]), BFS bắt đầu từ 1:

```javascript
L0: 1
L1: 2, 3, 4
L2: 6, 5
L3: (không còn)
```

Đường đi ngắn nhất tới 5 từ 1: 1→3→5 (2 cạnh).

```python
from collections import deque

def bfs(graph, start):
    visited = {start}
    queue = deque([start])
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order
```

#### DFS (Depth First Search)

- Duyệt càng sâu càng tốt (đi sâu vào 1 nhánh trước).

- Dùng **Stack (LIFO)** hoặc **Recursion**.

- Time Complexity: **O(V+E)**, Space: **O(V)**.

- Stack/Recursion = reachability, connected components, phát hiện chu trình (cycles).

- Use case: Topological sort, Cycle detection.

Ví dụ DFS bắt đầu từ 1 (một thứ tự khả dĩ, có thể có nhiều thứ tự khác nhau): 1, 2, 3, 5, 4, 6.

```python
def dfs(graph, start, visited=None, order=None):
    if visited is None:
        visited, order = set(), []
    visited.add(start)
    order.append(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, order)
    return order

# Phiên bản iterative dùng stack
def dfs_iterative(graph, start):
    visited = {start}
    stack = [start]
    order = []
    while stack:
        node = stack.pop()
        order.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)
    return order
```

> ⚠️ **Visited set là bắt buộc**: duy trì một visited set để tránh ghé lại các node, đánh dấu ngay khi push/enqueue. Thiếu visited set → vòng lặp vô hạn (đặc biệt trong graph có chu trình hoặc grid).

#### BFS vs DFS — so sánh

| Feature | BFS | DFS |
| --- | --- | --- |
| Strategy | Level by level | Đi sâu trước |
| Data Structure | Queue (FIFO) | Stack / Recursion |
| Time | O(V+E) | O(V+E) |
| Space | O(V) | O(V) |
| Memory | Nhiều hơn | Ít hơn |
| Shortest Path (unweighted) | Có | Không |
| Use Case | Level Search, Shortest path | Topo sort, Cycle detection, Path/Components |

**Grid như một Graph**: mỗi ô (cell) = một node, cạnh nối tới neighbor hợp lệ — dùng mô hình **4-neighbors** (trên/dưới/trái/phải) hoặc **8-neighbors** (thêm 4 đường chéo).

#### Dijkstra's Shortest Path (trọng số không âm)

Áp dụng cho graph có **trọng số không âm** (heap + dist[]).

**Ý tưởng**: tham lam theo khoảng cách nhỏ nhất. Dùng **min-heap** (node, dist). Relax cạnh, cập nhật dist[]. Time: **O((V+E) log V)**.

Ví dụ: A→B(4), A→C(1), B→D(2), C→B(2), C→D(5), C→E(4). Kết quả dist[]: A=0, B=4, C=1, D=3, E=4.

> Nếu graph có trọng số **âm**, dùng **Bellman-Ford** thay vì Dijkstra: relax tất cả cạnh |V|-1 lần, phát hiện chu trình âm ở lần lặp thứ |V|.

```python
import heapq

def dijkstra(graph, start):
    # graph: {node: [(neighbor, weight), ...]}
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, node = heapq.heappop(pq)
        if d > dist[node]:
            continue
        for neighbor, weight in graph[node]:
            new_dist = d + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))
    return dist
```

#### Topological Sort (cho DAG)

Áp dụng cho **Directed Acyclic Graph (DAG)**. Hai cách cài đặt: **Kahn (BFS)** hoặc **DFS finish order**.

- **Kahn (BFS)**: dùng in-degree. Đẩy các node có in-degree = 0 vào queue. Pop, thêm vào order, giảm in-degree của các neighbor.

- **DFS finish**: DFS và đẩy node vào stack khi finish (duyệt xong toàn bộ nhánh con), sau đó đảo ngược stack để ra thứ tự topo.

Ví dụ: A→B→D→F, A→C→E→F. Kết quả order khả dĩ: A, B, C, E, D, F.

```python
from collections import deque

def topo_sort_kahn(graph, num_nodes):
    indegree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            indegree[neighbor] += 1
    queue = deque([n for n in indegree if indegree[n] == 0])
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    if len(order) < num_nodes:
        raise ValueError("Graph có chu trình, không thể topo sort")
    return order
```

#### Phát hiện chu trình (Cycle Detection)

| Loại Graph | Cách phát hiện |
| --- | --- |
| Directed Graph | DFS với recursion stack (3 màu: white, gray, black), hoặc dùng Kahn's: nếu topo order size < V → tồn tại chu trình |
| Undirected Graph | DFS/BFS với parent tracking — nếu ghé một neighbor không phải parent → có chu trình |

#### Union-Find (cho components / MST)

Dùng để đếm **connected components** và trong **Kruskal's MST** để tránh chu trình khi thêm cạnh.

Ops chính: `find(x)`, `union(x, y)` — kèm tối ưu **path compression** và **union by rank**.

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        return True
```

#### Ứng dụng thực tế của Graph

- Social Networks → Người dùng là node, tình bạn là edge.

- Maps & Navigation (Google Maps) → Địa điểm là node, đường là edge; tìm shortest path.

- Web Pages → Trang web là node, link là edge (Web Crawlers).

- Recommendation Systems → User & item là node.

- Network Routing → Router là node, link là edge.

> 💡 Ghi nhớ: BFS → tìm shortest path (đồ thị unweighted). Graph có ở khắp mọi nơi trong thực tế.

> 👤 **Mẹo phỏng vấn**: chọn thuật toán dựa trên ràng buộc bài toán — trọng số không âm? → Dijkstra.

> ⚠️ **Lỗi thường gặp**: dùng Dijkstra với cạnh có trọng số âm (sai) — phải dùng Bellman-Ford trong trường hợp này.

---

> 🔗 **Ghi chú bổ sung — liên hệ giữa các cấu trúc**
> - **Heap** không chỉ dùng cho Priority Queue mà còn là thành phần cốt lõi để cài đặt **Dijkstra's shortest path** (min-heap lưu (dist, node)) và **Heap Sort**.
>
> - **BFS/DFS** vốn là ý tưởng duyệt của Tree (Level-order chính là BFS, Preorder/Inorder/Postorder là các biến thể của DFS) được **mở rộng sang Graph** — điểm khác biệt quan trọng là Graph cần thêm **visited set** để tránh lặp vô hạn do có thể tồn tại chu trình, điều mà Tree (không có chu trình) không gặp phải.
>
> - **BST** là một dạng đặc biệt của Tree với tính chất sắp xếp theo giá trị, trong khi **Heap** cũng là cây nhị phân hoàn chỉnh nhưng chỉ đảm bảo thứ tự một phần (partial order) theo độ ưu tiên — dễ nhầm lẫn nhưng bản chất và ứng dụng khác nhau.
>
> - **Topological Sort** (dùng cho DAG) có thể cài bằng BFS (Kahn) hoặc DFS (finish order), cho thấy hai kỹ thuật duyệt graph nền tảng (BFS, DFS) là công cụ chung để giải nhiều bài toán khác nhau: shortest path, cycle detection, ordering, connectivity.
>
> - **Union-Find** thường được dùng song song với DFS/BFS để giải các bài toán về connected components và là nền tảng cho thuật toán MST (Kruskal).
>
