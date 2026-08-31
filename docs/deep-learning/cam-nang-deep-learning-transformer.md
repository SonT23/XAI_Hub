# Cẩm nang Deep Learning: Transformer

> 🖼️ **6 ảnh gốc cho trang này (dán theo đúng thứ tự vào từng mục bên dưới):**
> 1311_transformer-self-attention-multi-head-attention.jpg
>
> 1312_transformer-decoded-kien-truc-encoder-decoder-chi-.jpg
>
> 1313_transformer-chuyen-sau-masked-attention-positional.jpg
>
> 1314_training-transformer-next-token-prediction-loss-op.jpg
>
> 1315_ung-dung-thuc-te-cua-transformer-trong-nlp-cv-spee.jpg
>
> 1316_tom-tat-nhanh-toan-bo-kien-thuc-transformer.jpg
>

> Ghi chú: Đây là phần tiếp nối bộ **cẩm nang Deep Learning** (bài 11–16, tiếp theo các chủ đề trước đó như CNN/RNN). Vì Transformer là **backbone** của phần lớn kiến trúc CBM (Concept Bottleneck Model) hiện đại (ví dụ dùng ViT/CLIP làm encoder trích concept), cần nắm chắc công thức attention gốc.

### 1. Transformer: Self-Attention & Multi-Head Attention (Trang 11)

> 🖼️ Dán ảnh: `1311_transformer-self-attention-multi-head-attention.jpg`

Transformer ("Attention Is All You Need") dùng cơ chế **self-attention** để hiểu mối quan hệ giữa **tất cả** các từ trong một chuỗi cùng lúc, thay vì xử lý tuần tự như RNN.

> ⭐ Mục tiêu: Nắm bắt long-range dependencies hiệu quả và cho phép training song song.

**Tại sao dùng Transformer?**

- Nắm bắt global context (mọi token "nhìn thấy" mọi token khác)

- Highly parallelizable (không phụ thuộc tuần tự như RNN)

- Tốt hơn cho chuỗi dài (long sequences)

- State-of-the-art trong NLP & nhiều lĩnh vực khác

#### 1.1 Bức tranh tổng thể

Luồng xử lý: **Input Tokens → Token Embedding (+ Positional Encoding) → Encoder Stack (N layers) → Decoder Stack (N layers) → Linear + Softmax → Output Probabilities**

- Encoder: hiểu input (context representation).

- Decoder: sinh output (auto-regressive – sinh từng token dựa trên các token đã sinh trước đó).

#### 1.2 Cơ chế Self-Attention

Mỗi từ nhìn vào **mọi** từ khác (kể cả chính nó) và quyết định mức độ chú ý (attention weight) cần dành cho từng từ đó, để tạo ra một biểu diễn (output) mới chứa thông tin ngữ cảnh.

Với mỗi token, ta tạo 3 vector chiếu (projection) từ embedding X: **Q (Query)**, **K (Key)**, **V (Value)**, rồi tính **Attention Scores** để ra **Output Z**.

$$\text{Attention}(Q,K,V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$

- $Q$ = Query ("tôi đang tìm gì")

- $K$ = Key ("tôi có thông tin gì để so khớp")

- $V$ = Value ("nội dung thực sự mang đi nếu được chọn")

- $d_k$ = số chiều của key (dùng để scale, tránh gradient quá nhỏ)

> 💡 Giải thích thêm: $QK^T$ đo độ "khớp" (similarity) giữa Query của token này với Key của tất cả token khác. Softmax biến điểm số đó thành trọng số xác suất (tổng = 1), rồi nhân với $V$ để lấy trung bình có trọng số các Value — chính là "mức độ chú ý" mà token dành cho các token khác.

#### 1.3 Multi-Head Attention

Thay vì dùng một attention duy nhất, ta dùng **nhiều head** để mô hình có thể tập trung vào các loại quan hệ khác nhau (ví dụ: head này học quan hệ cú pháp, head khác học quan hệ ngữ nghĩa).

Luồng: **X → (Head 1, Head 2, ..., Head h) → Concat → Linear → Output**

$$\text{MultiHead}(Q,K,V) = \text{Concat}(\text{head}_1, ..., \text{head}_h)W^O$$

$$\text{head}_i = \text{Attention}(QW_i^Q,\ KW_i^K,\ VW_i^V)$$

Mỗi head có bộ trọng số chiếu riêng ($W_i^Q, W_i^K, W_i^V$), kết quả các head được nối lại (concat) rồi qua một lớp Linear ($W^O$) để về đúng chiều mô hình ban đầu.

#### 1.4 Position-wise Feed Forward Network (FFN)

Sau attention, một mạng fully-connected đơn giản được áp dụng cho **mỗi vị trí một cách độc lập** (cùng trọng số cho mọi vị trí).

Luồng: **Input (from MHA) → Linear (d → dff) → ReLU → Linear (dff → d) → Output (same length)**

> 💡 Thêm phi tuyến tính (non-linearity) và giúp mô hình học các pattern phức tạp hơn.

#### 1.5 Encoder Layer (lặp lại N lần)

Input → Multi-Head Self-Attention → Add & Norm → Feed Forward Network → Add & Norm → Output

> 💡 Add & Norm = Residual Connection + Layer Normalization

#### 1.6 Decoder Layer (lặp lại N lần)

Input → Masked Multi-Head Self-Attention → Add & Norm → Multi-Head Cross-Attention (với Encoder Output) → Add & Norm → Feed Forward → Add & Norm

> 💡 Masked Self-Attention ngăn không cho nhìn thấy token tương lai (chỉ nhìn được token đã sinh trước đó). Cross-Attention giúp decoder tập trung vào encoder output (Query từ decoder, Key/Value từ encoder).

#### 1.7 Positional Encoding

Vì Transformer không có recurrence (không xử lý tuần tự), ta phải **thêm thông tin vị trí** vào embedding để mô hình biết thứ tự token.

**1. Sinusoidal Encoding (bản gốc, cố định):**

$$PE_{(pos,2i)} = \sin\left(\frac{pos}{10000^{2i/d}}\right)$$

$$PE_{(pos,2i+1)} = \cos\left(\frac{pos}{10000^{2i/d}}\right)$$

- $pos$ = vị trí token trong chuỗi; $i$ = chỉ số chiều; $d$ = số chiều embedding.

**2. Learned Embedding (Trainable):** một vector học được (learnable) được cộng trực tiếp vào token embedding.

Ví dụ bảng giá trị PE minh hoạ:

<table header-row="true"><tr><td>Pos</td><td>PE₀</td><td>PE₁</td><td>PE₂</td><td>PE₃</td></tr><tr><td>0</td><td>0.00</td><td>1.00</td><td>0.00</td><td>1.00</td></tr><tr><td>1</td><td>0.84</td><td>0.54</td><td>0.01</td><td>1.00</td></tr><tr><td>2</td><td>0.91</td><td>-0.42</td><td>0.02</td><td>1.00</td></tr></table>

Positional Encoding được **cộng vào** Token Embedding (không phải nối/concat).

#### 1.8 Transformer vs RNN

<table header-row="true"><tr><td>Khía cạnh</td><td>RNN</td><td>Transformer</td></tr><tr><td>Dependency</td><td>Tuần tự</td><td>Toàn cục (đồng thời)</td></tr><tr><td>Training</td><td>Khó song song hoá</td><td>Song song hoá cao</td></tr><tr><td>Chuỗi dài</td><td>Gặp khó khăn</td><td>Xử lý tốt với attention</td></tr></table>

> **Điểm mấu chốt:** Transformer dùng self-attention để nắm bắt global context. Multi-head attention cho phép mô hình tập trung vào các khía cạnh khác nhau.

---

### 2. Transformer Decoded: Kiến trúc Encoder–Decoder chi tiết (Trang 12)

> 🖼️ Dán ảnh: `1312_transformer-decoded-kien-truc-encoder-decoder-chi-.jpg`

Transformer được xây dựng từ 3 thành phần cốt lõi: **attention**, **nhận biết vị trí (position awareness)**, và **feed forward layer** để hiểu và sinh ra chuỗi.

> ⭐ Mục tiêu: Xây dựng mô hình hiểu context và mối quan hệ ở quy mô lớn.

**Tại sao dùng Transformer?**

- Nắm bắt long-range dependencies

- Xử lý song song (training nhanh hơn)

- Hiệu quả hơn RNN

- Backbone của các mô hình NLP hiện đại

#### 2.1 Tổng quan kiến trúc Transformer

Input (Source Sequence) → Token Embedding + Positional Encoding → **Encoder Stack (N layers)** → **Decoder Stack (N layers)** (nhận thêm Target Sequence đã shifted right) → Linear → Softmax → Output Probabilities (Next Token).

Chú thích màu: Input/Output, Embedding, Encoder, Decoder, Prediction (các khối được tô màu khác nhau theo vai trò trong ảnh gốc).

#### 2.2 Scaled Dot-Product Attention

Cho Query (Q), Key (K), Value (V):

$$\text{Attention}(Q,K,V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$

- $Q$ = ma trận Query, $K$ = ma trận Key, $V$ = ma trận Value, $d_k$ = số chiều của key.

> 💡 **Tại sao scale bởi **$\sqrt{d_k}$**?** Để tránh dot product có giá trị lớn đẩy softmax vào vùng gradient cực nhỏ (vanishing gradient), giúp việc học ổn định hơn.

#### 2.3 Multi-Head Attention

Input (X) → (Head 1, Head 2, ..., Head h) → Concat → Linear → Output

$$\text{MultiHead}(Q,K,V) = \text{Concat}(\text{head}_1,...,\text{head}_h)W^O$$

$$\text{head}_i = \text{Attention}(QW_i^Q, KW_i^K, VW_i^V)$$

#### 2.4 Positional Encoding

Vì Transformer không có recurrence, positional encoding thêm thông tin về vị trí token.

Hai loại phổ biến:

1. **Sinusoidal (Gốc):**

$$PE_{(pos,2i)} = \sin\left(\frac{pos}{10000^{2i/d}}\right),\quad PE_{(pos,2i+1)} = \cos\left(\frac{pos}{10000^{2i/d}}\right)$$

1. **Learned (Trainable):** một vector học được được cộng vào token embedding.

Bảng giá trị ví dụ:

<table header-row="true"><tr><td>Pos</td><td>PE₁</td><td>PE₂</td><td>PE₃</td></tr><tr><td>0</td><td>0.00</td><td>1.00</td><td>0.02</td></tr><tr><td>1</td><td>0.84</td><td>0.54</td><td>0.99</td></tr><tr><td>2</td><td>0.91</td><td>-0.42</td><td>-0.07</td></tr></table>

#### 2.5 Feed Forward Network (FFN)

Áp dụng theo từng vị trí (position-wise) và **giống nhau cho mọi vị trí**.

Input (from Attention) → Linear($d \to d_{ff}$) → ReLU → Linear($d_{ff} \to d$) → Output (same length)

Kích thước tiêu biểu: $d_{model}$ = 512/768/1024; $d_{ff}$ = 2048/3072/4096 (≈ 4× $d_{model}$).

#### 2.6 Layer Normalization & Residual

$$\text{Output} = \text{LayerNorm}(X + \text{Sublayer}(X))$$

- Residual connection giúp gradient lan truyền tốt hơn (chống vanishing gradient khi mạng sâu).

- LayerNorm ổn định training và tăng tốc hội tụ.

#### 2.7 Encoder vs Decoder Layer

**Encoder Layer:** Input → Multi-Head Self-Attention → Add & Norm → Feed Forward → Add & Norm

**Decoder Layer:** Input → Masked Multi-Head Self-Attention → Add & Norm → Multi-Head Cross-Attention (với Encoder Output) → Add & Norm → Feed Forward → Add & Norm

> 💡 Encoder dùng self-attention để hiểu context bên trong input. Decoder có 2 khối attention: (1) Masked self-attention (ngăn nhìn trước tương lai), (2) Cross-attention (tập trung vào encoder output — Query lấy từ decoder, Key/Value lấy từ encoder).

#### 2.8 Độ phức tạp mô hình (mỗi layer)

<table header-row="true"><tr><td>Component</td><td>Time Complexity</td><td>Space Complexity</td></tr><tr><td>Self-Attention</td><td>O(n²d)</td><td>O(n²)</td></tr><tr><td>Cross-Attention</td><td>O(nmd)</td><td>O(nm)</td></tr><tr><td>Feed Forward</td><td>O(n·d·dff)</td><td>O(n·dff)</td></tr></table>

Trong đó: $n$ = độ dài chuỗi, $d$ = model dim, $d_{ff}$ = feed-forward dim, $m$ = độ dài encoder output.

#### 2.9 Ứng dụng phổ biến

Language Translation, Text Summarization, Search & QA Systems, Speech Recognition, Image Captioning.

---

### 3. Transformer In Depth: Masked Attention & Positional Encoding (Trang 13)

> 🖼️ Dán ảnh: `1313_transformer-chuyen-sau-masked-attention-positional.jpg`

Transformer là **backbone** của NLP hiện đại.

> ⭐ Mục tiêu: Hiểu sâu cách Transformer hoạt động, tại sao chúng hiệu quả và được dùng ở đâu.

**Tại sao Transformer thống trị?**

- Nắm bắt long-range dependencies

- Song song hoá (training nhanh hơn)

- Mở rộng cho model & dataset khổng lồ

- State-of-the-art trong NLP, CV, Speech & hơn thế

#### 3.1 Khối Transformer (Encoder)

Input Tokens → Token Embedding + Positional Encoding → [lặp N lần: **Multi-Head Self-Attention → Add & Norm → Feed Forward Network → Add & Norm**] → Output (Encoder Representation)

Thành phần (Components):

1. Multi-Head Self-Attention

2. Add & Norm (Residual + LayerNorm)

3. Feed Forward Network (FFN)

4. Add & Norm

#### 3.2 Khối Transformer (Decoder)

Token Embedding (Output Tokens, shifted right) → [lặp N lần: **Masked Multi-Head Self-Attn → Add & Norm → Multi-Head Cross-Attention → Add & Norm → Feed Forward Network → Add & Norm**] → Linear → Softmax → Output Probabilities

Thành phần (Components):

1. Masked Multi-Head Self-Attn

2. Add & Norm

3. Cross-Attention

4. Add & Norm

5. Feed Forward Network

6. Add & Norm

#### 3.3 Scaled Dot-Product Attention

Input: Q (query), K (key), V (value)

$$\text{Attention}(Q,K,V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$

**Tại sao scale bởi **$\sqrt{d_k}$**?**

- Tránh softmax bị gradient rất nhỏ.

- Giúp training ổn định & hiệu quả.

**Ví dụ minh hoạ:**

$Q=[[1,0],[0,1]]$, $K=[[1,1],[0,1]]$, $V=[[1,2],[3,4]]$, $d_k=2$

> 💡 Với ví dụ trên: $QK^T\)$ tính độ khớp giữa mỗi hàng Query và hàng Key, chia cho $\sqrt{2}$, rồi softmax theo hàng để ra trọng số, cuối cùng nhân với $V$ để lấy tổng có trọng số — cho ra vector Attention output tương ứng cho mỗi Query.

#### 3.4 Multi-Head Attention

Input → h heads chạy Scaled Dot-Product Attention song song → Concat → Linear → Output

> 💡 Multi-head attention cho phép mô hình nắm bắt thông tin từ nhiều representation subspace khác nhau tại nhiều vị trí khác nhau (mỗi head "nhìn" theo một góc quan hệ khác nhau).

#### 3.5 Positional Encoding

Vì Transformer không có recurrence, ta thêm thông tin vị trí. Hai loại: (1) Sinusoidal (cố định), (2) Learned (trainable).

$$PE_{(pos,2i)} = \sin\left(\frac{pos}{10000^{2i/d}}\right),\quad PE_{(pos,2i+1)} = \cos\left(\frac{pos}{10000^{2i/d}}\right)$$

Được cộng vào token embedding.

#### 3.6 Masked Multi-Head Self-Attention

Trong decoder, ta **che (mask)** các token tương lai để ngăn "nhìn trộm" (prevent looking ahead) khi dự đoán token hiện tại — đảm bảo tính auto-regressive.

Ma trận mask minh hoạ (1 = nhìn thấy được / visible, 0 = bị che / masked):

<table header-row="true"><tr><td></td><td>0</td><td>1</td><td>2</td><td>3</td></tr><tr><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td></tr><tr><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td></tr><tr><td>2</td><td>1</td><td>1</td><td>1</td><td>0</td></tr><tr><td>3</td><td>1</td><td>1</td><td>1</td><td>1</td></tr></table>

Đây chính là ma trận tam giác dưới (lower-triangular / look-ahead mask): tại vị trí $i$ chỉ được attend tới các vị trí $j \le i$.

#### 3.7 Lợi ích của Transformer

- **Song song hoá:** Training nhanh hơn nhiều so với RNN.

- **Long-range Dependencies:** Attention có thể kết nối các từ ở xa nhau trực tiếp (không qua nhiều bước trung gian như RNN).

- **Scalability:** Mở rộng tốt cho model & dataset lớn.

#### 3.8 Ứng dụng thực tế

ChatGPT (Conversational AI), Google Translate (Language Translation), BERT (Search & QA).

#### 3.9 Tóm tắt

- Transformer dùng attention, không dùng recurrence.

- Self-attention nắm bắt mối quan hệ trong chuỗi.

- Positional Encoding thêm thông tin thứ tự.

- Multi-head attention tập trung vào nhiều phần khác nhau.

---

### 4. Training Transformer: Next-token Prediction, Loss & Optimizer (Trang 14)

> 🖼️ Dán ảnh: `1314_training-transformer-next-token-prediction-loss-op.jpg`

Training một Transformer nghĩa là dạy nó dự đoán **next token** bằng cách giảm thiểu sai số giữa token dự đoán và token thực tế.

> ⭐ Mục tiêu: Giảm thiểu sai số dự đoán để mô hình học pattern, hiểu context và tổng quát hoá với dữ liệu mới.

**Tại sao Training quan trọng?**

- Học pattern từ dữ liệu text khổng lồ

- Cải thiện hiểu context & semantics

- Dự đoán next-token chính xác

- Giúp mô hình tổng quát hoá với dữ liệu mới

- Backbone cho mọi downstream task

#### 4.1 Mục tiêu Training

Transformer được training bằng **Next Token Prediction**.

Ví dụ: Input Tokens = ["The", "cat", "sat", "on", "the"] → Transformer Model → Predicted Next Token = "mat".

Mô hình học bằng cách giảm thiểu độ khác biệt (error) giữa dự đoán và thực tế: So sánh với Actual Next Token ("mat") → Tính Loss (Cross-Entropy) → Cập nhật Model Parameters (Backpropagation).

#### 4.2 Quy trình Training

1. **Raw Text** — kho văn bản lớn

2. **Tokenization** — chuyển text thành token

3. **Input Sequences** — tạo chuỗi độ dài cố định

4. **Transformer** — xử lý & dự đoán next token

5. **Loss & Update** — tính loss, lan truyền & cập nhật weights

> 💡 **Training Loop (lặp lại nhiều lần):** Forward Pass → Compute Loss → Backpropagation → Update Weights.

#### 4.3 Loss Function (Cross-Entropy)

Cross-entropy đo lường sự khác biệt giữa phân phối xác suất dự đoán và next token thực tế.

$$\text{Loss} = -\sum_{i} y_i \log(\hat{y}_i)$$

- $V$ = kích thước vocabulary, $y_i$ = xác suất thực (one-hot), $\hat{y}_i$ = xác suất dự đoán.

> 💡 **Trực giác:** Loss thấp → mô hình tự tin & đúng. Loss cao → mô hình sai hoặc không chắc chắn.

#### 4.4 Optimization

<table header-row="true"><tr><td>Optimizer</td><td>Mô tả</td></tr><tr><td>Adam</td><td>Learning rate thích ứng (adaptive)</td></tr><tr><td>AdamW</td><td>Adam + Weight Decay</td></tr><tr><td>SGD + Momentum</td><td>Momentum tăng tốc hội tụ</td></tr></table>

Hyperparameter chính:

- Learning Rate (1e-4)

- Batch Size (32, 64)

- Optimizer (AdamW)

- Weight Decay (0.01)

- Warmup Steps

#### 4.5 Kỹ thuật Regularization

- **Dropout:** Ngẫu nhiên loại bỏ neuron khi training.

- **Weight Decay:** Phạt weight lớn để giảm overfitting.

- **Label Smoothing:** Ngăn mô hình quá tự tin (over-confident).

- **Early Stopping:** Dừng khi validation loss ngừng cải thiện.

#### 4.6 Dữ liệu & Scaling

**Yêu cầu dữ liệu:** Lượng lớn text (GB đến TB), miễn đa dạng, chất lượng cao quan trọng hơn số lượng.

**Scaling Laws:** Data nhiều hơn / Model lớn hơn / Compute nhiều hơn → Loss thấp hơn (nhưng lợi ích giảm dần — diminishing returns).

#### 4.7 Training quy mô lớn

- **Distributed Training:** Dùng nhiều GPU/TPU.

- **Data Parallelism:** Cùng model, khác data shard.

- **Model Parallelism:** Chia model qua nhiều thiết bị.

- **Mixed Precision:** Dùng FP16/BF16 để training nhanh & tốn ít bộ nhớ hơn.

#### 4.8 Đánh giá trong quá trình Training

**Metrics:** Training Loss, Validation Loss, Perplexity (PPL), Accuracy (cho task cụ thể).

Ghi chú biểu đồ: Training loss giảm dần đều; Validation loss giảm rồi tăng trở lại sau một điểm (dấu hiệu overfitting) — điểm tốt nhất để dừng là **Best Model (Early Stopping)**, trước khi validation loss tăng trở lại.

#### 4.9 Thách thức thường gặp khi Training

<table header-row="true"><tr><td>Thách thức</td><td>Tại sao xảy ra</td><td>Giải pháp</td></tr><tr><td>Overfitting</td><td>Mô hình học thuộc training data</td><td>Thêm data, regularization, early stopping</td></tr><tr><td>Underfitting</td><td>Model quá nhỏ hoặc training chưa đủ</td><td>Model lớn hơn, training nhiều hơn</td></tr><tr><td>Vanishing/Exploding Gradients</td><td>Khởi tạo sai hoặc model quá sâu</td><td>LayerNorm, Residual, khởi tạo tốt</td></tr><tr><td>Training chậm</td><td>Model lớn, compute hạn chế</td><td>Hardware tốt hơn, optimization, mixed precision</td></tr><tr><td>Dùng nhiều bộ nhớ</td><td>Batch lớn, chuỗi dài</td><td>Gradient checkpointing, batch nhỏ hơn, attention hiệu quả</td></tr></table>

> 💡 **Điểm mấu chốt:** Training Transformer tốt là sự kết hợp giữa dữ liệu chất lượng, kiến trúc phù hợp và tinh chỉnh optimization cẩn thận.

---

### 5. Ứng dụng thực tế của Transformer trong NLP/CV/Speech (Trang 15)

> 🖼️ Dán ảnh: `1315_ung-dung-thuc-te-cua-transformer-trong-nlp-cv-spee.jpg`

Transformer được dùng **ở khắp mọi nơi**! Sau đây là cách chúng vận hành các hệ thống AI hiện đại.

**Tại sao dùng Transformer?**

- Xử lý long-range dependencies

- Hiểu context & ý nghĩa

- Hoạt động tốt với dữ liệu quy mô lớn

- Thích ứng với nhiều task & domain

- Không ngừng cải tiến qua nghiên cứu

#### 5.1 Natural Language Processing (NLP)

<table header-row="true"><tr><td>Ứng dụng</td><td>Mô hình ví dụ</td><td>Transformer làm gì</td></tr><tr><td>Machine Translation</td><td>Google Translate, DeepL, mBERT</td><td>Dịch văn bản từ ngôn ngữ này sang ngôn ngữ khác</td></tr><tr><td>Text Summarization</td><td>BART, T5, PEGASUS</td><td>Tóm tắt bài viết hoặc tài liệu dài</td></tr><tr><td>Question Answering</td><td>BERT, RoBERTa, ALBERT</td><td>Tìm câu trả lời chính xác từ đoạn văn dài</td></tr><tr><td>Sentiment Analysis</td><td>BERT, DistilBERT, XLNet</td><td>Hiểu cảm xúc tích cực, tiêu cực hoặc trung lập</td></tr><tr><td>Text Generation</td><td>GPT, LLaMA, PaLM</td><td>Sinh văn bản giống người, hiểu context</td></tr></table>

#### 5.2 Computer Vision (CV)

<table header-row="true"><tr><td>Ứng dụng</td><td>Mô hình ví dụ</td><td>Transformer làm gì</td></tr><tr><td>Image Classification</td><td>ViT, DeiT, Swin Transformer</td><td>Phân loại hình ảnh với độ chính xác cao</td></tr><tr><td>Object Detection</td><td>DETR, Deformable DETR</td><td>Phát hiện và định vị object trong ảnh</td></tr><tr><td>Image Segmentation</td><td>SegFormer, Swin-UNet</td><td>Hiểu ảnh ở cấp độ pixel</td></tr><tr><td>Video Understanding</td><td>Video Transformer, TimeSformer</td><td>Hiểu hành động và sự kiện trong video</td></tr><tr><td>Medical Imaging</td><td>Swin Transformer, TransUNet</td><td>Phân tích X-ray, MRI, CT scan để chẩn đoán</td></tr></table>

#### 5.3 Speech & Audio

<table header-row="true"><tr><td>Ứng dụng</td><td>Mô hình ví dụ</td><td>Transformer làm gì</td></tr><tr><td>Speech Recognition</td><td>Whisper, Wav2Vec 2.0, Conformer</td><td>Chuyển giọng nói thành văn bản chính xác</td></tr><tr><td>Text-to-Speech</td><td>FastSpeech 2, VITS</td><td>Sinh giọng nói tự nhiên từ văn bản</td></tr><tr><td>Speech Translation</td><td>SeamlessM4T, SpeechT5</td><td>Dịch giọng nói giữa các ngôn ngữ khác nhau</td></tr><tr><td>Speaker Recognition</td><td>ECAPA-TDNN + Transformers</td><td>Nhận diện và xác minh người nói</td></tr></table>

#### 5.4 Recommendation Systems

<table header-row="true"><tr><td>Ứng dụng</td><td>Mô hình ví dụ</td><td>Transformer làm gì</td></tr><tr><td>Product Recommendation</td><td>SASRec, BERT4Rec, CoRel</td><td>Gợi ý sản phẩm dựa trên hành vi người dùng</td></tr><tr><td>Content Recommendation</td><td>YouTube DNN, TransNet</td><td>Đề xuất video, bài viết hoặc nội dung</td></tr><tr><td>Personalized Search</td><td>BERT, TFRS</td><td>Xếp hạng kết quả theo intent người dùng</td></tr><tr><td>News Feed Ranking</td><td>Transformer Ranker, DeepRec</td><td>Xếp hạng và hiển thị bài viết liên quan nhất</td></tr></table>

#### 5.5 Ứng dụng đa phương thức (Multi-modal)

<table header-row="true"><tr><td>Ứng dụng</td><td>Mô hình ví dụ</td><td>Transformer làm gì</td></tr><tr><td>Image + Text Understanding</td><td>CLIP, ViLT, BLIP-2</td><td>Hiểu cả hình ảnh và văn bản cùng lúc</td></tr><tr><td>Visual QA (VQA)</td><td>LLaVA, ViLT, BLIP</td><td>Trả lời câu hỏi về hình ảnh</td></tr><tr><td>Document AI</td><td>LayoutLM, Donut, DocFormer</td><td>Trích xuất thông tin từ tài liệu scan, form, hoá đơn</td></tr><tr><td>Code + Text Understanding</td><td>CodeBERT, PLBART, StarCoder</td><td>Hiểu và sinh code kèm ngôn ngữ tự nhiên</td></tr></table>

> 💡 Ghi chú cho CBM: CLIP (Image+Text, dòng đầu bảng trên) là ví dụ tiêu biểu của encoder Transformer đa phương thức, thường được dùng làm backbone trích "concept" trong các mô hình Concept Bottleneck (CBM) hiện đại (concept dưới dạng embedding văn bản/hình ảnh có thể diễn giải).

#### 5.6 Ứng dụng mới nổi khác

<table header-row="true"><tr><td>Ứng dụng</td><td>Mô hình ví dụ</td><td>Transformer làm gì</td></tr><tr><td>Scientific Research</td><td>SciBERT, Galactica, BioGPT</td><td>Phân tích paper, sinh giả thuyết, tóm tắt</td></tr><tr><td>Finance</td><td>FinBERT, Longformer, BloombergGPT</td><td>Phân tích tin tức thị trường, dự đoán xu hướng</td></tr><tr><td>Robotics</td><td>RT-1, PaLM-E, Perceiver IO</td><td>Hiểu môi trường và lên kế hoạch hành động</td></tr><tr><td>Healthcare NLP</td><td>BioBERT, ClinicalBERT, Med-PaLM</td><td>Phân tích hồ sơ y tế, dự đoán kết quả sức khoẻ</td></tr></table>

#### 5.7 Tại sao Transformer hoạt động tốt?

- Self-attention nắm bắt mọi mối quan hệ trong dữ liệu

- Song song hoá → training nhanh hơn trên phần cứng hiện đại

- Mở rộng tốt cho model & dataset khổng lồ

- Transfer learning giúp chúng thích ứng với nhiều task

- Kết quả state-of-the-art ở hầu hết mọi domain

#### 5.8 Thách thức & giới hạn

- Chi phí tính toán cao (training tốn kém)

- Cần lượng lớn dữ liệu

- Tốn nhiều bộ nhớ cho chuỗi dài

- Có thể sinh output thiên vị hoặc sai lệch

- Không phải lúc nào cũng dễ diễn giải (black box) — **đây chính là động lực chính cho các nghiên cứu Explainable AI/CBM**

#### 5.9 Tương lai

- Mô hình hiệu quả hơn (nhỏ hơn, nhanh hơn, xanh hơn)

- Hiểu long-context tốt hơn

- Tích hợp multi-modal mạnh mẽ hơn

- AI cá nhân hoá cho mọi người

- Transformer + Reasoning = tiềm năng AGI

> 🌟 **15.10 Tóm tắt:** Dù ở đâu có dữ liệu, Transformer đều có thể giúp ích!

---

### 6. Tóm tắt nhanh toàn bộ kiến thức Transformer (Trang 16)

> 🖼️ Dán ảnh: `1316_tom-tat-nhanh-toan-bo-kien-thuc-transformer.jpg`

> 💡 **Ghi nhớ:** Attention is all you need.

#### 6.1 Transformer là gì?

Transformer là một mô hình deep learning dựa trên cơ chế **self-attention** để hiểu mối quan hệ giữa tất cả các từ trong một chuỗi cùng lúc.

> 🎯 Mục tiêu: Nắm bắt long-range dependencies hiệu quả và cho phép training song song.

#### 6.2 Ý tưởng cốt lõi

Input (Tokens) → Transformer (Encoder/Decoder) → Output (Probabilities)

#### 6.3 Công thức chính — Scaled Dot-Product Attention

$$\text{Attention}(Q,K,V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$

$Q$ = ma trận Query, $K$ = ma trận Key, $V$ = ma trận Value, $d_k$ = số chiều của key.

**Mục đích:** Đo lường mức độ tập trung cần dành từ Query đến các Key khác nhau.

#### 6.4 Tổng quan kiến trúc

**ENCODER (N layers):** Input Embedding (+Positional Encoding) → Multi-Head Self-Attention → Add & Norm → Feed Forward Network → Add & Norm

**DECODER (N layers):** Output Embedding (Shifted Right) → Masked Multi-Head Self-Attention → Add & Norm → Multi-Head Cross-Attention → Add & Norm → Feed Forward → Add & Norm

#### 6.5 Các biến thể Attention

a) **Scaled Dot-Product Attention:** $\text{Attention}(Q,K,V) = \text{softmax}(QK^T/\sqrt{d_k})V$

Đặc điểm: No recurrence (không dùng RNN), song song hoá hoàn toàn, nắm bắt global context.

b) **Multi-Head Attention:** $\text{MultiHead}(Q,K,V) = \text{Concat}(\text{head}_1,...,\text{head}_h)W^O$, với $\text{head}_i = \text{Attention}(QW_i^Q, KW_i^K, VW_i^V)$

c) **Masked Multi-Head Self-Attention (trong Decoder):** Look-ahead mask ngăn attend đến token tương lai.

#### 6.6 Positional Encoding

a) **Sinusoidal (Gốc):**

$$PE_{(pos,2i)} = \sin\left(\frac{pos}{10000^{2i/d}}\right),\quad PE_{(pos,2i+1)} = \cos\left(\frac{pos}{10000^{2i/d}}\right)$$

<table header-row="true"><tr><td>Pos</td><td>PE₀</td><td>PE₁</td><td>PE₂</td><td>PE₃</td></tr><tr><td>0</td><td>0.00</td><td>1.00</td><td>0.00</td><td>1.00</td></tr><tr><td>1</td><td>0.84</td><td>0.54</td><td>0.01</td><td>1.00</td></tr></table>

b) **Learned (Trainable):** Một vector học được được cộng vào token embedding.

**Tại sao dùng Positional Encoding?** Thêm thông tin thứ tự; giúp hiểu sequence; tổng quát hoá với chuỗi dài hơn.

#### 6.7 Feed Forward Network

Áp dụng theo từng vị trí (position-wise) và giống hệt nhau. Input → Linear($d \to d_{ff}$) → ReLU → Linear($d_{ff} \to d$) → Output.

Kích thước: $d_{model}$ = 512/768/1024, $d_{ff}$ = 4× $d_{model}$.

#### 6.8 Layer Normalization & Residual

Input → Sub-layer → (+) cộng residual → LayerNorm → Output

- Residual connection giúp gradient lan truyền tốt.

- LayerNorm ổn định training và tăng tốc hội tụ.

#### 6.9 Độ phức tạp (mỗi layer)

<table header-row="true"><tr><td>Component</td><td>Time</td><td>Space</td></tr><tr><td>Self-Attention</td><td>O(n²d)</td><td>O(n²)</td></tr><tr><td>Cross-Attention</td><td>O(nmd)</td><td>O(nm)</td></tr><tr><td>Feed Forward</td><td>O(n·dff)</td><td>O(n·dff)</td></tr></table>

n=độ dài chuỗi, d=model dim, dff=FFN dim, m=độ dài encoder output.

#### 6.10 Transformer vs RNN

<table header-row="true"><tr><td>Khía cạnh</td><td>RNN</td><td>Transformer</td></tr><tr><td>Dependency</td><td>Tuần tự</td><td>Toàn cục</td></tr><tr><td>Training</td><td>Khó song song</td><td>Song song cao</td></tr><tr><td>Chuỗi dài</td><td>Gặp khó khăn</td><td>Xử lý tốt</td></tr><tr><td>Tốc độ</td><td>Chậm hơn</td><td>Nhanh hơn</td></tr><tr><td>Bộ nhớ</td><td>Cao (trạng thái tuần tự)</td><td>Hiệu quả hơn</td></tr></table>

#### 6.11 Ứng dụng phổ biến

Language Translation, Text Summarization, Question Answering, Code Generation, Speech Recognition, Image Captioning, Recommendation, Search & Ranking, Time Series Forecasting, Scientific Research.

#### 6.12 Training cơ bản

- Loss Function: Cross-Entropy Loss

- Optimizer: Adam / AdamW

- Learning Rate: 1e-4 (warmup + decay)

- Dropout: 0.1 (phổ biến)

- Batch Size: 32/64 (tuỳ GPU)

- Warmup Steps: thường 4000–10000

- Label Smoothing: 0.1 (giúp tổng quát hoá)

- Weight Decay: 0.01 (phổ biến)

#### 6.13 Thách thức & giới hạn

- Chi phí tính toán cao (O(n²) trong attention)

- Cần lượng lớn dữ liệu

- Tốn nhiều bộ nhớ cho chuỗi dài

- Có thể sinh output thiên vị/sai lệch

- Không phải lúc nào cũng dễ diễn giải (black box)

#### 6.14 Tại sao Transformer mạnh?

- Self-attention nắm bắt mọi mối quan hệ

- Hoạt động tốt với dữ liệu quy mô lớn

- Song song hoá → training nhanh hơn

- Transfer learning giúp linh hoạt

- State-of-the-art ở nhiều domain

#### 6.15 Tương lai & xu hướng

- Mô hình hiệu quả hơn (nhỏ, nhanh, xanh)

- Mô hình hiểu long-context tốt hơn

- Tích hợp multi-modal mạnh hơn

- AI cá nhân hoá

- Transformer + Reasoning = tiềm năng AGI

#### 6.16 Công thức tham khảo nhanh

<table header-row="true"><tr><td>Công thức</td><td>Nội dung</td></tr><tr><td>1. Attention</td><td>softmax(QKᵀ/√dₖ)V</td></tr><tr><td>3. Positional Encoding (Sinusoidal)</td><td>sin/cos(pos/10000^(2i/d))</td></tr><tr><td>4. Layer Norm</td><td>(x−μ)/√(σ²+ε)</td></tr><tr><td>Notation</td><td>Q, K, V, dₖ, d_model, d_ff</td></tr></table>

> 💡 Ghi chú công thức Layer Norm: $\text{LayerNorm}(x) = \frac{x-\mu}{\sqrt{\sigma^2+\epsilon}}$, trong đó $\mu$, $\sigma^2$ là trung bình và phương sai tính theo chiều feature, $\epsilon$ là hằng số nhỏ tránh chia cho 0 — công thức này không hiện rõ ở các trang 11–15 nhưng được tóm tắt tại mục 16 (Công thức tham khảo nhanh) của trang 16.
