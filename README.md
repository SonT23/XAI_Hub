# Bilingual Glossary: Explainable AI & Computer Vision (EN-VI)

A bilingual (English-Vietnamese) glossary of terms used in machine learning, computer vision, and Explainable AI (XAI), with a focus on Concept Bottleneck Models (CBM). Source of truth is a Notion database; this repo is a periodically refreshed export for public reference.

**Total terms:** 165

## Table of contents

- [Toán](#toán)
- [ML cơ bản](#ml-cơ-bản)
- [Deep Learning](#deep-learning)
- [CNN](#cnn)
- [Autoencoder](#autoencoder)
- [Transformer/CLIP](#transformerclip)
- [XAI](#xai)
- [CBM](#cbm)

## Toán

| Term (EN) | Tiếng Việt | Viết tắt | Định nghĩa ngắn | Dễ nhầm với |
|---|---|---|---|---|
| Basis Vectors | Vectơ cơ sở |  | Các vectơ gốc dùng làm hệ quy chiếu của không gian. Các cột của một Matrix cho biết các vectơ cơ sở sẽ đáp xuống đâu sau khi biến đổi. |  |
| Cosine Similarity | Độ tương đồng cosine |  | Đo độ giống nhau giữa hai vectơ bằng góc giữa chúng, bỏ qua độ dài. CLIP dùng phép này để so khớp vectơ ảnh với vectơ văn bản. |  |
| Determinant | Định thức | det | Một số cho biết phép biến đổi của Matrix làm không gian giãn ra hay co lại bao nhiêu lần. det = 0 nghĩa là không gian bị sụp đổ về số chiều thấp hơn. |  |
| Eigenvalue | Trị riêng |  | Hệ số cho biết vectơ riêng bị kéo giãn (hoặc nén) bao nhiêu lần sau phép biến đổi. Dùng để tìm ra các thành phần cốt lõi ẩn trong dữ liệu. | Eigenvector |
| Eigenvector | Vectơ riêng |  | Hướng đặc biệt mà khi không gian bị biến đổi, vectơ nằm trên hướng đó chỉ bị kéo giãn hoặc nén lại chứ không bị chệch hướng. | Eigenvalue — eigenvector là hướng, eigenvalue là hệ số kéo giãn trên hướng đó. |
| Evidence Lower Bound | Cận dưới của bằng chứng | ELBO | Hàm mục tiêu của VAE: Reconstruction Loss trừ đi KL Divergence. Gọi là cận dưới vì nó chặn dưới log-likelihood thật (thứ không tính được). Huấn luyện VAE = cực đại hóa ELBO. |  |
| Frobenius Norm | Chuẩn Frobenius |  | Cách đo độ lớn của một ma trận bằng căn bậc hai tổng bình phương mọi phần tử. |  |
| Gradient | Gradient (vectơ đạo hàm) |  | Vectơ chỉ hướng hàm số tăng nhanh nhất. Huấn luyện mạng nơ-ron chính là đi ngược hướng gradient của hàm Loss để giảm sai số. |  |
| Jacobian | Ma trận Jacobian |  | Ma trận chứa toàn bộ đạo hàm riêng của một hàm nhiều đầu vào - nhiều đầu ra. Contractive Autoencoder phạt chuẩn Frobenius của Jacobian để Latent Space ổn định. |  |
| KL Divergence | Độ phân kỳ KL | KL | Thước đo độ lệch giữa hai phân phối xác suất. Trong VAE, nó ép phân phối latent tiến gần phân phối chuẩn N(0,1); trong Sparse Autoencoder nó ép nơ-ron thưa. | Không đối xứng: KL(P\|\|Q) khác KL(Q\|\|P), nên không phải là khoảng cách theo nghĩa toán học. |
| Linear Algebra | Đại số tuyến tính |  | Lĩnh vực toán học đóng gói nhiều đại lượng thành Vector và Matrix để xử lý cùng lúc, thay vì giải hàng nghìn phương trình rời rạc. |  |
| Linear Transformation | Biến đổi tuyến tính |  | Phép biến đổi đưa một Vector từ vị trí này sang vị trí khác trong cùng không gian, thực hiện bằng phép nhân với Matrix. |  |
| Matrix | Ma trận |  | Bảng số hai chiều đại diện cho một phép biến đổi không gian. Có thể xem Matrix như động từ: nó bóp méo, xoay, kéo giãn hay nén không gian chứa Vector. |  |
| Principal Component Analysis | Phân tích thành phần chính | PCA | Kỹ thuật giảm chiều dữ liệu tuyến tính dựa trên trị riêng. Autoencoder dạng nông học được điều tương tự PCA, còn Deep Autoencoder mạnh hơn vì học được quan hệ phi tuyến. |  |
| Prior / Posterior | Tiên nghiệm / Hậu nghiệm |  | Prior p(z) là phân phối giả định trước khi thấy dữ liệu — trong VAE thường chọn N(0,I). Posterior p(z\|x) là phân phối sau khi đã quan sát dữ liệu x. |  |
| Variational Inference | Suy luận biến phân |  | Kỹ thuật dùng một phân phối đơn giản q(z\|x) để XẤP XỈ một phân phối không tính được p(z\|x). Chữ 'Variational' trong tên VAE đến từ đây. |  |
| Vector | Vectơ |  | Một dãy số có thứ tự, biểu diễn một điểm hoặc một hướng trong không gian. Trong đại số tuyến tính có thể xem Vector như danh từ. |  |

## ML cơ bản

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

## Deep Learning

| Term (EN) | Tiếng Việt | Viết tắt | Định nghĩa ngắn | Dễ nhầm với |
|---|---|---|---|---|
| Activation Function | Hàm kích hoạt |  | Hàm phi tuyến đặt sau mỗi lớp để mạng học được quan hệ phi tuyến. Phổ biến nhất là ReLU; lớp đầu ra phân loại thường dùng Softmax. |  |
| Backbone | Mạng xương sống / Mạng nền |  | Mạng trích xuất đặc trưng chính của một hệ thống, ví dụ ResNet, Inception hay ViT. CBM gốc dùng Inception-v3 làm backbone. |  |
| Backpropagation | Lan truyền ngược |  | Thuật toán tính gradient của hàm Loss theo từng trọng số bằng cách lan truyền sai số ngược từ đầu ra về đầu vào, dựa trên quy tắc chuỗi đạo hàm. |  |
| Batch Normalization | Chuẩn hóa theo lô | BN | Chuẩn hóa lại phân phối giá trị trong mỗi kênh dựa trên thống kê của batch hiện tại. Giúp mạng sâu hội tụ nhanh và ổn định hơn nhiều. Thứ tự chuẩn: Conv → BatchNorm → ReLU. | Chuẩn hóa dữ liệu đầu vào (chia 255) — việc đó chỉ làm một lần ở Input, còn BN nằm giữa mạng và học được tham số |
| Data Augmentation | Tăng cường dữ liệu |  | Sinh thêm mẫu huấn luyện bằng cách biến đổi ảnh gốc (lật, xoay, cắt, đổi màu). Cần thiết vì CNN chỉ bất biến với dịch chuyển nhỏ, không tự bất biến với xoay hay co giãn. | Denoising Autoencoder — cũng làm hỏng đầu vào, nhưng mục tiêu là học biểu diễn bền vững chứ không phải tăng số lượng mẫu |
| Dropout | Ngắt ngẫu nhiên nơ-ron |  | Trong lúc huấn luyện, ngẫu nhiên tắt một tỉ lệ nơ-ron (thường 0.5) để mạng không phụ thuộc vào vài nơ-ron nhất định. Tự động tắt khi đánh giá. Là một dạng Regularization. | Sparse Autoencoder — cũng làm ít nơ-ron hoạt động, nhưng bằng số hạng phạt trong Loss chứ không phải tắt ngẫu nhiên |
| Embedding | Vectơ nhúng |  | Biểu diễn một đối tượng (từ, ảnh, khái niệm) dưới dạng vectơ số thực, sao cho các đối tượng giống nhau nằm gần nhau. |  |
| Feature Vector | Vector đặc trưng |  | Vector biểu diễn lấy từ lớp áp chót (penultimate layer) của một mạng phân loại, trước khi đưa vào lớp quyết định cuối. Đây chính là thứ được dùng khi nói trích xuất đặc trưng từ CNN. | Feature Map — là tensor 3 chiều còn giữ cấu trúc không gian; feature vector đã bị duỗi phẳng |
| Flatten | Làm phẳng |  | Duỗi một tensor nhiều chiều (ví dụ 4x4x128) thành vector 1 chiều (2048) để đưa vào lớp Fully Connected. Không có tham số, nhưng vứt bỏ hoàn toàn cấu trúc không gian. | Global Average Pooling — cùng mục đích chuyển sang FC nhưng lấy trung bình mỗi kênh thay vì duỗi hết, nên gọn hơn nhiều |
| Foundation Model | Mô hình nền tảng |  | Mô hình lớn huấn luyện trên lượng dữ liệu khổng lồ, dùng làm nền cho nhiều tác vụ hạ nguồn khác nhau. CLIP, GPT, ViT quy mô lớn đều thuộc nhóm này. |  |
| Gradient | Gradient (vectơ đạo hàm) |  | Vectơ chỉ hướng hàm số tăng nhanh nhất. Huấn luyện mạng nơ-ron chính là đi ngược hướng gradient của hàm Loss để giảm sai số. |  |
| Latent Diffusion Model | Mô hình khuếch tán trong không gian tiềm ẩn | LDM | Biến thể Diffusion thực hiện quá trình khuếch tán TRONG latent space thay vì trên pixel, nhờ đó nhẹ hơn rất nhiều. Đây là nền của Stable Diffusion — và là ví dụ cho thấy latent space không chỉ dùng cho Autoencoder. | VAE — LDM thực ra DÙNG một VAE để đi vào và ra khỏi latent space, rồi mới chạy diffusion ở giữa |
| Latent Factor | Yếu tố tiềm ẩn |  | Những yếu tố ẩn sinh ra dữ liệu quan sát được — ví dụ với ảnh khuôn mặt thì là tuổi, góc quay, độ dài tóc. Mô hình tự tìm ra chúng mà không ai gán nhãn. | Concept trong CBM — cũng là yếu tố sinh dữ liệu nhưng được con người đặt tên trước |
| Latent Traversal | Đi dọc một chiều tiềm ẩn |  | Kỹ thuật giữ nguyên toàn bộ vector z và chỉ kéo MỘT chiều từ -3 đến +3, rồi xem ảnh giải mã thay đổi thế nào. Là cách chuẩn để kiểm tra mức độ disentangled của latent space. | Interpolation — đi giữa hai điểm có thật, còn traversal đi dọc theo một trục tọa độ |
| Latent Vector / Latent Code | Vector tiềm ẩn / mã tiềm ẩn | z | Một ĐIỂM cụ thể trong Latent Space — tức biểu diễn nén của một mẫu dữ liệu. Thường ký hiệu là z. | Latent Space — là cả không gian, còn latent vector chỉ là một phần tử trong đó |
| Logits | Điểm số thô (chưa chuẩn hóa) |  | Vector số thực do lớp cuối của mạng xuất ra TRƯỚC khi qua Softmax. Có thể âm, không cộng lại thành 1. Khi huấn luyện với CrossEntropyLoss trong PyTorch thì truyền thẳng logits, không tự thêm Softmax. | Xác suất — chỉ có được sau khi áp Softmax lên logits |
| Pre-training / Fine-tuning | Tiền huấn luyện / Tinh chỉnh |  | Pre-training là huấn luyện trước trên tập dữ liệu lớn tổng quát; fine-tuning là huấn luyện tiếp trên tập nhỏ chuyên biệt của bài toán cụ thể. |  |
| ReLU | Hàm kích hoạt ReLU | ReLU | Rectified Linear Unit: f(x) = max(0, x). Giữ nguyên số dương, ép mọi số âm về 0. Là hàm kích hoạt mặc định cho lớp ẩn của CNN vì tạo được tính phi tuyến mà tính toán rất rẻ. | Sigmoid (dùng ở đầu ra khi cần giá trị trong [0,1]); LeakyReLU (cho phép số âm đi qua một chút để tránh nơ-ron chết) |
| Representation Learning | Học biểu diễn |  | Lĩnh vực nghiên cứu về cách để máy tự học ra biểu diễn tốt cho dữ liệu, thay vì phải thiết kế đặc trưng thủ công. Autoencoder, CLIP và contrastive learning đều thuộc lĩnh vực này. | Feature Engineering — cách làm truyền thống, do con người tự thiết kế đặc trưng |
| Residual Connection | Kết nối tắt |  | Đường nối cộng thẳng đầu vào của một khối vào đầu ra của nó, giúp huấn luyện được mạng rất sâu mà không bị triệt tiêu gradient. |  |
| Softmax | Hàm Softmax |  | Biến một vector logits bất kỳ thành các số dương cộng lại đúng bằng 1, đọc được như xác suất. Luôn là bước cuối của bài toán phân loại nhiều lớp. | Sigmoid — dùng cho phân loại nhị phân hoặc đa nhãn, các đầu ra KHÔNG cộng lại thành 1 |
| t-SNE | Kỹ thuật chiếu dữ liệu nhiều chiều xuống 2D |  | Phương pháp giảm chiều phi tuyến dùng để Vẽ latent space lên mặt phẳng. Lưu ý: chỉ bảo toàn quan hệ lân cận cục bộ, nên KÍCH THƯỚC cụm và KHOẢNG CÁCH giữa các cụm trên hình không mang ý nghĩa. | PCA — tuyến tính, bảo toàn cấu trúc toàn cục; UMAP — nhanh hơn và giữ cấu trúc toàn cục tốt hơn t-SNE |
| Transfer Learning | Học chuyển giao |  | Giữ nguyên phần trích xuất đặc trưng của một mạng đã huấn luyện trên tập dữ liệu lớn (ví dụ ImageNet), chỉ thay và huấn luyện lại vài lớp cuối cho bài toán mới. Hoạt động được vì phần Conv học đặc trưng dùng chung cho mọi loại ảnh. | Fine-tuning — là một cách làm transfer learning, trong đó mở khóa và huấn luyện lại cả phần backbone với learning rate rất nhỏ |
| Vanishing Gradient | Gradient tiêu biến |  | Khi mạng quá sâu, gradient nhân dồn qua nhiều lớp và teo dần về gần 0, khiến các lớp đầu gần như không học được gì. Là lý do ra đời Residual Connection trong ResNet. | Exploding Gradient — hiện tượng ngược lại, gradient phình to gây NaN; khắc phục bằng gradient clipping |

## CNN

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

## Autoencoder

| Term (EN) | Tiếng Việt | Viết tắt | Định nghĩa ngắn | Dễ nhầm với |
|---|---|---|---|---|
| Anomaly Detection | Phát hiện bất thường |  | Dùng Reconstruction Loss làm tín hiệu: dữ liệu giống tập huấn luyện cho loss thấp, dữ liệu bất thường cho loss cao vượt ngưỡng. |  |
| Autoencoder | Mạng tự mã hóa | AE | Mạng nơ-ron học tự giám sát, nén dữ liệu đầu vào thành biểu diễn nhỏ hơn rồi tái tạo lại, qua đó học được các đặc trưng quan trọng nhất. |  |
| Binary Cross-Entropy | Entropy chéo nhị phân | BCE | Hàm Loss dùng khi dữ liệu là nhị phân hoặc đã chuẩn hóa về [0,1]. Coi mỗi điểm như một bài toán xác suất độc lập. | MSE — chọn theo bản chất dữ liệu: liên tục dùng MSE, nhị phân/chuẩn hóa dùng BCE. |
| Bottleneck | Nút thắt cổ chai |  | Lớp hẹp nhất nằm giữa Encoder và Decoder, chứa biểu diễn nén của dữ liệu. Là phần quan trọng nhất và trớ trêu thay lại là phần nhỏ nhất của mạng. | Latent Space — Bottleneck là lớp vật lý, Latent Space là không gian toán học mà vectơ tại nút thắt nằm trong. |
| Contractive Autoencoder | Autoencoder co rút | CAE | Phạt đạo hàm (Jacobian) của biểu diễn tiềm ẩn theo đầu vào, ép Latent Space bất biến với các nhiễu loạn nhỏ. | Viết tắt CAE trùng với Convolutional Autoencoder — cần ghi rõ khi viết bài. |
| Decoder | Bộ giải mã |  | Phần sau của Autoencoder, nhận vectơ nén từ Bottleneck và tái tạo lại dữ liệu có kích thước bằng đúng đầu vào ban đầu. |  |
| Denoising Autoencoder | Autoencoder khử nhiễu | DAE | Nhận đầu vào đã bị thêm nhiễu nhưng phải tái tạo bản gốc sạch, buộc mô hình học bản chất dữ liệu thay vì học thuộc lòng. |  |
| Dimensionality Reduction | Giảm chiều dữ liệu |  | Biến dữ liệu nhiều chiều thành ít chiều hơn mà vẫn giữ thông tin quan trọng. Autoencoder làm việc này theo cách phi tuyến, tốt hơn PCA. |  |
| Disentangled Representation | Biểu diễn phân tách |  | Biểu diễn mà mỗi chiều latent mang một ý nghĩa độc lập, dễ hiểu với con người. Đây là cầu nối quan trọng giữa VAE và hướng nghiên cứu CBM không cần nhãn. |  |
| Encoder | Bộ mã hóa |  | Phần đầu của Autoencoder, nén dữ liệu đầu vào lớn thành một vectơ nhỏ gọn nhưng vẫn giữ nét đặc trưng chính. |  |
| Evidence Lower Bound | Cận dưới của bằng chứng | ELBO | Hàm mục tiêu của VAE: Reconstruction Loss trừ đi KL Divergence. Gọi là cận dưới vì nó chặn dưới log-likelihood thật (thứ không tính được). Huấn luyện VAE = cực đại hóa ELBO. |  |
| Frobenius Norm | Chuẩn Frobenius |  | Cách đo độ lớn của một ma trận bằng căn bậc hai tổng bình phương mọi phần tử. |  |
| Generative Model | Mô hình sinh |  | Mô hình học được phân phối của dữ liệu nên có thể tạo ra mẫu mới chưa từng có. VAE là một ví dụ; Autoencoder thường thì không phải. |  |
| Identity Function | Hàm đồng nhất |  | Hàm trả về đúng đầu vào. Nếu Bottleneck quá lớn, Autoencoder sẽ học hàm này - tức chỉ sao chép dữ liệu mà không học được quy luật nào. |  |
| Interpolation | Nội suy |  | Lấy các điểm nằm giữa hai điểm trong Latent Space rồi giải mã. Ở VAE cho kết quả chuyển đổi mượt và có nghĩa; ở AE thường ra nhiễu. |  |
| Jacobian | Ma trận Jacobian |  | Ma trận chứa toàn bộ đạo hàm riêng của một hàm nhiều đầu vào - nhiều đầu ra. Contractive Autoencoder phạt chuẩn Frobenius của Jacobian để Latent Space ổn định. |  |
| KL Divergence | Độ phân kỳ KL | KL | Thước đo độ lệch giữa hai phân phối xác suất. Trong VAE, nó ép phân phối latent tiến gần phân phối chuẩn N(0,1); trong Sparse Autoencoder nó ép nơ-ron thưa. | Không đối xứng: KL(P\|\|Q) khác KL(Q\|\|P), nên không phải là khoảng cách theo nghĩa toán học. |
| Latent Representation | Biểu diễn tiềm ẩn |  | Vectơ nén mà Encoder tạo ra, nắm bắt các đặc trưng cốt lõi của dữ liệu ở dạng cô đọng, đã lọc nhiễu và dư thừa. |  |
| Latent Space | Không gian tiềm ẩn |  | Không gian nhiều chiều chứa các biểu diễn nén của dữ liệu. Vectơ tại Bottleneck chính là một điểm trong không gian này. |  |
| Latent Vector / Latent Code | Vector tiềm ẩn / mã tiềm ẩn | z | Một ĐIỂM cụ thể trong Latent Space — tức biểu diễn nén của một mẫu dữ liệu. Thường ký hiệu là z. | Latent Space — là cả không gian, còn latent vector chỉ là một phần tử trong đó |
| Mean Squared Error | Sai số toàn phương trung bình | MSE | Trung bình bình phương sai lệch. Phạt rất nặng các điểm sai lệch lớn. Là hàm Loss phổ biến cho Autoencoder với dữ liệu liên tục. |  |
| Posterior Collapse | Sụp đổ hậu nghiệm |  | Lỗi thường gặp khi huấn luyện VAE: Decoder quá mạnh nên bỏ qua z hoàn toàn, KL bị đẩy về 0 và latent space mất hết thông tin. Khắc phục bằng KL annealing. |  |
| Prior / Posterior | Tiên nghiệm / Hậu nghiệm |  | Prior p(z) là phân phối giả định trước khi thấy dữ liệu — trong VAE thường chọn N(0,I). Posterior p(z\|x) là phân phối sau khi đã quan sát dữ liệu x. |  |
| Reconstruction Loss | Lỗi tái tạo |  | Độ sai khác giữa dữ liệu gốc và dữ liệu được tái tạo ở đầu ra. Đây là hàm mục tiêu chính của mọi Autoencoder. |  |
| Reparameterization Trick | Mẹo tái tham số hóa |  | Kỹ thuật giúp VAE lan truyền ngược qua phép lấy mẫu ngẫu nhiên: lấy epsilon từ N(0,1) rồi tính z = mu + sigma * epsilon. |  |
| Self-supervised Learning | Học tự giám sát |  | Mô hình tự tạo nhãn từ chính dữ liệu đầu vào. Autoencoder thuộc nhóm này vì nó dùng chính đầu vào làm mục tiêu tái tạo. | Unsupervised Learning — self-supervised là một nhánh cụ thể, chính xác hơn khi nói về Autoencoder. |
| Sparse Autoencoder | Autoencoder thưa | SAE | Không ép nhỏ Bottleneck mà thêm ràng buộc thưa (L1 hoặc KL) để mỗi lần chỉ một số ít nơ-ron được kích hoạt. |  |
| Transposed Convolution | Tích chập chuyển vị |  | Phép ngược của tích chập, dùng để tăng kích thước ảnh. Decoder của Convolutional Autoencoder dùng phép này để khôi phục kích thước gốc. | Thường bị gọi sai là Deconvolution — thực ra không phải phép nghịch đảo toán học. |
| Undercomplete Autoencoder | Autoencoder thiếu đầy |  | Dạng cơ bản nhất: Bottleneck nhỏ hơn đầu vào, ép mô hình phải học đặc trưng thay vì sao chép. |  |
| Variational Autoencoder | Autoencoder biến phân | VAE | Ánh xạ đầu vào thành một phân phối xác suất (mu, sigma) thay vì một điểm, nhờ đó Latent Space liên tục và sinh được dữ liệu mới. |  |
| Variational Inference | Suy luận biến phân |  | Kỹ thuật dùng một phân phối đơn giản q(z\|x) để XẤP XỈ một phân phối không tính được p(z\|x). Chữ 'Variational' trong tên VAE đến từ đây. |  |

## Transformer/CLIP

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

## XAI

| Term (EN) | Tiếng Việt | Viết tắt | Định nghĩa ngắn | Dễ nhầm với |
|---|---|---|---|---|
| Black Box | Hộp đen |  | Mô hình chỉ thấy được đầu vào và đầu ra, không hiểu được cơ chế bên trong. Đây chính là vấn đề mà XAI sinh ra để giải quyết. |  |
| Calibration | Hiệu chỉnh xác suất |  | Mức độ mà điểm tin cậy của mô hình phản ánh đúng xác suất thực tế. Quan trọng khi đánh giá độ tin cậy của khái niệm trong CBM và của điểm số CLIP. |  |
| Choice Blindness | Mù lựa chọn |  | Con người không nhớ chính xác lựa chọn trước đó, và vẫn đưa ra lý do thuyết phục cho những lựa chọn mà họ chưa từng chọn. |  |
| Concept Activation Vector | Vectơ kích hoạt khái niệm | CAV | Vectơ pháp tuyến của siêu phẳng tách ảnh có khái niệm với ảnh không có, trong không gian activation. Đại diện cho hướng của khái niệm đó. |  |
| Concept Space | Không gian khái niệm |  | Một Latent Space mà MỖI CHIỀU đã được gán nhãn một khái niệm con người hiểu được. Đây chính là thứ CBM tạo ra — có thể hiểu CBM là một latent space bị buộc phải diễn giải được. | Latent Space thông thường — không ai biết chiều thứ 42 nghĩa là gì |
| Confabulation | Bịa lý do |  | Con người ra quyết định trước rồi gắn lý do vào sau, mà vẫn tin đó là lý do thật. Bằng chứng thần kinh học: dấu hiệu quyết định xuất hiện trước tới 10 giây so với lúc ý thức được. |  |
| Counterfactual Explanation | Giải thích phản thực |  | Lời giải thích dạng 'nếu đầu vào khác đi thì quyết định sẽ đổi'. Mô tả thay đổi NHỎ NHẤT đủ để lật kết quả. Ưu điểm: không làm lộ cơ chế bên trong. |  |
| Decision Accuracy | Độ chính xác của quyết định |  | Phán đoán của hệ thống đúng hay sai. Đây là thứ các chỉ số accuracy/F1 thông thường đang đo. | Explanation Accuracy — nhầm hai cái này là lỗi cơ bản nhất khi viết bài về XAI. |
| Disentangled Representation | Biểu diễn phân tách |  | Biểu diễn mà mỗi chiều latent mang một ý nghĩa độc lập, dễ hiểu với con người. Đây là cầu nối quan trọng giữa VAE và hướng nghiên cứu CBM không cần nhãn. |  |
| Dunning-Kruger Effect | Hiệu ứng Dunning-Kruger |  | Hầu hết mọi người, kể cả chuyên gia, ước lượng sai năng lực của chính mình. Trong NIST IR 8312, đây là bằng chứng cho thấy con người cũng không đạt nguyên tắc Knowledge Limits. |  |
| Explainability | Khả năng giải thích |  | Khả năng đưa ra lời giải thích cho MỘT QUYẾT ĐỊNH CỤ THỂ, kể cả khi bên trong mô hình vẫn là hộp đen. | Interpretability |
| Explainable AI | AI có khả năng giải thích | XAI | Lĩnh vực nghiên cứu các phương pháp giúp con người hiểu được tại sao một mô hình AI đưa ra một dự đoán cụ thể. |  |
| Explanation (Principle 1) | Nguyên tắc Có lời giải thích |  | Nguyên tắc 1 của NIST: hệ thống phải cung cấp bằng chứng hoặc lý do kèm theo đầu ra. Độc lập với việc lời giải thích có đúng hay dễ hiểu hay không — chỉ đòi hỏi nó TỒN TẠI. |  |
| Explanation Accuracy (Principle 3) | Độ chính xác của lời giải thích | EA | Nguyên tắc 3 của NIST: lời giải thích phải phản ánh ĐÚNG lý do/quy trình thực sự mà hệ thống dùng để ra kết quả. | Decision Accuracy — cặp này HOÀN TOÀN ĐỘC LẬP: mô hình dự đoán đúng vẫn có thể giải thích sai. |
| Fairwashing | Tẩy trắng công bằng |  | Tấn công đối kháng: sinh ra các mô hình dễ hiểu xấp xỉ hộp đen nhưng TRÔNG CÔNG BẰNG HƠN thực tế, qua đó che giấu sự bất công của mô hình gốc. |  |
| Faithfulness | Độ trung thực |  | Lời giải thích có phản ánh ĐÚNG quá trình mô hình thực sự dùng để quyết định hay không. | Plausibility — hai tiêu chí này có thể đối lập nhau. |
| Fidelity | Độ trung thành |  | Mức độ lời giải thích hậu kỳ phản ánh trung thực hành vi của mô hình gốc. Là cách vận hành hóa cụ thể của Explanation Accuracy trong đo lường. | Faithfulness — gần nghĩa, thường dùng thay nhau; fidelity hay dùng cho mô hình thay thế (surrogate). |
| Global Average Pooling | Gộp trung bình toàn cục | GAP | Lấy trung bình toàn bộ mỗi kênh của Feature Map, biến HxWxC thành đúng C số. Thay thế hiện đại cho Flatten + FC lớn, cắt được phần lớn tham số và là cơ chế giúp Grad-CAM hoạt động. | Max Pooling 2x2 — chỉ giảm một nửa kích thước, còn GAP nén cả kênh về một số duy nhất |
| Grad-CAM | Grad-CAM |  | Dùng gradient tại lớp tích chập cuối để tạo heatmap chỉ vùng ảnh mô hình nhìn vào. Chỉ trả lời được 'ở đâu' chứ không phải 'cái gì'. |  |
| Ground Truth | Nhãn chuẩn / Sự thật nền |  | Giá trị đúng được coi là chuẩn để đối chiếu kết quả mô hình. Vấn đề lớn của XAI: không có ground truth cho lời giải thích — không ai biết lời giải thích đúng tuyệt đối trông như thế nào. |  |
| Human Simulatability | Khả năng con người mô phỏng |  | Khả năng con người hiểu mô hình đủ để TỰ dự đoán đúng đầu ra của nó. Là cách đo chính cho nguyên tắc Meaningful. Đo bằng độ chính xác, thời gian, và đánh giá chủ quan. |  |
| Influence Functions | Hàm ảnh hưởng |  | Phương pháp giải thích cục bộ: ước lượng điểm dữ liệu HUẤN LUYỆN nào ảnh hưởng nhiều nhất đến một quyết định cụ thể. Khác các phương pháp khác ở chỗ nó quy trách nhiệm cho dữ liệu chứ không phải đặc trưng. |  |
| Input Invariance | Bất biến với đầu vào |  | Tính chất mà một phương pháp giải thích tốt phải có: thay đổi nhỏ không đáng kể ở đầu vào không được làm lời giải thích đảo lộn. Nhiều phương pháp saliency KHÔNG đạt tính này. |  |
| Interpretability | Tính dễ hiểu (nội tại) |  | Mức độ mà con người hiểu được CƠ CHẾ NỘI TẠI của mô hình, ví dụ đọc được toàn bộ luồng suy luận của một cây quyết định. | Explainability — interpretability nói về bên trong mô hình, explainability nói về lời giải thích cho từng quyết định. Rất hay bị dùng lẫn. |
| Intervention Curve | Đường cong can thiệp |  | Đồ thị thể hiện độ chính xác tăng ra sao khi sửa đúng dần từng khái niệm. Đường dốc lên là dấu hiệu tốt; đường phẳng báo hiệu concept leakage. |  |
| Intrinsic (Ante-hoc) Interpretability | Giải thích nội tại |  | Tính giải thích được thiết kế sẵn vào kiến trúc mô hình, nên lời giải thích chính là đường đi thật của dữ liệu. CBM thuộc nhóm này. | Post-hoc |
| Introspection Illusion | Ảo tưởng nội quan |  | Hiện tượng tâm lý: con người tin rằng nhìn vào nội tâm sẽ biết được lý do thật cho quyết định của mình — nhưng niềm tin đó sai lầm. |  |
| Knowledge Limits (Principle 4) | Giới hạn tri thức |  | Nguyên tắc 4 của NIST: hệ thống chỉ hoạt động trong điều kiện nó được thiết kế và khi đủ tự tin. Hai con đường chạm giới hạn: nằm ngoài miền hoạt động, và độ tin cậy quá thấp. CBM gốc không đề cập nguyên tắc này. |  |
| Latent Traversal | Đi dọc một chiều tiềm ẩn |  | Kỹ thuật giữ nguyên toàn bộ vector z và chỉ kéo MỘT chiều từ -3 đến +3, rồi xem ảnh giải mã thay đổi thế nào. Là cách chuẩn để kiểm tra mức độ disentangled của latent space. | Interpolation — đi giữa hai điểm có thật, còn traversal đi dọc theo một trục tọa độ |
| LIME | LIME |  | Xấp xỉ mô hình phức tạp bằng một mô hình tuyến tính đơn giản quanh một điểm dữ liệu cụ thể, rồi đọc hệ số để biết đặc trưng nào quan trọng. |  |
| Local vs Global Explanation | Giải thích cục bộ vs toàn cục |  | Local giải thích một dự đoán cụ thể; Global giải thích hành vi tổng thể của mô hình trên toàn bộ dữ liệu. |  |
| Meaningful (Principle 2) | Nguyên tắc Có ý nghĩa |  | Nguyên tắc 2 của NIST: lời giải thích phải dễ hiểu với đúng người tiếp nhận mục tiêu (intended consumer). Phụ thuộc đối tượng, không phải thuộc tính tuyệt đối. | Explanation Accuracy — hai nguyên tắc này có thể xung đột với nhau. |
| Model Risk | Rủi ro mô hình |  | Hậu quả tiêu cực từ mô hình không hợp lệ hoặc bị dùng sai (định nghĩa của Cục Dự trữ Liên bang Mỹ). Hai nguồn: lỗi trong mô hình, và dùng mô hình vượt giới hạn tri thức. |  |
| Model-agnostic | Độc lập với mô hình |  | Phương pháp giải thích dùng được cho bất kỳ mô hình nào, chỉ cần quan sát đầu vào và đầu ra. Ngược lại là model-specific. |  |
| Out-of-Distribution | Ngoài phân phối | OOD | Dữ liệu khác biệt đáng kể so với phân phối của tập huấn luyện. Mô hình thường hoạt động rất kém trên OOD — liên quan trực tiếp tới nguyên tắc Knowledge Limits. |  |
| Partial Dependence Plot | Đồ thị phụ thuộc từng phần | PDP | Phương pháp giải thích toàn cục: cho thấy dự đoán thay đổi thế nào khi một đặc trưng thay đổi, giúp xác định quan hệ là tuyến tính hay phức tạp. |  |
| Plausibility | Độ hợp lý |  | Lời giải thích có THUYẾT PHỤC với con người hay không. Một lời giải thích plausible nhưng không faithful là nguy hiểm nhất vì tạo cảm giác an tâm giả. | Faithfulness |
| Post-hoc Explanation | Giải thích hậu kỳ |  | Mô hình được huấn luyện bình thường như hộp đen, sau đó dùng công cụ khác ước lượng từ bên ngoài xem nó dựa vào đâu. Ví dụ: LIME, SHAP, Grad-CAM. | Intrinsic — đây là trục phân loại quan trọng nhất để định vị CBM. |
| Prototype | Mẫu đại diện |  | Mẫu tiêu biểu của một lớp, dùng làm lời giải thích dạng 'giống với cái này'. Ví dụ: 'con chim này là hồng y vì nó giống các con hồng y trong tập huấn luyện'. |  |
| Saliency Map | Bản đồ nổi bật |  | Heatmap chỉ ra pixel nào quan trọng, tính bằng gradient của đầu ra theo từng pixel. Đã bị chỉ trích vì không vượt được sanity check. |  |
| SHAP / Shapley Value | Giá trị Shapley |  | Chia công bằng đóng góp của từng đặc trưng vào dự đoán, dựa trên lý thuyết trò chơi hợp tác. Ổn định hơn LIME nhưng tốn tính toán. |  |
| TCAV | Kiểm thử bằng vectơ kích hoạt khái niệm |  | Phương pháp post-hoc đo xem một khái niệm (ví dụ 'sọc') ảnh hưởng bao nhiêu đến dự đoán của một lớp. Là tiền đề trực tiếp của CBM. |  |

## CBM

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

---

Source of truth: a Notion database maintained during NCKH research on Explainable AI for Computer Vision. Data files (`glossary.json`, `glossary.csv`) are machine-readable exports kept in sync with this README.
