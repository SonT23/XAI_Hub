# Cẩm nang Deep Learning: Nền tảng Neural Network

> 🖼️ **11 ảnh gốc cho trang này (dán theo đúng thứ tự vào từng mục bên dưới):**
> 1300_trang-bia-cam-nang-deep-learning-so-do-neural-netw.jpg
>
> 1301_gioi-thieu-deep-learning-so-sanh-ml-vs-dl.jpg
>
> 1302_nen-tang-neural-network-perceptron-layers-weights.jpg
>
> 1303_activation-functions-relu-sigmoid-tanh-softmax.jpg
>
> 1304_forward-propagation-va-backpropagation-trong-neura.jpg
>
> 1305_loss-functions-mse-binary-categorical-cross-entrop.jpg
>
> 1306_gradient-descent-va-cac-thuat-toan-optimization-ad.jpg
>
> 1307_overfitting-va-cac-ky-thuat-regularization-dropout.jpg
>
> 1308_tong-quan-kien-truc-neural-network-fnn-cnn-rnn-lst.jpg
>
> 1309_convolutional-neural-networks-cnn-convolution-pool.jpg
>
> 1310_recurrent-neural-networks-rnn-cong-thuc-vanishing-.jpg
>

Trang này tổng hợp lại **cẩm nang viết tay "Deep Learning" (bộ 11 ảnh cheat-sheet)**, đi từ nền tảng đến kiến trúc mạng cụ thể, theo đúng mạch: (1) trang bìa & tổng quan → (2) DL là gì, so với ML → (3) neuron/perceptron & các layer → (4) activation functions → (5) forward & backpropagation → (6) loss functions → (7) gradient descent & optimizer → (8) overfitting & regularization → (9) tổng quan các kiến trúc mạng (FNN/CNN/RNN/LSTM/GRU/Autoencoder/Transformer) → (10) đi sâu CNN → (11) đi sâu RNN (kèm vanishing/exploding gradient). Đây là tài liệu nền tảng cho phần NCKH về Explainable AI/CBM vì các kỹ thuật XAI (Grad-CAM, saliency map, concept bottleneck...) đều xây trên các khối này (CNN, backprop, loss, activation).

---

### 1. Trang bìa & Sơ đồ tổng quan Deep Learning

> 🖼️ Dán ảnh: `1300_trang-bia-cam-nang-deep-learning-so-do-neural-netw.jpg`

**Cẩm nang Deep Learning v1.0** — khẩu hiệu: *"Nắm vững khái niệm. Xây dựng hệ thống thông minh. Định hình tương lai cùng Deep Learning."*

- Sơ đồ minh hoạ một neural network cơ bản: **Input → Hidden Layers → Output**, với các neuron (nodes) nối đầy đủ (fully-connected) giữa các lớp bằng các đường weight.

- Từ khoá chủ đề xuyên suốt cẩm nang: **Feature Learning • Representation Learning • Automation • Scalability • Innovation**.

**Nội dung bên trong (11 chương gốc của cẩm nang đầy đủ):**

1. Giới thiệu về Deep Learning

2. Kiến thức cơ bản về Neural Networks

3. Activation Functions

4. Loss Functions

5. Optimization Algorithms

6. Convolutional Neural Networks (CNN)

7. Recurrent Neural Networks (RNN)

8. Long Short-Term Memory (LSTM)

9. Transformers & Attention

10. Generative Models (GAN, VAE)

11. Deployment & Best Practices
    - Kèm thêm: Cheat Sheet & Interview Q&A

**Deep Learning qua các con số (ước tính):**

| Chỉ số | Giá trị ước tính |
| --- | --- |
| Nhà phát triển | 2.5+ triệu |
| Framework phổ biến | TensorFlow, PyTorch, Keras, JAX |
| Dữ liệu huấn luyện | GBs đến TBs |
| Thời gian huấn luyện | Vài phút đến vài ngày |
| Bộ nhớ GPU | 4GB đến 80GB+ |
| Độ chính xác đạt được | 90% đến 99%+ |

**Chủ đề bao gồm:** Neural Networks, CNN & Computer Vision, RNN/LSTM/GRU, Transformers & NLP, Activation Functions, Loss Functions, Optimization, Regularization, Transfer Learning, Generative Models, Model Evaluation, Deployment & MLOps, Best Practices.

**Tài liệu này dành cho ai?** Học sinh/sinh viên & người mới bắt đầu; Kỹ sư & lập trình viên ML; Bất kỳ ai đam mê AI.

> 💡 "Cách tốt nhất để dự đoán tương lai là tự tạo ra nó cùng Deep Learning."

---

### 2. Giới thiệu Deep Learning & So sánh ML vs DL

> 🖼️ Dán ảnh: `1301_gioi-thieu-deep-learning-so-sanh-ml-vs-dl.jpg`

> "Deep Learning là một nhánh con của Machine Learning, được lấy cảm hứng từ cấu trúc và chức năng của bộ não con người, gọi là **Artificial Neural Networks**."

#### 2.1. Deep Learning là gì?

- Deep Learning (DL) là một phần của Machine Learning (ML), sử dụng **Artificial Neural Networks (ANNs)** với nhiều lớp (**hidden layers**) để học các pattern từ dữ liệu.

- Nó có thể **tự động học các feature** từ dữ liệu thô mà không cần feature engineering thủ công (đây là khác biệt cốt lõi so với ML truyền thống).

- Hoạt động cực kỳ hiệu quả với **lượng dữ liệu lớn** và các bài toán phức tạp.

#### 2.2. Tại sao cần Deep Learning?

- Xử lý tốt **unstructured data** như hình ảnh, âm thanh, văn bản, video.

- Tự động học các **hierarchical feature** (đặc trưng theo tầng bậc: từ cạnh/nét đơn giản → hình khối → đối tượng phức tạp).

- **Độ chính xác** cao trong các tác vụ phức tạp.

- Mở rộng tốt cùng **big data** và sức mạnh tính toán (GPU/TPU).

- Là sức mạnh đứng sau các ứng dụng **AI hiện đại** (ChatGPT, xe tự lái, nhận diện giọng nói...).

#### 2.3. So sánh ML vs DL

| Khía cạnh | Machine Learning (ML) | Deep Learning (DL) |
| --- | --- | --- |
| Feature Engineering | Cần feature engineering thủ công | Tự động học feature từ dữ liệu |
| Yêu cầu dữ liệu | Hoạt động tốt với dataset nhỏ đến vừa | Cần lượng dữ liệu lớn để đạt hiệu suất tốt nhất |
| Mô hình | Shallow model (vd: Linear Regression, SVM, Decision Tree) | Deep Neural Network với nhiều hidden layer |
| Hiệu suất | Tốt cho bài toán đơn giản | Xuất sắc cho bài toán phức tạp |
| Tính toán | Ít tốn tài nguyên tính toán hơn | Cao, cần GPU/TPU |
| Ví dụ | Phát hiện spam, dự đoán giá nhà | Nhận diện hình ảnh, giọng nói, xe tự lái, ChatGPT... |

**DL trong thực tế:** Nhận diện hình ảnh; Nhận diện giọng nói; Xe tự lái; Chatbot & NLP.

#### 2.4. Ứng dụng thực tế

Gợi ý YouTube/Netflix • Gợi ý E-commerce • Trợ lý giọng nói (Siri, Alexa) • Phát hiện Email spam • Phân tích hình ảnh y tế • Chatbot AI (ChatGPT).

---

### 3. Nền tảng Neural Network: Perceptron, Layers, Weights

> 🖼️ Dán ảnh: `1302_nen-tang-neural-network-perceptron-layers-weights.jpg`

Các mô hình Deep Learning được xây dựng bằng **Artificial Neural Networks (ANNs)**, lấy cảm hứng từ bộ não con người.

#### 3.1. Neuron (Perceptron)

Neuron là đơn vị cơ bản cấu tạo nên một neural network. Một neuron nhận các input $x_1, x_2, ..., x_n$, nhân với trọng số (weight) tương ứng $w_1, w_2, ..., w_n$, cộng thêm bias $b$, tạo ra tổng có trọng số $z$ (weighted sum), rồi đưa $z$ qua một **activation function** $f(z)$ để ra output $y$.

**Ký hiệu:**

- $x_i$ = inputs

- $w_i$ = weights

- $b$ = bias

- $z$ = weighted sum

- $f(z)$ = activation function

**Công thức toán học:**

$$z = w_1x_1 + w_2x_2 + ... + w_nx_n + b$$

$$y = f(z)$$

#### 3.2. Các layer trong Neural Network

- **Input Layer**: Nhận dữ liệu thô.

- **Hidden Layer(s)**: Thực hiện tính toán và trích xuất feature.

- **Output Layer**: Cho ra kết quả dự đoán cuối cùng.

Một mạng có thể có nhiều hidden layer — **nhiều layer hơn → học được pattern phức tạp hơn.**

#### 3.3. Weights & Biases

- **Weights (**$w_i$**)** kiểm soát độ mạnh của kết nối giữa các neuron.

- **Bias (**$b$**)** cho phép mô hình dịch chuyển activation function (giúp mô hình linh hoạt hơn, không bị ép đi qua gốc toạ độ).

- Trong quá trình training, **weights và biases** được học để giảm thiểu lỗi (error/loss).

#### 3.4. Các loại Neural Network (ví dụ)

| Loại | Mô tả |
| --- | --- |
| Feedforward NN | Thông tin chỉ di chuyển về phía trước (Input → Output) |
| CNN (Convolutional NN) | Dùng cho dữ liệu hình ảnh |
| RNN (Recurrent NN) | Dùng cho dữ liệu tuần tự / time series |
| LSTM / GRU | Loại RNN đặc biệt, xử lý long-term dependencies |
| Transformers | Dùng trong NLP, Computer Vision và nhiều mô hình AI hiện đại |

#### 3.5. Neural Network dự đoán như thế nào? (Quy trình 5 bước)

1. **Input**: Dữ liệu thô được đưa vào network.

2. **Forward Propagation**: Dữ liệu đi qua các layer, mỗi neuron thực hiện $(w \cdot x + b)$ và activation.

3. **Output**: Network cho ra dự đoán.

4. **Error Calculation**: So sánh dự đoán với giá trị thực bằng loss function.

5. **Backpropagation**: Lỗi được truyền ngược lại, weights & biases được cập nhật.

Quá trình này **lặp lại qua nhiều iteration** cho đến khi mô hình học được!

> 💡 Tip: Hãy hình dung neural network như một <b>function approximator</b> — học ánh xạ giữa Input (X) và Output (Y) từ dữ liệu.

---

### 4. Activation Functions: ReLU, Sigmoid, Tanh, Softmax

> 🖼️ Dán ảnh: `1303_activation-functions-relu-sigmoid-tanh-softmax.jpg`

Activation function thêm **non-linearity** vào neural network, giúp nó học được các pattern phức tạp.

> 💡 Nếu không có activation function, một neural network chỉ là một mô hình <b>linear regression</b> (dù có xếp bao nhiêu lớp, tổ hợp các phép biến đổi tuyến tính vẫn chỉ là một phép tuyến tính).

#### ① ReLU (Rectified Linear Unit)

$$f(x) = \max(0, x)$$

- **Range**: $[0, \infty)$

- **Pros**: Đơn giản & nhanh; giúp giảm vanishing gradient.

- **Cons**: Dying ReLU problem (neuron có thể "chết" — luôn output 0 nếu z âm mãi); không zero-centered.

- **Dùng trong**: Hidden layers.

#### ② Sigmoid

$$f(x) = \frac{1}{1 + e^{-x}}$$

- **Range**: $(0, 1)$

- **Pros**: Output từ 0 đến 1; hữu ích cho probability.

- **Cons**: Vanishing gradient; không zero-centered.

- **Dùng trong**: Output layer (binary classification), gates trong LSTM/GRU.

#### ③ Tanh (Hyperbolic Tangent)

$$f(x) = \frac{e^{x} - e^{-x}}{e^{x} + e^{-x}}$$

- **Range**: $(-1, 1)$

- **Pros**: Zero-centered; mượt hơn sigmoid.

- **Cons**: Vẫn gặp vanishing gradient.

- **Dùng trong**: Hidden layers (mạng cũ, nay chủ yếu dùng ReLU).

#### ④ Softmax (Multi-class output)

$$f(z_i) = \frac{e^{z_i}}{\sum_j e^{z_j}}$$

- **Range**: $(0,1)$, tổng các output = 1

- **Pros**: Chuyển score thành probability; dùng cho multi-class classification.

- **Cons**: Không dùng trong hidden layers.

- **Dùng trong**: Output layer cho bài toán multi-class.

#### Tóm tắt so sánh

| Function | Formula | Range | Zero-Centered? | Dùng tốt nhất trong |
| --- | --- | --- | --- | --- |
| ReLU | max(0,x) | [0,∞) | Không | Hidden Layers (Mặc định) |
| Sigmoid | 1/(1+e^-x) | (0,1) | Không | Output (Binary), Gates |
| Tanh | (eˣ-e⁻ˣ)/(eˣ+e⁻ˣ) | (-1,1) | Có | Hidden Layers |
| Softmax | e^zi/Σe^zj | (0,1), tổng=1 | Không | Output (Multi-class) |

> 💡 TIPS: Dùng <b>ReLU</b> trong hidden layers để training tốt hơn. Dùng <b>Softmax</b> cho output multi-class. Chọn activation function phù hợp với loại bài toán!

☆ **Ghi nhớ:** Chọn đúng activation function có thể tạo ra **khác biệt lớn** trong khả năng học của mô hình.

---

### 5. Forward Propagation và Backpropagation

> 🖼️ Dán ảnh: `1304_forward-propagation-va-backpropagation-trong-neura.jpg`

**Forward Propagation** là cách mô hình đưa ra dự đoán. **Backpropagation** là cách mô hình **học** từ những sai lầm của nó.

#### 5.1. Forward Propagation

Dữ liệu chảy từ input layer → hidden layer(s) → output layer để tạo ra kết quả cuối cùng.

Với một neuron đơn lẻ:

$$z = w_1x_1 + w_2x_2 + ... + w_nx_n + b$$

$$a = f(z) \quad \text{(a = activation/output)}$$

- $z$ = weighted sum (phần linear)

- $a$ = activation (sau khi áp dụng activation function)

- $f()$ = activation function

**Ký hiệu (Notations):** $x$ = input vector, $W$ = weights, $b$ = bias vector, $z$ = linear output, $a$ = activation, $\hat{y}$ = dự đoán/output, $y$ = actual output (giá trị thực).

Ví dụ mạng 2 lớp (1 hidden layer):

$$z^1 = W^1x + b^1, \quad a^1 = f(z^1)$$

$$z^2 = W^2a^1 + b^2, \quad a^2 = f(z^2) = \hat{y} \text{ (dự đoán)}$$

#### 5.2. Backpropagation (tổng quan)

Backpropagation hoạt động **ngược lại** — từ output layer đến input layer — để cập nhật weights và biases nhằm giảm thiểu error. Gồm 4 bước:

1. **Tính loss** bằng predicted và actual output.

2. **Tính error** (gradient) tại output layer.

3. **Lan truyền error** ngược qua các hidden layer.

4. **Cập nhật** weights & biases bằng gradient.

**Mục tiêu:** Giảm thiểu loss function bằng cách điều chỉnh weights và biases.

*Tại sao nó hoạt động?* Calculus (**Chain Rule**) giúp tính từng weight đóng góp thế nào vào lỗi cuối cùng.

#### 5.3. Backpropagation (chi tiết)

**1. Output Layer Error (**$\delta^{[L]}$**):**

- Cho regression (MSE):

$$\delta^{[L]} = (\hat{y}-y) \odot f'(z^{[L]})$$

- Cho classification (Cross Entropy với Softmax):

$$\delta^{[L]} = \hat{y} - y$$

($\odot$ = element-wise multiplication)

**2. Hidden Layer Error:**

$$\delta^{[l]} = (W^{[l+1]})^T \delta^{[l+1]} \odot f'(z^{[l]})$$

Trong đó: $l$ = layer hiện tại, $L$ = layer cuối cùng.

**3. Gradient (để cập nhật):**

$$dW^{[l]} = \delta^{[l]}(a^{[l-1]})^T, \quad db^{[l]} = \delta^{[l]}$$

$W, b$ được cập nhật bằng **Gradient Descent**:

$$W^{[l]} = W^{[l]} - \eta \, dW^{[l]}, \quad b^{[l]} = b^{[l]} - \eta \, db^{[l]}$$

($\eta$ = learning rate)

#### 5.4. Tóm tắt trực quan

**Forward Pass**: Input (x) → mạng → Output ($\hat{y}$).

**Backward Pass**: Error (cập nhật weights & biases) truyền ngược từ output về input.

**TIPS:**

- Hiểu luồng: Forward → Loss → Backward → Update.

- Activation function thêm non-linearity.

- Backpropagation là ứng dụng của chain rule.

- Thay đổi nhỏ ở weights có thể giảm loss đáng kể.

- Luyện tập với ví dụ nhỏ để xây dựng trực giác!

> 💡 Ghi nhớ: Forward Propagation tạo ra dự đoán, Backpropagation làm mô hình <b>tốt hơn</b>. ❤️

---

### 6. Loss Functions: MSE, Binary/Categorical Cross-Entropy

> 🖼️ Dán ảnh: `1305_loss-functions-mse-binary-categorical-cross-entrop.jpg`

Loss function đo lường mức độ **sai** của dự đoán. Mục tiêu là giảm thiểu loss.

> 💡 Loss thấp hơn → dự đoán tốt hơn → mô hình tốt hơn.

#### 6.1. Mean Squared Error (MSE) — dùng cho Regression

$$MSE = \frac{1}{n}\sum_{i}(y_i - \hat{y}_i)^2$$

- $y_i$ = giá trị thực, $\hat{y}_i$ = giá trị dự đoán, $n$ = số lượng mẫu.

- **Pros**: Phạt các lỗi lớn nhiều hơn (do bình phương); mượt và khả vi (differentiable).

- **Cons**: Nhạy cảm với outlier; không lý tưởng cho classification.

#### 6.2. Binary Cross Entropy (Log Loss) — dùng cho Binary Classification

$$BCE = -\frac{1}{n}\sum_i \left[ y_i\log(\hat{y}_i) + (1-y_i)\log(1-\hat{y}_i) \right]$$

- $y_i \in \{0,1\}$ (nhãn thực); $\hat{y}_i \in (0,1)$ (probability dự đoán).

- **Pros**: Tốt nhất cho binary classification; xử lý probability tốt.

- **Cons**: Không dùng cho regression; chỉ cho output binary.

#### 6.3. Categorical Cross Entropy — dùng cho Multi-class Classification (2 lớp trở lên)

$$CCE = -\frac{1}{n}\sum_i \sum_j y_{ij}\log(\hat{y}_{ij})$$

- $C$ = số lượng class; $y_{ij} = 1$ nếu mẫu $i$ thuộc class $j$, ngược lại = 0; $\hat{y}_{ij}$ = probability dự đoán class $j$ cho mẫu $i$.

- **Pros**: Hoàn hảo cho multi-class classification; hoạt động tốt với softmax output.

- **Cons**: Không dùng cho binary (dùng BCE); nhạy cảm với label nhiễu.

#### So sánh nhanh

| Loss Function | Dùng cho | Loại Output | Range | Dùng tốt nhất khi |
| --- | --- | --- | --- | --- |
| MSE | Regression | Continuous | [0,∞) | Dự đoán số (giá, chiều cao,...) |
| Binary Cross Entropy | Binary Classification | Probability (0/1) | [0,∞) | Yes/No, Spam/Not Spam |
| Categorical Cross Entropy | Multi-class Classification | Probability (multi-class) | [0,∞) | Cat/Dog/Bird classification |

> 💡 Quy tắc ngón tay cái: Regression → MSE | Binary Classification → BCE | Multi-class Classification → CCE

---

### 7. Gradient Descent và các thuật toán Optimization (Adam...)

> 🖼️ Dán ảnh: `1306_gradient-descent-va-cac-thuat-toan-optimization-ad.jpg`

Gradient Descent là một thuật toán **optimization** dùng để **giảm thiểu** loss function bằng cách cập nhật các tham số theo hướng ngược với gradient.

> 💡 Mục tiêu: Tìm tập tham số (weights, biases) giúp giảm thiểu loss.

#### 7.1. Gradient Descent là gì?

- Bắt đầu với random weights.

- Tính **gradient** (độ dốc) của loss function.

- Cập nhật tham số theo hướng **ngược lại** với gradient.

- Lặp lại cho đến khi loss được giảm thiểu.

**Quy tắc cập nhật:**

$$w_{t+1} = w_t - \eta \nabla L(w_t)$$

- $w_t$ = weights hiện tại

- $\eta$ = learning rate

- $\nabla L(w_t)$ = gradient của loss function theo weights

#### 7.2. Các loại Gradient Descent

1. **Batch Gradient Descent**: Dùng toàn bộ dataset để tính gradient. Cập nhật 1 lần mỗi epoch. Ổn định nhưng chậm hơn.

2. **Stochastic Gradient Descent (SGD)**: Dùng một training example mỗi lần. Cập nhật cho mỗi example. Nhanh hơn nhưng nhiễu (dao động).

3. **Mini-Batch Gradient Descent**: Dùng một batch nhỏ các example. Cập nhật cho mỗi mini-batch. Cân bằng tốt giữa tốc độ và ổn định.

4. **Online Gradient Descent**: Tương tự SGD, dùng cho dữ liệu online/streaming. Cập nhật mô hình liên tục khi dữ liệu đến. Thích ứng nhanh.

#### 7.3. Các thuật toán Optimization

- **1. SGD (Vanilla GD)**: Dạng đơn giản nhất, baseline tốt.

$$w_{t+1} = w_t - \eta \nabla L(w_t)$$

- **2. Momentum**: Tăng tốc theo hướng phù hợp & giảm dao động.

$$v_t = \gamma v_{t-1} + \eta \nabla L(w_t), \quad w_{t+1} = w_t - v_t$$

- **3. RMSProp**: Điều chỉnh learning rate cho từng tham số. Tốt cho RNN.

$$s_t = \beta s_{t-1} + (1-\beta)(\nabla L)^2$$

- **4. Adam**: Kết hợp Momentum & RMSProp. Optimizer phổ biến nhất, dùng $m_t, v_t$ (bias correction).

**TIPS**: Bắt đầu với Adam (mặc định). Điều chỉnh cẩn thận learning rate ($\eta$). Quá cao → vọt qua minima. Quá thấp → hội tụ chậm.

#### 7.4. So sánh các Optimizer

| Optimizer | Memory | Tốc độ | Hội tụ | Dùng tốt nhất trong | Ghi chú |
| --- | --- | --- | --- | --- | --- |
| SGD | Thấp | Nhanh (mỗi update) | Chậm | Dataset lớn | Đơn giản, có thể dao động |
| Momentum | Trung bình | Nhanh hơn | Tốt hơn | CNN, Deep Nets | Giảm dao động |
| RMSProp | Trung bình | Nhanh | Tốt | RNN, bài toán non-stationary | Xử lý gradient thay đổi |
| Adam | Cao | Nhanh | Xuất sắc | Hầu hết bài toán Deep Learning | Lựa chọn mặc định tốt nhất |

★ **Ghi nhớ:** Optimization là chìa khoá để training mô hình hiệu quả. ❤️

---

### 8. Overfitting và các kỹ thuật Regularization (Dropout...)

> 🖼️ Dán ảnh: `1307_overfitting-va-cac-ky-thuat-regularization-dropout.jpg`

**Overfitting** xảy ra khi mô hình học **quá kỹ** training data, bao gồm cả noise, và hoạt động kém trên **dữ liệu chưa từng thấy**.

**Tại sao xảy ra?** Mô hình quá phức tạp; quá nhiều tham số; quá ít training data; training quá lâu.

> 💡 Mục tiêu: Xây dựng mô hình tổng quát hoá tốt trên dữ liệu mới.

#### 8.1. Hiểu về Overfitting

1. **Underfitting**: Mô hình quá đơn giản → Bias cao, error cao.

2. **Good Fit**: Độ phức tạp phù hợp → Bias thấp, variance thấp.

3. **Overfitting**: Mô hình quá phức tạp → Bias thấp, variance cao.

**Đánh đổi Bias vs Variance:** Tăng độ phức tạp → Bias giảm, Variance tăng → Cần sự cân bằng phù hợp!

#### 8.2. Các kỹ thuật Regularization

1. **L2 Regularization (Ridge)**: Thêm penalty bằng bình phương độ lớn của weights.

$$L = L_0 + \lambda \sum w_i^2$$

Thu nhỏ weight lớn; giảm overfitting; $\lambda$ = độ mạnh regularization.

1. **L1 Regularization (Lasso)**: Thêm penalty bằng giá trị tuyệt đối của weights.

$$L = L_0 + \lambda \sum |w_i|$$

Có thể đưa weight về 0; tạo mô hình sparse; tốt cho feature selection.

1. **Dropout**: Ngẫu nhiên loại bỏ (set = 0) một số neuron khi training. Ngăn co-adaptation; hoạt động như training nhiều mạng con.

2. **Early Stopping**: Dừng training khi hiệu suất trên validation set ngừng cải thiện. Đơn giản nhưng hiệu quả; ngăn overfitting.

3. **Batch Normalization**: Chuẩn hoá output của một layer về mean 0, variance 1.

$$\hat{x} = \frac{x - \mu}{\sqrt{\sigma^2 + \epsilon}}$$

Ổn định & tăng tốc training; có vai trò như regularizer.

1. **Data Augmentation**: Tăng nhân tạo dữ liệu training bằng các phép biến đổi (flip, crop, rotate, zoom, noise...). Cải thiện khả năng tổng quát hoá; phổ biến với ảnh.

2. **Đơn giản hoá Model**: Dùng mô hình đơn giản hơn hoặc giảm số tham số — ít layer hơn, ít neuron hơn, bỏ feature không cần thiết.

#### 8.3. Training Curve (phát hiện overfitting)

| Quan sát | Training Loss | Validation Loss | Kết luận |
| --- | --- | --- | --- |
| Cả hai đều cao | Cao | Cao | Underfitting (Tăng model capacity) |
| Cả hai đều thấp | Thấp | Thấp | Good Fit (Mô hình tổng quát hoá tốt) |
| Train thấp, Val cao | Thấp | Cao | Overfitting (Áp dụng Regularization) |

> 💡 Điểm mấu chốt: Đừng chỉ fit dữ liệu, hãy <b>hiểu</b> nó. Regularization giúp mô hình tổng quát hoá và hoạt động tốt trên dữ liệu chưa từng thấy. ❤️

---

### 9. Tổng quan các kiến trúc Neural Network: FNN, CNN, RNN, LSTM...

> 🖼️ Dán ảnh: `1308_tong-quan-kien-truc-neural-network-fnn-cnn-rnn-lst.jpg`

Mỗi architecture được thiết kế để xử lý hiệu quả các loại **dữ liệu** và **tác vụ học** khác nhau.

#### 9.1. Feedforward Neural Network (FNN)

- Dữ liệu chỉ đi về phía trước, từ input layer đến output layer. Không có cycle hay loop.

- **Dùng cho**: Classification, Regression, Tabular data.

#### 9.2. Convolutional Neural Network (CNN)

- Dùng convolutional layer để trích xuất spatial feature. Tốt nhất cho dữ liệu hình ảnh và video.

- Luồng: Input Image → Conv Layer → Pooling Layer → FC Layer → Output.

- **Dùng cho**: Nhận diện hình ảnh, Object detection, Medical imaging.

#### 9.3. Recurrent Neural Network (RNN)

- Thiết kế cho dữ liệu tuần tự. Có loop để duy trì hidden state (bộ nhớ).

- **Dùng cho**: Text, Speech, Time series, Language modeling.

#### 9.4. LSTM (Long Short-Term Memory)

- Khắc phục vấn đề vanishing gradient của RNN. Dùng gate để kiểm soát luồng thông tin.

- **Dùng cho**: Chuỗi dài, Translation, Video analysis.

#### 9.5. GRU (Gated Recurrent Unit)

- Phiên bản đơn giản hoá của LSTM. Có reset gate và update gate.

- **Dùng cho**: Tương tự LSTM nhưng nhanh hơn và ít phức tạp hơn.

#### 9.6. Autoencoder

- Mô hình unsupervised learning. Học nén dữ liệu rồi tái tạo lại (Input → Encoder → Latent Space → Decoder → Output/Reconstruction).

- **Dùng cho**: Dimensionality reduction, Denoising, Anomaly detection.

#### 9.7. Transformer (Attention-based Model)

- Dùng self-attention mechanism thay vì recurrence. Highly parallelizable, hoạt động tốt trên chuỗi dài.

- Kiến trúc: Input (Embedding) → Encoder Stack (Nx: Multi-Head Self-Attention + Feed Forward) → Decoder Stack (Nx: Masked Self-Attention + Multi-Head Attention + Feed Forward) → Output (Softmax).

- **Dùng cho**: NLP (BERT, GPT), Translation, Summarization.

#### So sánh các Architecture

| Architecture | Tốt nhất cho | Xử lý Sequence? | Nắm bắt Spatial Info? | Tốc độ Training |
| --- | --- | --- | --- | --- |
| FNN | Tabular Data | Không | Không | Nhanh |
| CNN | Images/Videos | Không | Có | Trung bình |
| RNN | Sequences | Có | Không | Chậm |
| LSTM | Long Sequences | Có | Không | Chậm |
| GRU | Sequences | Có | Không | Nhanh hơn |
| Autoencoder | Unsupervised Learning | Không | Không | Trung bình |
| Transformer | NLP/Long Sequences | Có | Không | Nhanh (Parallel) |

> 💡 Điểm mấu chốt: Lựa chọn architecture phụ thuộc vào loại dữ liệu và bài toán bạn đang giải quyết. Hiểu dữ liệu → Chọn đúng architecture → Training hiệu quả → Đạt kết quả tốt hơn. ☆

---

### 10. Convolutional Neural Networks (CNN) — Convolution, Pooling

> 🖼️ Dán ảnh: `1309_convolutional-neural-networks-cnn-convolution-pool.jpg`

CNN được thiết kế để tự động học **spatial hierarchy** của các feature từ hình ảnh bằng convolution operation.

**Tại sao dùng CNN?** Tận dụng spatial structure của dữ liệu; ít tham số hơn; translation invariance; rất tốt cho hình ảnh & video.

#### 10.1. Convolution Operation

Một filter (kernel) nhỏ trượt qua input và tính element-wise multiplication rồi cộng lại.

**Công thức Output size:**

$$O = \frac{N - F + 2P}{S} + 1$$

- $N$ = input size, $F$ = filter size, $P$ = padding, $S$ = stride.

Ví dụ minh hoạ: Input Image 5x5 nhân chập (convolve, ký hiệu $*$) với Filter/Kernel 3x3 cho ra Feature Map (Output) 3x3.

#### 10.2. CNN Architecture (luồng điển hình)

Input (64x64x3) → Convolution + ReLU → Pooling (Max Pool) → Convolution + ReLU → Pooling (Max Pool) → Flatten → Fully Connected Layers → Output (Softmax).

**Tóm tắt luồng:** Conv: Trích xuất feature → Pool: Giảm spatial size → FC: Học pattern bậc cao → Softmax: Dự đoán class.

#### 10.3. Các layer phổ biến trong CNN

1. **Convolution Layer**: Áp dụng filter để trích xuất feature.

2. **Activation Layer (ReLU)**: Thêm non-linearity.

3. **Pooling Layer (Max/Average)**: Giảm spatial size.

4. **Batch Normalization**: Chuẩn hoá activation, tăng tốc training.

5. **Dropout**: Ngăn co-adaptation.

6. **Fully Connected Layer**: Thực hiện classification cuối cùng.

7. **Softmax Layer**: Chuyển score thành probability.

#### 10.4. Ví dụ Pooling (Max Pooling 2x2, stride=2)

Input Feature Map 4x4 qua Max Pool (2x2, s=2) → Output 2x2 (lấy giá trị lớn nhất trong mỗi vùng 2x2, ví dụ vùng {1,3,4,6} → 6; vùng {2,0,6,1} → 6...).

#### 10.5. Các kiến trúc CNN phổ biến

| Architecture | Năm | Ý tưởng chính | Tốt nhất cho |
| --- | --- | --- | --- |
| LeNet-5 | 1998 | CNN đầu tiên cho nhận diện chữ số | Chữ số viết tay |
| AlexNet | 2012 | Deep CNN, ReLU, Dropout | ImageNet classification |
| VGGNet | 2014 | Rất sâu với filter 3x3 | Tác vụ cần độ chính xác cao |
| GoogLeNet (Inception) | 2014 | Inception modules | Trích xuất feature hiệu quả |
| ResNet | 2015 | Residual (skip) connections | Mạng rất sâu |
| EfficientNet | 2019 | Scale depth, width, resolution | Độ chính xác cao, ít compute |

**Điểm mấu chốt:** CNN tận dụng spatial structure của hình ảnh. Convolution trích xuất pattern cục bộ. Pooling giảm size và tính toán. Mạng sâu hơn học được feature phức tạp hơn. Dùng ReLU, BatchNorm, Dropout để training tốt hơn. Softmax cho ra class probability cuối cùng.

> 💡 🎯 Ghi nhớ: CNN biến đổi pixel thô thành feature có ý nghĩa, giúp mô hình tập trung vào <b>"CÁI GÌ"</b> quan trọng, chứ không phải <b>"Ở ĐÂU"</b>.

---

### 11. Recurrent Neural Networks (RNN) — Công thức, Vanishing Gradient

> 🖼️ Dán ảnh: `1310_recurrent-neural-networks-rnn-cong-thuc-vanishing-.jpg`

RNN được thiết kế để xử lý **dữ liệu tuần tự** bằng cách duy trì hidden state (bộ nhớ) lưu lại thông tin từ các bước thời gian trước đó.

**Tại sao dùng RNN?** Xử lý chuỗi độ dài bất kỳ; nắm bắt temporal dependencies; chia sẻ tham số theo thời gian; lý tưởng cho text, speech & time series.

> 💡 Mục tiêu: Xử lý chuỗi độ dài bất kỳ bằng cách ghi nhớ những gì đã xảy ra trước đó.

#### 11.1. Recurrent Neural Network (dạng Unfold)

Ở dạng **Compact Form**, một ô $h$ nhận input $x_t$, tự nối vòng (loop) lại chính nó, và cho output $y_t$. Khi **unfold (trải ra)** theo thời gian, ta thấy chuỗi $h_0 \to h_1 \to h_2 \to ... \to h_t$, mỗi bước nhận input tương ứng $x_0, x_1, x_2, ..., x_t$ và cho output $y_0, y_1, y_2, ..., y_t$ — hidden state được truyền từ bước này sang bước kế tiếp.

#### 11.2. Công thức RNN

$$h_t = f(W_{hx}x_t + W_{hh}h_{t-1} + b_h)$$

$$y_t = g(W_{yh}h_t + b_y)$$

- $h_t$ = hidden state tại thời điểm $t$

- $x_t$ = input tại thời điểm $t$

- $y_t$ = output tại thời điểm $t$

- $W_{hx}, W_{hh}, W_{yh}$ = ma trận weight

- $b_h, b_y$ = vector bias

- $f, g$ = activation function (tanh, ReLU, softmax)

#### 11.3. Các loại output của RNN

1. **One-to-One** (Image Classification): Single input, single output.

2. **One-to-Many** (Image Captioning): Single input, multiple outputs.

3. **Many-to-One** (Sentiment Analysis): Multiple inputs, single output.

#### 11.4. Output Many-to-Many

- a) **Đồng bộ** (POS Tagging): Input và output sequence có cùng độ dài.

- b) **Encoder-Decoder** (Machine Translation): Input và output sequence có thể khác độ dài.

#### 11.5. Activation Function trong RNN

- **tanh**: Range (-1,1) — thường dùng nhất trong RNN.

- **ReLU**: Range [0,∞) — training nhanh hơn nhưng có thể kém ổn định.

- **sigmoid**: Range (0,1) — hữu ích cho gate và output.

#### 11.6. Vanishing & Exploding Gradients

- **Vanishing Gradients**: Gradient trở nên quá nhỏ khi lan truyền ngược qua nhiều bước thời gian (mô hình quên thông tin dài hạn).

- **Exploding Gradients**: Gradient trở nên quá lớn khi lan truyền ngược (mô hình trở nên không ổn định).

**Giải pháp:** Dùng LSTM/GRU, Gradient Clipping, khởi tạo hợp lý (weight initialization), Layer Normalization.

#### 11.7. So sánh các biến thể RNN

| Model | Ý tưởng chính | Long-term Dependencies? | Tốt nhất trong |
| --- | --- | --- | --- |
| RNN | Kết nối đệ quy cơ bản | Không (Vanishing) | Chuỗi ngắn |
| LSTM | Dùng gate (input, forget, output) | Có | Chuỗi dài, NLP, Time series |
| GRU | LSTM đơn giản hoá (update, reset) | Có | Ứng dụng real-time, Chatbot |
| BiRNN | Xử lý chuỗi theo cả 2 chiều | Có | Speech, NER, Text understanding |

**TÓM TẮT:**

- RNN xử lý dữ liệu tuần tự bằng hidden state.

- Chúng gặp vấn đề vanishing/exploding gradient.

- LSTM và GRU giải quyết vấn đề long-term dependency.

- Chọn architecture phù hợp với dữ liệu & bài toán.

- Architecture tốt hơn → Hiệu suất tốt hơn.

> 💡 Điểm mấu chốt: RNN ghi nhớ quá khứ để dự đoán tương lai. Hiểu về sequence chính là chìa khoá để giải quyết các bài toán thực tế. ☆
