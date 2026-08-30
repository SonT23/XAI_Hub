# Toán

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
