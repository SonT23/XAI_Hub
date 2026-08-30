# 5. Các biến thể & cải tiến của CBM

CBM gốc (Koh et al., 2020) có 3 điểm yếu lớn, và mỗi biến thể sau đây sinh ra để vá một trong số đó:

> **3 điểm yếu của CBM gốc:**
>
> 1. **Chi phí gán nhãn khái niệm** rất đắt, cần chuyên gia.
> 2. **Đánh đổi độ chính xác** — ép qua bottleneck khái niệm thường làm giảm accuracy so với mô hình hộp đen.
> 3. **Rò rỉ khái niệm (concept leakage)** — giá trị khái niệm liên tục bí mật mã hóa thêm thông tin ngoài ý nghĩa đã nêu, phá vỡ tính minh bạch.

## 1. Post-hoc CBM (PCBM)

**Vá điểm yếu số 1 và 2.** Thay vì huấn luyện lại từ đầu, PCBM chuyển **một mô hình hộp đen đã huấn luyện sẵn** thành dạng CBM bằng cách chiếu không gian ẩn của nó lên một tập khái niệm (có thể lấy từ nguồn bên ngoài như ConceptNet hoặc CAV của TCAV). PCBM còn thêm một **residual predictor** để bù lại phần thông tin mà tập khái niệm không biểu diễn được, giúp giữ độ chính xác gần bằng mô hình gốc.

## 2. Label-free CBM / LaBo

**Vá điểm yếu số 1 triệt để hơn.** Dùng **mô hình ngôn ngữ lớn (LLM)** để tự sinh ra danh sách khái niệm cho từng lớp (ví dụ hỏi GPT: "những đặc điểm nhìn thấy được của chim sẻ là gì?"), rồi dùng **CLIP** để tự động chấm điểm mức độ xuất hiện của từng khái niệm trên ảnh — **không cần con người gán nhãn khái niệm nào cả**.

## 3. Concept Embedding Models (CEM)

**Vá điểm yếu số 2 và 3.** Vấn đề của CBM gốc: mỗi khái niệm chỉ là **một con số vô hướng** (có/không, hay xác suất) → quá ít sức chứa thông tin, dẫn đến mất độ chính xác hoặc bị rò rỉ. CEM thay mỗi khái niệm bằng **một vector nhúng (embedding)** gồm hai trạng thái (khái niệm có mặt / vắng mặt), vừa giữ được khả năng can thiệp của con người, vừa có đủ dung lượng biểu diễn để không mất độ chính xác.

## 4. Interactive / Intervention-aware CBM

Tập trung vào việc **tối ưu hóa can thiệp (intervention)**: khi chuyên gia chỉ có thời gian sửa 3 khái niệm trong số 100, nên sửa khái niệm nào để cải thiện kết quả nhiều nhất? Các phương pháp này học một **chính sách ưu tiên can thiệp** thay vì để người dùng chọn ngẫu nhiên.

## Nguồn tham khảo

- [Concept Bottleneck Models – Koh et al. (bài báo gốc)](https://arxiv.org/abs/2007.04612)
- [Post-hoc Concept Bottleneck Models – Yuksekgonul et al.](https://arxiv.org/abs/2205.15480)
- [Label-free Concept Bottleneck Models – Oikarinen et al.](https://arxiv.org/abs/2304.06129)
- [Concept Embedding Models – Espinosa Zarlenga et al.](https://arxiv.org/abs/2209.09056)
- [Promises and Pitfalls of Black-Box Concept Learning Models – Margeloiu et al. (về concept leakage)](https://arxiv.org/abs/2106.13314)
