# Autoencoder

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
