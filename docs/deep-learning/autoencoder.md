# Autoencoder

> 🎓 **NCKH** / **Deep Learning** / **Autoencoder**

## Tổng quan

**Autoencoder (AE)** là mạng nơ-ron **học tự giám sát (self-supervised)**: nén dữ liệu đầu vào thành một biểu diễn nhỏ hơn rồi **tái tạo lại chính nó**. Điểm đặc biệt: nó **không cần nhãn do con người gán** — chính dữ liệu đầu vào đóng vai trò nhãn.

Diễn đạt bằng công thức, toàn bộ ý tưởng gọn trong ba ký hiệu:

$$z = f_{\theta}(x) \quad \longrightarrow \quad \hat{x} = g_{\phi}(z) \quad \longrightarrow \quad \min_{\theta,\phi} \; L(x, \hat{x})$$

Trong đó $f$ là Encoder, $g$ là Decoder, $z$ là biểu diễn tiềm ẩn tại Bottleneck.

> 💡 **Trực giác dễ nhớ:** hãy nghĩ tới việc **tóm tắt một cuốn sách rồi viết lại nó từ bản tóm tắt**. Bản viết lại sẽ không giống hệt bản gốc — nhưng nếu bản tóm tắt tốt, nó sẽ giữ được cốt truyện và bỏ đi các chi tiết vụn vặt. **Bản tóm tắt đó chính là Bottleneck**, và việc bỏ được chi tiết vụn vặt chính là lý do Autoencoder hữu ích.

### Ba ý then chốt phải nắm

> 🔒 **Ràng buộc là tất cả**
> Nếu không có ràng buộc nào, mạng chỉ cần **sao chép** đầu vào sang đầu ra là đạt Loss = 0 — và không học được gì cả.
>

> ⚖️ **Luôn là một đánh đổi**
> Nén càng mạnh thì càng loại được nhiễu, nhưng cũng càng dễ mất thông tin quan trọng.
>

> 🎯 **Giá trị nằm ở giữa**
> Sản phẩm thực sự của AE thường **không phải ảnh tái tạo**, mà là **vectơ z ở giữa**. Decoder nhiều khi chỉ là công cụ để huấn luyện Encoder.
>

> 🔑 **Ý thứ ba là điều người mới hay hiểu sai nhất.** Khi dùng AE để giảm chiều, phát hiện bất thường, hay trích xuất đặc trưng — sau khi huấn luyện xong, ta thường **vứt bỏ Decoder** và chỉ giữ lại Encoder.

---

## 5 phần

Nên đọc theo đúng thứ tự dưới đây — mỗi phần xây trên phần trước:

- _Autoencoder_ (chưa được đồng bộ riêng)

- _Hàm mất mát Loss Function của Autoencoder_ (chưa được đồng bộ riêng)

- _Các Siêu tham số (Hyperparameters) quan trọng_ (chưa được đồng bộ riêng)

- _Các biến thể phổ biến của Autoencoder_ (chưa được đồng bộ riêng)

> 🎲 **Phần 5 — nằm ở ngoài hub này:** [Variational Autoencoder (VAE)](vae.md)
> VAE được tách thành một trang riêng trực thuộc **Deep Learning** vì nó không còn là một "biến thể nhỏ" nữa mà là một **mô hình sinh** với nền tảng xác suất riêng (ELBO, reparameterization trick).
>

> 🗺️ **Mỗi phần trả lời một câu hỏi:**
> **1. Autoencoder** — *Nó là gì và cấu tạo ra sao?* (Encoder, Bottleneck, Decoder)
>
> **2. Hàm mất mát** — *Làm sao đo được nó tái tạo tốt hay dở?* (MSE, BCE, Reconstruction Loss)
>
> **3. Siêu tham số** — *Phải tự đặt những gì trước khi huấn luyện?* (Code size, số lớp, learning rate)
>
> **4. Các biến thể** — *Có mấy loại và mỗi loại giải quyết vấn đề gì?* (Sparse, Denoising, Contractive, Convolutional, Stacked)
>
> **5. VAE** — *Vì sao có một biến thể được tách riêng?* (mô hình sinh, so sánh AE vs VAE)
>

---

## Bản đồ khái niệm nhanh

Dùng để tra cứu nhanh hoặc ôn trước khi gặp thầy.

| Khái niệm | Ý nghĩa trong một câu |
| --- | --- |
| **Encoder** | Nén đầu vào lớn thành vectơ nhỏ, giữ lại nét đặc trưng chính |
| **Bottleneck** | Lớp hẹp nhất — phần quan trọng nhất và cũng nhỏ nhất của mạng |
| **Latent Space** | Không gian toán học chứa các biểu diễn nén — có trang riêng, xem callout ngay dưới bảng |
| **Decoder** | Giải nén từ Bottleneck, tái tạo lại kích thước ban đầu |
| **Reconstruction Loss** | Đo độ sai khác giữa ảnh gốc và ảnh tái tạo |
| **Identity Function** | Cái bẫy cần tránh: mạng chỉ sao chép mà không học gì |
| **Code size** | Siêu tham số quan trọng nhất — số chiều của Bottleneck |

> 🌌 **Latent Space không phải khái niệm riêng của Autoencoder.** Bạn gặp nó lần đầu ở đây, nhưng nó xuất hiện ở GAN, Diffusion, Word2Vec, CLIP, ViT và cả CBM. Vì vậy nó được đặt thành một trang riêng ở cấp Deep Learning:
> → [Latent Space (Không gian tiềm ẩn)](latent-space.md)
>

---

## Ứng dụng thực tế

> 📉 **Giảm chiều dữ liệu**
> Phi tuyến nên mạnh hơn PCA. Dùng Encoder để nén dữ liệu trước khi đưa vào mô hình khác.
>

> 🧹 **Khử nhiễu ảnh**
> Denoising Autoencoder phục hồi ảnh sạch từ ảnh nhiễu, xử lý được cả ảnh phức tạp.
>

> 🚨 **Phát hiện bất thường**
> Dữ liệu giống tập huấn luyện cho Loss thấp; dữ liệu lạ cho Loss cao vượt ngưỡng. Rất phổ biến trong giám sát thiết bị và phát hiện gian lận.
>

> ✨ **Sinh dữ liệu mới**
> Chỉ VAE làm được, nhờ Latent Space liên tục. AE thường không sinh được.
>

---

## Năm sai lầm thường gặp khi mới học

| Hiểu sai | Thực tế |
| --- | --- |
| "AE là học không giám sát" | Chính xác hơn là **học tự giám sát** — vẫn có nhãn, nhưng nhãn chính là đầu vào |
| "Mục tiêu là tái tạo ảnh thật đẹp" | Tái tạo hoàn hảo thường nghĩa là mô hình **học vẹt**. Sản phẩm cần là vectơ z |
| "Bottleneck càng nhỏ càng tốt" | Quá nhỏ gây **underfitting** — Decoder không đủ manh mối để giải mã |
| "AE cũng sinh được ảnh mới" | Không. Lấy z ngẫu nhiên ở AE thường sẽ ra nhiễu — cần **VAE** |
| "Contractive AE và Convolutional AE đều viết tắt là CAE" | Đúng, và đây là **bẫy thực sự** — khi viết bài phải ghi rõ tên đầy đủ |

---

## Liên hệ với đề tài NCKH

> 🔗 Autoencoder không chỉ là kiến thức nền — nó **nối trực tiếp vào hướng CBM** qua ba đường:
> **Latent Space & Embedding** → nền tảng để hiểu [Concept Embedding Models](https://arxiv.org/abs/2209.09056), biến thể thay khái niệm vô hướng bằng vector nhúng.
>
> **Bottleneck** → chính là ý tưởng kiến trúc mà CBM mượn lại, chỉ khác ở chỗ CBM ép nút thắt đó phải mang **ý nghĩa con người đọc được**.
>
> **Disentanglement (β-VAE)** → nếu mỗi chiều latent mang một ý nghĩa riêng thì đó là **khái niệm không cần nhãn** — hướng nghiên cứu đáng theo đuổi.
>

---

## Nguồn học tổng quan

- [Autoencoders in Deep Learning: Tutorial & Use Cases — V7 Labs](https://www.v7labs.com/blog/autoencoders-guide) — tổng quan trực quan, có so sánh các biến thể.

- [From Autoencoder to Beta-VAE — Lilian Weng (Lil'Log)](https://lilianweng.github.io/posts/2018-08-12-vae/) — đi từ AE cơ bản qua từng biến thể, chất lượng học thuật cao.

- [Introduction to Autoencoders — DataCamp](https://www.datacamp.com/tutorial/introduction-to-autoencoders) — có kèm code PyTorch để thực hành.

- [Different types of Autoencoders — OpenGenus](https://iq.opengenus.org/types-of-autoencoder/) — liệt kê ngắn gọn từng biến thể, tiện tra cứu.

- [Deep Learning Book — Chapter 14: Autoencoders (Goodfellow, Bengio, Courville)](https://www.deeplearningbook.org/contents/autoencoders.html) — **chương sách chuẩn mực**, đọc khi cần trích dẫn học thuật.

- [CS231n — Stanford](https://cs231n.github.io/) — bài giảng chính thức, phần Generative Models.

> 🧪 **Bài tập thực hành đáng làm nhất:** huấn luyện một AE đơn giản trên MNIST với `code size = 2`, rồi **vẽ toàn bộ tập test lên mặt phẳng 2 chiều**, tô màu theo chữ số. Bạn sẽ thấy tận mắt các cụm chữ số và các **lỗ hổng** giữa chúng. Sau đó làm y hệt với VAE và so sánh — đây là cách nhanh nhất để hiểu vì sao VAE ra đời.
