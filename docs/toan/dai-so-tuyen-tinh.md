# 1. Đại số tuyến tính (Linear Algebra)

> 🎓 **NCKH** / **Toán** / **Đại số tuyến tính**

> 🎯 **Câu hỏi lớn của cả trang:** *Vì sao Đại số tuyến tính được gọi là "xương sống" của toàn bộ ngành AI?*
> Câu trả lời ngắn: vì **mọi thứ trong AI đều là vector, và mọi việc AI làm đều là phép biến đổi vector**. Phần còn lại của trang này giải thích câu đó.
>

---

## 1. Vì sao cần Đại số tuyến tính?

Đại số tuyến tính là một trong những lĩnh vực mà ở đó ta đi vào phương pháp xử lý các bài toán có liên quan đến ma trận. Ở đây ta không giải các bài toán ma trận mà ta đi từ khởi nguồn của ma trận và tác dụng của nó đã tạo ra là gì?

Đầu tiên, đại số cổ điển ta biết sẽ giải quyết các vấn đề về các đại lượng vô hướng như là nhiệt độ, khối lượng, giá tiền… Tuy nhiên khi gặp các trạng thái của một cỗ máy, các điểm ảnh của một bức ảnh… ta tính toán nó như thế nào? Đại số tuyến tính sẽ cung cấp một cơ chế đóng gói cấu trúc. Nó gom tất cả các con số ấy thành **Vector** và **Matrix**. Với một mục tiêu duy nhất: thay vì giải quyết 10.000 phương trình rời rạc, ta gom nó thành **1 phương trình duy nhất**.

> 📦 **Đây là ý tưởng gốc: đóng gói cấu trúc.**
> Một bức ảnh 28×28 không phải là 784 con số rời rạc cần 784 phép tính riêng, mà là **một vector** cần **một** phép tính.
>
> Không có cách đóng gói này thì không thể viết nổi một mạng nơ-ron, và cũng không thể tận dụng được GPU — vốn là phần cứng được chế tạo **chuyên để nhân ma trận thật nhanh**.
>

---

## 2. Matrix là động từ, Vector là danh từ

Matrix được coi như là một **động từ**, Vector là một **danh từ**. Việc ta nhân một Vector với một Matrix, ta có thể coi như là mình đang thực hiện Matrix Vector đó, Matrix này sẽ đưa vector $x$ hiện tại sang một vị trí khác $y$ trong cùng một không gian.

Tất cả những trọng số hiển thị trên Matrix tượng trưng cho những biến đổi sẽ xảy ra đối với Vector $x$. **Các cột của ma trận cho ta biết các vectơ cơ sở (basis vectors) của không gian gốc sẽ hạ cánh ở đâu** sau khi quá trình biến đổi tuyến tính kết thúc.

Thông qua việc nhân ma trận, đại số tuyến tính có thể làm giãn nở, nén ép, cắt xô (shear), xoay, hoặc làm sụp đổ hoàn toàn một chiều không gian nhiều chiều. Bản chất của đại số tuyến tính là việc **số hóa các "chuyển động" của không gian hình học**, cho phép máy tính thao tác hình học thông qua các phép cộng, nhân số học thuần túy. Hay nói cách khác **Matrix là một phép tính làm bóp méo không gian**.

### Kiểm chứng bằng số: các cột thực sự là nơi basis vector hạ cánh

Lấy $A = \begin{bmatrix} 2 & -1 \\ 1 & 3 \end{bmatrix}$ và $x = \begin{bmatrix} 3 \\ 1 \end{bmatrix}$.

**Cách 1 — nhân theo hàng (cách dạy ở trường):**

$$Ax = \begin{bmatrix} 2(3) + (-1)(1) \\ 1(3) + 3(1) \end{bmatrix} = \begin{bmatrix} 5 \\ 6 \end{bmatrix}$$

**Cách 2 — nhìn theo cột (cách hiểu đúng bản chất):**

$$Ax = 3 \cdot \underbrace{\begin{bmatrix} 2 \\ 1 \end{bmatrix}}_{\text{nơi } \hat{i} \text{ hạ cánh}} + 1 \cdot \underbrace{\begin{bmatrix} -1 \\ 3 \end{bmatrix}}_{\text{nơi } \hat{j} \text{ hạ cánh}} = \begin{bmatrix} 6 \\ 3 \end{bmatrix} + \begin{bmatrix} -1 \\ 3 \end{bmatrix} = \begin{bmatrix} 5 \\ 6 \end{bmatrix}$$

> 💡 Hai cách cho cùng kết quả, nhưng **cách 2 mới cho thấy ý nghĩa**: vector $x = [3, 1]$ có nghĩa là "đi 3 bước theo $\hat{i}$, 1 bước theo $\hat{j}$". Sau biến đổi, ta vẫn đi **đúng 3 bước và 1 bước như cũ**, chỉ khác là hai vectơ cơ sở giờ đã nằm ở chỗ khác.
> **Đó chính là toàn bộ nội dung của câu "các cột cho biết basis vector hạ cánh ở đâu".**
>

### Bốn phép bóp méo điển hình

| Ma trận | $\hat{i} = [1,0]$ đi đâu | $\hat{j} = [0,1]$ đi đâu | Không gian bị gì | Det |
| --- | --- | --- | --- | --- |
| [[2, 0], [0, 1]] | [2, 0] | [0, 1] | **Giãn gấp 2 theo chiều ngang** | 2 |
| [[1, 1], [0, 1]] | [1, 0] | [1, 1] | **Cắt xô (shear)** — hình vuông thành hình bình hành | 1 |
| [[0, -1], [1, 0]] | [0, 1] | [-1, 0] | **Xoay 90 độ** ngược chiều kim đồng hồ | 1 |
| [[1, 2], [2, 4]] | [1, 2] | [2, 4] | **Sụp đổ** — cả mặt phẳng bị ép dẹp xuống một đường thẳng | **0** |

> 🔍 Hàng cuối đáng chú ý: hai cột $[1,2]$ và $[2,4]$ **cùng phương** (cột sau gấp đôi cột trước). Khi hai basis vector hạ cánh trên cùng một đường thẳng, cả mặt phẳng 2 chiều bị bóp dẹp còn 1 chiều — diện tích bằng 0, nên **det = 0**.
> Mất chiều thì **không thể quay ngược lại** — đó là lý do ma trận có det = 0 **không khả nghịch**.
>

---

## 3. Định thức (Determinant)

Khi này chúng ta cần biết **Det** hay còn gọi là định thức của một ma trận cho ta biết được rằng việc **bóp méo không gian sẽ diễn ra tới mức độ nào**.

Nói chính xác hơn: định thức là **hệ số thay đổi diện tích (hoặc thể tích)** sau phép biến đổi.

| Giá trị det | Ý nghĩa hình học | Hệ quả |
| --- | --- | --- |
| det = 3 | Diện tích **phình ra gấp 3** | Khả nghịch, thông tin được giữ nguyên |
| det = 1 | Diện tích **không đổi** (xoay, cắt xô) | Khả nghịch, chỉ đổi hình dạng |
| det = 0.5 | Diện tích **co lại một nửa** | Khả nghịch, nhưng đang nén |
| **det = 0** | **Sụp đổ** xuống chiều thấp hơn | **Không khả nghịch** — mất thông tin vĩnh viễn |
| det < 0 | Diện tích đổi kèm **lật mặt phẳng** (như soi gương) | Khả nghịch, nhưng hướng bị đảo |

> 🔗 **Liên hệ AI:** det = 0 nghĩa là ma trận làm mất chiều. Đây đúng là thứ xảy ra ở **Bottleneck của Autoencoder** — ta *cố tình* ép dữ liệu xuống chiều thấp hơn để buộc mô hình phải chọn lọc. Khác biệt là AE dùng phép biến đổi phi tuyến chứ không chỉ một ma trận.
> Ngược lại, các mô hình **Normalizing Flow** lại đòi mọi phép biến đổi phải khả nghịch, nên chúng phải theo dõi định thức Jacobian ở từng bước.
>

---

## 4. Trị riêng và Vectơ riêng (Eigenvalues & Eigenvectors)

Trong quá trình bị bóp méo, luôn tồn tại những **"trục" đặc biệt** mà dọc theo đó, các vectơ chỉ bị **kéo giãn ra hoặc nén lại** chứ tuyệt đối **không bị chệch hướng**. Các hướng bất biến đó chính là các **Vectơ riêng**, và hệ số kéo giãn chính là **Trị riêng**.

Viết thành công thức, toàn bộ ý trên gói gọn trong một dòng:

$$A\mathbf{v} = \lambda \mathbf{v}$$

Vế trái là "đưa $\mathbf{v}$ qua phép biến đổi phức tạp $A$". Vế phải là "chỉ nhân $\mathbf{v}$ với một con số". Chúng bằng nhau — nghĩa là **với riêng hướng **$\mathbf{v}$** đó, cả một ma trận rắc rối rút gọn thành một phép nhân vô hướng**.

### Ví dụ tính tay

Lấy $A = \begin{bmatrix} 3 & 1 \\ 0 & 2 \end{bmatrix}$. Ma trận tam giác nên trị riêng chính là hai số trên đường chéo: $\lambda_1 = 3$ và $\lambda_2 = 2$.

**Với **$\lambda_1 = 3$**:** vectơ riêng là $\mathbf{v}_1 = [1, 0]$. Kiểm tra:

$$A\begin{bmatrix} 1 \\ 0 \end{bmatrix} = \begin{bmatrix} 3 \\ 0 \end{bmatrix} = 3\begin{bmatrix} 1 \\ 0 \end{bmatrix} \quad \checkmark$$

**Với **$\lambda_2 = 2$**:** vectơ riêng là $\mathbf{v}_2 = [1, -1]$. Kiểm tra:

$$A\begin{bmatrix} 1 \\ -1 \end{bmatrix} = \begin{bmatrix} 3(1) + 1(-1) \\ 0(1) + 2(-1) \end{bmatrix} = \begin{bmatrix} 2 \\ -2 \end{bmatrix} = 2\begin{bmatrix} 1 \\ -1 \end{bmatrix} \quad \checkmark$$

> 🧭 **Đọc kết quả:** ma trận $A$ làm méo cả mặt phẳng, nhưng có đúng hai hướng "sống sót" không bị chệch: hướng $[1,0]$ bị kéo dài **3 lần**, hướng $[1,-1]$ bị kéo dài **2 lần**. Mọi vectơ khác đều vừa bị kéo vừa bị xoay.
> Biết hai hướng này là **biết bản chất của phép biến đổi** — mọi thứ còn lại chỉ là tổ hợp của chúng.
>

Bằng cách tính toán Trị riêng, đại số tuyến tính có khả năng **tìm ra những thành phần cốt lõi, độc lập, ẩn sâu bên trong các con số hỗn loạn**. Điều này lý giải tại sao nó là công cụ sống còn để giảm chiều dữ liệu (PCA) hay nhận diện khuôn mặt, bởi nó **bóc tách được bản chất thông tin khỏi sự nhiễu loạn**.

> 📉 **PCA thực chất là gì, nói bằng ngôn ngữ vừa học:** lấy ma trận hiệp phương sai của dữ liệu, tìm các **vectơ riêng** của nó. Vectơ riêng có **trị riêng lớn nhất** chính là hướng mà dữ liệu **trải rộng nhất** — hướng chứa nhiều thông tin nhất. Giữ lại vài hướng đầu, vứt phần còn lại, thế là giảm chiều xong.
> Đây cũng là lý do PCA hay được so sánh với [Autoencoder](../deep-learning/autoencoder.md): cùng mục tiêu giảm chiều, nhưng PCA chỉ làm được **tuyến tính**, còn Autoencoder làm được **phi tuyến**.
>

---

## 5. Bốn phép toán phải nắm chắc

Bốn phép này chiếm khoảng 90% những gì bạn sẽ gặp khi đọc bài báo AI.

### 5.1. Tích vô hướng (Dot product) — đo độ giống nhau

$$\mathbf{a} \cdot \mathbf{b} = \sum_i a_i b_i = |\mathbf{a}||\mathbf{b}|\cos\theta$$

Ví dụ: $[1,2,3] \cdot [4,5,6] = 4 + 10 + 18 = 32$.

> 📏 **Đây là phép toán quan trọng nhất trong cả AI hiện đại**, vì $\cos\theta$ trong công thức cho ta **góc giữa hai vector** — tức **độ giống nhau về ngữ nghĩa**.
> Cosine similarity trong [Latent Space (Không gian tiềm ẩn)](../deep-learning/latent-space.md), cách CLIP ghép ảnh với chữ, cách Attention tính $QK^\top$, cách vector database tìm kết quả gần nhất — **tất cả đều chỉ là tích vô hướng**.
>

### 5.2. Nhân ma trận với ma trận — ghép nhiều phép biến đổi

$AB$ nghĩa là "làm phép $B$ trước, rồi làm phép $A$" — đọc **từ phải sang trái**, giống hàm hợp $f(g(x))$.

> ⚠️ Điều này giải thích vì sao $AB \neq BA$: **xoay rồi kéo giãn** cho kết quả khác **kéo giãn rồi xoay**. Thứ tự của động từ có ý nghĩa.

### 5.3. Chuyển vị (Transpose) — lật ngang thành dọc

$A^\top$ đổi hàng thành cột. Xuất hiện khắp nơi trong công thức AI, ví dụ $QK^\top$ trong Attention hay $W^\top$ khi lan truyền ngược gradient.

### 5.4. Hạng (Rank) — số chiều thật sự còn lại

Số chiều mà không gian còn giữ được sau phép biến đổi. Ma trận 2×2 với det = 0 có rank = 1 (mặt phẳng đã sụp thành đường thẳng).

> 💰 **Rank là lý do kỹ thuật LoRA hoạt động.** Thay vì huấn luyện lại cả ma trận trọng số khổng lồ $W$ (ví dụ 4096×4096 ≈ 16.7 triệu tham số), LoRA chỉ học một hiệu chỉnh **hạng thấp** $\Delta W = BA$ với $B$ là 4096×8 và $A$ là 8×4096 — chỉ khoảng 65 nghìn tham số, tức **ít hơn 250 lần**.
> Giả định phía sau: cái mà mô hình cần học thêm cho một tác vụ mới thực ra "nằm gọn trong vài chiều", tức là có hạng thấp.
>

---

## 6. Đại số tuyến tính nằm ở đâu trong AI?

Đây là bảng trả lời trực tiếp cho tiêu đề video: *vì sao nó là "xương sống"*.

| Trong AI | Thực chất là phép gì | Khái niệm đã học ở trên |
| --- | --- | --- |
| Một bức ảnh | Tensor $H \times W \times C$ | Đóng gói cấu trúc |
| Một embedding của từ / ảnh | Vector trong $\mathbb{R}^d$ | Vector là danh từ |
| **Một lớp Dense (Fully Connected)** | $y = Wx + b$ | **Ma trận là động từ** — đúng nghĩa đen |
| Cả một mạng nơ-ron | Chuỗi phép biến đổi tuyến tính xen kẽ hàm phi tuyến | Nhân ma trận = ghép động từ |
| Hàm kích hoạt (ReLU) | Phép **phi tuyến** chen vào giữa | Nếu bỏ nó đi, 100 lớp gộp lại vẫn chỉ bằng **1** ma trận |
| Attention trong Transformer | $\text{softmax}(QK^\top / \sqrt{d})V$ | Tích vô hướng + nhân ma trận |
| Phép tích chập trong CNN | Quy về nhân ma trận (kỹ thuật im2col) | Đó là lý do GPU chạy CNN nhanh |
| PCA | Vectơ riêng của ma trận hiệp phương sai | Trị riêng / Vectơ riêng |
| Tìm ảnh / văn bản tương tự | Cosine similarity | Tích vô hướng |
| Huấn luyện theo batch | Nhân **một** ma trận với **nhiều** vector cùng lúc | Đóng gói cấu trúc |
| Fine-tune bằng LoRA | Xấp xỉ hạng thấp $\Delta W = BA$ | Hạng (Rank) |
| GPU / TPU | Phần cứng **chuyên nhân ma trận** | Toàn bộ ngành phần cứng AI dựng quanh một phép toán duy nhất |

> 🦴 **Vì sao gọi là "xương sống":** nhìn cột giữa của bảng trên sẽ thấy — dù là ảnh, chữ, âm thanh hay video, dù là CNN, Transformer hay Diffusion, **mọi thứ cuối cùng đều quy về nhân ma trận và tích vô hướng**.
> Học sâu không phát minh ra phép toán mới. Nó chỉ **xếp chồng thật nhiều phép biến đổi tuyến tính, xen giữa là các hàm phi tuyến**, rồi dùng đạo hàm để dò tìm bộ trọng số tốt. Phần "đạo hàm để dò tìm" chính là nội dung của **Toán** → Giải tích.
>

---

## 7. Bảng thuật ngữ nhanh

| Thuật ngữ | Hiểu trong một câu |
| --- | --- |
| **Scalar** (vô hướng) | Một con số đơn lẻ: nhiệt độ, giá tiền |
| **Vector** | Một danh sách số có thứ tự — một **điểm** hoặc một **mũi tên** trong không gian |
| **Matrix** | Một **động từ**: phép biến đổi bóp méo cả không gian |
| **Tensor** | Tổng quát hóa: 0 chiều là scalar, 1 chiều là vector, 2 chiều là matrix, 3+ chiều là tensor |
| **Basis vectors** | Bộ vectơ đơn vị $\hat{i}, \hat{j}$ — "thước đo" của không gian; các cột ma trận cho biết chúng hạ cánh ở đâu |
| **Linear transformation** | Phép biến đổi giữ đường thẳng vẫn thẳng và gốc tọa độ đứng yên |
| **Determinant** | Hệ số thay đổi diện tích / thể tích. Bằng 0 nghĩa là mất chiều |
| **Eigenvector** | Hướng **không bị chệch** qua phép biến đổi, chỉ bị co giãn |
| **Eigenvalue** | Hệ số co giãn dọc theo hướng đó |
| **Rank** | Số chiều thật sự còn sống sót sau phép biến đổi |
| **Dot product** | Phép đo độ giống nhau giữa hai vector |

---

## 8. Nguồn học

### Video đã xem

- [Tại sao Đại số Tuyến tính là "Xương sống" của toàn bộ ngành AI? — Học Giải Thuật Cùng HPN](https://youtu.be/yvGuMIWuh4E) — **video gốc của trang này**, giải thích bằng tiếng Việt vì sao mọi thứ trong AI đều quy về ma trận.

### Nên xem tiếp

- [Essence of Linear Algebra — 3Blue1Brown (toàn bộ series)](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab) — **nguồn tốt nhất tồn tại** cho phần trực giác hình học. 15 tập ngắn, có hình động cho đúng những khái niệm ở trên: basis vector, determinant, eigenvector.

- [Immersive Linear Algebra](http://immersivemath.com/ila/index.html) — sách trực tuyến miễn phí, mọi hình vẽ đều **tương tác kéo thả được**.

- [MIT 18.06 — Linear Algebra, Gilbert Strang](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/) — khóa học kinh điển, dùng khi cần độ chặt chẽ để trích dẫn.

- [Mathematics for Machine Learning — Deisenroth, Faisal, Ong (PDF miễn phí)](https://mml-book.github.io/) — **sách để trích dẫn trong bài báo**. Chương 2–4 là đại số tuyến tính, viết riêng cho người làm ML.

> 🧪 **Bài thực hành 15 phút, làm ngay được:**
> ```python
> import numpy as np
A = np.array([[3, 1], [0, 2]])
vals, vecs = np.linalg.eig(A)
print(vals)              # [3. 2.]  <- đúng hai trị riêng tính tay ở mục 4
print(np.linalg.det(A))  # 6.0      <- diện tích phình gấp 6
x = np.array([3, 1])
print(A @ x)             # kiểm chứng mục 2
> ```
>
> Sau đó thử với ma trận `[[1, 2], [2, 4]]` và xem `det` ra 0, còn `np.linalg.inv` báo lỗi — chính là hiện tượng "sụp đổ mất chiều" đã nói ở mục 3.
>
