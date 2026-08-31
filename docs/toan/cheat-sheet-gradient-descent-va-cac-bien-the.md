# Cheat Sheet: Gradient Descent và các biến thể

> 🖼️ **Ảnh gốc dùng cho trang này:** `1368_cheat-sheet-toan-hoc-gradient-descent-cac-bien-the.jpg`

### 1. Bức tranh tổng quan (The Big Picture)

- **Mục tiêu (Goal):** Tìm bộ tham số $\theta^*$ sao cho hàm mất mát (loss function) $J(\theta)$ đạt giá trị nhỏ nhất:

$$\theta^* = \arg\min_{\theta} J(\theta)$$

- **Ý tưởng (Idea):** Xuất phát từ một điểm bất kỳ trong không gian tham số, sau đó di chuyển theo hướng làm giảm giá trị hàm mất mát nhanh nhất tại điểm hiện tại. Lặp lại quá trình này nhiều lần cho đến khi hội tụ về điểm cực tiểu (hoặc gần cực tiểu).

- Hình minh họa trong ảnh là một mặt cong 3D theo hai tham số $\theta_1, \theta_2$ với trục đứng là $J(\theta)$: điểm **Start** (chấm đen) di chuyển dần theo **Gradient Descent Path** (đường nối các chấm) để tiến tới **Minimum** (ngôi sao) — nơi giá trị loss thấp nhất.

> 💡 Gradient Descent là thuật toán tối ưu lặp (iterative optimization) — không giải trực tiếp bằng công thức đóng (closed-form) mà **dò dần từng bước nhỏ** theo hướng dốc nhất đi xuống, giống như "đi xuống núi trong sương mù" chỉ dựa vào độ dốc dưới chân.

---

### 2. Quy tắc cập nhật Gradient Descent (Update Rule)

Tại mỗi bước lặp (iteration) $t$, tham số được cập nhật theo công thức:

$$\theta_{t+1} = \theta_t - \eta \nabla J(\theta_t)$$

**Giải nghĩa ký hiệu:**

| Ký hiệu | Ý nghĩa |
| --- | --- |
| $\theta_t$ | Vector tham số tại bước $t$ |
| $\eta$ | Tốc độ học (learning rate / step size) — quyết định bước nhảy dài hay ngắn |
| $\nabla J(\theta_t)$ | Gradient của hàm mất mát theo $\theta$, tính tại $\theta_t$ |

**Dạng theo từng thành phần (component-wise):**

$$\theta_{t+1}^{(i)} = \theta_t^{(i)} - \eta \, \frac{\partial J(\theta_t)}{\partial \theta^{(i)}}$$

- Nghĩa là mỗi thành phần $\theta^{(i)}$ của vector tham số được cập nhật độc lập theo đạo hàm riêng (partial derivative) của $J$ theo chính thành phần đó.

- **Lưu ý quan trọng:** ta di chuyển theo **hướng ngược lại** với gradient (gradient chỉ hướng đi lên dốc nhất — steepest ascent), vì mục tiêu là **giảm** loss, không phải tăng.

---

### 3. Gradient là gì?

- Gradient của hàm $J(\theta)$ luôn **chỉ theo hướng tăng nhanh nhất (steepest increase)** của hàm tại điểm đang xét.

- Với $\theta \in \mathbb{R}^n$, gradient là một vector cột chứa tất cả đạo hàm riêng:

$$\nabla J(\theta) = \begin{bmatrix} \dfrac{\partial J}{\partial \theta_1} \\ \dfrac{\partial J}{\partial \theta_2} \\ \vdots \\ \dfrac{\partial J}{\partial \theta_n} \end{bmatrix} \in \mathbb{R}^n$$

- Ví dụ cụ thể với hàm 2 biến $J(\theta_1, \theta_2)$:

$$\nabla J(\theta) = \begin{bmatrix} \dfrac{\partial J}{\partial \theta_1} \\ \dfrac{\partial J}{\partial \theta_2} \end{bmatrix}$$

- Trên đồ thị đường đồng mức (contour plot) của $J(\theta_1,\theta_2)$, các mũi tên gradient tại nhiều điểm khác nhau đều **hướng ra ngoài, lên phía "đồi cao" (points uphill)** — tức hướng có loss tăng. Đây chính là lý do thuật toán phải lấy dấu **trừ** gradient để đi xuống "thung lũng" loss thấp.

---

### 4. Tốc độ học — Learning Rate ($\eta$)

Learning rate quyết định **độ dài bước nhảy** mỗi lần cập nhật. Ảnh minh họa 3 trường hợp trên đường đồng mức:

| Trường hợp | Đặc điểm | Hệ quả |
| --- | --- | --- |
| $\eta$ quá nhỏ (Too small) | Bước đi rất ngắn | Hội tụ rất chậm (very slow convergence), cần rất nhiều bước lặp (many steps) |
| $\eta$ phù hợp (Good) | Bước đi vừa phải, đều đặn tiến vào tâm | Hội tụ nhanh (fast convergence) và ổn định (stable) |
| $\eta$ quá lớn (Too large) | Bước đi quá dài, nhảy qua lại quanh đáy | Có thể vọt qua điểm cực tiểu (overshoot minimum), thậm chí phân kỳ không hội tụ (may diverge) |

> ⚠️ **Việc chọn learning rate hợp lý là yếu tố then chốt (crucial) cho tối ưu hiệu quả.** Trong thực hành, người ta thường dùng learning rate schedule (giảm dần theo thời gian) hoặc các thuật toán thích nghi (Adam, RMSProp — xem mục 6 mở rộng) để tự động điều chỉnh $\eta$.

---

### 5. Sự hội tụ (Convergence)

- **Điều kiện hội tụ về cực tiểu toàn cục:** Nếu $J(\theta)$ là hàm lồi (convex) và $\eta$ đủ nhỏ, Gradient Descent sẽ hội tụ về **cực tiểu toàn cục (global minimum)**.

- **Điều kiện cụ thể cho hàm L-smooth và lồi:**

$$0 < \eta < \frac{2}{L}$$

đảm bảo thuật toán hội tụ, trong đó $L$ là hằng số Lipschitz của gradient (đo độ "trơn" — độ biến thiên tối đa của gradient).

- **Tốc độ hội tụ (rate of convergence)** — xấp xỉ theo cấp số nhân (tuyến tính) đối với hàm lồi mạnh (strongly convex):

$$J(\theta_t) - J(\theta^*) \le (1 - \eta \mu)^t \big(J(\theta_0) - J(\theta^*)\big)$$

trong đó $\mu$ là **hằng số lồi mạnh (strong convexity constant)** của $J$.

- **Ý nghĩa:** khoảng cách giữa loss hiện tại và loss tối ưu giảm theo hàm mũ $(1-\eta\mu)^t$ khi số bước lặp $t$ tăng — đồ thị minh họa trong ảnh cho thấy $J(\theta_t)$ giảm dần từ $J(\theta_0)$ và tiệm cận về $J(\theta^*)$ theo số vòng lặp (iterations).

> 💡 $\mu$ càng lớn (hàm càng "cong", lồi mạnh) và $\eta$ càng lớn (trong giới hạn cho phép) thì hệ số $(1-\eta\mu)$ càng nhỏ → hội tụ càng nhanh. Nếu $J$ không lồi (như mạng neural sâu), Gradient Descent chỉ đảm bảo hội tụ về **cực tiểu cục bộ (local minimum)** hoặc điểm yên ngựa (saddle point), không đảm bảo tối ưu toàn cục.

---

### 6. Các biến thể phổ biến (Common Variants)

Điểm khác biệt giữa các biến thể nằm ở **lượng dữ liệu dùng để tính gradient** mỗi lần cập nhật.

#### 6.1. Batch Gradient Descent (BGD)

$$\theta_{t+1} = \theta_t - \eta \nabla J(\theta_t)$$

- Dùng **toàn bộ tập dữ liệu huấn luyện (all training data)** để tính gradient tại mỗi bước.

- Ưu điểm: hướng cập nhật chính xác, ổn định, hội tụ mượt.

- Nhược điểm: rất chậm và tốn bộ nhớ khi dữ liệu lớn, vì phải duyệt toàn bộ dataset mỗi lần cập nhật một bước.

#### 6.2. Stochastic Gradient Descent (SGD)

$$\theta_{t+1} = \theta_t - \eta \nabla J_i(\theta_t)$$

- Dùng **một mẫu dữ liệu ngẫu nhiên duy nhất **$i$ (one random training example) để ước lượng gradient mỗi bước.

- Ưu điểm: cập nhật rất nhanh, có thể học online (streaming), dễ thoát khỏi cực tiểu cục bộ nhờ nhiễu (noise) trong ước lượng gradient.

- Nhược điểm: đường đi tối ưu "lắc lư" (nhiễu cao), hội tụ không mượt, cần learning rate nhỏ dần theo thời gian để ổn định.

#### 6.3. Mini-Batch Gradient Descent

$$\theta_{t+1} = \theta_t - \eta \nabla J_{\mathcal{B}}(\theta_t)$$

- Dùng **một batch nhỏ **$\mathcal{B}$** gồm một số ví dụ** (a small batch of examples) — dung hòa giữa BGD và SGD.

- Đây là lựa chọn phổ biến nhất trong thực hành deep learning hiện đại (kết hợp tốc độ của SGD và độ ổn định gần với BGD, tận dụng được tính toán song song trên GPU).

| Biến thể | Dữ liệu dùng mỗi bước | Tốc độ mỗi bước | Độ ổn định hướng cập nhật |
| --- | --- | --- | --- |
| Batch GD | Toàn bộ dataset | Chậm | Rất ổn định |
| SGD | 1 mẫu ngẫu nhiên | Rất nhanh | Nhiễu cao, dao động mạnh |
| Mini-Batch GD | Một batch nhỏ $\mathcal{B}$ | Nhanh | Cân bằng, dùng phổ biến nhất |

> 📌 Ảnh cheat sheet chỉ liệt kê 3 biến thể nền tảng này (Batch / Stochastic / Mini-batch). Các biến thể nâng cao hơn như Momentum, RMSProp, Adam (được nhắc tới trong mô tả nhiệm vụ) **không xuất hiện trong ảnh gốc** — nếu cần bổ sung, nên tìm thêm cheat sheet riêng cho nhóm thuật toán tối ưu thích nghi (adaptive optimizers) để không lẫn lộn nguồn thông tin.

> 🖼️ **Dán ảnh gốc tại đây:** `1368_cheat-sheet-toan-hoc-gradient-descent-cac-bien-the.jpg`

---

### 7. Ví dụ tính Gradient trong các mô hình cụ thể

#### 7.a. Hồi quy tuyến tính (Linear Regression) với MSE

Mô hình dự đoán: $\hat{y}_i = w x_i + b$

Hàm mất mát (Mean Squared Error):

$$J(w,b) = \frac{1}{2n} \sum_{i=1}^{n} (\hat{y}_i - y_i)^2$$

Đạo hàm riêng theo từng tham số:

$$\frac{\partial J}{\partial w} = \frac{1}{n} \sum_{i=1}^{n} (\hat{y}_i - y_i)\, x_i$$

$$\frac{\partial J}{\partial b} = \frac{1}{n} \sum_{i=1}^{n} (\hat{y}_i - y_i)$$

- Trực quan: gradient theo $w$ tỉ lệ với sai số $(\hat y_i - y_i)$ nhân với đầu vào $x_i$; gradient theo $b$ chỉ là trung bình sai số. Đồ thị minh họa là một đường thẳng hồi quy khớp qua các điểm dữ liệu $(x,y)$.

#### 7.b. Hồi quy Logistic (Logistic Regression) với Binary Cross-Entropy

Hàm kích hoạt sigmoid: $\hat{y}_i = \sigma(w x_i + b)$, với $z = wx+b$

Hàm mất mát (Binary Cross-Entropy):

$$J(w,b) = -\frac{1}{n} \sum_{i=1}^{n} \Big[ y_i \log(\hat{y}_i) + (1-y_i)\log(1-\hat{y}_i) \Big]$$

Đạo hàm riêng (có dạng **giống hệt** công thức của Linear Regression MSE, đây là một tính chất đẹp khi kết hợp sigmoid + cross-entropy):

$$\frac{\partial J}{\partial w} = \frac{1}{n} \sum_{i=1}^{n} (\hat{y}_i - y_i)\, x_i$$

$$\frac{\partial J}{\partial b} = \frac{1}{n} \sum_{i=1}^{n} (\hat{y}_i - y_i)$$

- Đồ thị minh họa là đường cong sigmoid hình chữ S, trục hoành là $z = wx+b$, trục tung là $\hat y$ nằm trong khoảng $[0,1]$.

> 💡 Sự trùng khớp giữa gradient của MSE (hồi quy tuyến tính) và gradient của Binary Cross-Entropy (hồi quy logistic) không phải ngẫu nhiên: cả hai đều thuộc họ mô hình tuyến tính tổng quát (Generalized Linear Model) với hàm liên kết (link function) và hàm mất mát tương ứng được chọn sao cho đạo hàm luôn có dạng $(\hat y - y)x$.

#### 7.c. Hàm bậc hai tổng quát (Quadratic Function)

$$J(\theta) = \frac{1}{2}\theta^T A \theta - b^T \theta + c$$

trong đó $A$ là **ma trận đối xứng xác định dương (symmetric positive definite)**.

Gradient của hàm này:

$$\nabla J(\theta) = A\theta - b$$

Quy tắc cập nhật Gradient Descent áp dụng cho hàm bậc hai:

$$\theta_{t+1} = \theta_t - \eta (A\theta_t - b)$$

- Đây là dạng tổng quát hóa của bài toán tối ưu bậc hai (quadratic optimization) — mặt loss có dạng bát úp (bowl shape) lồi hoàn hảo trong không gian $\theta_1,\theta_2$ như hình minh họa 3D trong ảnh, giúp trực quan hóa vì sao Gradient Descent luôn hội tụ tốt trên các hàm dạng này (khi $A$ xác định dương).

#### 7.d. Hàm mất mát có chính quy hóa L2 (Regularized Loss)

$$J(\theta) = L(\theta) + \frac{\lambda}{2} \lVert \theta \rVert^2_2$$

Gradient:

$$\nabla J(\theta) = \nabla L(\theta) + \lambda \theta$$

Quy tắc cập nhật:

$$\theta_{t+1} = \theta_t - \eta \big(\nabla L(\theta_t) + \lambda \theta_t\big)$$

- $\lambda$ là hệ số chính quy hóa (regularization strength), $L(\theta)$ là hàm mất mát gốc (ví dụ MSE hoặc Cross-Entropy).

- **Ý nghĩa của số hạng **$\lambda\theta$** trong gradient:** mỗi bước cập nhật đều kéo $\theta$ về gần $0$ hơn một chút (weight decay), giúp giảm overfitting bằng cách hạn chế độ lớn của trọng số mô hình.

- Trên đồ thị đường đồng mức minh họa, các mũi tên gradient tại nhiều điểm đều có xu hướng bị "kéo thêm" về phía tâm (gốc tọa độ) so với gradient của riêng $L(\theta)$.

> 📌 **Tổng kết mục 7:** Cả 4 ví dụ đều là ứng dụng trực tiếp của quy tắc chuỗi (chain rule) và đạo hàm ma trận để tính $\nabla J(\theta)$ cho từng loại mô hình/hàm mất mát cụ thể, sau đó cắm vào công thức cập nhật chung ở Mục 2: $\theta_{t+1} = \theta_t - \eta \nabla J(\theta_t)$.
