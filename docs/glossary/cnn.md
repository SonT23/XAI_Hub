# CNN

| Term (EN) | Tiếng Việt | Viết tắt | Định nghĩa ngắn | Dễ nhầm với |
|---|---|---|---|---|
| Batch Normalization | Chuẩn hóa theo lô | BN | Chuẩn hóa lại phân phối giá trị trong mỗi kênh dựa trên thống kê của batch hiện tại. Giúp mạng sâu hội tụ nhanh và ổn định hơn nhiều. Thứ tự chuẩn: Conv → BatchNorm → ReLU. | Chuẩn hóa dữ liệu đầu vào (chia 255) — việc đó chỉ làm một lần ở Input, còn BN nằm giữa mạng và học được tham số |
| Convolution | Phép tích chập |  | Phép trượt một Kernel qua ảnh, tại mỗi vị trí nhân từng phần tử rồi cộng dồn để cho ra một giá trị. |  |
| Convolutional Neural Network | Mạng nơ-ron tích chập | CNN | Mạng chuyên xử lý dữ liệu dạng lưới như ảnh, dùng phép tích chập để mỗi nơ-ron chỉ nhìn một vùng cục bộ và chia sẻ trọng số giữa các vùng. |  |
| Data Augmentation | Tăng cường dữ liệu |  | Sinh thêm mẫu huấn luyện bằng cách biến đổi ảnh gốc (lật, xoay, cắt, đổi màu). Cần thiết vì CNN chỉ bất biến với dịch chuyển nhỏ, không tự bất biến với xoay hay co giãn. | Denoising Autoencoder — cũng làm hỏng đầu vào, nhưng mục tiêu là học biểu diễn bền vững chứ không phải tăng số lượng mẫu |
| Feature Map | Bản đồ đặc trưng |  | Kết quả đầu ra sau khi một filter quét hết ảnh, cho biết đặc trưng đó xuất hiện mạnh ở đâu trên ảnh. |  |
| Feature Vector | Vector đặc trưng |  | Vector biểu diễn lấy từ lớp áp chót (penultimate layer) của một mạng phân loại, trước khi đưa vào lớp quyết định cuối. Đây chính là thứ được dùng khi nói trích xuất đặc trưng từ CNN. | Feature Map — là tensor 3 chiều còn giữ cấu trúc không gian; feature vector đã bị duỗi phẳng |
| Flatten | Làm phẳng |  | Duỗi một tensor nhiều chiều (ví dụ 4x4x128) thành vector 1 chiều (2048) để đưa vào lớp Fully Connected. Không có tham số, nhưng vứt bỏ hoàn toàn cấu trúc không gian. | Global Average Pooling — cùng mục đích chuyển sang FC nhưng lấy trung bình mỗi kênh thay vì duỗi hết, nên gọn hơn nhiều |
| Fully Connected Layer | Lớp kết nối đầy đủ | FC / Dense | Lớp mà mỗi nơ-ron nối với toàn bộ nơ-ron lớp trước. Đặt ở cuối CNN để tổng hợp đặc trưng và đưa ra quyết định. |  |
| Global Average Pooling | Gộp trung bình toàn cục | GAP | Lấy trung bình toàn bộ mỗi kênh của Feature Map, biến HxWxC thành đúng C số. Thay thế hiện đại cho Flatten + FC lớn, cắt được phần lớn tham số và là cơ chế giúp Grad-CAM hoạt động. | Max Pooling 2x2 — chỉ giảm một nửa kích thước, còn GAP nén cả kênh về một số duy nhất |
| Grad-CAM | Grad-CAM |  | Dùng gradient tại lớp tích chập cuối để tạo heatmap chỉ vùng ảnh mô hình nhìn vào. Chỉ trả lời được 'ở đâu' chứ không phải 'cái gì'. |  |
| Inductive Bias | Định kiến quy nạp |  | Những giả định được cài sẵn vào kiến trúc mô hình. CNN có inductive bias mạnh (tính cục bộ), ViT có bias yếu nên cần nhiều dữ liệu hơn. |  |
| Kernel / Filter | Bộ lọc |  | Ma trận trọng số nhỏ (ví dụ 3x3) trượt qua ảnh. Mỗi filter học nhận diện một loại đặc trưng: cạnh dọc, cạnh ngang, màu sắc, họa tiết. |  |
| Padding | Viền đệm |  | Thêm pixel (thường giá trị 0) quanh viền ảnh trước khi tích chập, để kiểm soát kích thước đầu ra và không bỏ sót thông tin ở rìa. |  |
| Pooling | Phép gộp |  | Giảm kích thước không gian của Feature Map. Max Pooling lấy giá trị lớn nhất mỗi vùng, Average Pooling lấy giá trị trung bình. |  |
| Receptive Field | Vùng tiếp nhận |  | Vùng ảnh gốc mà một nơ-ron nhìn thấy. Càng ở lớp sâu thì vùng này càng rộng. |  |
| ReLU | Hàm kích hoạt ReLU | ReLU | Rectified Linear Unit: f(x) = max(0, x). Giữ nguyên số dương, ép mọi số âm về 0. Là hàm kích hoạt mặc định cho lớp ẩn của CNN vì tạo được tính phi tuyến mà tính toán rất rẻ. | Sigmoid (dùng ở đầu ra khi cần giá trị trong [0,1]); LeakyReLU (cho phép số âm đi qua một chút để tránh nơ-ron chết) |
| Stride | Bước trượt |  | Số pixel mà filter dịch chuyển mỗi lần. Stride lớn làm Feature Map nhỏ nhanh hơn nhưng dễ bỏ sót chi tiết. |  |
| Transfer Learning | Học chuyển giao |  | Giữ nguyên phần trích xuất đặc trưng của một mạng đã huấn luyện trên tập dữ liệu lớn (ví dụ ImageNet), chỉ thay và huấn luyện lại vài lớp cuối cho bài toán mới. Hoạt động được vì phần Conv học đặc trưng dùng chung cho mọi loại ảnh. | Fine-tuning — là một cách làm transfer learning, trong đó mở khóa và huấn luyện lại cả phần backbone với learning rate rất nhỏ |
| Translation Invariance | Bất biến tịnh tiến |  | Một đặc trưng dù xuất hiện ở vị trí nào trong ảnh vẫn được nhận diện như nhau. |  |
| Transposed Convolution | Tích chập chuyển vị |  | Phép ngược của tích chập, dùng để tăng kích thước ảnh. Decoder của Convolutional Autoencoder dùng phép này để khôi phục kích thước gốc. | Thường bị gọi sai là Deconvolution — thực ra không phải phép nghịch đảo toán học. |
| Weight Sharing | Chia sẻ trọng số |  | Cùng một filter được dùng cho mọi vị trí trên ảnh, giúp giảm mạnh số tham số cần huấn luyện so với lớp Dense. |  |
