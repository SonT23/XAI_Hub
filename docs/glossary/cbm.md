# CBM

| Term (EN) | Tiếng Việt | Viết tắt | Định nghĩa ngắn | Dễ nhầm với |
|---|---|---|---|---|
| Bottleneck | Nút thắt cổ chai |  | Lớp hẹp nhất nằm giữa Encoder và Decoder, chứa biểu diễn nén của dữ liệu. Là phần quan trọng nhất và trớ trêu thay lại là phần nhỏ nhất của mạng. | Latent Space — Bottleneck là lớp vật lý, Latent Space là không gian toán học mà vectơ tại nút thắt nằm trong. |
| CLIP | CLIP (học tương phản ảnh - ngôn ngữ) |  | Mô hình huấn luyện trên 400 triệu cặp ảnh-chữ, học một không gian nhúng chung cho cả ảnh lẫn văn bản. Là công cụ chấm điểm khái niệm tự động trong Label-free CBM. |  |
| Concept | Khái niệm |  | Một thuộc tính có nghĩa với con người, do người tạo hoặc chuyên gia định nghĩa. Ví dụ: 'mỏ đỏ', 'có gai xương', 'hẹp khe khớp'. |  |
| Concept Accuracy | Độ chính xác khái niệm |  | Độ chính xác của riêng tầng dự đoán khái niệm (x-c), đo tách biệt với độ chính xác tác vụ cuối (c-y). |  |
| Concept Activation Vector | Vectơ kích hoạt khái niệm | CAV | Vectơ pháp tuyến của siêu phẳng tách ảnh có khái niệm với ảnh không có, trong không gian activation. Đại diện cho hướng của khái niệm đó. |  |
| Concept Bottleneck Model | Mô hình nút thắt khái niệm | CBM | Kiến trúc ép dữ liệu đi qua một tầng khái niệm con người đọc được trước khi ra nhãn cuối: x - c - y, thay vì đi thẳng x - y. |  |
| Concept Entanglement | Rối khái niệm |  | Khái niệm học được lại mã hóa thông tin của các khái niệm KHÁC không liên quan. Cùng với leakage và impurity, đây là ba bệnh của VLM-CBM. | Disentangled Representation — là trạng thái ngược lại, mục tiêu cần đạt. |
| Concept Leakage | Rò rỉ khái niệm |  | Hiện tượng giá trị khái niệm bí mật mã hóa thêm thông tin ngoài ý nghĩa đã nêu, khiến mô hình vẫn chính xác nhưng mất tính minh bạch. Đây là điểm yếu lớn nhất của CBM và là khe hở nghiên cứu đáng giá. |  |
| Concept Predictor | Mạng dự đoán khái niệm |  | Mô đun đầu của CBM, nhận ảnh đầu vào x và dự đoán vectơ gồm K khái niệm. |  |
| Concept Space | Không gian khái niệm |  | Một Latent Space mà MỖI CHIỀU đã được gán nhãn một khái niệm con người hiểu được. Đây chính là thứ CBM tạo ra — có thể hiểu CBM là một latent space bị buộc phải diễn giải được. | Latent Space thông thường — không ai biết chiều thứ 42 nghĩa là gì |
| Data Annotation | Gán nhãn dữ liệu |  | Quá trình con người gán nhãn cho dữ liệu thô. Với CBM, phải gán cả nhãn lớp lẫn nhãn khái niệm nên chi phí rất lớn. |  |
| Independent Bottleneck | Huấn luyện độc lập |  | Hai mạng (x-c và c-y) huấn luyện hoàn toàn tách biệt. Mạng dự đoán nhãn học trên nhãn khái niệm chuẩn, không biết gì về lỗi của mạng trước. |  |
| Intervention Curve | Đường cong can thiệp |  | Đồ thị thể hiện độ chính xác tăng ra sao khi sửa đúng dần từng khái niệm. Đường dốc lên là dấu hiệu tốt; đường phẳng báo hiệu concept leakage. |  |
| Intrinsic (Ante-hoc) Interpretability | Giải thích nội tại |  | Tính giải thích được thiết kế sẵn vào kiến trúc mô hình, nên lời giải thích chính là đường đi thật của dữ liệu. CBM thuộc nhóm này. | Post-hoc |
| Joint Bottleneck | Huấn luyện đồng thời |  | Cả hai mô đun huấn luyện cùng lúc với Loss = Loss_y + lambda * Loss_c. Linh hoạt nhất nhưng dễ gây concept leakage nếu lambda quá nhỏ. |  |
| Knowledge Limits (Principle 4) | Giới hạn tri thức |  | Nguyên tắc 4 của NIST: hệ thống chỉ hoạt động trong điều kiện nó được thiết kế và khi đủ tự tin. Hai con đường chạm giới hạn: nằm ngoài miền hoạt động, và độ tin cậy quá thấp. CBM gốc không đề cập nguyên tắc này. |  |
| Label Predictor | Mạng dự đoán nhãn |  | Mô đun sau của CBM, nhận vectơ khái niệm và đưa ra nhãn phân loại cuối cùng. Thường chỉ là một lớp tuyến tính đơn giản để giữ tính minh bạch. |  |
| Sequential Bottleneck | Huấn luyện nối tiếp |  | Mạng thứ hai học trên KẾT QUẢ DỰ ĐOÁN khái niệm của mạng thứ nhất, nên quen với lỗi và nhiễu thực tế. | Independent — khác nhau ở chỗ dùng nhãn chuẩn hay dùng dự đoán. |
| TCAV | Kiểm thử bằng vectơ kích hoạt khái niệm |  | Phương pháp post-hoc đo xem một khái niệm (ví dụ 'sọc') ảnh hưởng bao nhiêu đến dự đoán của một lớp. Là tiền đề trực tiếp của CBM. |  |
| Test-time Intervention | Can thiệp lúc suy luận |  | Chuyên gia sửa trực tiếp giá trị khái niệm bị dự đoán sai rồi cho mô hình tính lại nhãn cuối. Đây là khả năng độc đáo mà các phương pháp post-hoc không có. |  |
| Vision-Language Model | Mô hình thị giác – ngôn ngữ | VLM | Mô hình xử lý đồng thời ảnh và văn bản trong một không gian nhúng chung. CLIP và G-DINO là ví dụ. Được dùng để tự động chấm điểm khái niệm trong Label-free CBM. |  |
