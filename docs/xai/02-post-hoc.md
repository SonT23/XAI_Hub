# 2. Các phương pháp hậu kỳ (Post-hoc)

Các phương pháp này **không thay đổi mô hình gốc**. Mô hình vẫn được huấn luyện như hộp đen, sau đó ta dùng công cụ bên ngoài để ước lượng xem nó đã dựa vào đâu để quyết định. Đây là nhóm phương pháp **đối lập** với CBM, cần nắm để hiểu vì sao CBM được đề xuất.

### 1. LIME (Local Interpretable Model-agnostic Explanations)

**Ý tưởng:** Một mô hình phức tạp có thể rất phi tuyến trên toàn bộ không gian dữ liệu, nhưng **quanh một điểm dữ liệu cụ thể** thì có thể xấp xỉ bằng một mô hình tuyến tính đơn giản.

**Cách hoạt động:**

1. Lấy mẫu dữ liệu "nhiễu loạn" xung quanh điểm cần giải thích (với ảnh: tắt/bật ngẫu nhiên các vùng superpixel).

2. Đưa các mẫu này qua mô hình hộp đen để lấy dự đoán.

3. Huấn luyện một mô hình tuyến tính đơn giản trên các cặp (mẫu, dự đoán), có trọng số ưu tiên các mẫu gần điểm gốc.

4. Đọc hệ số của mô hình tuyến tính này → biết đặc trưng nào đóng góp bao nhiêu.

**Hạn chế:** kết quả không ổn định (chạy hai lần có thể ra hai lời giải thích khác nhau do lấy mẫu ngẫu nhiên), và định nghĩa "lân cận" rất nhạy cảm với tham số.

### 2. SHAP (SHapley Additive exPlanations)

**Ý tưởng:** Mượn khái niệm **giá trị Shapley** từ lý thuyết trò chơi hợp tác: coi mỗi đặc trưng như một "người chơi" trong một đội, và chia công bằng "phần thưởng" (tức giá trị dự đoán) cho từng đặc trưng dựa trên đóng góp biên trung bình của nó qua mọi tổ hợp có thể.

**Ưu điểm:** có nền tảng toán học vững chắc với các tính chất đẹp (tính cộng tính, tính công bằng), ổn định hơn LIME, và có thể tổng hợp các giải thích local thành cái nhìn global.

**Hạn chế:** chi phí tính toán rất lớn (số tổ hợp tăng theo cấp số mũ), nên thực tế phải dùng các bản xấp xỉ (KernelSHAP, TreeSHAP, DeepSHAP).

### 3. Saliency Maps (Bản đồ nổi bật)

**Ý tưởng:** Tính **gradient của điểm số đầu ra theo từng pixel đầu vào**. Pixel nào có gradient lớn nghĩa là thay đổi nhỏ ở pixel đó sẽ làm đầu ra thay đổi nhiều → pixel đó "quan trọng". Kết quả hiển thị dưới dạng heatmap chồng lên ảnh gốc.

**Hạn chế nặng:** Saliency map thường nhiễu, và nghiêm trọng hơn — nhiều nghiên cứu cho thấy một số phương pháp saliency cho ra heatmap **gần như không đổi** ngay cả khi trọng số mô hình bị ngẫu nhiên hóa (sanity check của Adebayo et al.), tức là chúng không thực sự phản ánh những gì mô hình học được.

### 4. Grad-CAM (Gradient-weighted Class Activation Mapping)

**Ý tưởng:** Thay vì làm việc ở mức pixel, Grad-CAM dùng gradient chảy về **lớp tích chập cuối cùng** để tính trọng số cho từng feature map, rồi tổ hợp chúng thành một heatmap thô chỉ ra vùng ảnh mà mô hình "nhìn vào" khi dự đoán một lớp cụ thể.

**Ưu điểm:** ổn định hơn saliency thuần, trực quan, rất phổ biến với [CNN](../deep-learning/cnn.md).

**Hạn chế:** độ phân giải thấp (vì lấy từ feature map đã bị thu nhỏ nhiều lần), và chỉ trả lời được **"ở đâu"** chứ không trả lời được **"cái gì"**.

> 🎯 **Đây chính là động lực dẫn tới CBM.** Grad-CAM chỉ cho biết mô hình nhìn vào **vùng nào** của ảnh, nhưng không cho biết nó nhìn thấy **đặc điểm gì** ở đó. Bác sĩ cần nghe "có gai xương và hẹp khe khớp" chứ không phải một vệt màu đỏ trên ảnh. CBM ra đời để giải quyết đúng khoảng trống này.

### Nguồn tham khảo

- ["Why Should I Trust You?" Explaining the Predictions of Any Classifier – Ribeiro et al. (LIME)](https://arxiv.org/abs/1602.04938)

- [A Unified Approach to Interpreting Model Predictions – Lundberg & Lee (SHAP)](https://arxiv.org/abs/1705.07874)

- [Grad-CAM: Visual Explanations from Deep Networks – Selvaraju et al.](https://arxiv.org/abs/1610.02391)

- [Sanity Checks for Saliency Maps – Adebayo et al.](https://arxiv.org/abs/1810.03292)
