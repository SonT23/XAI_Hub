# 2. Các phương pháp hậu kỳ (Post-hoc)

Các phương pháp này **không thay đổi mô hình gốc**. Mô hình vẫn được huấn luyện như hộp đen, sau đó ta dùng công cụ bên ngoài để ước lượng xem nó đã dựa vào đâu để quyết định. Đây là nhóm phương pháp **đối lập** với CBM, cần nắm để hiểu vì sao CBM được đề xuất.

### 1. LIME (Local Interpretable Model-agnostic Explanations)

**Ý tưởng:** Một mô hình phức tạp có thể rất phi tuyến trên toàn bộ không gian dữ liệu, nhưng **quanh một điểm dữ liệu cụ thể** thì có thể xấp xỉ bằng một mô hình tuyến tính đơn giản. Ở đâu muốn nói rằng khi ta nhìn một mô hình hiện nay ( hộp đen ) ta có thể thấy chúng không phải là một đường thẳng mà rất ngoằn ngoèo và phụ thuộc rất nhiều vào vô số biến số. Như khi bạn tự tưởng tưởng ra một ma trận hàng chục chiều chẳng hạn. Vậy hãy thử phóng to nó ra, bỏ ngoài mắt các yếu tố xung quanh và tập trung vào 1 điểm, 1 khu vực cực nhỏ, nó sẽ trông giống hệt một đường thẳng. Tại đây ta dùng các phương trình tuyến tính đơn giản để giải thích cho điểm này, nó có quan trọng hay không?. Bạn không cần hiểu hết mô hình mà chỉ cần biết mình muốn gì để tìm ra mục đích và thông tin cần có để từ đó có style (cách biểu diễn phù hợp) phù hợp ( liên quan đến Meaningfulness đã nhắc ở phần 1 :four principle for XAI). Tiếp tục với một bức ảnh 100x100, LIME sẽ gom đống này thành 1 mảng có nghĩa, lúc này LIME sẽ che đi từng mảng để xem dự đoán thay đổi thế nào để cuối cùng có thể đưa ra đánh giá về mức đóng góp của mảng đó trong quá trình dự đoán.

**Cách hoạt động:**

1. Lấy mẫu dữ liệu "nhiễu loạn" xung quanh điểm cần giải thích (với ảnh: tắt/bật ngẫu nhiên các vùng superpixel). Có thể hiểu là từ ảnh hoàn thiện ta bỏ bớt một vài thứ của bức ảnh đó ra để đánh giá xem cái bỏ ra đó có quan trọng trong việc dự đoán hay không.

2. Đưa các mẫu này qua mô hình hộp đen để lấy dự đoán.

3. Huấn luyện một mô hình tuyến tính đơn giản trên các cặp (mẫu, dự đoán), có trọng số ưu tiên các mẫu gần điểm gốc.

4. Đọc hệ số của mô hình tuyến tính này → biết đặc trưng nào đóng góp bao nhiêu.

**Hạn chế:** kết quả không ổn định (chạy hai lần có thể ra hai lời giải thích khác nhau do lấy mẫu ngẫu nhiên), và định nghĩa "lân cận" rất nhạy cảm với tham số.

### 2. SHAP (SHapley Additive exPlanations)

**Ý tưởng:** Mượn khái niệm **giá trị Shapley** từ lý thuyết trò chơi hợp tác: coi mỗi đặc trưng như một "người chơi" trong một đội, và chia công bằng "phần thưởng" (tức giá trị dự đoán) cho từng đặc trưng dựa trên đóng góp biên trung bình của nó qua mọi tổ hợp có thể.

Ví dụ với các đặc trưng đầu vào, ta sẽ tính mức đóng gọp trung bình của từng đặc trừng bằng cách ghép các nhóm lại với nhau với các trường hợp có B, không có B, khi ghép 2 đặc trưng A,B thì sao? A,C thì sao? Từ đó tìm ra giá trị mà đặc trưng xứng đáng nhận.

**Ưu điểm:** có nền tảng toán học vững chắc với các tính chất đẹp (tính cộng tính, tính công bằng), ổn định hơn LIME, và có thể tổng hợp các giải thích local thành cái nhìn global.

**Hạn chế:** chi phí tính toán rất lớn (số tổ hợp tăng theo cấp số mũ), nên thực tế phải dùng các bản xấp xỉ (KernelSHAP, TreeSHAP, DeepSHAP).

### 3. Saliency Maps (Bản đồ nổi bật)

**Ý tưởng:** Tính **gradient của điểm số đầu ra theo từng pixel đầu vào**. Pixel nào có gradient lớn nghĩa là thay đổi nhỏ ở pixel đó sẽ làm đầu ra thay đổi nhiều → pixel đó "quan trọng". Kết quả hiển thị dưới dạng heatmap chồng lên ảnh gốc.

**Hạn chế nặng:** Saliency map thường nhiễu, và nghiêm trọng hơn — nhiều nghiên cứu cho thấy một số phương pháp saliency cho ra heatmap **gần như không đổi** ngay cả khi trọng số mô hình bị ngẫu nhiên hóa (sanity check của Adebayo et al.), tức là chúng không thực sự phản ánh những gì mô hình học được.

### 4. Grad-CAM (Gradient-weighted Class Activation Mapping)

**Ý tưởng:** Thay vì làm việc ở mức pixel, Grad-CAM dùng gradient chảy về **lớp tích chập cuối cùng** để tính trọng số cho từng feature map, rồi tổ hợp chúng thành một heatmap thô chỉ ra vùng ảnh mà mô hình "nhìn vào" khi dự đoán một lớp cụ thể. Nơi màu đỏ/cam chỉ ra vùng AI quan tâm nhất, còn màu xanh là vùng bị phớt lờ.

- **Feature Map (Lớp tích chập cuối cùng):** Trong mạng CNN, các lớp đầu tiên nhìn vào những chi tiết vụn vặt (cạnh, góc, màu sắc). Khi đi sâu đến lớp tích chập cuối cùng, AI đã gom các chi tiết này thành những "khái niệm" lớn hơn (như: hình dáng cái bánh xe, đôi tai chó, biển số xe). Lớp cuối này giống như các **Trưởng phòng** đang cầm bản tóm tắt báo cáo.

- **Gradient (Tín hiệu phản hồi):** Khi AI đưa ra kết luận cuối cùng (ví dụ: "Đây là xe ô tô"), quyết định này giống như **Tổng giám đốc** chốt hạ. Grad-CAM sẽ chạy ngược từ quyết định của Tổng giám đốc về lại các Trưởng phòng để hỏi: *"Trưởng phòng nào cung cấp dữ liệu quan trọng nhất dẫn đến quyết định này?"*.

- **Tổ hợp Heatmap:** Phản hồi ngược này (gradient) chính là điểm số trọng lượng. Trưởng phòng báo cáo "bánh xe" được chấm điểm cao nhất. Grad-CAM lấy báo cáo đó, phóng to lên và đắp lên bức ảnh gốc thành một bản đồ nhiệt (Heatmap) rực đỏ ở ngay vị trí các bánh xe.

**Ưu điểm:** ổn định hơn saliency thuần, trực quan, rất phổ biến với [CNN](../deep-learning/cnn.md). Bạn không cần đọc các con số hay phương trình. Chỉ cần nhìn vào ảnh có mảng màu đỏ là hiểu ngay AI đang tập trung vào đâu.

**Hạn chế:** độ phân giải thấp (vì lấy từ feature map đã bị thu nhỏ nhiều lần), và chỉ trả lời được **"ở đâu"** chứ không trả lời được **"cái gì"**.

> 🎯 **Đây chính là động lực dẫn tới CBM.** Grad-CAM chỉ cho biết mô hình nhìn vào **vùng nào** của ảnh, nhưng không cho biết nó nhìn thấy **đặc điểm gì** ở đó. Bác sĩ cần nghe "có gai xương và hẹp khe khớp" chứ không phải một vệt màu đỏ trên ảnh. CBM ra đời để giải quyết đúng khoảng trống này.

### Nguồn tham khảo

- ["Why Should I Trust You?" Explaining the Predictions of Any Classifier – Ribeiro et al. (LIME)](https://arxiv.org/abs/1602.04938)

- [A Unified Approach to Interpreting Model Predictions – Lundberg & Lee (SHAP)](https://arxiv.org/abs/1705.07874)

- [Grad-CAM: Visual Explanations from Deep Networks – Selvaraju et al.](https://arxiv.org/abs/1610.02391)

- [Sanity Checks for Saliency Maps – Adebayo et al.](https://arxiv.org/abs/1810.03292)
