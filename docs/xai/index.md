# XAI — Explainable AI

**Explainable AI (XAI — AI có khả năng giải thích)** là lĩnh vực nghiên cứu các phương pháp giúp con người hiểu được **tại sao** một mô hình AI đưa ra một dự đoán cụ thể, thay vì chỉ nhận được kết quả từ một "hộp đen" (black box).

> **💡 Tại sao cần XAI?** Các mô hình Deep Learning hiện đại có hàng triệu tham số và hoạt động như hộp đen. Trong các lĩnh vực rủi ro cao (y tế, tài chính, pháp lý, xe tự lái), việc không giải thích được quyết định làm mất niềm tin, khó gỡ lỗi, và có thể vi phạm quy định pháp lý (ví dụ GDPR có "quyền được giải thích").

1. [Tổng quan & Phân loại XAI](01-tong-quan.md) — hiểu bức tranh lớn, biết CBM nằm ở đâu trong đó.
2. [Các phương pháp hậu kỳ (Post-hoc)](02-post-hoc.md) — LIME, SHAP, Saliency Maps, Grad-CAM.
3. [Phương pháp dựa trên khái niệm (Concept-based)](03-concept-based.md) — TCAV, tiền đề trực tiếp dẫn tới CBM.
4. [CBM — Concept Bottleneck Models](04-cbm.md) — **trọng tâm nghiên cứu của đề tài.**
5. [Các biến thể & cải tiến của CBM](05-bien-the-cbm.md) — hướng phát triển mới nhất.
6. [Đánh giá chất lượng lời giải thích](06-danh-gia.md) — làm sao biết một lời giải thích là đáng tin.
7. [Bộ dữ liệu & Công cụ](07-du-lieu-cong-cu.md) — phục vụ phần thực nghiệm.
