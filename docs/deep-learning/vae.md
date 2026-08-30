# Variational Autoencoder (VAE)

> **NCKH** / [Deep Learning](index.md) / [Autoencoder](autoencoder.md) / **Variational Autoencoder**

> **📌 Nền tảng cần có trước:** **Autoencoder** · **Hàm mất mát Loss Function** · [Latent Space (Không gian tiềm ẩn)](latent-space.md) · khái niệm **KL Divergence** trong bảng Thuật ngữ.

---

# 1. Vì sao cần VAE? Vấn đề của Autoencoder thường

Autoencoder thường học rất tốt việc **nén và tái tạo**. Nhưng nếu bạn thử lấy một điểm ngẫu nhiên trong Latent Space rồi đưa qua Decoder, kết quả thường là **một mớ vô nghĩa**. Vì sao?

## Ba vấn đề của Latent Space trong AE thường

**1. Không liên tục (discontinuous).** AE ánh xạ mỗi ảnh thành **một điểm cố định**. Không có gì bắt buộc các điểm phải nằm gần nhau hay lấp đầy không gian. Kết quả: Latent Space đầy **"lỗ hổng"** — những vùng mà Decoder chưa từng thấy trong lúc huấn luyện.

**2. Không có cấu trúc.** Hai ảnh giống nhau có thể bị ánh xạ tới hai điểm rất xa nhau. Không có ràng buộc nào về khoảng cách.

**3. Không nội suy được.** Lấy trung điểm giữa vector của ảnh số 3 và ảnh số 8, đưa qua Decoder — bạn không nhận được thứ gì "ở giữa 3 và 8", mà thường là nhiễu.

> **💡 Ý tưởng giải quyết:** thay vì ánh xạ mỗi ảnh thành **một điểm**, hãy ánh xạ nó thành **một vùng** — cụ thể là một **phân phối xác suất**. Khi mỗi ảnh chiếm một vùng và các vùng chồng lấn nhau, Latent Space trở nên **liên tục và lấp đầy**, không còn lỗ hổng.

---

# 2. Ý tưởng cốt lõi của VAE

VAE do **Kingma & Welling** đề xuất năm 2013. Điểm khác biệt căn bản: VAE là **mô hình xác suất (probabilistic)**, không phải mô hình xác định (deterministic) như AE thường.

**Encoder của AE:** ảnh x → vector z (một điểm)

**Encoder của VAE:** ảnh x → **hai vector μ và σ**, mô tả một phân phối chuẩn $`N(\mu, \sigma^2)`$

Sau đó, một điểm z được **lấy mẫu ngẫu nhiên** từ phân phối đó rồi đưa vào Decoder.

> **🎲 Hệ quả quan trọng:** cùng một ảnh đầu vào, mỗi lần chạy sẽ cho z **khác nhau một chút**. Decoder buộc phải học cách tái tạo đúng ảnh đó từ **cả một vùng** trong Latent Space, chứ không phải từ đúng một điểm. Đây chính là cơ chế làm cho không gian trở nên liên tục.

## Góc nhìn xác suất (để hiểu tên gọi "Variational")

Mục tiêu thật sự của VAE là học phân phối dữ liệu $`p(x)`$. Theo quy tắc xác suất:

$$
p(x) = \int p(x|z) \, p(z) \, dz
$$

Tích phân này **không tính được** trong thực tế (intractable) vì phải duyệt qua mọi giá trị z có thể. Tương tự, hậu nghiệm $`p(z|x)`$ cũng không tính được.

**Giải pháp — suy luận biến phân (variational inference):** dùng một phân phối đơn giản $`q_\phi(z|x)`$ do Encoder học ra để **xấp xỉ** $`p(z|x)`$. Chữ **"Variational"** trong tên VAE đến từ đây.

## Ví dụ dễ hiểu: tấm bản đồ và vùng đất

> Hãy coi Latent Space là một **tấm bản đồ**.
>
> **Autoencoder thường** đóng cho mỗi bức ảnh một **cái đinh ghăm** tại một tọa độ chính xác. Giữa các cái đinh là **biển khơi trống rỗng** — Decoder chưa bao giờ đặt chân tới đó, nên hỏi nó "chỗ này có gì?" thì nó trả về nhiễu.
>
> **VAE** thay mỗi cái đinh bằng một **vệt mực loang**: tâm vệt là $`\mu`$, bán kính loang là $`\sigma`$. Huấn luyện xong, các vệt mực **chồng mép lên nhau** và phủ kín tấm bản đồ. Giờ chọc vào **bất kỳ điểm nào**, Decoder đều trả về một bức ảnh có nghĩa.

| Ảnh đầu vào | AE trả về | VAE trả về | Ý nghĩa |
|---|---|---|---|
| Số "3" viết rất rõ | z = [1.2, −0.5] | μ = [1.2, −0.5], σ = [**0.1**, **0.1**] | Vệt mực **nhỏ** — mô hình rất chắc chắn |
| Số "3" viết nguyệch ngoạc, giống "8" | z = [0.4, 0.9] | μ = [0.4, 0.9], σ = [**0.9**, **1.1**] | Vệt mực **to** — mô hình tự nói "tôi không chắc" |

> **💡** Đây là điểm AE **không bao giờ** làm được: VAE không chỉ nói **"ảnh này nằm ở đâu"** mà còn nói **"tôi chắc chắn tới mức nào"** — tức là mô hình hóa được **độ bất định (uncertainty)**. Trong hướng XAI của bạn, đây là một tính chất rất đáng giá: nó liên quan trực tiếp tới nguyên tắc **Knowledge Limits** của NIST — mô hình biết khi nào mình không biết.

---

# 3. Kiến trúc chi tiết

Luồng dữ liệu đi qua 5 bước:

**Bước 1 — Encoder.** Ảnh x đi qua mạng nơ-ron, cho ra **hai vector cùng kích thước**: `mu` (trung bình) và `logvar` (log của phương sai).

**Bước 2 — Lấy mẫu.** Từ $`N(\mu, \sigma^2)`$ lấy ra một điểm z.

**Bước 3 — Decoder.** z đi qua mạng giải mã, cho ra ảnh tái tạo x̂.

**Bước 4 — Tính Loss.** Gồm hai thành phần (mục 5).

**Bước 5 — Backpropagation.** Cập nhật trọng số của cả Encoder lẫn Decoder.

> **⚠️ Vì sao Encoder xuất ra `logvar` chứ không phải `σ` trực tiếp?**
> Vì phương sai **bắt buộc phải dương**, mà đầu ra của mạng nơ-ron thì có thể âm. Nếu để mạng xuất ra $`\log \sigma^2`$ (nhận giá trị âm thoải mái) rồi tính $`\sigma = \exp(\frac{1}{2}\log\sigma^2)`$ thì luôn được số dương. Đây là **mẹo kỹ thuật bắt buộc phải biết khi đọc code VAE**.

---

# 4. Reparameterization Trick

Đây là **đóng góp kỹ thuật quan trọng nhất** của bài báo gốc.

## Vấn đề

Phép **lấy mẫu ngẫu nhiên là một thao tác không khả vi (non-differentiable)**. Gradient không thể chảy ngược qua nó. Nghĩa là ta không thể huấn luyện Encoder bằng backpropagation — mô hình bị "đứt" ngay giữa.

## Giải pháp

Tách phần ngẫu nhiên ra khỏi đường đi của gradient. Thay vì lấy mẫu trực tiếp $`z \sim N(\mu, \sigma^2)`$, ta viết lại thành:

$$
z = \mu + \sigma \odot \epsilon, \quad \text{với } \epsilon \sim N(0, I)
$$

Trong đó $`\odot`$ là phép nhân từng phần tử.

> **🔑 Vì sao mẹo này hiệu quả:** phần ngẫu nhiên giờ nằm ở $`\epsilon`$ — một **hằng số được lấy mẫu từ bên ngoài**, không phụ thuộc tham số mô hình. Còn $`\mu`$ và $`\sigma`$ tham gia vào z bằng **phép cộng và phép nhân thông thường** — hoàn toàn khả vi. Gradient chảy ngược qua chúng bình thường.
>
> Hình dung: thay vì "rút ngẫu nhiên từ một cái hộp do mô hình tạo ra", ta "rút ngẫu nhiên từ một cái hộp chuẩn cố định, rồi mô hình co giãn và dịch chuyển kết quả".

## Ví dụ số cụ thể của Reparameterization

Giả sử latent chỉ có **2 chiều**. Với một ảnh, Encoder xuất ra:

$$
\mu = [\,1.2,\; -0.5\,], \qquad \sigma = [\,0.3,\; 0.8\,]
$$

Mỗi lần chạy, máy rút một $`\epsilon`$ mới từ $`N(0, I)`$:

| Lần chạy | $`\epsilon`$ rút được | Tính $`z = \mu + \sigma \odot \epsilon`$ | Kết quả z |
|---|---|---|---|
| 1 | [0.5, −1.0] | [1.2 + 0.3(0.5), −0.5 + 0.8(−1.0)] | **[1.35, −1.30]** |
| 2 | [−1.2, 0.4] | [1.2 + 0.3(−1.2), −0.5 + 0.8(0.4)] | **[0.84, −0.18]** |
| 3 | [0.0, 0.0] | [1.2 + 0, −0.5 + 0] | **[1.20, −0.50]** = đúng tâm μ |

> **🔍 Ba điều nhìn ra ngay từ bảng:**
> 1. Cùng một ảnh nhưng **z mỗi lần một khác** — Decoder buộc phải trả về đúng ảnh đó từ **cả một vùng**, chứ không phải từ một điểm.
> 2. Chiều thứ hai ($`\sigma = 0.8`$) **dao động mạnh hơn** chiều thứ nhất ($`\sigma = 0.3`$) — đúng như ý nghĩa của σ.
> 3. Phần ngẫu nhiên nằm **toàn bộ ở** $`\epsilon`$. Với máy tính, khi đã rút xong $`\epsilon = 0.5`$ thì phép `1.2 + 0.3*0.5` chỉ là **cộng và nhân bình thường** — đạo hàm theo μ và σ tính được dễ dàng. Đó chính là toàn bộ phép màu của mẹo này.

> **🎰 Liên tưởng:** tưởng tượng bạn cần một số ngẫu nhiên "quanh 1.2, lệch khoảng 0.3".
> **Cách sai (không khả vi):** đặt làm một con xúc xắc đặc biệt có sẵn hai thông số đó, rồi tung. Bạn không thể hỏi "nếu đổi 1.2 thành 1.3 thì kết quả đổi bao nhiêu" — vì phải đi đúc lại xúc xắc.
> **Cách đúng (khả vi):** tung một con xúc xắc **chuẩn, cố định** ra $`\epsilon`$, rồi tự tay tính `1.2 + 0.3*`$`\epsilon`$. Giờ thì câu hỏi trên trả lời được ngay.

---

# 5. Hàm mất mát của VAE

Loss gồm **hai thành phần đối kháng nhau**:

$$
\mathcal{L} = \underbrace{\mathbb{E}_{q(z|x)}[\log p(x|z)]}_{\text{Reconstruction Loss}} - \underbrace{D_{KL}(q(z|x) \, \| \, p(z))}_{\text{Regularization}}
$$

Biểu thức này gọi là **ELBO (Evidence Lower Bound)** — cận dưới của log-likelihood. Huấn luyện VAE chính là **cực đại hóa ELBO**, tương đương cực tiểu hóa giá trị âm của nó.

## Thành phần 1 — Reconstruction Loss

Giống hệt Autoencoder thường: đo độ giống giữa ảnh gốc và ảnh tái tạo. Dùng **MSE** cho dữ liệu liên tục, **Binary Cross-Entropy** cho dữ liệu đã chuẩn hóa về [0,1].

**Vai trò:** ép mô hình tái tạo cho đúng.

## Thành phần 2 — KL Divergence

Đo độ lệch giữa phân phối latent mà Encoder học được và **phân phối tiên nghiệm chuẩn** $`N(0, I)`$.

Với hai phân phối Gaussian, KL có **dạng đóng (closed form)** rất gọn:

$$
D_{KL} = -\frac{1}{2} \sum_{j=1}^{J} \left( 1 + \log \sigma_j^2 - \mu_j^2 - \sigma_j^2 \right)
$$

**Vai trò:** ép mọi phân phối latent **tiến về gốc tọa độ và có phương sai gần 1**. Điều này khiến các vùng chồng lấn nhau, lấp đầy không gian, và **loại bỏ lỗ hổng**.

> **⚖️ Sự căng thẳng giữa hai thành phần — điểm cốt lõi phải hiểu:**
> **Reconstruction Loss** muốn mỗi ảnh có một vùng latent **riêng biệt, tách xa nhau** để tái tạo cho chính xác.
> **KL Divergence** muốn mọi vùng **dồn về giữa và chồng lên nhau** để không gian liên tục.
> Nếu chỉ có Reconstruction → quay về AE thường, latent space có lỗ hổng.
> Nếu KL quá mạnh → mọi ảnh dồn về cùng một chỗ, Decoder không phân biệt được gì (hiện tượng **posterior collapse**).
> **Huấn luyện VAE tốt = cân bằng được hai lực này.**

## Ví dụ tính tay KL Divergence

Công thức dạng đóng ở trên trông đáng sợ, nhưng chỉ cần **thế số vào một chiều latent** là hiểu ngay nó đang phạt cái gì:

| μ | σ | KL | Mô hình đang làm gì — và bị phạt vì sao |
|---|---|---|---|
| 0 | 1 | **0** | Đúng hệt $`N(0,1)`$ → **không bị phạt gì cả** |
| **5** | 1 | **12.50** | Trốn ra xa gốc tọa độ để khỏi chồng lấn ảnh khác → phạt **rất nặng** |
| 0 | **0.1** | **1.81** | Thu vệt mực thật nhỏ để tái tạo cho sắc nét (hành vi của AE thường) → bị phạt |
| 0 | **3.0** | **2.90** | Vệt mực loang quá rộng, nuốt cả ảnh khác → cũng bị phạt |

> **⚖️ Đây chính là "sự căng thẳng" ở trên, nhưng nhìn bằng số:**
> Reconstruction Loss luôn muốn đẩy mô hình về hàng **μ = 5** (tách xa nhau) hoặc **σ = 0.1** (thật gọn) — vì như vậy tái tạo sẽ chính xác nhất.
> KL thì phạt đúng hai hành vi đó (12.50 và 1.81) để kéo mọi thứ về hàng đầu — nơi KL = 0.
> **Điểm tối ưu thực tế nằm ở đâu đó giữa** — đó là lý do huấn luyện VAE khó hơn AE.

---

# 6. Ba vấn đề thực tế khi dùng VAE

**Ảnh sinh ra bị mờ (blurry).** Đây là nhược điểm nổi tiếng nhất của VAE. Nguyên nhân: Reconstruction Loss dạng MSE khiến mô hình có xu hướng **xuất ra trung bình của nhiều khả năng** thay vì chọn dứt khoát một khả năng. Đây là lý do GAN và Diffusion Model cho ảnh sắc nét hơn VAE.

**Posterior collapse.** Khi Decoder quá mạnh, nó có thể bỏ qua z hoàn toàn và tự sinh ảnh. Lúc đó KL bị đẩy về 0, latent space **mất hết thông tin**. Cách khắc phục thường dùng: **KL annealing** — cho trọng số KL tăng dần từ 0 trong các epoch đầu.

**Cân bằng hai thành phần.** Dẫn tới biến thể **β-VAE** (Higgins et al., 2017): thêm hệ số β vào trước KL. β > 1 ép latent space **phân tách (disentangled)** hơn — mỗi chiều mang một ý nghĩa riêng — nhưng đánh đổi bằng chất lượng tái tạo.

> **🔗 β-VAE chính là cầu nối giữa Autoencoder và đề tài CBM của bạn:** nếu mỗi chiều latent mang một ý nghĩa độc lập, đó chính là **khái niệm không cần nhãn**. Xem **bài báo CBM liên quan** trong Thư viện bài báo.

---

# 7. So sánh Autoencoder và VAE

| Tiêu chí | Autoencoder (AE) | Variational Autoencoder (VAE) |
|---|---|---|
| Bản chất | Xác định (deterministic) | Xác suất (probabilistic) |
| Encoder xuất ra | Một vector z duy nhất | Hai vector μ và σ (một phân phối) |
| Cùng input, chạy 2 lần | Cho kết quả giống hệt nhau | Cho kết quả khác nhau (do lấy mẫu) |
| Hàm mất mát | Chỉ Reconstruction Loss | Reconstruction Loss + KL Divergence |
| Latent Space | Rời rạc, có lỗ hổng, không có cấu trúc | Liên tục, lấp đầy, có cấu trúc quanh gốc |
| Nội suy giữa 2 điểm | Thường ra nhiễu vô nghĩa | Ra kết quả trung gian có nghĩa, chuyển mượt |
| Sinh dữ liệu mới | Không (lấy z ngẫu nhiên ra rác) | Có — đây là mục đích chính |
| Là mô hình sinh? | Không | Có (generative model) |
| Chất lượng tái tạo | Sắc nét hơn | Mờ hơn (do Loss trung bình hóa) |
| Độ khó huấn luyện | Đơn giản, ổn định | Khó hơn: cân bằng KL, tránh posterior collapse |
| Nền tảng toán học | Tối ưu hóa thuần túy | Suy luận biến phân, Bayes |

## Khi nào dùng cái nào?

**Dùng AE khi:** giảm chiều dữ liệu, khử nhiễu, phát hiện bất thường, trích xuất đặc trưng để đưa vào mô hình khác. Nói chung — khi bạn chỉ cần **nén và tái tạo**.

**Dùng VAE khi:** cần **sinh dữ liệu mới**, cần **nội suy mượt** giữa các mẫu, cần latent space **có cấu trúc và diễn giải được**, hoặc cần mô hình hóa **độ bất định** của biểu diễn.

> **🎯 Câu trả lời gọn nếu thầy hỏi:** *"AE học cách nén một điểm thành một điểm. VAE học cách nén một điểm thành một phân phối. Chính sự thay đổi đó — cộng với ràng buộc KL — biến một mạng nén dữ liệu thành một mô hình sinh."*

---

# 7b. Ba ví dụ trực quan chỉ VAE làm được

Bảng so sánh ở mục 7 liệt kê sự khác biệt. Ba ví dụ dưới đây cho bạn **nhìn thấy** sự khác biệt đó — và đều chạy được trong một buổi.

## Ví dụ 1 — Nội suy: biến số 3 thành số 8

Lấy ảnh một số **3** và một số **8**, mã hóa thành $`z_3`$ và $`z_8`$, rồi đi dần từ điểm này sang điểm kia:

$$
z_{\alpha} = (1-\alpha)\, z_3 + \alpha\, z_8, \qquad \alpha = 0,\; 0.25,\; 0.5,\; 0.75,\; 1
$$

| α | AE thường cho ra | VAE cho ra |
|---|---|---|
| 0.00 | Số 3 rõ ràng | Số 3 rõ ràng |
| 0.25 | Số 3 bắt đầu vỡ ra, lấm tấm | Số 3 hơi đóng nét tròn bên trái |
| 0.50 | **Một mảng nhiễu**, không ra chữ số nào | **Một ký tự lai 3–8** — vẫn trông như chữ viết tay |
| 0.75 | Nhiễu mờ | Gần thành số 8, vòng trên chưa kín hẳn |
| 1.00 | Số 8 rõ ràng | Số 8 rõ ràng |

> **🔎** Ô α = 0.50 là ô quan trọng nhất của cả bảng. Đó chính là **cái "lỗ hổng"** đã nói ở mục 1 — AE chưa từng được huấn luyện ở vùng đó nên trả về rác; còn KL Divergence của VAE đã **ép các vệt mực chồng lấn**, nên vùng đó vẫn nằm trong phạm vi mà Decoder biết.

## Ví dụ 2 — Sinh ảnh hoàn toàn mới từ con số không

Không cần ảnh đầu vào nào cả — **vứt luôn Encoder đi**:

```python
z = torch.randn(16, 20)        # 16 điểm ngẫu nhiên từ N(0, I)
imgs = model.decode(z)         # -> 16 chữ số viết tay CHƯA TỪNG TỒN TẠI
```

> **✨** Đoạn code này chạy được **chính xác vì KL đã ép latent về** $`N(0,I)`$. Ta biết chắc ở đâu trong không gian thì có dữ liệu, nên lấy mẫu đúng chỗ đó.
> Chạy đúng hai dòng này với một **AE thường** thì sẽ ra 16 mảng nhiễu — vì không ai biết latent của AE phân bố ở đâu.
> **Đây là câu trả lời ngắn nhất cho câu hỏi "VAE hơn AE chỗ nào": đúng hai dòng code này.**

## Ví dụ 3 — Đi dọc một chiều latent (ví dụ của β-VAE)

Giữ nguyên toàn bộ vectơ z, chỉ **kéo một chiều duy nhất** từ −3 đến +3 rồi xem ảnh đổi thế nào:

| Chiều bị kéo | Ảnh thay đổi ra sao (trên khuôn mặt CelebA) | Diễn giải |
|---|---|---|
| $`z_4`$ | Mặt xoay dần từ trái sang phải | Chiều này đã học được khái niệm **"góc quay"** |
| $`z_{11}`$ | Miệng chuyển từ mím sang cười | Khái niệm **"nụ cười"** |
| $`z_{17}`$ | Tóc dài dần ra | Khái niệm **"độ dài tóc"** |

> **🔗** Đây chính là cầu nối trực tiếp tới đề tài NCKH của bạn. Mỗi chiều latent mang đúng **một khái niệm con người đọc được** — nhưng **không ai gán nhãn cho chúng cả**, chúng tự nổi lên từ ràng buộc β·KL. Đó là **disentanglement**.
> Đặt cạnh **CBM** — vốn bắt buộc phải có nhãn khái niệm do người gán — thì đây là **hướng đối lập**, và khoảng trống giữa hai hướng chính là chỗ có thể đặt câu hỏi nghiên cứu: *làm sao có khái niệm diễn giải được mà không cần nhãn thủ công?*

> **🧪 Bài thực hành đáng làm nhất (1 buổi):** huấn luyện **một AE** và **một VAE** trên MNIST với `latent_dim = 2`, rồi vẽ toàn bộ tập test lên mặt phẳng, tô màu theo chữ số.
> Bạn sẽ thấy: **AE** cho các cụm rời rạc, tản mát, giữa chúng là khoảng trống. **VAE** cho một đám mây tròn đặc quanh gốc tọa độ, các cụm tiếp giáp nhau.
> Sau đó lấy một lưới đều 20×20 điểm trên mặt phẳng đó và giải mã hết — **một tấm poster 400 chữ số** cho bạn thấy toàn bộ không gian trên một bức ảnh. Đây là hình minh họa tốt nhất để đưa vào báo cáo.

---

# 8. Code minh họa (PyTorch)

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class VAE(nn.Module):
    def __init__(self, input_dim=784, hidden_dim=400, latent_dim=20):
        super().__init__()
        # Encoder
        self.fc1 = nn.Linear(input_dim, hidden_dim)
        self.fc_mu = nn.Linear(hidden_dim, latent_dim)      # trung bình
        self.fc_logvar = nn.Linear(hidden_dim, latent_dim)  # log phương sai
        # Decoder
        self.fc3 = nn.Linear(latent_dim, hidden_dim)
        self.fc4 = nn.Linear(hidden_dim, input_dim)

    def encode(self, x):
        h = F.relu(self.fc1(x))
        return self.fc_mu(h), self.fc_logvar(h)

    def reparameterize(self, mu, logvar):
        std = torch.exp(0.5 * logvar)   # sigma = exp(0.5 * log sigma^2)
        eps = torch.randn_like(std)     # epsilon ~ N(0, I)
        return mu + eps * std           # z = mu + sigma * epsilon

    def decode(self, z):
        h = F.relu(self.fc3(z))
        return torch.sigmoid(self.fc4(h))

    def forward(self, x):
        mu, logvar = self.encode(x)
        z = self.reparameterize(mu, logvar)
        return self.decode(z), mu, logvar


def vae_loss(recon_x, x, mu, logvar):
    # Thanh phan 1: Reconstruction Loss
    recon = F.binary_cross_entropy(recon_x, x, reduction='sum')
    # Thanh phan 2: KL Divergence (dang dong cho Gaussian)
    kld = -0.5 * torch.sum(1 + logvar - mu.pow(2) - logvar.exp())
    return recon + kld
```

> **👀** Đọc kỹ hàm `reparameterize` và dòng tính `kld` — hai dòng đó chính là **toàn bộ sự khác biệt về code** giữa VAE và một Autoencoder thường.

---

# 9. Nguồn học — từ cơ bản đến nâng cao

## Bước 1 — Hiểu trực quan (đọc trước tiên)

- [From Autoencoder to Beta-VAE — Lilian Weng (Lil'Log)](https://lilianweng.github.io/posts/2018-08-12-vae/) — **nguồn tốt nhất để bắt đầu**. Đi từ AE cơ bản qua từng biến thể tới VAE và β-VAE, có hình minh họa và công thức đầy đủ.
- [Variational autoencoders — Jeremy Jordan](https://www.jeremyjordan.me/variational-autoencoders/) — giải thích rất trực quan về vấn đề "lỗ hổng trong latent space".
- [Understanding Variational Autoencoders (VAEs) — Joseph Rocca](https://towardsdatascience.com/understanding-variational-autoencoders-vaes-f70510919f73) — nhiều hình vẽ, giải thích rõ vì sao cần phân phối thay vì điểm.

## Bước 2 — Video

- [Variational Autoencoders — Arxiv Insights (YouTube)](https://www.youtube.com/watch?v=9zKuYvjFFS8) — 15 phút, giải thích trực quan xuất sắc.
- [CS231n — Stanford: Generative Models](https://cs231n.github.io/) — bài giảng chính thức, có phần VAE.

## Bước 3 — Tài liệu học thuật

- [Tutorial on Variational Autoencoders — Carl Doersch, 2016 (arXiv:1606.05908)](https://arxiv.org/abs/1606.05908) — **tài liệu bắc cầu tốt nhất** giữa blog và bài báo gốc. Giải thích cặn kẽ phần toán mà bài báo gốc viết quá súc tích.
- [An Introduction to Variational Autoencoders — Kingma & Welling, 2019 (arXiv:1906.02691)](https://arxiv.org/abs/1906.02691) — chính tác giả viết lại đầy đủ hơn sau 6 năm. Nếu đọc bài gốc thấy khó, đọc cái này.

## Bước 4 — Bài báo gốc

- [Auto-Encoding Variational Bayes — Kingma & Welling, 2013 (arXiv:1312.6114)](https://arxiv.org/abs/1312.6114) — **bài gốc, bắt buộc trích dẫn**. Ngắn nhưng rất đặc, nên đọc sau khi đã nắm trực giác.
- [β-VAE — Higgins et al., ICLR 2017](https://openreview.net/forum?id=Sy2fzU9gl) — biến thể quan trọng cho hướng disentanglement.

## Bước 5 — Thực hành

- [PyTorch official VAE example](https://github.com/pytorch/examples/tree/main/vae) — code chuẩn, chạy trên MNIST, đọc rất dễ.
- [Keras VAE tutorial](https://keras.io/examples/generative/vae/) — bản TensorFlow/Keras tương đương.

> **🧭 Thứ tự mình khuyên:** xem video Arxiv Insights (15 phút) → đọc Lil'Log → chạy thử code PyTorch trên MNIST và tự vẽ latent space 2 chiều → đọc Doersch tutorial → cuối cùng mới đọc bài báo gốc Kingma & Welling.
> Việc **tự vẽ latent space 2 chiều** rồi so sánh giữa AE và VAE trên cùng bộ MNIST là bài tập cho bạn thấy rõ nhất sự khác biệt — chỉ mất khoảng 1 buổi.

---

# 10. Ghi chú của mình

*(Điền sau khi học: chỗ nào còn vướng, câu hỏi cần hỏi thầy.)*
