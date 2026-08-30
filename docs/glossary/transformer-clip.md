# Transformer/CLIP

| Term (EN) | Tiếng Việt | Viết tắt | Định nghĩa ngắn | Dễ nhầm với |
|---|---|---|---|---|
| Attention | Cơ chế chú ý |  | Cơ chế cho phép mô hình quyết định nên tập trung vào phần nào của đầu vào, bằng cách tính tổng có trọng số của các Value dựa trên độ khớp giữa Query và Key. |  |
| CLIP | CLIP (học tương phản ảnh - ngôn ngữ) |  | Mô hình huấn luyện trên 400 triệu cặp ảnh-chữ, học một không gian nhúng chung cho cả ảnh lẫn văn bản. Là công cụ chấm điểm khái niệm tự động trong Label-free CBM. |  |
| CLS Token | Token phân lớp |  | Token đặc biệt thêm vào đầu chuỗi; vectơ tại vị trí này sau các lớp Transformer được dùng làm biểu diễn tổng thể của cả ảnh. |  |
| Contrastive Learning | Học tương phản |  | Học bằng cách kéo các cặp đúng lại gần nhau và đẩy các cặp sai ra xa trong không gian nhúng. |  |
| Cosine Similarity | Độ tương đồng cosine |  | Đo độ giống nhau giữa hai vectơ bằng góc giữa chúng, bỏ qua độ dài. CLIP dùng phép này để so khớp vectơ ảnh với vectơ văn bản. |  |
| Embedding | Vectơ nhúng |  | Biểu diễn một đối tượng (từ, ảnh, khái niệm) dưới dạng vectơ số thực, sao cho các đối tượng giống nhau nằm gần nhau. |  |
| Foundation Model | Mô hình nền tảng |  | Mô hình lớn huấn luyện trên lượng dữ liệu khổng lồ, dùng làm nền cho nhiều tác vụ hạ nguồn khác nhau. CLIP, GPT, ViT quy mô lớn đều thuộc nhóm này. |  |
| Inductive Bias | Định kiến quy nạp |  | Những giả định được cài sẵn vào kiến trúc mô hình. CNN có inductive bias mạnh (tính cục bộ), ViT có bias yếu nên cần nhiều dữ liệu hơn. |  |
| Multi-Head Attention | Chú ý đa đầu |  | Chạy song song nhiều đầu Attention độc lập, mỗi đầu học một loại quan hệ khác nhau, rồi nối kết quả lại. |  |
| Patch Embedding | Nhúng mảnh ảnh |  | Chia ảnh thành các ô vuông nhỏ (ví dụ 16x16), làm phẳng rồi chiếu tuyến tính thành vectơ. Tên ViT-B/16 chính là chỉ kích thước patch. |  |
| Positional Encoding | Mã hóa vị trí |  | Vectơ cộng thêm vào đầu vào để mô hình biết thứ tự/vị trí, vì bản thân Attention không phân biệt thứ tự. |  |
| Prompt Engineering | Thiết kế câu nhắc |  | Việc chọn cách diễn đạt câu đầu vào để mô hình cho kết quả tốt nhất, ví dụ mẫu 'a photo of a {tên lớp}' trong CLIP. |  |
| Query / Key / Value | Truy vấn / Khóa / Giá trị | Q/K/V | Ba vai trò trong Attention, ví như tra cứu thư viện: Query là câu hỏi, Key là nhãn trên sách, Value là nội dung sách. |  |
| Residual Connection | Kết nối tắt |  | Đường nối cộng thẳng đầu vào của một khối vào đầu ra của nó, giúp huấn luyện được mạng rất sâu mà không bị triệt tiêu gradient. |  |
| Self-Attention | Tự chú ý |  | Dạng Attention mà Q, K, V đều sinh ra từ cùng một chuỗi đầu vào - mô hình tự hỏi các phần của chính nó. |  |
| Transformer | Mạng Transformer |  | Kiến trúc dựa hoàn toàn trên cơ chế Attention, cho phép mọi phần tử trong chuỗi nhìn trực tiếp vào nhau và xử lý song song. |  |
| Vision Transformer | Transformer thị giác | ViT | Áp dụng Transformer cho ảnh bằng cách cắt ảnh thành các patch và coi mỗi patch như một từ trong chuỗi. |  |
| Vision-Language Model | Mô hình thị giác – ngôn ngữ | VLM | Mô hình xử lý đồng thời ảnh và văn bản trong một không gian nhúng chung. CLIP và G-DINO là ví dụ. Được dùng để tự động chấm điểm khái niệm trong Label-free CBM. |  |
| Zero-shot Learning | Học không mẫu |  | Mô hình phân loại được cả những lớp chưa từng được huấn luyện riêng, nhờ mô tả bằng ngôn ngữ tự nhiên. |  |
