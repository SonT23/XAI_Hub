# Deep Learning

Đây là nhóm các kiến trúc mạng nơ-ron sâu (Deep Neural Network) đang được tìm hiểu trong đề tài NCKH, xây dựng trên nền tảng kiến thức Machine Learning cơ bản. Hiện tại bao gồm:

- **[Autoencoder](autoencoder.md)** — kiến trúc học tự giám sát dùng để nén và tái tạo dữ liệu, cùng các biến thể (Sparse, Denoising, Contractive, Convolutional).
- **[Variational Autoencoder (VAE)](vae.md)** — biến thể mang bản chất xác suất, là **mô hình sinh (generative model)**. Có trang riêng với phần **so sánh chi tiết AE vs VAE**.
- **[CNN (Convolutional Neural Network)](cnn.md)** — kiến trúc chuyên xử lý dữ liệu dạng lưới như ảnh, nền tảng của hầu hết các mô hình Computer Vision hiện đại.
- **[Transformer & ViT](transformer-vit.md)** — cơ chế Attention và Vision Transformer, backbone của mọi bài CBM từ 2023 trở đi.
- **[CLIP](clip.md)** — mô hình đa phương thức ảnh–chữ, công cụ giúp xóa bỏ chi phí gán nhãn khái niệm trong CBM.
- **[Latent Space](latent-space.md)** — khái niệm **xuyên suốt mọi kiến trúc ở trên**, không riêng Autoencoder. Đọc trang này để hiểu phạm vi áp dụng thật sự của nó và vì sao **CBM chính là một latent space bị buộc phải diễn giải được**.
