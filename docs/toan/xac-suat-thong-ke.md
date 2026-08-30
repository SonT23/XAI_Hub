# 3. Xác suất & Thống kê (Probability & Statistics)

> 🎓 **NCKH** / [Toán](../toan/index.md) / **Xác suất & Thống kê**

> 🎯 **Câu hỏi lớn của cả trang:** *Vì sao mô hình AI không bao giờ nói "đây là con mèo" mà luôn nói "78% là con mèo"?*
> Vì **mọi dự đoán đều là một phân phối xác suất**, và **mọi hàm mất mát đều là một thước đo khoảng cách giữa hai phân phối**.
> Ba trang Toán gắn vào nhau như sau: [Đại số tuyến tính](dai-so-tuyen-tinh.md) cho biết AI **tính** thế nào, [Giải tích](giai-tich.md) cho biết AI **học** thế nào, còn trang này cho biết AI **biểu diễn sự không chắc chắn** thế nào.

---

# 1. Biến ngẫu nhiên và phân phối

**Biến ngẫu nhiên** là một đại lượng mà ta chưa biết giá trị, chỉ biết **khả năng nó nhận từng giá trị**. **Phân phối xác suất** là bảng (hoặc đường cong) mô tả các khả năng đó.

| | Rời rạc (Discrete) | Liên tục (Continuous) |
|---|---|---|
| Ví dụ | Mặt xúc xắc, nhãn lớp (mèo/chó/ngựa) | Chiều cao, giá trị pixel, vector latent |
| Hàm mô tả | **PMF** $P(X = x)$ | **PDF** $p(x)$ |
| Tổng bằng 1 | $\sum_x P(x) = 1$ | $\int p(x)\,dx = 1$ |
| Trong AI | Đầu ra của **Softmax** | Phân phối latent của **VAE** |

> ⚠️ **Bẫy của biến liên tục:** với phân phối liên tục, xác suất tại **đúng một điểm luôn bằng 0**. Hỏi "xác suất một người cao đúng 170,000000 cm là bao nhiêu" thì câu trả lời là 0. Chỉ hỏi được xác suất **rơi vào một khoảng**, và tính bằng **tích phân** — đúng thứ đã học ở trang Giải tích.
> Vì vậy $p(x)$ gọi là **mật độ** chứ không phải xác suất, và nó **có thể lớn hơn 1**.

---

# 2. Kỳ vọng, Phương sai, Độ lệch chuẩn

Ba con số tóm tắt mọi phân phối: **tâm nằm ở đâu** và **trải rộng bao nhiêu**.

$$
\mathbb{E}[X] = \sum_x x \cdot P(x), \qquad \text{Var}(X) = \mathbb{E}[X^2] - (\mathbb{E}[X])^2, \qquad \sigma = \sqrt{\text{Var}(X)}
$$

## Ví dụ tính tay: một con xúc xắc

Sáu mặt, mỗi mặt xác suất 1/6.

$$
\mathbb{E}[X] = \frac{1+2+3+4+5+6}{6} = \frac{21}{6} = \mathbf{3.5}
$$

$$
\mathbb{E}[X^2] = \frac{1+4+9+16+25+36}{6} = \frac{91}{6} \approx 15.17
$$

$$
\text{Var}(X) = 15.17 - 3.5^2 = 15.17 - 12.25 = \mathbf{2.92}, \qquad \sigma = \sqrt{2.92} \approx \mathbf{1.71}
$$

> 💡 **Hai điều đáng chú ý:**
> **Kỳ vọng 3.5 là một giá trị không bao giờ xảy ra** — không có mặt nào là 3.5. Kỳ vọng là giá trị trung bình **về lâu dài**, không phải giá trị dễ xảy ra nhất.
> **Độ lệch chuẩn $\sigma \approx 1.71$ cùng đơn vị với dữ liệu**, còn phương sai thì không (nó là "đơn vị bình phương"). Đó là lý do khi nói chuyện ta dùng $\sigma$.
> Đây cũng chính là cặp $\mu, \sigma$ mà Encoder của **VAE** xuất ra.

---

# 3. Phân phối chuẩn (Gaussian / Normal)

Phân phối quan trọng nhất trong toàn bộ ML, ký hiệu $N(\mu, \sigma^2)$.

$$
p(x) = \frac{1}{\sigma\sqrt{2\pi}} \exp\left( -\frac{(x-\mu)^2}{2\sigma^2} \right)
$$

Chỉ cần nhớ phần **bên trong hàm mũ**: $-(x-\mu)^2$ — càng xa tâm $\mu$ thì mật độ càng tụt nhanh theo hàm mũ. Phần phía trước chỉ là hằng số để tổng diện tích bằng đúng 1.

| Khoảng | Chứa bao nhiêu dữ liệu |
|---|---|
| $\mu \pm 1\sigma$ | **68%** |
| $\mu \pm 2\sigma$ | **95%** |
| $\mu \pm 3\sigma$ | **99.7%** |

> 🔔 **Vì sao Gaussian có mặt ở khắp nơi?** Ba lý do:
> **1. Định lý giới hạn trung tâm.** Tổng của nhiều yếu tố ngẫu nhiên độc lập luôn tiến về phân phối chuẩn, bất kể từng yếu tố có phân phối gì.
> **2. Toán rất đẹp.** Tổng hai Gaussian vẫn là Gaussian; KL Divergence giữa hai Gaussian có **dạng đóng** — chính công thức bạn thấy trong hàm Loss của VAE.
> **3. Trong AI cụ thể:** khởi tạo trọng số, nhiễu trong Denoising AE, tiên nghiệm $N(0, I)$ của VAE, nhiễu trong Diffusion Model — tất cả đều là Gaussian.

---

# 4. Xác suất có điều kiện và Định lý Bayes

$$
P(A \mid B) = \frac{P(B \mid A) \, P(A)}{P(B)}
$$

Đọc bằng lời: *"niềm tin của tôi về A sau khi thấy bằng chứng B, bằng niềm tin ban đầu về A, nhân với mức độ B ủng hộ A."*

## Ví dụ tính tay

Một căn bệnh có tỉ lệ mắc **1%** dân số. Có một xét nghiệm: người **có bệnh** thì dương tính **99%**; người **không bệnh** vẫn dương tính **5%** (dương tính giả).

**Bạn xét nghiệm và nhận kết quả dương tính. Xác suất bạn thực sự có bệnh là bao nhiêu?** Hầu hết mọi người đoán khoảng 95%. Hãy tính:

$$
P(+) = 0.99 \times 0.01 + 0.05 \times 0.99 = 0.0099 + 0.0495 = 0.0594
$$

$$
P(\text{bệnh} \mid +) = \frac{0.0099}{0.0594} \approx \mathbf{16.7\%}
$$

> 💡 **Chỉ 16.7%, không phải 95%.**
> Lý do: nhóm không bệnh **đông gấp 99 lần** nhóm có bệnh. Trong 10.000 người, có 99 người bệnh dương tính thật, nhưng có tới **495 người khỏe mạnh bị dương tính giả**. Trong tổng số 594 ca dương tính, chỉ 99 ca là thật.
> **Bài học cho AI:** một mô hình đạt độ chính xác 99% trên lớp hiếm vẫn có thể sai hầu hết các lần nó báo động. Đây là lý do phải nhìn **Precision và Recall** chứ không chỉ nhìn Accuracy, và là lý do các bài toán mất cân bằng lớp (phát hiện gian lận, chẩn đoán bệnh hiếm, phát hiện bất thường) khó hơn vẻ ngoài rất nhiều.

---

# 5. Likelihood, MLE và vì sao Cross-Entropy tồn tại

**Likelihood** đảo ngược câu hỏi của xác suất:

| | Biết trước cái gì | Đi tìm cái gì |
|---|---|---|
| **Xác suất** | Tham số mô hình | Khả năng ra dữ liệu này |
| **Likelihood** | **Dữ liệu đã quan sát** | **Tham số nào giải thích dữ liệu tốt nhất** |

**MLE (Maximum Likelihood Estimation)** là chọn bộ tham số làm cho dữ liệu quan sát được trở nên **khả dĩ nhất**:

$$
\theta^* = \arg\max_\theta \prod_{i=1}^{N} p(x_i \mid \theta) \;\;\Longleftrightarrow\;\; \arg\max_\theta \sum_{i=1}^{N} \log p(x_i \mid \theta)
$$

> 🔑 **Hai mẹo trong dòng công thức trên, cả hai đều quan trọng:**
> **1. Lấy log để biến tích thành tổng.** Nhân 10.000 số nhỏ hơn 1 với nhau sẽ cho kết quả nhỏ tới mức máy tính làm tròn thành 0. Lấy log thì thành phép cộng nên an toàn. Log là hàm đồng biến nên **điểm cực đại không đổi**.
> **2. Đảo dấu để thành bài toán cực tiểu.** Cực đại của log-likelihood chính là cực tiểu của **âm log-likelihood**, và đó **chính xác là hàm Cross-Entropy Loss**.
> Nói cách khác: **`nn.CrossEntropyLoss()` không phải một công thức ai đó nghĩ ra cho tiện — nó là MLE viết lại.** Điều tương tự đúng với MSE: MSE chính là MLE khi ta giả định nhiễu có phân phối Gaussian. Xem thêm **Hàm mất mát Loss Function của Autoencoder**.

---

# 6. Entropy, Cross-Entropy và KL Divergence

Ba khái niệm liên quan chặt với nhau, và cả ba đều xuất hiện trực tiếp trong hàm Loss.

## Entropy — mức độ bất định

$$
H(p) = -\sum_x p(x) \log p(x)
$$

| Tình huống | Entropy | Ý nghĩa |
|---|---|---|
| Đồng xu cân (50/50) | **1 bit** | Bất định tối đa, không đoán được gì |
| Đồng xu lệch (90/10) | **0.47 bit** | Đã đoán được kha khá |
| Đồng xu hai mặt giống nhau | **0 bit** | Không còn bất định nào |

## Cross-Entropy — cái giá phải trả khi dùng sai phân phối

$$
H(p, q) = -\sum_x p(x) \log q(x)
$$

Trong đó $p$ là **sự thật** (nhãn) và $q$ là **dự đoán của mô hình**. Ví dụ nhãn thật là lớp 1, tức $p = [1, 0, 0]$:

| Mô hình dự đoán q | Cross-Entropy | Nhận xét |
|---|---|---|
| $[0.98, 0.01, 0.01]$ | **0.02** | Rất tự tin và đúng, gần như không bị phạt |
| $[0.70, 0.20, 0.10]$ | **0.36** | Đúng nhưng chưa chắc chắn |
| $[0.34, 0.33, 0.33]$ | **1.08** | Đoán mò hoàn toàn |
| $[0.05, 0.90, 0.05]$ | **3.00** | Sai mà còn rất tự tin, bị phạt cực nặng |

> ⚖️ Chỉ có **xác suất mà mô hình gán cho lớp ĐÚNG** là được tính vào Loss, vì các thành phần khác của $p$ đều bằng 0. Mô hình chia bao nhiêu cho các lớp sai không quan trọng bằng việc **nó dám đặt bao nhiêu vào lớp đúng**.

## KL Divergence — độ lệch giữa hai phân phối

$$
D_{KL}(p \,\|\, q) = \sum_x p(x) \log \frac{p(x)}{q(x)} = \underbrace{H(p,q)}_{\text{Cross-Entropy}} - \underbrace{H(p)}_{\text{Entropy}}
$$

> 🔗 **Ba điều phải nhớ về KL:**
> 1. **Luôn lớn hơn hoặc bằng 0**, và bằng 0 **chỉ khi** hai phân phối trùng khớp hoàn toàn.
> 2. **Không đối xứng**, nên nó **không phải một khoảng cách** theo nghĩa toán học, dù ai cũng gọi nó như vậy.
> 3. **Khi nhãn cố định** thì $H(p)$ là hằng số, nên **cực tiểu Cross-Entropy chính là cực tiểu KL**. Đó là lý do hai khái niệm này hay bị dùng lẫn lộn.
> **Đây là thành phần thứ hai trong hàm Loss của VAE** — xem mục 5 của [VAE](../deep-learning/vae.md), nơi KL giữa phân phối latent và $N(0,I)$ được rút gọn thành một công thức đóng.

---

# 7. Xác suất nằm ở đâu trong AI?

| Trong AI | Khái niệm xác suất đứng sau |
|---|---|
| Đầu ra của Softmax | Phân phối rời rạc trên các lớp |
| **Cross-Entropy Loss** | MLE cộng Cross-Entropy |
| **MSE Loss** | MLE với giả định nhiễu Gaussian |
| Encoder của VAE xuất ra hai vector | Phân phối Gaussian nhiều chiều |
| **Thành phần KL trong ELBO** | KL Divergence giữa hai Gaussian |
| Dropout | Phân phối Bernoulli trên từng nơ-ron |
| Khởi tạo trọng số (Xavier, He) | Lấy mẫu từ Gaussian có phương sai được tính trước |
| Diffusion Model | Chuỗi Markov thêm rồi khử nhiễu Gaussian |
| **Calibration trong XAI** | Mô hình nói 80% thì có đúng 80% số lần nó đúng không |
| **Knowledge Limits (nguyên tắc 4 của NIST)** | Ước lượng độ bất định — mô hình biết khi nào mình không biết |

> 🔍 **Hai hàng cuối là phần gắn trực tiếp với đề tài NCKH của bạn.** Một mô hình có thể đạt độ chính xác cao mà vẫn **hiệu chỉnh kém (poorly calibrated)** — luôn báo 99% kể cả khi sai. Với hệ thống cần giải thích được, điều đó nguy hiểm hơn cả việc sai, vì người dùng mất khả năng biết khi nào nên tin.

---

# 8. Bảng thuật ngữ nhanh

| Thuật ngữ | Hiểu trong một câu |
|---|---|
| **Random Variable** | Đại lượng chưa biết giá trị, chỉ biết khả năng nhận từng giá trị |
| **PMF / PDF** | Hàm mô tả phân phối, dành cho biến rời rạc / liên tục |
| **Expectation** | Giá trị trung bình về lâu dài, có trọng số theo xác suất |
| **Variance / Std** | Mức độ trải rộng quanh giá trị trung bình |
| **Gaussian** | Phân phối hình chuông, phân phối quan trọng nhất trong ML |
| **Prior / Posterior** | Niềm tin **trước** và **sau** khi thấy dữ liệu |
| **Likelihood** | Dữ liệu này khả dĩ tới mức nào nếu tham số là như vậy |
| **MLE** | Chọn tham số làm dữ liệu quan sát khả dĩ nhất, nguồn gốc của mọi hàm Loss |
| **Entropy** | Mức độ bất định trong một phân phối |
| **Cross-Entropy** | Cái giá phải trả khi dùng phân phối q để mô tả sự thật p |
| **KL Divergence** | Độ lệch giữa hai phân phối. Không âm, không đối xứng |
| **i.i.d.** | Các mẫu độc lập và cùng phân phối, giả định ngầm của gần như mọi mô hình ML |

---

# 9. Nguồn học

- [Seeing Theory — Brown University](https://seeing-theory.brown.edu/) — **nguồn trực quan tốt nhất**. Toàn bộ xác suất cơ bản trình bày bằng hình động tương tác, kéo thả được.
- [StatQuest with Josh Starmer — YouTube](https://www.youtube.com/c/joshstarmer) — giải thích từng khái niệm thống kê cực dễ hiểu, mỗi video 5 đến 15 phút.
- [Bayes theorem, the geometry of changing beliefs — 3Blue1Brown](https://www.youtube.com/watch?v=HZGCoVF3YvM) — hình dung định lý Bayes bằng diện tích, giúp thấy ngay vì sao bài toán xét nghiệm ở mục 4 ra 16.7%.
- [Mathematics for Machine Learning — Deisenroth, Faisal, Ong (PDF miễn phí)](https://mml-book.github.io/) — **sách để trích dẫn**. Chương 6 là Probability and Distributions.
- [Deep Learning Book — Chapter 3: Probability and Information Theory (Goodfellow et al.)](https://www.deeplearningbook.org/contents/prob.html) — chương chuẩn cho Entropy, Cross-Entropy và KL Divergence.

> 🧪 **Bài thực hành 20 phút:**
>
> ```python
> import numpy as np
> # 1. Kiem chung vi du xuc xac o muc 2
> x = np.arange(1, 7)
> print(x.mean(), x.var())        # 3.5   2.9167
>
> # 2. Kiem chung bai toan Bayes o muc 4
> p_pos = 0.99*0.01 + 0.05*0.99
> print(0.99*0.01 / p_pos)        # 0.1667
>
> # 3. Cross-entropy cho tung dong trong bang o muc 6
> for q in [0.98, 0.70, 0.34, 0.05]:
>     print(q, round(-np.log(q), 2))
> ```
>
> Ba đoạn này kiểm chứng đúng ba bảng số trong trang. Tự chạy một lần thì nhớ lâu hơn đọc mười lần.

---

# 10. Ghi chú của mình

*(Điền sau khi học: chỗ nào còn vướng, câu hỏi cần hỏi thầy.)*
