# 1. Tổng quan & Phân loại XAI

### Khái niệm

**Explainable AI (XAI)** là tập hợp các kỹ thuật giúp con người hiểu và tin tưởng được kết quả do mô hình AI tạo ra. Cần phân biệt hai khái niệm thường bị dùng lẫn lộn:

- **Interpretability (Tính dễ hiểu):** mức độ mà con người có thể hiểu được **cơ chế nội tại** của mô hình. Một cây quyết định nông là interpretable vì ta đọc được toàn bộ luồng suy luận.

- **Explainability (Khả năng giải thích):** khả năng đưa ra **lời giải thích cho một quyết định cụ thể**, kể cả khi bên trong mô hình vẫn là hộp đen.

### Bốn nguyên tắc của XAI theo NIST

NIST (Viện Tiêu chuẩn và Công nghệ Quốc gia Hoa Kỳ) đề xuất 4 nguyên tắc làm chuẩn đánh giá một hệ thống XAI:

1. **Explanation (Có lời giải thích):** hệ thống phải cung cấp bằng chứng/lý do kèm theo mỗi đầu ra.

2. **Meaningful (Có ý nghĩa):** lời giải thích phải dễ hiểu đối với người dùng mục tiêu (bác sĩ và kỹ sư ML cần hai kiểu giải thích khác nhau). Ví dụ với bức ảnh 100x100, AI sẽ nhìn nhận nó như là 10000 con số, khi dự đoán ra bức ảnh, AI đã thực hiện rất nhiều các phương trình toán học phức tạp trên 10.000 con số này.

3. **Explanation Accuracy (Chính xác):** lời giải thích phải phản ánh đúng quá trình mà mô hình thực sự dùng để ra quyết định.

4. **Knowledge Limits (Biết giới hạn):** hệ thống phải biết khi nào nó không đủ tin cậy để trả lời.

> ⚠️ **Lưu ý quan trọng:** một lời giải thích **dễ hiểu** không tự động đồng nghĩa với **chính xác**. Đây chính là vấn đề "faithfulness" (độ trung thực) — sẽ học kỹ ở phần Đánh giá chất lượng lời giải thích.

### Ba trục phân loại các phương pháp XAI

#### Trục 1: Intrinsic vs Post-hoc (Nội tại vs Hậu kỳ)

Đây là trục phân loại **quan trọng nhất** để hiểu vị trí của CBM.

- **Intrinsic (Nội tại / Ante-hoc):** tính giải thích được **thiết kế sẵn vào kiến trúc** mô hình. Ví dụ: cây quyết định, hồi quy tuyến tính, và **CBM**.

- **Post-hoc (Hậu kỳ):** mô hình được huấn luyện bình thường như hộp đen, sau đó dùng công cụ khác để "đoán" xem nó đã dựa vào đâu. Ví dụ: LIME, SHAP, Grad-CAM.

**Đánh đổi:** Post-hoc linh hoạt (áp được cho mọi mô hình có sẵn) nhưng lời giải thích chỉ là **ước lượng gần đúng** từ bên ngoài, có thể không phản ánh đúng cơ chế thật. Intrinsic cho lời giải thích trung thực hơn vì nó **chính là** đường đi của dữ liệu, nhưng thường phải đánh đổi một phần độ chính xác và tốn chi phí gán nhãn.

#### Trục 2: Model-specific vs Model-agnostic

- **Model-specific:** chỉ dùng được cho một loại mô hình nhất định (ví dụ Grad-CAM chỉ dùng cho mạng CNN vì cần truy cập gradient và feature map).

- **Model-agnostic:** dùng được cho bất kỳ mô hình nào, chỉ cần đưa đầu vào và quan sát đầu ra (LIME, SHAP).

#### Trục 3: Local vs Global

- **Local:** giải thích **một dự đoán cụ thể** ("tại sao ảnh X-quang này bị chẩn đoán là viêm phổi?").

- **Global:** giải thích **hành vi tổng thể** của mô hình ("nói chung mô hình này coi trọng đặc trưng nào nhất?").

### Bảng định vị các phương pháp

| Phương pháp | Intrinsic/Post-hoc | Phạm vi | Áp dụng cho |
| --- | --- | --- | --- |
| Decision Tree | Intrinsic | Global + Local | Mô hình cây |
| LIME | Post-hoc | Local | Mọi mô hình |
| SHAP | Post-hoc | Local + Global | Mọi mô hình |
| Saliency / Grad-CAM | Post-hoc | Local | Mạng nơ-ron (CNN) |
| TCAV | Post-hoc | Global | Mạng nơ-ron |
| CBM | Intrinsic | Local + Global | Kiến trúc riêng |

### Nguồn tham khảo

- [NIST – Four Principles of Explainable Artificial Intelligence](https://www.nist.gov/publications/four-principles-explainable-artificial-intelligence)

- [Interpretable Machine Learning – Christoph Molnar (sách miễn phí online)](https://christophm.github.io/interpretable-ml-book/)

- [Google PAIR – People + AI Guidebook](https://pair.withgoogle.com/)
