# Sơ đồ tư duy: Phân loại các nhánh Machine Learning

> 🖼️ **Dán ảnh gốc tại đây:** `1403_so-do-tu-duy-phan-loai-cac-nhanh-machine-learning-.jpg`

> 💡 Sơ đồ tổng quan phân loại **Machine Learning (ML)** thành 10 nhánh lớn: Supervised, Unsupervised, Reinforcement, Self-Supervised, Semi-Supervised, Transfer Learning, Deep Learning, Generative AI, Ensemble Learning, và Probabilistic Graphical Models. Ảnh có ghi chú "2026 update", phản ánh các mô hình/thuật toán hiện đại tính đến thời điểm cập nhật.

### 1. Supervised Learning (Học có giám sát)

Học từ dữ liệu đã được gán nhãn (input-output cho trước) để dự đoán nhãn cho dữ liệu mới.

- **Regression** (Hồi quy) — dự đoán giá trị liên tục
    - Linear Regression — hồi quy tuyến tính, mô hình quan hệ tuyến tính giữa biến đầu vào và đầu ra

    - Polynomial Regression — mở rộng hồi quy tuyến tính bằng các bậc đa thức để khớp quan hệ phi tuyến

    - Ridge/Lasso Regression — hồi quy tuyến tính có regularization (L2/L1) để chống overfitting

- **Classification** (Phân loại) — dự đoán nhãn rời rạc
    - Logistic Regression — mô hình tuyến tính dùng hàm sigmoid để phân loại nhị phân/đa lớp

    - Decision Trees — cây quyết định, phân chia dữ liệu theo các luật if-else

    - SVM (Support Vector Machine) — tìm siêu phẳng phân tách tối ưu giữa các lớp

    - Naive Bayes — phân loại xác suất dựa trên định lý Bayes với giả định độc lập giữa các đặc trưng

    - k-NN (k-Nearest Neighbors) — phân loại dựa trên nhãn của k điểm dữ liệu gần nhất

### 2. Unsupervised Learning (Học không giám sát)

Học cấu trúc/quy luật ẩn trong dữ liệu không có nhãn.

- **Clustering** (Phân cụm) — nhóm các điểm dữ liệu tương tự nhau
    - K-Means — phân cụm dựa trên khoảng cách tới k tâm cụm

    - DBSCAN — phân cụm dựa trên mật độ, phát hiện được cụm hình dạng bất kỳ và nhiễu

    - Agglomerative — phân cụm phân cấp theo kiểu gộp dần từ dưới lên

    - Mean Shift — phân cụm bằng cách dịch chuyển các điểm về vùng mật độ cao nhất

    - Fuzzy C-Means — phân cụm mờ, mỗi điểm có thể thuộc nhiều cụm với mức độ khác nhau

- **Association Rule Learning** (Luật kết hợp) — tìm mối liên hệ giữa các mục trong tập dữ liệu (ví dụ giỏ hàng)
    - FP-Growth — thuật toán khai phá tập phổ biến hiệu quả hơn Apriori nhờ cấu trúc cây FP-tree

    - Eclat — khai phá tập phổ biến dựa trên biểu diễn giao (intersection) của các tập giao dịch

    - Apriori — thuật toán kinh điển tìm tập mục phổ biến và sinh luật kết hợp

- **Dimensionality Reduction** (Giảm chiều dữ liệu)
    - t-SNE — giảm chiều phi tuyến, thường dùng để trực quan hóa dữ liệu nhiều chiều

    - PCA (Principal Component Analysis) — giảm chiều tuyến tính bằng cách chiếu dữ liệu lên các thành phần chính

    - UMAP — giảm chiều phi tuyến, giữ cấu trúc cục bộ và toàn cục tốt, nhanh hơn t-SNE

    - SVD (Singular Value Decomposition) — phân tích ma trận thành các thành phần suy biến, nền tảng của PCA và nhiều kỹ thuật giảm chiều khác

    - LDA (Linear Discriminant Analysis) — giảm chiều có giám sát, tối đa hóa khả năng phân tách giữa các lớp

### 3. Reinforcement Learning (Học tăng cường)

Agent học chính sách hành động thông qua tương tác với môi trường và nhận phần thưởng/phạt.

- Q-Learning — học giá trị hành động (Q-value) off-policy dựa trên bảng hoặc hàm xấp xỉ

- Deep Q-Network (DQN) — kết hợp Q-Learning với mạng nơ-ron sâu để xử lý không gian trạng thái lớn

- SARSA — thuật toán học tăng cường on-policy, cập nhật giá trị dựa trên hành động thực sự được thực hiện

- Policy Gradient — tối ưu trực tiếp chính sách (policy) bằng gradient ascent trên kỳ vọng phần thưởng

- Actor-Critic (A2C, PPO, DDPG) — kết hợp một mạng "actor" chọn hành động và một mạng "critic" đánh giá hành động; PPO và DDPG là các biến thể phổ biến, ổn định hơn cho không gian hành động phức tạp/liên tục

### 4. Self-Supervised Learning (Học tự giám sát)

Tạo nhãn giả (pseudo-label) từ chính dữ liệu để học biểu diễn mà không cần gán nhãn thủ công.

- Contrastive Learning — học biểu diễn bằng cách kéo gần các mẫu tương đồng và đẩy xa các mẫu khác nhau trong không gian embedding

- Masked Language Modeling — che một phần dữ liệu (từ/token) và huấn luyện mô hình dự đoán lại phần bị che (nền tảng của BERT)

- Generative Pretext Tasks — các tác vụ tự tạo (ví dụ dự đoán phần ảnh bị thiếu) để mô hình học đặc trưng hữu ích trước khi fine-tune

- Bootstrap Your Own Latent (BYOL) — học biểu diễn tự giám sát không cần cặp âm (negative pairs), dùng hai mạng student-teacher cập nhật lẫn nhau

### 5. Semi-Supervised Learning (Học bán giám sát)

Kết hợp một lượng nhỏ dữ liệu có nhãn với lượng lớn dữ liệu không nhãn để cải thiện mô hình.

- Self-Training — mô hình tự gán nhãn cho dữ liệu chưa có nhãn dựa trên dự đoán tin cậy cao, rồi dùng lại để huấn luyện tiếp

- Co-Training — huấn luyện hai mô hình trên hai tập đặc trưng khác nhau, mỗi mô hình gán nhãn giúp mô hình còn lại

### 6. Transfer Learning (Học chuyển giao)

Tái sử dụng kiến thức từ một mô hình đã huấn luyện trên tác vụ/dữ liệu nguồn cho một tác vụ đích khác.

- Fine-Tuning — tinh chỉnh lại toàn bộ hoặc một phần trọng số của mô hình đã huấn luyện trước trên dữ liệu mới

- Feature Extraction — giữ nguyên các lớp trích xuất đặc trưng của mô hình gốc, chỉ huấn luyện lại lớp phân loại/đầu ra mới

### 7. Deep Learning (Học sâu)

Các kiến trúc mạng nơ-ron nhiều lớp, nền tảng cho phần lớn AI hiện đại.

- **Feedforward Neural Networks (FNN)** — mạng nơ-ron truyền thẳng cơ bản, dữ liệu đi một chiều từ input đến output
    - MLP (Multi-Layer Perceptron) — mạng FNN nhiều lớp ẩn kinh điển

- **Convolutional Neural Networks (CNN)** — mạng tích chập, chuyên xử lý dữ liệu dạng lưới như ảnh
    - ResNet — CNN dùng kết nối tắt (skip connection) giúp huấn luyện mạng rất sâu

    - EfficientNet — CNN được thiết kế để cân bằng tối ưu giữa độ chính xác và chi phí tính toán

    - Vision Transformers (ViT) — áp dụng kiến trúc Transformer cho ảnh bằng cách chia ảnh thành các patch

- **Recurrent Neural Networks (RNN)** — mạng hồi quy, xử lý dữ liệu tuần tự bằng cách duy trì trạng thái ẩn
    - LSTM — RNN có cơ chế cổng (gate) giúp ghi nhớ thông tin dài hạn, hạn chế vanishing gradient

    - GRU — biến thể đơn giản hơn của LSTM với ít cổng hơn nhưng hiệu quả tương đương trong nhiều bài toán

    - BiLSTM — LSTM hai chiều, xử lý chuỗi theo cả hai hướng (trái→phải và phải→trái)

- **Transformers** — kiến trúc dựa trên cơ chế attention, thay thế phần lớn RNN trong xử lý chuỗi
    - BERT — Transformer chỉ dùng encoder, huấn luyện bằng Masked Language Modeling

    - GPT — Transformer chỉ dùng decoder, huấn luyện theo kiểu tự hồi quy (autoregressive) để sinh văn bản

    - T5 — kiến trúc encoder-decoder coi mọi tác vụ NLP như bài toán text-to-text

    - LLaMA — họ mô hình ngôn ngữ lớn mã nguồn mở của Meta dựa trên kiến trúc Transformer decoder

    - ViT — Vision Transformer (cũng được liệt kê ở nhánh CNN vì áp dụng ý tưởng Transformer cho ảnh)

- **Graph Neural Networks (GNN)** — mạng nơ-ron xử lý dữ liệu dạng đồ thị
    - GCN (Graph Convolutional Network) — tích chập trên đồ thị, tổng hợp thông tin từ các nút lân cận

    - GraphSAGE — học biểu diễn nút bằng cách lấy mẫu và tổng hợp đặc trưng từ hàng xóm, mở rộng tốt cho đồ thị lớn

    - GAT (Graph Attention Network) — dùng cơ chế attention để gán trọng số khác nhau cho các nút lân cận

- **Autoencoders & Representation Learning** — học biểu diễn nén của dữ liệu
    - Autoencoders — mạng nén dữ liệu đầu vào thành biểu diễn ẩn rồi tái tạo lại, dùng để học đặc trưng/giảm nhiễu

    - Variational Autoencoders (VAE) — autoencoder xác suất, học phân phối tiềm ẩn để có thể sinh dữ liệu mới

    - Contrastive Learning — (xem thêm ở nhánh Self-Supervised Learning) cũng là một hướng học biểu diễn quan trọng trong Deep Learning

### 8. Generative AI (AI tạo sinh)

Các mô hình tạo ra nội dung mới (văn bản, ảnh, đa phương thức...).

- **Large Language Models (LLMs)** — mô hình ngôn ngữ lớn, sinh và hiểu văn bản
    - GPT-4/4o, Claude 3, Llama 3, Gemini 1.5, Mistral Large — các LLM tiêu biểu của OpenAI, Anthropic, Meta, Google, Mistral

- **Diffusion Models** — sinh ảnh bằng cách khử nhiễu dần từ nhiễu ngẫu nhiên
    - Stable Diffusion 3, DALL-E 3, Imagen 3, Midjourney — các mô hình sinh ảnh dựa trên diffusion phổ biến

- **Generative Adversarial Networks (GANs)** — hai mạng generator và discriminator cạnh tranh nhau để tạo dữ liệu giả giống thật
    - StyleGAN3, CycleGAN, Pix2Pix, BigGAN — các biến thể GAN cho sinh ảnh, chuyển đổi ảnh, ảnh độ phân giải cao

- **Multimodal Models** — mô hình xử lý đồng thời nhiều loại dữ liệu (văn bản, ảnh, v.v.)
    - GPT-4V, Gemini 1.5 Pro, LLaVA, Qwen-VL — các mô hình đa phương thức thị giác-ngôn ngữ tiêu biểu

### 9. Ensemble Learning (Học kết hợp)

Kết hợp nhiều mô hình yếu để tạo mô hình mạnh hơn.

- **Bagging** (Bootstrap Aggregating) — huấn luyện nhiều mô hình song song trên các tập con lấy mẫu ngẫu nhiên (có hoàn lại), rồi lấy trung bình/vote
    - Random Forest — tập hợp nhiều cây quyết định huấn luyện theo Bagging

- **Boosting** — huấn luyện tuần tự các mô hình yếu, mô hình sau tập trung sửa lỗi của mô hình trước
    - XGBoost, LightGBM, CatBoost, AdaBoost — các thuật toán boosting phổ biến, hiệu quả cao trên dữ liệu dạng bảng

- **Stacking** — kết hợp dự đoán của nhiều mô hình khác nhau bằng một mô hình meta-learner ở tầng trên

- **Voting** — kết hợp kết quả từ nhiều mô hình bằng biểu quyết
    - Hard Voting — lấy nhãn được đa số mô hình dự đoán

    - Soft Voting — lấy trung bình xác suất dự đoán của các mô hình rồi chọn nhãn có xác suất cao nhất

### 10. Probabilistic Graphical Models (Mô hình đồ thị xác suất)

Biểu diễn quan hệ phụ thuộc xác suất giữa các biến bằng đồ thị.

- Bayesian Networks — đồ thị có hướng phi chu trình biểu diễn quan hệ nhân quả/phụ thuộc xác suất giữa các biến

- Markov Random Fields (MRF) — đồ thị vô hướng biểu diễn quan hệ phụ thuộc xác suất đối xứng giữa các biến

- Hidden Markov Models (HMM) — mô hình chuỗi trạng thái ẩn tuân theo tính chất Markov, dùng nhiều trong nhận dạng chuỗi (giọng nói, POS tagging...)

---

*Nguồn: sơ đồ tư duy "Phân loại các nhánh Machine Learning" (*[*GenAI.works*](http://genai.works/)*, bản cập nhật 2026).*
