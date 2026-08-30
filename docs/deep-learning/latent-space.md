# Latent Space (Không gian tiềm ẩn)

> **NCKH** / [Deep Learning](index.md) / **Latent Space**

> **❓ Vì sao trang này nằm ở cấp Deep Learning chứ không nằm trong Autoencoder?**
> Vì Latent Space **không phải khái niệm riêng của Autoencoder**. Bạn gặp nó lần đầu ở AE, nhưng nó xuất hiện ở gần như **mọi mô hình học sâu**: GAN, Diffusion, Word2Vec, BERT, CLIP, ViT — và cả **CBM** trong đề tài của bạn. Đặt nó ngang hàng với AE và CNN là đúng phạm vi của nó.

---

# 1. Định nghĩa

> **📌 Latent Space (không gian tiềm ẩn)** là **không gian vectơ nhiều chiều mà mô hình dùng để biểu diễn dữ liệu ở dạng nén, trừu tượng** — nơi mỗi mẫu dữ liệu trở thành **một điểm**, và **khoảng cách giữa các điểm phản ánh mức độ giống nhau về ý nghĩa**.

Chữ **"latent"** trong tiếng Anh nghĩa là **ẩn, tiềm tàng, chưa lộ ra**. Nó ẩn theo hai nghĩa:

- **Ẩn về mặt vật lý:** nó nằm bên trong mạng, không phải đầu vào cũng không phải đầu ra. Bạn không nhìn thấy nó trừ khi cố tình lấy ra.
- **Ẩn về mặt ý nghĩa:** các chiều của nó là những **yếu tố sinh ra dữ liệu** (latent factors) mà không ai gán nhãn cả — mô hình tự tìm ra. Với ảnh khuôn mặt thì đó có thể là góc quay, tuổi, độ dài tóc; nhưng chúng **không được ghi tên ở đâu cả**.

Một cách viết gọn: nếu $`x`$ là dữ liệu gốc và $`f`$ là mạng mã hóa thì

$$
z = f(x) \in \mathbb{R}^d, \qquad d \ll \dim(x)
$$

Tập hợp mọi giá trị $`z`$ có thể có chính là **Latent Space**, và $`d`$ là **số chiều** của nó.

---

# 2. Ví dụ dễ hiểu nhất: hồ sơ khuôn mặt

> **👤** Một ảnh khuôn mặt 256×256 màu có **196.608** con số. Nhưng nếu chỉ cần mô tả để người khác hình dung ra, bạn cần bao nhiêu?
> Khoảng **5 con số** là đủ dùng: *tuổi, giới tính, độ dài tóc, đang cười hay không, góc quay mặt*.
> **Không gian 5 chiều đó chính là một Latent Space.** Ảnh gốc sống trong không gian 196.608 chiều; latent space nén nó xuống 5 chiều mà vẫn giữ được những gì thật sự quan trọng.

| Không gian | Số chiều | Một điểm trong đó là gì | Khoảng cách nghĩa là gì |
|---|---|---|---|
| Không gian ảnh gốc (pixel space) | 196.608 | Một danh sách giá trị pixel | **Gần như vô nghĩa** — cùng một người, chỉ cần dịch ảnh 5 pixel là khoảng cách đã rất lớn |
| **Latent Space** | 5 (hoặc 128, 512...) | Một "bản mô tả" cô đọng | **Rất có nghĩa** — hai điểm gần nhau nghĩa là hai khuôn mặt giống nhau về bản chất |

> **💡** **Đây là điều quan trọng nhất của cả trang.** Giá trị của latent space không nằm ở chỗ nó **nhỏ hơn**, mà nằm ở chỗ **khoảng cách trong đó mang ý nghĩa ngữ nghĩa**.
> Trong không gian pixel, ảnh số 1 màu trắng và ảnh số 1 màu xám cách xa nhau hơn ảnh số 1 và ảnh số 7 cùng độ sáng. Trong latent space tốt thì ngược lại — và đó mới là điều ta cần.

---

# 3. Ba tính chất quyết định latent space tốt hay dở

> **📐 Cô đọng (compact)**
> Số chiều nhỏ hơn hẳn dữ liệu gốc, đã loại bỏ nhiễu và phần dư thừa.

> **🧭 Có cấu trúc (structured)**
> Điểm gần nhau thì giống nhau về ngữ nghĩa. Đây là tính chất khiến latent space dùng được cho tìm kiếm, gom cụm, phân loại.

> **🎚️ Tách bạch (disentangled)**
> Mỗi chiều mang **một** yếu tố độc lập. Đây là tính chất **khó nhất**, và cũng là tính chất mà XAI quan tâm nhất.

> **⚠️** Phần lớn latent space trong thực tế đạt được tính chất **1** và **2** một cách tự nhiên, nhưng **không** đạt tính chất **3**. Trong một latent space chưa tách bạch, thay đổi chiều thứ 7 có thể vừa làm người trong ảnh già đi vừa làm tóc dài ra — **hai khái niệm bị trộn vào cùng một chiều**.
> Làm sao ép được tính tách bạch là cả một hướng nghiên cứu riêng (β-VAE, FactorVAE), và nó nằm rất gần đề tài của bạn.

---

# 4. Phạm vi áp dụng — không chỉ Autoencoder

Đây là phần trả lời trực tiếp cho câu hỏi *"latent space chỉ dùng cho AE hay cả lĩnh vực khác?"*. Câu trả lời: **nó có mặt ở gần như mọi nơi trong học sâu**, chỉ khác nhau ở chỗ nó **nằm ở đâu trong mô hình** và **ai quyết định cấu trúc của nó**.

| Lĩnh vực / Mô hình | Latent Space nằm ở đâu | Số chiều điển hình | Dùng để làm gì |
|---|---|---|---|
| **Autoencoder** | Vector z tại Bottleneck | 16 – 128 | Giảm chiều, khử nhiễu, phát hiện bất thường |
| **VAE** | Phân phối $`N(\mu, \sigma^2)`$ tại Bottleneck | 20 – 256 | Sinh dữ liệu mới, nội suy mượt |
| **GAN** | Vector nhiễu z **đầu vào** của Generator | 100 – 512 | Sinh ảnh; StyleGAN còn có thêm không gian W tách bạch hơn |
| **Diffusion / Stable Diffusion** | Khuếch tán diễn ra **trong latent space** thay vì trên pixel | 64×64×4 | Đây chính là chữ "Latent" trong **Latent Diffusion Model** — làm việc ở latent nhẹ hơn pixel khoảng 48 lần |
| **NLP — Word2Vec, GloVe** | Vector nhúng của mỗi từ | 100 – 300 | Đo độ giống nghĩa giữa các từ; đây là latent space nổi tiếng nhất lịch sử |
| **NLP — BERT, GPT** | Vector ẩn ở mỗi lớp Transformer | 768 – 4096 | Biểu diễn câu/đoạn theo ngữ cảnh; nền của tìm kiếm ngữ nghĩa và RAG |
| **CLIP** | **Một** không gian dùng chung cho **cả ảnh và chữ** | 512 | Ảnh con mèo và dòng chữ "a photo of a cat" rơi vào **gần cùng một điểm** — nền của phân loại zero-shot |
| **CNN / ViT (phân loại)** | Vector ngay **trước** lớp FC cuối (penultimate layer) | 512 – 2048 | Transfer learning, tìm ảnh tương tự, trích xuất đặc trưng |
| **Hệ gợi ý (Netflix, Spotify)** | Vector latent của **người dùng** và của **bộ phim** | 50 – 200 | Tích vô hướng hai vector = mức độ người này sẽ thích phim kia |
| **Giảm chiều cổ điển (PCA)** | Các thành phần chính | 2 – 50 | Latent space **tuyến tính** — tổ tiên của mọi thứ ở trên |
| **Tin sinh học** | Vector nhúng của mỗi tế bào / chuỗi protein | 30 – 1280 | Gom cụm loại tế bào, dự đoán cấu trúc protein (AlphaFold) |
| **CBM (đề tài của bạn)** | Lớp Bottleneck khái niệm giữa mạng | = số khái niệm (112 với CUB) | **Trường hợp đặc biệt**: mỗi chiều được **gán nhãn sẵn** một khái niệm con người hiểu được |

> **🧩 Hàng cuối cùng của bảng chính là chìa khóa của đề tài NCKH.**
> Ở **mọi dòng khác**, latent space là **ẩn theo cả hai nghĩa** — không ai biết chiều thứ 42 nghĩa là gì.
> Ở **CBM**, người ta cố tình **ép mỗi chiều phải mang một khái niệm đã được đặt tên** ("có mỏ vàng", "cánh có sọc"). Nói cách khác:
> **CBM = một latent space bị buộc phải diễn giải được.**
> Đó là toàn bộ ý tưởng của Concept Bottleneck Model, phát biểu bằng ngôn ngữ latent space. Nếu thầy hỏi "CBM khác gì AE", đây là câu trả lời gọn nhất: cùng là nút thắt, nhưng một bên để trống cho máy tự học, một bên bắt buộc phải có nghĩa với người.

## Điểm chung của mọi latent space trong bảng

Dù ở lĩnh vực nào, cả 12 dòng trên đều chia sẻ đúng bốn tính chất:

1. **Là vector số thực nhiều chiều** — không phải ảnh, không phải chữ, chỉ là một dãy số.
2. **Số chiều nhỏ hơn hẳn dữ liệu gốc** — nén là điều kiện để mô hình buộc phải khái quát hóa thay vì ghi nhớ.
3. **Khoảng cách mang ý nghĩa ngữ nghĩa** — đây là thứ khiến nó hữu dụng, không phải việc nó nhỏ.
4. **Do mô hình tự học ra, không phải do người thiết kế** — trừ đúng trường hợp CBM.

> **🎯 Cách nhận ra latent space khi đọc bài báo:** cứ tìm chỗ nào tác giả nói tới `embedding`, `representation`, `feature vector`, `code`, `bottleneck`, `hidden state`, hay ký hiệu $`z`$ / $`h`$ — gần như chắc chắn họ đang nói tới một latent space, chỉ là gọi bằng tên khác.

---

# 5. Phân biệt các thuật ngữ hay bị dùng lẫn lộn

Đây là chỗ gây rối nhất khi mới đọc bài báo, vì nhiều từ chỉ **gần như** cùng một thứ.

| Thuật ngữ | Nghĩa chính xác | Khác biệt cần nhớ |
|---|---|---|
| **Latent Space** | **Cả không gian** — tập hợp mọi vector có thể có | Là cái **không gian**, không phải một điểm |
| **Latent Vector / Latent Code (z)** | **Một điểm** cụ thể trong không gian đó | Là **một phần tử** của Latent Space |
| **Embedding** | Vector biểu diễn của một đối tượng rời rạc (từ, ảnh, người dùng) | Gần như đồng nghĩa với latent vector; hay dùng hơn trong NLP và tìm kiếm |
| **Feature Vector** | Vector đặc trưng, thường lấy từ lớp áp chót của mạng phân loại | Nhấn mạnh **công dụng** (đưa vào bộ phân loại), latent nhấn mạnh **tính ẩn** |
| **Representation** | Từ bao trùm nhất, chỉ mọi cách máy biểu diễn dữ liệu | Chữ trong "**Representation** Learning" — tên gọi chung của cả lĩnh vực |
| **Feature Map** | Đầu ra của một lớp Conv, còn giữ **cấu trúc không gian** H×W×C | Là tensor **3 chiều**, chưa bị duỗi phẳng. Xem [CNN](cnn.md) |
| **Concept Space** | Latent space mà mỗi chiều **đã được gán nhãn** một khái niệm | Chính là thứ CBM tạo ra — latent space có nghĩa |

> **💬 Nói ngắn gọn:** *Latent Space* là **cái sân**, *latent vector z* là **một người đứng trong sân**, *embedding* là cách gọi khác của người đó khi bạn đang làm NLP, và *Concept Space* là cái sân đã được kẻ vạch và ghi tên từng ô.

---

# 6. Làm được gì trong Latent Space

Vì latent space là không gian vector, ta có thể **làm toán** trên nó — và phép toán lại ra kết quả có nghĩa. Đây là điều làm nhiều người kinh ngạc khi mới gặp.

## Phép cộng trừ vector

Ví dụ kinh điển của **Word2Vec** (Mikolov, 2013):

$$
\text{vec}(\text{"king"}) - \text{vec}(\text{"man"}) + \text{vec}(\text{"woman"}) \approx \text{vec}(\text{"queen"})
$$

Điều tương tự xảy ra với ảnh khuôn mặt trong latent space của GAN:

$$
\text{(người đàn ông đeo kính)} - \text{(người đàn ông)} + \text{(người phụ nữ)} = \text{(người phụ nữ đeo kính)}
$$

> **✨ Ý nghĩa sâu xa:** phép trừ vừa rồi **cô lập được khái niệm "đeo kính"** thành một **hướng** trong không gian. Mô hình chưa bao giờ được dạy từ "kính", nhưng khái niệm đó vẫn tồn tại như một hướng đi trong latent space.
> Đây chính là nền tảng toán học của **TCAV** (Testing with Concept Activation Vectors) — một trong những phương pháp XAI quan trọng nhất và là tiền thân trực tiếp của CBM. TCAV chỉ làm đúng một việc: **đi tìm hướng vector ứng với một khái niệm**, rồi đo xem quyết định của mô hình nhạy cảm với hướng đó tới mức nào.

## Nội suy (interpolation)

Đi dần từ điểm này sang điểm kia trên đường thẳng nối chúng:

$$
z_{\alpha} = (1-\alpha)\, z_A + \alpha\, z_B, \qquad \alpha \in [0, 1]
$$

Nếu latent space **liên tục**, mọi điểm giữa đường đều giải mã ra kết quả có nghĩa (số 3 biến dần thành số 8). Nếu không liên tục, phần giữa ra nhiễu. Đây đúng là khác biệt giữa AE và VAE — xem [Variational Autoencoder (VAE)](vae.md).

## Tìm kiếm theo ngữ nghĩa

Muốn tìm ảnh giống một ảnh cho trước: mã hóa tất cả thành vector, rồi **tìm vector gần nhất** theo cosine similarity. Toàn bộ ngành **vector database** (Pinecone, FAISS, Qdrant) và kỹ thuật **RAG** đứng trên đúng một ý tưởng này.

## Phát hiện bất thường

Dữ liệu bình thường rơi vào vùng dày đặc của latent space; dữ liệu lạ rơi ra ngoài rìa và cho Reconstruction Loss cao. Đây là ứng dụng phổ biến nhất của Autoencoder trong công nghiệp.

---

# 7. Làm sao nhìn thấy được Latent Space?

Latent space có 128 hay 512 chiều — mắt người không hình dung nổi. Có ba cách thông dụng để "nhìn" nó:

| Cách | Làm gì | Nhìn ra được điều gì |
|---|---|---|
| **Chiếu xuống 2D** (t-SNE, UMAP, PCA) | Ép 128 chiều xuống 2 chiều rồi vẽ lên mặt phẳng, tô màu theo nhãn | Các lớp có **tách thành cụm riêng** không. Cách kiểm tra nhanh nhất xem biểu diễn có tốt hay không |
| **Nội suy** (interpolation) | Đi từ mẫu A sang mẫu B, giải mã từng bước | Không gian có **liên tục** không, hay có lỗ hổng |
| **Đi dọc một chiều** (latent traversal) | Giữ nguyên z, chỉ kéo **một** chiều từ −3 đến +3 | Chiều đó có mang **một khái niệm riêng** không — tức mức độ **disentangled** |

> **⚠️ Lưu ý khi dùng t-SNE — rất hay bị hiểu sai trong báo cáo:** t-SNE chỉ bảo toàn **quan hệ lân cận cục bộ**, không bảo toàn khoảng cách toàn cục. Vì vậy **kích thước của các cụm** và **khoảng cách giữa các cụm** trên hình t-SNE **không mang ý nghĩa gì cả**. Chỉ nên kết luận "các lớp có tách rời nhau hay không", đừng kết luận "cụm A gần cụm B hơn cụm C".

---

# 8. Liên hệ trực tiếp với đề tài NCKH

> **🔗 Toàn bộ hướng XAI dựa trên khái niệm có thể phát biểu lại bằng ngôn ngữ latent space:**
>
> **Vấn đề gốc.** Mạng nơ-ron ra quyết định dựa trên một vector latent 2048 chiều mà **không ai đọc hiểu được**. Đó chính là "hộp đen".
>
> **Hướng giải quyết 1 — hậu kiểm (post-hoc).** Giữ nguyên mô hình, đi tìm ý nghĩa trong latent space đã có: **TCAV** tìm hướng ứng với khái niệm; **Sparse Autoencoder** trong mechanistic interpretability tách latent thành nhiều đặc trưng thưa dễ đọc hơn.
>
> **Hướng giải quyết 2 — thiết kế sẵn (intrinsic).** Bắt latent space phải có nghĩa **ngay từ đầu**: đó là **CBM**. Mỗi chiều được gán một khái niệm, và quyết định cuối cùng chỉ được phép dựa trên các chiều đó.
>
> **Chỗ đứng của β-VAE.** Nằm giữa hai hướng: khái niệm **tự nổi lên** mà không cần nhãn, nhưng lại **không kiểm soát được** chúng là khái niệm gì.
>
> **Khoảng trống nghiên cứu đáng chú ý:** liệu có cách nào có được tính diễn giải của CBM mà **không phải trả giá bằng nhãn khái niệm thủ công**? Đây đúng là câu hỏi mà Label-free CBM và các hướng dùng CLIP đang cố trả lời.

> **🕳️ Một cạm bẫy phải biết — Concept Leakage.** Ngay cả trong CBM, latent space vẫn có thể "gian lận": lớp bottleneck khái niệm học cách **giấu thêm thông tin không liên quan tới khái niệm** vào chính các giá trị khái niệm đó (ví dụ dùng giá trị 0.63 thay vì 0 hoặc 1 để mã hóa lén một thứ khác). Khi đó phần giải thích **trông thì có nghĩa nhưng thực ra không phản ánh đúng thứ mô hình đang dùng**.
> Đây là lý do phải phân biệt **faithfulness** (giải thích có đúng với những gì mô hình thật sự làm không) và **plausibility** (giải thích nghe có hợp lý với người không). Xem **Đánh giá chất lượng lời giải thích (Faithfulness & Plausibility)**.

---

# 9. Nguồn học

- [Understanding Latent Space in Machine Learning — Ekin Tiu (Towards Data Science)](https://towardsdatascience.com/understanding-latent-space-in-machine-learning-de5a7c687d8d) — bài giới thiệu ngắn gọn, dễ đọc nhất để bắt đầu.
- [From Autoencoder to Beta-VAE — Lilian Weng](https://lilianweng.github.io/posts/2018-08-12-vae/) — nói rất kỹ về cấu trúc latent space và tính disentanglement.
- [Deep Learning Book — Chapter 15: Representation Learning (Goodfellow et al.)](https://www.deeplearningbook.org/contents/representation.html) — **chương sách chuẩn để trích dẫn học thuật** khi viết về biểu diễn.
- [Efficient Estimation of Word Representations in Vector Space — Mikolov et al., 2013](https://arxiv.org/abs/1301.3781) — bài Word2Vec gốc, nơi phép "king − man + woman" xuất hiện.
- [Interpretability Beyond Feature Attribution: TCAV — Kim et al., ICML 2018](https://arxiv.org/abs/1711.11279) — **bài phải đọc cho đề tài của bạn**: định nghĩa khái niệm như một hướng vector trong latent space.
- [High-Resolution Image Synthesis with Latent Diffusion Models — Rombach et al., CVPR 2022](https://arxiv.org/abs/2112.10752) — bài Stable Diffusion, cho thấy vì sao làm việc trong latent space lại rẻ hơn pixel space rất nhiều.
- [Distill — How to Use t-SNE Effectively](https://distill.pub/2016/misread-tsne/) — bài tương tác giải thích các bẫy khi đọc hình t-SNE.

> **🧪 Bài thực hành liên kết mọi thứ trong trang này (khoảng một buổi):**
> Huấn luyện một Autoencoder trên MNIST với `code size = 2`, rồi vẽ toàn bộ tập test lên mặt phẳng và tô màu theo chữ số. Bạn sẽ **nhìn thấy tận mắt một latent space**.
> Sau đó làm ba việc: (1) thử nội suy giữa một số 3 và một số 8; (2) làm lại y hệt với VAE và so sánh hai tấm hình; (3) thử tính `vec(số 8) − vec(số 3)` xem hướng đó có nghĩa gì không.
> Ba thí nghiệm nhỏ này chính là phiên bản thu nhỏ của TCAV, của Latent Diffusion và của β-VAE.

---

# 10. Ghi chú của mình

*(Điền sau khi học: chỗ nào còn vướng, câu hỏi cần hỏi thầy.)*
