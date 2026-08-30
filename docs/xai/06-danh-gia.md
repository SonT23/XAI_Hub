# 6. Đánh giá chất lượng lời giải thích

Một lời giải thích **trông hợp lý** chưa chắc đã **đúng**. Đây là vấn đề trung tâm của XAI hiện đại và là phần bắt buộc phải nắm khi viết báo cáo NCKH.

## Hai tiêu chí dễ nhầm lẫn nhất

- **Faithfulness (Độ trung thực):** lời giải thích có phản ánh đúng quá trình mà mô hình **thực sự** dùng để ra quyết định hay không?
- **Plausibility (Độ hợp lý):** lời giải thích có **thuyết phục với con người** hay không?

> Hai tiêu chí này **có thể đối lập nhau**. Một lời giải thích rất plausible nhưng không faithful là **nguy hiểm nhất**: nó tạo cảm giác an tâm giả tạo, khiến người dùng tin vào một mô hình đang thực sự quyết định dựa trên lý do khác hẳn.

## Các phép đo thường dùng

### Cho phương pháp attribution (LIME, SHAP, Grad-CAM)

- **Deletion / Insertion:** lần lượt xóa (hoặc thêm) các pixel được cho là quan trọng nhất rồi đo độ tụt (hoặc tăng) của điểm số dự đoán. Độ tụt càng nhanh → lời giải thích càng faithful.
- **Sanity Check (Adebayo et al.):** ngẫu nhiên hóa dần trọng số mô hình; nếu heatmap **không đổi** thì phương pháp đó không thực sự đo lường mô hình.

### Cho CBM và các mô hình dựa trên khái niệm

- **Concept Accuracy:** độ chính xác của tầng dự đoán khái niệm (x → c), đo **tách biệt** với độ chính xác tác vụ cuối (c → y).
- **Intervention Curve:** đồ thị thể hiện độ chính xác tác vụ tăng như thế nào khi ta lần lượt sửa đúng từng khái niệm. **Đường cong dốc lên đều** chứng tỏ mô hình thực sự dùng khái niệm để quyết định; đường cong phẳng là dấu hiệu của **concept leakage**.
- **Calibration:** điểm tin cậy của khái niệm có phản ánh đúng xác suất thực tế hay không.

## Đánh giá có sự tham gia của con người

Cuối cùng, XAI phục vụ con người nên cần **human study**: đo xem người dùng có dự đoán đúng hành vi mô hình tốt hơn khi có lời giải thích không, và họ có phát hiện được lỗi của mô hình nhanh hơn không.

## Nguồn tham khảo

- [Sanity Checks for Saliency Maps – Adebayo et al.](https://arxiv.org/abs/1810.03292)
- [Towards A Rigorous Science of Interpretable Machine Learning – Doshi-Velez & Kim](https://arxiv.org/abs/1702.08608)
- [The Mythos of Model Interpretability – Lipton](https://arxiv.org/abs/1606.03490)
- [Probability Calibration – scikit-learn](https://scikit-learn.org/stable/modules/calibration.html)
