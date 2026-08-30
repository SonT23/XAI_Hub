# Tổng quan luồng dữ liệu của CBM.

Các mô hình thông thường sẽ có dạng x → y.

Mô hình CBM sẽ thay đổi cấu trúc thành x → c → y.

Trong đó, toàn bộ kiến trúc sẽ được chia làm hai mô đun chính: 

- Dự đoán các khái niệm ( Concept Prediction): chúng ta sẽ lấy ảnh đầu vào x và dự đoán ra vector chứa K khái niệm (concepts).

- Mạng dự đoán nhãn (Label Predictor): Lấy đầu vào là vector khái niệm đã được dữ đoán ở trong mô đun trước đó để đoán ra nhãn phân loại cuối cùng của ảnh đầu vào x.

Các khái niệm sẽ được đặt bởi người tạo hoặc bởi các chuyên gia trong lĩnh vực.


---

## Các Phương Pháp Huấn Luyện

1. **Independent Bottleneck (Huấn luyện Độc lập)**

**Cách hoạt động:** Hai mạng nơ-ron được huấn luyện hoàn toàn tách biệt. Đầu tiên, một mạng được huấn luyện để dự đoán khái niệm từ đầu vào ( x → c). Một mạng khác được huấn luyện độc lập để dựy đoán kết quả cuối cùng từ các khái niệm chuẩn do con người gán nhãn (c → y).
**Đặc điểm:** Mô hình dự đoán nhãn (c → y) không hề biết đến các lỗi sai của mô hình dự đoán khái niệm (x → c). Khi chạy thực tế, đầu ra của mạng thứ nhất được cắm thẳng vào mạng thứ hai.

1. **Sequential Bottleneck (Huấn luyện Nối tiếp)**


**Cách hoạt động:** Tương tự như Độc lập, nhưng mạng thứ hai (c → y) được huấn luyện bằng cách sử dụng **kết quả dự đoán khái niệm** (c mũ) của mạng thứ nhất, thay vì sử dụng nhãn khái niệm chuẩn c.
**Đặc điểm:** Giúp mạng dự đoán kết quả cuối cùng làm quen với các "lỗi" hoặc độ nhiễu từ mạng dự đoán khái niệm, giúp mô hình hoạt động thực tế trơn tru hơn.

**3. Joint Bottleneck (Huấn luyện Đồng thời)**


**Cách hoạt động:** Cả hai quá trình (x → c và c → y) được liên kết thành một mạng duy nhất và huấn luyện cùng lúc. Hàm mất mát (Loss function) là sự kết hợp có trọng số giữa lỗi dự đoán khái niệm và lỗi dự đoán kết quả cuối cùng: Loss = Loss_y + lambda .Loss_c.
**Đặc điểm:** Cho phép mạng cập nhật trọng số linh hoạt hơn. Tuy nhiên, nếu trọng số lambda không đủ lớn, mô hình có xu hướng giấu thông tin của đầu vào $x$ thẳng vào kết quả y mà không qua khái niệm $c$, làm mất đi tính minh bạch cốt lõi của CBM.


---

## Điểm mạnh, hạn chế và ứng dụng

CBM là một dạng [explainable AI](https://www.ultralytics.com/glossary/explainable-ai-xai) nội tại: cấu trúc dễ giải thích của chúng được tích hợp ngay vào quá trình dự đoán thay vì được thêm vào sau đó. Điều này khác với các công cụ hậu kỳ như [saliency maps](https://www.ultralytics.com/glossary/saliency-maps), vốn ước tính những yếu tố ảnh hưởng đến một hộp đen đã được huấn luyện.

Tầng khái niệm hỗ trợ một số tương tác hữu ích:

- Người dùng có thể kiểm tra những khái niệm nào đã gây ra một quyết định.

- Các chuyên gia miền có thể chỉnh sửa một khái niệm không chính xác và tính toán lại kết quả đầu ra.

- Các lập trình viên có thể kiểm tra xem bộ dự đoán mục tiêu có tuân theo logic miền hợp lệ hay không.

- Các nhóm có thể đo lường độ chính xác của khái niệm tách biệt với độ chính xác của tác vụ cuối cùng.

Các khả năng này phù hợp với [NIST guidance on explainable AI](https://www.nist.gov/publications/four-principles-explainable-artificial-intelligence) và các biện pháp kiểm soát lấy con người làm trung tâm được thảo luận trong [People + AI Guidebook](https://pair.withgoogle.com/old-gb/). Tuy nhiên, một lời giải thích dễ hiểu không tự động đồng nghĩa với một lời giải thích chính xác. Độ trung thực của khái niệm phải được đánh giá thay vì giả định.

#### **Các ứng dụng trong thực tế:**

- [**Medical Image Analysis**](https://www.ultralytics.com/glossary/medical-image-analysis)**:** Một mô hình kiểm tra phim X-quang có thể ước tính các khái niệm như gai xương, thu hẹp khoảng cách khớp và xơ hóa trước khi phân loại mức độ nghiêm trọng của bệnh. Bác sĩ lâm sàng có thể xem xét hoặc chỉnh sửa các kết quả trung gian này thay vì chỉ nhận được một điểm số mức độ nghiêm trọng. Sự tương tác giữa con người và mô hình này đặc biệt có liên quan đến [FDA transparency principles for machine-learning medical devices](https://www.fda.gov/medical-devices/software-medical-device-samd/transparency-machine-learning-enabled-medical-devices-guiding-principles).

- [**Manufacturing Visual Inspection**](https://www.ultralytics.com/use-cases/visual-inspection)**:** Một hệ thống thị giác máy tính có thể nhận diện các concept như linh kiện bị thiếu, vết nứt, sự đổi màu hoặc căn chỉnh sai, sau đó sử dụng chúng để quyết định xem một sản phẩm có đạt kiểm tra hay cần sửa chữa cụ thể. [Object detection](https://www.ultralytics.com/glossary/object-detection) có thể xác định vị trí của các linh kiện và lỗi, trong khi trình phân loại dựa trên concept ở hạ nguồn cung cấp quyết định chất lượng có thể kiểm toán được.

#### **Hạn chế và Các Khái niệm Liên quan**[**#**](https://www.ultralytics.com/vi/glossary/concept-bottleneck-models#h%E1%BA%A1n-ch%E1%BA%BF-v%C3%A0-c%C3%A1c-kh%C3%A1i-ni%E1%BB%87m-li%C3%AAn-quan)

Nhãn khái niệm tạo ra các chi phí [data annotation](https://www.ultralytics.com/glossary/data-annotation) bổ sung và có thể yêu cầu kiến thức chuyên môn. Các khái niệm được định nghĩa kém có thể mang tính chủ quan, có tương quan, chưa đầy đủ hoặc khó nhận dạng từ đầu vào. Các nhóm nên thiết lập các quy tắc gán nhãn chính xác và kiểm toán sự bất đồng giữa những người gán nhãn.

Các rủi ro quan trọng khác bao gồm lỗi dự đoán khái niệm, điểm số chưa được hiệu chỉnh và **rò rỉ khái niệm (concept leakage)**, trong đó các giá trị khái niệm liên tục mã hóa thông tin ngoài ý muốn vượt ra ngoài ý nghĩa đã nêu của chúng. Hướng dẫn về [probability calibration](https://scikit-learn.org/stable/modules/calibration.html) có thể giúp xác định xem các giá trị độ tin cậy của khái niệm có đáng tin cậy hay không.

CBM cũng khác biệt so với kỹ thuật đặc trưng (feature engineering): các đặc trưng được thiết kế là đầu vào được tính toán thủ công, trong khi các khái niệm thường được dự đoán từ dữ liệu thô và được giám sát rõ ràng. Nó không giống với nguyên tắc nút thắt thông tin, vốn nén các biểu diễn mà không yêu cầu mọi chiều phải có thể đọc được đối với con người.

Hiệu suất của khái niệm nên được kiểm tra trên các lát dữ liệu liên quan vì các chú thích bị thiên lệch hoặc thiếu khái niệm có thể tạo ra các lỗi không đồng đều. [Google’s guidance for identifying ML bias](https://developers.google.com/machine-learning/crash-course/fairness/identifying-bias) và [NIST AI RMF Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/) cung cấp các thực tiễn đánh giá và quản trị hữu ích.
