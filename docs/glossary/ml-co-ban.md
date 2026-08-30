# ML cơ bản

| Term (EN) | Tiếng Việt | Viết tắt | Định nghĩa ngắn | Dễ nhầm với |
|---|---|---|---|---|
| Ablation Study | Nghiên cứu loại bỏ |  | Thí nghiệm lần lượt bỏ từng thành phần của mô hình để chứng minh thành phần đó thực sự đóng góp vào kết quả. Bắt buộc có trong bài báo tốt. |  |
| Accuracy | Độ chính xác |  | Tỷ lệ dự đoán đúng trên tổng số mẫu. Dễ gây hiểu lầm khi dữ liệu mất cân bằng giữa các lớp. |  |
| Anomaly Detection | Phát hiện bất thường |  | Dùng Reconstruction Loss làm tín hiệu: dữ liệu giống tập huấn luyện cho loss thấp, dữ liệu bất thường cho loss cao vượt ngưỡng. |  |
| Backpropagation | Lan truyền ngược |  | Thuật toán tính gradient của hàm Loss theo từng trọng số bằng cách lan truyền sai số ngược từ đầu ra về đầu vào, dựa trên quy tắc chuỗi đạo hàm. |  |
| Baseline | Mô hình đối chuẩn |  | Mô hình hoặc phương pháp có sẵn dùng làm mốc so sánh cho phương pháp mới. Bài báo khoa học bắt buộc phải so với baseline hợp lý. |  |
| Batch Size | Kích thước lô |  | Số mẫu dữ liệu đưa vào mô hình trong một lần cập nhật trọng số. |  |
| Binary Cross-Entropy | Entropy chéo nhị phân | BCE | Hàm Loss dùng khi dữ liệu là nhị phân hoặc đã chuẩn hóa về [0,1]. Coi mỗi điểm như một bài toán xác suất độc lập. | MSE — chọn theo bản chất dữ liệu: liên tục dùng MSE, nhị phân/chuẩn hóa dùng BCE. |
| Calibration | Hiệu chỉnh xác suất |  | Mức độ mà điểm tin cậy của mô hình phản ánh đúng xác suất thực tế. Quan trọng khi đánh giá độ tin cậy của khái niệm trong CBM và của điểm số CLIP. |  |
| Confusion Matrix | Ma trận nhầm lẫn |  | Bảng đối chiếu dự đoán với thực tế, gồm 4 ô: TP, TN, FP, FN. Mọi chỉ số phân loại đều suy ra từ bảng này. |  |
| Data Annotation | Gán nhãn dữ liệu |  | Quá trình con người gán nhãn cho dữ liệu thô. Với CBM, phải gán cả nhãn lớp lẫn nhãn khái niệm nên chi phí rất lớn. |  |
| Decision Accuracy | Độ chính xác của quyết định |  | Phán đoán của hệ thống đúng hay sai. Đây là thứ các chỉ số accuracy/F1 thông thường đang đo. | Explanation Accuracy — nhầm hai cái này là lỗi cơ bản nhất khi viết bài về XAI. |
| Dimensionality Reduction | Giảm chiều dữ liệu |  | Biến dữ liệu nhiều chiều thành ít chiều hơn mà vẫn giữ thông tin quan trọng. Autoencoder làm việc này theo cách phi tuyến, tốt hơn PCA. |  |
| Dropout | Ngắt ngẫu nhiên nơ-ron |  | Trong lúc huấn luyện, ngẫu nhiên tắt một tỉ lệ nơ-ron (thường 0.5) để mạng không phụ thuộc vào vài nơ-ron nhất định. Tự động tắt khi đánh giá. Là một dạng Regularization. | Sparse Autoencoder — cũng làm ít nơ-ron hoạt động, nhưng bằng số hạng phạt trong Loss chứ không phải tắt ngẫu nhiên |
| Epoch | Vòng lặp toàn tập |  | Một lần toàn bộ tập dữ liệu huấn luyện đi qua mạng. | Iteration — một epoch gồm nhiều iteration, mỗi iteration xử lý một batch. |
| F1-Score | Điểm F1 |  | Trung bình điều hòa của Precision và Recall. Chỉ cao khi cả hai cùng cao, nên phản ánh khách quan hơn Accuracy. |  |
| Ground Truth | Nhãn chuẩn / Sự thật nền |  | Giá trị đúng được coi là chuẩn để đối chiếu kết quả mô hình. Vấn đề lớn của XAI: không có ground truth cho lời giải thích — không ai biết lời giải thích đúng tuyệt đối trông như thế nào. |  |
| Learning Rate | Tốc độ học | lr | Độ lớn của mỗi bước cập nhật trọng số. Quá lớn thì mô hình không hội tụ, quá nhỏ thì học rất chậm. |  |
| Logits | Điểm số thô (chưa chuẩn hóa) |  | Vector số thực do lớp cuối của mạng xuất ra TRƯỚC khi qua Softmax. Có thể âm, không cộng lại thành 1. Khi huấn luyện với CrossEntropyLoss trong PyTorch thì truyền thẳng logits, không tự thêm Softmax. | Xác suất — chỉ có được sau khi áp Softmax lên logits |
| Loss Function | Hàm mất mát |  | Hàm đo mức độ sai lệch giữa dự đoán của mô hình và giá trị mong muốn. Mục tiêu huấn luyện là làm giá trị này nhỏ nhất có thể. |  |
| Mean Absolute Error | Sai số tuyệt đối trung bình | MAE | Trung bình trị tuyệt đối của sai lệch giữa dự đoán và thực tế. Ít nhạy cảm với ngoại lai hơn MSE. |  |
| Mean Squared Error | Sai số toàn phương trung bình | MSE | Trung bình bình phương sai lệch. Phạt rất nặng các điểm sai lệch lớn. Là hàm Loss phổ biến cho Autoencoder với dữ liệu liên tục. |  |
| Model Hyperparameter | Siêu tham số |  | Các giá trị cấu hình do NGƯỜI ĐẶT trước khi huấn luyện, nằm ngoài mô hình và không phụ thuộc dữ liệu. Ví dụ: learning rate, số lớp ẩn, kích thước Bottleneck. | Model Parameter |
| Model Parameter | Tham số mô hình |  | Các giá trị mô hình TỰ HỌC được từ dữ liệu huấn luyện, ví dụ trọng số mạng nơ-ron. Con người không đặt thủ công. | Model Hyperparameter — parameter do máy học, hyperparameter do người đặt. |
| Out-of-Distribution | Ngoài phân phối | OOD | Dữ liệu khác biệt đáng kể so với phân phối của tập huấn luyện. Mô hình thường hoạt động rất kém trên OOD — liên quan trực tiếp tới nguyên tắc Knowledge Limits. |  |
| Overfitting | Học vẹt / Quá khớp |  | Mô hình thuộc lòng dữ liệu huấn luyện nên làm rất tốt trên tập đó nhưng kém trên dữ liệu mới. Bottleneck quá lớn là một nguyên nhân gây overfitting ở Autoencoder. | Underfitting |
| Peer Review | Bình duyệt đồng nghiệp |  | Quy trình các nhà nghiên cứu khác thẩm định bài báo trước khi đăng. Có thể đọc nội dung bình duyệt của ICLR, NeurIPS, TMLR trên OpenReview — cách nhanh nhất để học đọc phản biện. |  |
| Precision | Độ chính xác dương tính |  | Trong số những gì mô hình lấy ra, bao nhiêu phần trăm là đúng. Công thức: TP / (TP + FP). | Recall — Precision hỏi 'lấy ra có đúng không', Recall hỏi 'có bỏ sót không'. |
| Preprint | Tiền ấn phẩm |  | Bản thảo công bố công khai trước khi qua bình duyệt, ví dụ trên arXiv. Không có nghĩa là sai, nhưng phải đọc hoài nghi hơn. Luôn tra dblp xem bài sau này đăng chính thức ở đâu. |  |
| Principal Component Analysis | Phân tích thành phần chính | PCA | Kỹ thuật giảm chiều dữ liệu tuyến tính dựa trên trị riêng. Autoencoder dạng nông học được điều tương tự PCA, còn Deep Autoencoder mạnh hơn vì học được quan hệ phi tuyến. |  |
| Recall | Độ bao phủ |  | Trong số những trường hợp đúng thực tế, mô hình tìm ra được bao nhiêu phần trăm. Công thức: TP / (TP + FN). | Precision |
| Regularization | Chính quy hóa / Ràng buộc |  | Kỹ thuật thêm một số hạng phạt vào hàm Loss để hạn chế mô hình học vẹt. Sparse và Contractive Autoencoder đều dựa trên ý tưởng này. |  |
| ROC-AUC | Diện tích dưới đường cong ROC | AUC | Đo khả năng phân biệt hai lớp của mô hình trên mọi ngưỡng. AUC = 1 là hoàn hảo, AUC = 0.5 tương đương đoán ngẫu nhiên. |  |
| Root Mean Squared Error | Căn sai số toàn phương trung bình | RMSE | Căn bậc hai của MSE, đưa đơn vị sai số về đúng đơn vị biến mục tiêu nên dễ diễn giải hơn. |  |
| Self-supervised Learning | Học tự giám sát |  | Mô hình tự tạo nhãn từ chính dữ liệu đầu vào. Autoencoder thuộc nhóm này vì nó dùng chính đầu vào làm mục tiêu tái tạo. | Unsupervised Learning — self-supervised là một nhánh cụ thể, chính xác hơn khi nói về Autoencoder. |
| Softmax | Hàm Softmax |  | Biến một vector logits bất kỳ thành các số dương cộng lại đúng bằng 1, đọc được như xác suất. Luôn là bước cuối của bài toán phân loại nhiều lớp. | Sigmoid — dùng cho phân loại nhị phân hoặc đa nhãn, các đầu ra KHÔNG cộng lại thành 1 |
| Supervised Learning | Học có giám sát |  | Học từ dữ liệu đã có nhãn do con người gán sẵn. |  |
| t-SNE | Kỹ thuật chiếu dữ liệu nhiều chiều xuống 2D |  | Phương pháp giảm chiều phi tuyến dùng để Vẽ latent space lên mặt phẳng. Lưu ý: chỉ bảo toàn quan hệ lân cận cục bộ, nên KÍCH THƯỚC cụm và KHOẢNG CÁCH giữa các cụm trên hình không mang ý nghĩa. | PCA — tuyến tính, bảo toàn cấu trúc toàn cục; UMAP — nhanh hơn và giữ cấu trúc toàn cục tốt hơn t-SNE |
| Underfitting | Thiếu khớp |  | Mô hình quá đơn giản hoặc bị ép nén quá mức nên không học được cả quy luật cơ bản. Ví dụ: Bottleneck quá nhỏ khiến ảnh tái tạo bị mờ. | Overfitting |
| Unsupervised Learning | Học không giám sát |  | Học từ dữ liệu không có nhãn, tự tìm ra cấu trúc ẩn bên trong. |  |
