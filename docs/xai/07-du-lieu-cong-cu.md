# 7. Bộ dữ liệu & Công cụ

Phần này phục vụ trực tiếp cho khâu thực nghiệm của đề tài.

### Bộ dữ liệu có nhãn khái niệm

Để huấn luyện CBM, dữ liệu phải có **cả nhãn lớp (y) lẫn nhãn khái niệm (c)** — điều mà đa số bộ dữ liệu thông thường không có.

- **CUB-200-2011 (Caltech-UCSD Birds):** bộ dữ liệu **chuẩn nhất** cho CBM. 200 loài chim, ~11.788 ảnh, kèm **312 thuộc tính nhị phân** (màu mỏ, hình cánh, họa tiết lông...). Hầu hết bài báo về CBM đều báo cáo kết quả trên bộ này.

- **AwA2 (Animals with Attributes 2):** 50 loài động vật, 85 thuộc tính ngữ nghĩa.

- **OAI (Osteoarthritis Initiative):** ảnh X-quang khớp gối kèm các khái niệm lâm sàng (gai xương, hẹp khe khớp, xơ hóa) — chính là ví dụ y tế được dùng trong bài báo CBM gốc.

- **Derm7pt:** ảnh tổn thương da kèm 7 tiêu chí chẩn đoán da liễu.

### Thư viện & công cụ

- **Captum** (PyTorch, của Meta) — thư viện XAI toàn diện nhất cho PyTorch: Integrated Gradients, Grad-CAM, TCAV, Shapley.

- **SHAP** — thư viện chính thức của phương pháp SHAP.

- **LIME** — thư viện chính thức của LIME.

- **pytorch-grad-cam** — triển khai nhiều biến thể CAM (Grad-CAM, Grad-CAM++, Score-CAM...).

- **CLIP** (OpenAI) — dùng để tự động chấm điểm khái niệm trong Label-free CBM.

### Nguồn tham khảo

- [CUB-200-2011 Dataset](https://www.vision.caltech.edu/datasets/cub_200_2011/)

- [Captum – Model Interpretability for PyTorch](https://captum.ai/)

- [SHAP documentation](https://shap.readthedocs.io/)

- [Awesome Concept Bottleneck Models (tổng hợp bài báo)](https://github.com/Kaist-AIPRLab/Awesome-Concept-Bottleneck-Models)
