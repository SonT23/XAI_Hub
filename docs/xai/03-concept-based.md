# 3. Phương pháp dựa trên khái niệm (Concept-based)

Nhóm phương pháp này chuyển đơn vị giải thích từ **pixel/đặc trưng thô** sang **khái niệm mà con người hiểu được** (ví dụ: "có sọc", "màu đỏ", "có bánh xe"). Đây là tiền đề trực tiếp dẫn tới **4. CBM — Concept Bottleneck Models**.

### TCAV (Testing with Concept Activation Vectors)

**Ý tưởng:** Google đề xuất năm 2018. Thay vì hỏi "pixel nào quan trọng", TCAV hỏi: **"khái niệm 'sọc' ảnh hưởng bao nhiêu đến việc mô hình phân loại ảnh này là con ngựa vằn?"**

**Cách hoạt động:**

1. Người dùng chuẩn bị một tập ảnh **có** khái niệm (ví dụ: ảnh có sọc) và một tập ảnh ngẫu nhiên **không có** khái niệm đó.

2. Đưa cả hai tập qua mạng, lấy activation ở một lớp ẩn.

3. Huấn luyện một bộ phân loại tuyến tính để tách hai tập này trong không gian activation. Vector pháp tuyến của siêu phẳng phân tách chính là **CAV (Concept Activation Vector)** — hướng đại diện cho khái niệm đó.

4. Tính **đạo hàm có hướng** của điểm số lớp dự đoán theo hướng CAV → cho biết khái niệm đó đẩy dự đoán theo hướng nào và mạnh bao nhiêu.

**Ưu điểm:** lời giải thích ở **cấp độ khái niệm** chứ không phải pixel; là giải thích **global** (đúng cho cả lớp, không chỉ một ảnh); không cần huấn luyện lại mô hình.

**Hạn chế:** vẫn là **post-hoc** — chỉ "dò xem" mô hình có nhạy cảm với khái niệm hay không, chứ không **bắt buộc** mô hình phải dùng khái niệm đó để quyết định. Người dùng cũng không thể can thiệp sửa khái niệm rồi xem kết quả thay đổi.

### Từ TCAV đến CBM

| Tiêu chí | TCAV | CBM |
| --- | --- | --- |
| Loại | Post-hoc | Intrinsic |
| Khái niệm nằm ở đâu | Dò tìm trong không gian ẩn có sẵn | Là một tầng bắt buộc trong kiến trúc |
| Có can thiệp được không | Không | Có — sửa khái niệm, tính lại kết quả |
| Chi phí nhãn | Chỉ cần tập ảnh ví dụ cho khái niệm | Cần gán nhãn khái niệm cho toàn bộ dữ liệu |

### Nguồn tham khảo

- [Interpretability Beyond Feature Attribution: TCAV – Kim et al.](https://arxiv.org/abs/1711.11279)

- [Network Dissection: Quantifying Interpretability of Deep Visual Representations – Bau et al.](https://arxiv.org/abs/1704.05796)
