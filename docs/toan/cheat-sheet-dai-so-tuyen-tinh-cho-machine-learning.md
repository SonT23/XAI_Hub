# Cheat Sheet: Đại số tuyến tính cho Machine Learning

> 🖼️ **Dán ảnh gốc tại đây:** `1402_machine-learning-mathematics-cheat-sheet-dai-so-xa.jpg`

> 💡 Cheat sheet gốc gồm 7 mảng kiến thức toán cho ML: (1) Đại số tuyến tính, (2) Vector & Ma trận trong ML, (3) Hàm mất mát phổ biến, (4) Xác suất & Thống kê, (5) Tối ưu hóa, (6) Hàm kích hoạt, (7) Các phân phối xác suất. Trang này số hóa và diễn giải đầy đủ cả 7 phần.

### 1. Đại số tuyến tính (Linear Algebra)

- **Vector**: một vector cột $n$ chiều

$$\mathbf{v} = \begin{bmatrix} v_1 \\ v_2 \\ \vdots \\ v_n \end{bmatrix} \in \mathbb{R}^n$$

- Trong ML, vector dùng để biểu diễn một điểm dữ liệu (feature vector), một trọng số (weight vector), hoặc một embedding (ví dụ word embedding trong NLP).

- **Tích vô hướng (Dot Product)**:

$$\mathbf{a}^T \mathbf{b} = \sum_{i=1}^{n} a_i b_i$$

- Là phép toán lõi trong mọi lớp fully-connected/linear layer: đầu ra $z = \mathbf{w}^T \mathbf{x} + b$. Cũng dùng để đo độ tương đồng (cosine similarity) giữa hai vector.

- **Nhân ma trận (Matrix Multiplication)**:

$$(AB)_{ij} = \sum_{k=1}^{m} A_{ik} B_{kj}$$

- Toàn bộ forward pass của mạng neural (batch dữ liệu nhân với ma trận trọng số) là chuỗi các phép nhân ma trận này, được tăng tốc bằng GPU.

- **Chuyển vị (Transpose)**: $(A^T)_{ij} = A_{ji}$ — đổi hàng thành cột. Dùng khi tính gradient, khi đổi chiều dữ liệu (ví dụ chuyển từ (features × samples) sang (samples × features)).

- **Ma trận nghịch đảo (Inverse)**:

$$A^{-1}A = AA^{-1} = I$$

- Dùng trong nghiệm dạng đóng (closed-form) của hồi quy tuyến tính: $\hat{\beta} = (X^TX)^{-1}X^Ty$. Trong Deep Learning ít dùng trực tiếp vì ma trận lớn, tốn chi phí tính toán $O(n^3)$.

- **Định thức (Determinant, ma trận 2×2)**:

$$\det(A) = \begin{vmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{vmatrix} = a_{11}a_{22} - a_{12}a_{21}$$

- Định thức bằng 0 nghĩa là ma trận suy biến (singular), không khả nghịch — dấu hiệu dữ liệu bị đa cộng tuyến (multicollinearity).

- **Vết ma trận (Trace)**:

$$\text{tr}(A) = \sum_{i=1}^{n} A_{ii}$$

- Tổng các phần tử trên đường chéo chính. Xuất hiện trong nhiều công thức regularization và trong tính toán ma trận hiệp phương sai.

- **Phương trình trị riêng – vector riêng (Eigenvalue Equation)**:

$$A\mathbf{v} = \lambda \mathbf{v}$$

- Nền tảng của **PCA (Principal Component Analysis)**: các vector riêng của ma trận hiệp phương sai là các trục thành phần chính, trị riêng thể hiện lượng phương sai giữ lại theo trục đó. Cũng liên quan đến độ ổn định của mạng neural sâu (spectral norm).

> 📌 Ghi nhớ: Concept Bottleneck Models (CBM) dùng phép chiếu tuyến tính (ma trận trọng số) để ánh xạ đặc trưng ẩn sang không gian concept — toàn bộ dựa trên các phép toán ma trận/vector ở mục này.

### 2. Vector & Ma trận trong ML (đạo hàm bậc cao)

- **Gradient (Vector đạo hàm)**: với hàm vô hướng $f: \mathbb{R}^n \to \mathbb{R}$

$$\nabla f(\mathbf{x}) = \begin{bmatrix} \dfrac{\partial f}{\partial x_1} \\ \dfrac{\partial f}{\partial x_2} \\ \vdots \\ \dfrac{\partial f}{\partial x_n} \end{bmatrix}$$

- Là đại lượng trung tâm của **backpropagation**: gradient của hàm mất mát theo từng trọng số cho biết hướng cập nhật trọng số.

- **Ma trận Jacobian**: với hàm vector $f: \mathbb{R}^n \to \mathbb{R}^m$

$$J_f(\mathbf{x}) = \begin{bmatrix} \dfrac{\partial f_1}{\partial x_1} & \cdots & \dfrac{\partial f_1}{\partial x_n} \\ \vdots & \ddots & \vdots \\ \dfrac{\partial f_m}{\partial x_1} & \cdots & \dfrac{\partial f_m}{\partial x_n} \end{bmatrix}$$

- Dùng khi một lớp mạng có nhiều đầu ra (ví dụ softmax) — cần Jacobian để lan truyền ngược qua nhiều chiều đầu ra cùng lúc. Cũng dùng để đo độ nhạy (sensitivity) của mô hình — liên quan trực tiếp tới các phương pháp **giải thích mô hình (XAI)** như Saliency Map, Integrated Gradients.

- **Ma trận Hessian**: đạo hàm bậc hai

$$H_f(\mathbf{x}) = \nabla^2 f(\mathbf{x})$$

- Cho biết độ cong của hàm mất mát, dùng trong các thuật toán tối ưu bậc hai (Newton's method), phân tích độ sắc nét (sharpness) của cực tiểu, và trong một số phương pháp phân tích độ nhạy/độ tin cậy trong XAI.

- **Chuẩn Frobenius (Frobenius Norm)**:

$$\|A\|_F = \sqrt{\sum_{i=1}^{m}\sum_{j=1}^{n} a_{ij}^2}$$

- Đo "độ lớn" tổng thể của một ma trận (ví dụ ma trận trọng số) — dùng trong regularization (weight decay dạng ma trận) và đo khoảng cách giữa hai ma trận.

- **Chuẩn L2 (Euclidean Norm) của vector**:

$$\|\mathbf{v}\|_2 = \sqrt{\sum_{i=1}^{n} v_i^2}$$

- Dùng trong Ridge Regression (L2 regularization), tính khoảng cách Euclid giữa các embedding, chuẩn hóa gradient (gradient clipping).

- **Chuẩn L1 (Manhattan Norm) của vector**:

$$\|\mathbf{v}\|_1 = \sum_{i=1}^{n} |v_i|$$

- Dùng trong Lasso Regression (L1 regularization) để tạo ra nghiệm thưa (sparse) — hữu ích khi cần chọn lọc concept quan trọng trong Concept Bottleneck Models.

### 3. Các hàm mất mát phổ biến (Common Loss Functions)

- **Sai số bình phương trung bình (MSE)** — dùng cho hồi quy:

$$L = \frac{1}{n}\sum_{i=1}^{n} (y_i - \hat{y}_i)^2$$

- **Sai số tuyệt đối trung bình (MAE)** — dùng cho hồi quy, ít nhạy với outlier hơn MSE:

$$L = \frac{1}{n}\sum_{i=1}^{n} |y_i - \hat{y}_i|$$

- **Log Loss (phân loại nhị phân)** — hay còn gọi Binary Cross-Entropy:

$$L = -\frac{1}{n}\sum_{i=1}^{n}\left[y_i \log(\hat{y}_i) + (1-y_i)\log(1-\hat{y}_i)\right]$$

- **Cross Entropy Loss (phân loại đa lớp)**:

$$L = -\frac{1}{n}\sum_{i=1}^{n}\sum_{k=1}^{K} y_{ik}\log(\hat{y}_{ik})$$

- Đây là hàm mất mát tiêu chuẩn khi huấn luyện các mô hình phân loại đa lớp, bao gồm cả nhánh dự đoán nhãn cuối trong Concept Bottleneck Models.

- **Hinge Loss** — dùng trong SVM và một số mô hình margin-based:

$$L = \frac{1}{n}\sum_{i=1}^{n} \max(0, 1 - y_i\hat{y}_i)$$

> 📌 Trong CBM, tổng loss thường là tổ hợp: loss dự đoán concept (thường Binary Cross-Entropy cho từng concept) + loss dự đoán nhãn cuối (Cross Entropy) — xem thêm ở trang về kiến trúc CBM.

### 4. Xác suất & Thống kê (Probability & Statistics)

- **Xác suất có điều kiện**:

$$P(A|B) = \frac{P(A \cap B)}{P(B)}$$

- **Định lý Bayes**:

$$P(A|B) = \frac{P(B|A)P(A)}{P(B)}$$

- Nền tảng của các mô hình xác suất (Naive Bayes, Bayesian Networks) và của tư duy suy luận nhân quả/giải thích trong XAI.

- **Kỳ vọng (Expectation) — biến rời rạc**:

$$\mathbb{E}[X] = \sum_x xP(X=x)$$

- **Kỳ vọng — biến liên tục**:

$$\mathbb{E}[X] = \int_{-\infty}^{\infty} xp(x)\,dx$$

- **Phương sai (Variance)**:

$$\text{Var}(X) = \mathbb{E}[(X-\mu)^2] = \mathbb{E}[X^2] - (\mathbb{E}[X])^2$$

- Đo mức độ phân tán của dữ liệu/dự đoán — liên quan tới khái niệm uncertainty trong ML.

- **Hiệp phương sai (Covariance)**:

$$\text{Cov}(X,Y) = \mathbb{E}[(X-\mu_X)(Y-\mu_Y)]$$

- Ma trận hiệp phương sai giữa các đặc trưng chính là đầu vào của PCA (liên hệ mục Eigenvalue ở phần 1).

- **Hệ số tương quan (Correlation)**:

$$\rho_{X,Y} = \frac{\text{Cov}(X,Y)}{\sigma_X \sigma_Y}$$

- Chuẩn hóa covariance về khoảng $[-1,1]$, dùng để phân tích mối quan hệ tuyến tính giữa các concept trong CBM hoặc giữa các đặc trưng đầu vào.

### 5. Tối ưu hóa (Optimization)

- **Cập nhật Gradient Descent**:

$$\mathbf{x}_{t+1} = \mathbf{x}_t - \eta \nabla f(\mathbf{x}_t)$$

- $\eta$ là learning rate. Đây là thuật toán nền tảng để huấn luyện hầu hết các mô hình ML/DL.

- **Stochastic Gradient Descent (SGD)** — dùng một mẫu (hoặc mini-batch) ngẫu nhiên thay vì toàn bộ dữ liệu:

$$\mathbf{x}_{t+1} = \mathbf{x}_t - \eta \nabla f_i(\mathbf{x}_t) \quad \text{(sử dụng mẫu } i\text{)}$$

- Giúp huấn luyện nhanh hơn trên tập dữ liệu lớn, là cơ sở của Adam, RMSProp và các optimizer hiện đại.

- **Quy tắc chuỗi (Chain Rule)**:

$$\frac{d}{dx} f(g(x)) = f'(g(x)) \cdot g'(x)$$

- Là nguyên lý toán học cốt lõi đằng sau thuật toán **backpropagation** trong mạng neural.

- **Đạo hàm riêng (Partial Derivative)**:

$$\frac{\partial f}{\partial x_i} = \lim_{h \to 0} \frac{f(x_1,\ldots,x_i+h,\ldots,x_n) - f(\mathbf{x})}{h}$$

- **Xấp xỉ Taylor bậc nhất (First Order Taylor Approximation)**:

$$f(\mathbf{x}+\mathbf{h}) \approx f(\mathbf{x}) + \nabla f(\mathbf{x})^T\mathbf{h}$$

- Dùng để xấp xỉ tuyến tính hàm phi tuyến quanh một điểm — cơ sở toán học của các phương pháp giải thích mô hình cục bộ như **LIME** (xấp xỉ mô hình phức tạp bằng mô hình tuyến tính đơn giản quanh một điểm dữ liệu).

### 6. Các hàm kích hoạt (Activation Functions)

| Hàm | Công thức | Đặc điểm / Ứng dụng |
| --- | --- | --- |
| Sigmoid | $\sigma(x) = \dfrac{1}{1+e^{-x}}$ | Đầu ra trong (0,1); dùng cho phân loại nhị phân, cổng trong LSTM/GRU. Trong CBM thường dùng để dự đoán xác suất từng concept. |
| Tanh | $\tanh(x) = \dfrac{e^x - e^{-x}}{e^x + e^{-x}}$ | Đầu ra trong (-1,1), có tâm tại 0, hội tụ nhanh hơn sigmoid trong nhiều trường hợp. |
| ReLU | $f(x) = \max(0,x)$ | Đơn giản, tính toán nhanh, giảm vanishing gradient; hàm kích hoạt phổ biến nhất trong mạng sâu hiện đại. |
| Leaky ReLU | $f(x) = \max(\alpha x, x),\ 0<\alpha<1$ | Khắc phục vấn đề "dying ReLU" bằng cách cho phép gradient nhỏ khi x âm. |
| Softmax (vector z) | $\text{softmax}(z_i) = \dfrac{e^{z_i}}{\sum_{j=1}^{K} e^{z_j}}$ | Chuyển vector logits thành phân phối xác suất trên K lớp; dùng ở lớp đầu ra phân loại đa lớp. |

### 7. Các phân phối xác suất (Probability Distributions)

| Phân phối | Hàm khối/mật độ xác suất | Kỳ vọng E[X] | Phương sai Var(X) |
| --- | --- | --- | --- |
| Bernoulli (p) | $P(X=1)=p,\ P(X=0)=1-p$ | $p$ | $p(1-p)$ |
| Normal / Gaussian $(\mu, \sigma^2)$ | $p(x) = \dfrac{1}{\sqrt{2\pi\sigma^2}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}$ | $\mu$ | $\sigma^2$ |
| Binomial (n, p) | $P(X=k) = \binom{n}{k}p^k(1-p)^{n-k}$ | $np$ | $np(1-p)$ |
| Poisson $(\lambda)$ | $P(X=k) = \dfrac{e^{-\lambda}\lambda^k}{k!}$ | $\lambda$ | $\lambda$ |
| Uniform (a, b) | $p(x) = \dfrac{1}{b-a},\ x \in [a,b]$ | $\dfrac{a+b}{2}$ | $\dfrac{(b-a)^2}{12}$ |

> 💡 **Liên hệ tới đề tài NCKH (XAI / CBM):** Đại số tuyến tính (phần 1–2) là nền tảng tính toán forward/backward pass; hàm mất mát (phần 3) định hình mục tiêu huấn luyện concept + nhãn; xác suất/thống kê (phần 4, 7) hỗ trợ diễn giải độ tin cậy và tương quan giữa các concept; tối ưu hóa (phần 5) — đặc biệt xấp xỉ Taylor — là cơ sở toán của các phương pháp giải thích cục bộ như LIME/SHAP; hàm kích hoạt (phần 6) quyết định cách concept được kích hoạt/lan truyền qua mạng.
