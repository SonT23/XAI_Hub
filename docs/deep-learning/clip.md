# CLIP & Mô hình đa phương thức (Vision-Language)

> **🎯 Vì sao phần này cực kỳ quan trọng với đề tài:** CLIP là thứ giúp **xóa bỏ điểm yếu lớn nhất của CBM** — chi phí gán nhãn khái niệm. Thay vì thuê chuyên gia gán 312 thuộc tính cho 11.788 ảnh, ta dùng CLIP chấm điểm tự động. Đây là nền tảng của Label-free CBM và LaBo.

## CLIP là gì

**CLIP (Contrastive Language-Image Pre-training)** do OpenAI công bố năm 2021, được huấn luyện trên khoảng **400 triệu cặp (ảnh, mô tả văn bản)** thu thập từ Internet. Điểm đột phá: nó học được một **không gian nhúng chung (shared embedding space)** cho cả ảnh lẫn chữ — trong đó ảnh một con mèo và dòng chữ "a photo of a cat" nằm gần nhau.

## Cơ chế học tương phản (Contrastive Learning)

Với một lô (batch) gồm N cặp (ảnh, chữ):

1. **Image Encoder** (thường là ViT hoặc ResNet) biến mỗi ảnh thành một vector.
2. **Text Encoder** (Transformer) biến mỗi câu mô tả thành một vector.
3. Tính ma trận độ tương đồng N×N giữa mọi cặp ảnh–chữ (bằng cosine similarity).
4. **Mục tiêu:** đẩy N cặp đúng (trên đường chéo) lại gần nhau, đồng thời đẩy N²−N cặp sai ra xa. Đây chính là ý nghĩa của từ "contrastive".

Không cần bất kỳ nhãn thủ công nào — chính các câu mô tả có sẵn trên web đóng vai trò giám sát.

## Zero-shot classification

Sau khi huấn luyện, CLIP phân loại được **các lớp chưa từng được huấn luyện riêng**: ta viết các câu mô tả dạng "a photo of a {tên lớp}", đưa qua Text Encoder, rồi xem vector ảnh gần câu nào nhất. Đây gọi là **prompt engineering cho thị giác**.

## Ứng dụng trực tiếp vào CBM

> **🔑 Đây là ý tưởng cần nắm kỹ nhất trong toàn bộ trang này.**
> Thay vì hỏi "ảnh này là loài chim gì", ta hỏi CLIP: ảnh này gần với câu **"a photo of a bird with a red beak"** đến mức nào? Điểm tương đồng thu được chính là **giá trị của khái niệm "mỏ đỏ"** — thay thế hoàn toàn nhãn do chuyên gia gán.

Quy trình của **Label-free CBM** (Oikarinen et al., 2023):

1. Hỏi một **LLM** (GPT): "những đặc điểm nhìn thấy được của loài X là gì?" → thu được danh sách khái niệm dạng văn bản.
2. Dùng **CLIP** chấm điểm từng khái niệm trên từng ảnh → thu được ma trận khái niệm thay cho nhãn thủ công.
3. Huấn luyện lớp dự đoán nhãn tuyến tính trên ma trận đó — giống hệt CBM gốc từ bước này trở đi.

## Hạn chế cần biết (cơ hội nghiên cứu)

- CLIP **kế thừa định kiến (bias)** từ dữ liệu web — ảnh hưởng tính công bằng của mô hình hạ nguồn.
- Điểm số CLIP **chưa được hiệu chỉnh (uncalibrated)** — liên hệ trực tiếp với phần calibration trong trang Đánh giá chất lượng lời giải thích.
- CLIP yếu với **khái niệm chuyên ngành hẹp** (thuật ngữ y khoa như "gai xương", "xơ hóa") vì dữ liệu web ít xuất hiện các cặp này — **đây là một khe hở nghiên cứu rất đáng giá** nếu bạn muốn làm CBM cho ảnh y tế.
- CLIP kém trong đếm số lượng và hiểu quan hệ không gian giữa các vật thể.

## Nguồn học

### Bài báo gốc

- [Learning Transferable Visual Models From Natural Language Supervision – Radford et al., 2021](https://arxiv.org/abs/2103.00020) — bài CLIP gốc.
- [Label-free Concept Bottleneck Models – Oikarinen et al., 2023](https://arxiv.org/abs/2304.06129) — ứng dụng CLIP vào CBM.
- [LaBo: Language in a Bottle – Yang et al., 2023](https://arxiv.org/abs/2211.11158) — dùng LLM sinh khái niệm cho CBM.

### Giải thích & thực hành

- [OpenAI – CLIP: Connecting Text and Images (blog chính thức)](https://openai.com/index/clip/) — giải thích trực quan, nhiều hình minh họa.
- [OpenAI CLIP – GitHub repository](https://github.com/openai/CLIP) — code và model pre-trained, chạy được ngay.
- [OpenCLIP](https://github.com/mlfoundations/open_clip) — bản mã nguồn mở với nhiều checkpoint huấn luyện trên LAION.
- [Lil'Log – Contrastive Representation Learning](https://lilianweng.github.io/posts/2021-05-31-contrastive/) — tổng quan học thuật về học tương phản nói chung.
