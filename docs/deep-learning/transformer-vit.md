# Transformer & Vision Transformer (ViT)

> **🎯 Vì sao phải học phần này cho đề tài XAI/CBM?** Bài báo CBM gốc (2020) dùng Inception-v3 — kiến trúc từ 2015. Nhưng **mọi bài CBM từ 2023 trở đi đều dựa trên ViT/CLIP**. Không nắm phần này thì không đọc được các bài mới nhất, cũng không làm được hướng label-free CBM.

## Phần 1: Cơ chế Attention

### Vấn đề mà Attention giải quyết

Trước Transformer, xử lý chuỗi dùng RNN/LSTM — đọc tuần tự từng phần tử, nên (1) không song song hóa được và (2) thông tin ở đầu chuỗi bị "quên" khi đến cuối. Attention cho phép **mọi phần tử nhìn trực tiếp vào mọi phần tử khác** trong một bước duy nhất.

### Query, Key, Value — trực giác

Hình dung việc tra cứu trong thư viện:

- **Query (Q):** câu hỏi bạn đang cần trả lời ("tôi cần thông tin về loại chim này").
- **Key (K):** nhãn dán trên từng cuốn sách ("cuốn này nói về chim").
- **Value (V):** nội dung thực sự bên trong cuốn sách.

Mô hình tính **độ tương đồng giữa Q và từng K** (bằng tích vô hướng), chuẩn hóa thành trọng số bằng Softmax, rồi lấy **tổng có trọng số của các V**. Kết quả: mỗi vị trí thu được một biểu diễn mới đã "hỏi ý kiến" toàn bộ các vị trí khác.

$$
\text{Attention}(Q,K,V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V
$$

Phép chia cho căn bậc hai của $`d_k`$ (số chiều của Key) là để tránh giá trị tích vô hướng quá lớn làm Softmax bị bão hòa (gradient gần bằng 0).

### Self-Attention và Multi-Head

- **Self-Attention:** Q, K, V đều sinh ra từ **cùng một chuỗi đầu vào** — mô hình tự hỏi các phần của chính nó.
- **Multi-Head Attention:** chạy song song nhiều "đầu" attention độc lập, mỗi đầu học một loại quan hệ khác nhau (đầu này chú ý màu sắc, đầu kia chú ý hình dạng), rồi nối kết quả lại.

## Phần 2: Vision Transformer (ViT)

### Ý tưởng cốt lõi

Transformer sinh ra cho văn bản (chuỗi từ). ViT (Dosovitskiy et al., 2020) đặt câu hỏi: **nếu coi ảnh như một chuỗi thì sao?** Câu trả lời: cắt ảnh thành các ô vuông nhỏ (patch) và coi mỗi patch như một "từ".

### Luồng xử lý

1. **Patch Embedding:** chia ảnh (ví dụ 224×224) thành các patch 16×16 → được 196 patch. Mỗi patch được làm phẳng và chiếu tuyến tính thành một vector. Đây chính lý do tên mô hình là **ViT-B/16** (patch size 16).
2. **Positional Encoding:** vì Attention không biết thứ tự, phải cộng thêm vector vị trí để mô hình biết patch nào nằm ở đâu trong ảnh.
3. **CLS Token:** thêm một token đặc biệt ở đầu chuỗi. Sau khi qua các lớp Transformer, vector tại vị trí này được dùng làm **biểu diễn tổng thể của cả ảnh** — chính là thứ sẽ được đưa vào tầng khái niệm nếu bạn xây CBM trên ViT.
4. **Transformer Encoder:** lặp L lần khối gồm Multi-Head Self-Attention + MLP, kèm Layer Normalization và kết nối tắt (residual).
5. **MLP Head:** lớp phân loại cuối cùng đặt trên CLS token.

## So sánh ViT với CNN

| Tiêu chí | CNN | ViT |
|---|---|---|
| Phạm vi nhìn | Cục bộ, mở rộng dần theo độ sâu | Toàn cục ngay từ lớp đầu tiên |
| Inductive bias | Mạnh (tính cục bộ, bất biến tịnh tiến) | Yếu — phải tự học từ dữ liệu |
| Nhu cầu dữ liệu | Huấn luyện tốt với dữ liệu vừa | Cần dữ liệu rất lớn hoặc pre-training |
| Khả năng giải thích | Grad-CAM trên feature map | Attention map theo patch |

> **💡 Liên hệ với XAI:** Attention map của ViT trông rất giống một lời giải thích, nhưng cộng đồng nghiên cứu đã chỉ ra rằng **"Attention is not Explanation"** — trọng số attention cao không chứng minh đặc trưng đó thực sự quyết định đầu ra. Đây lại là một lập luận nữa ủng hộ hướng intrinsic (CBM) thay vì dựa vào attention.

## Nguồn học

### Bài báo gốc

- [Attention Is All You Need – Vaswani et al., 2017](https://arxiv.org/abs/1706.03762) — bài khai sinh Transformer.
- [An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale – Dosovitskiy et al., 2020](https://arxiv.org/abs/2010.11929) — bài ViT gốc.
- [Attention is not Explanation – Jain & Wallace, 2019](https://arxiv.org/abs/1902.10186) — quan trọng cho phần lập luận XAI.

### Giải thích trực quan (nên đọc trước bài báo gốc)

- [The Illustrated Transformer – Jay Alammar](https://jalammar.github.io/illustrated-transformer/) — tài liệu trực quan nổi tiếng nhất, giải thích Q/K/V bằng hình vẽ từng bước.
- [3Blue1Brown – Visualizing Attention (video)](https://www.youtube.com/watch?v=eMlx5fFNoYc) — giải thích toán học của attention bằng hình ảnh động.
- [Lil'Log – The Transformer Family](https://lilianweng.github.io/posts/2023-01-27-the-transformer-family-v2/) — tổng hợp hệ thống, chất lượng học thuật cao.

### Thực hành và code

- [The Annotated Transformer – Harvard NLP](https://nlp.seas.harvard.edu/annotated-transformer/) — cài đặt Transformer từng dòng bằng PyTorch song song với bài báo.
- [Hugging Face – Transformers Course](https://huggingface.co/learn/nlp-course) — khóa miễn phí, thực hành trực tiếp.
- [timm – PyTorch Image Models](https://github.com/huggingface/pytorch-image-models) — thư viện chứa mọi biến thể ViT pre-trained, dùng được ngay làm backbone.

### Bài giảng đại học

- [CS231n – Stanford (có phần Attention & Transformers)](https://cs231n.github.io/)
- [CS25: Transformers United – Stanford](https://web.stanford.edu/class/cs25/) — khóa chuyên sâu riêng về Transformer, có video công khai.
