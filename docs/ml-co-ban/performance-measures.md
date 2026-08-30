# Performance Measures

### **Đối với bài toán classification**

Đối với dạng bài toán phân lớp chúng ta có thể sử dụng một số phương pháp để đo độ chính xác của mô hình học máy như sau:

#### **Precision - bao nhiêu cái đúng được lấy ra**

Xem xét trên tập dữ liệu kiểm tra xem có bao nhiêu dữ liệu được mô hình dự đoán đúng. Đây chính là chỉ số **accuracy - độ chính xác**. 

Tuy nhiên để cho khách quan hơn người ta cần phải xem xét thêm một yếu tố nữa chính là **Recall**

#### **Recall - bao nhiêu cái được lấy ra là đúng**

Chỉ số này còn được gọi là **độ bao phủ** tức là xem xét xem mô hình tìm được có khả năng **tổng quát hóa** như thế nào. Từ hai yếu tố **độ chính xác** và **độ bao phủ** phía trên người ta đưa ra một chỉ số khác gọi là **F1-Score**

#### **F1-Score**

Đây được gọi là một **trung bình điều hòa**(harmonic mean) của các tiêu chí Precision và Recall. Nó có xu hướng lấy giá trị gần với giá trị nào nhỏ hơn giữa 2 giá trị **Precision** và **Recall** và đồng thời nó có giá trị lớn nếu cả 2 giá trị **Precision** và **Recall** đều lớn. Chính vì thế **F1-Score** thể hiện được một cách khách quan hơn **performance** của một mô hình học máy.

### **Đối với bài toán Regression**

bài toán **regression - hồi quy** tức là biến y*y* của chúng ta không phải là một giá trị rời rạc mà là một giá trị **liên tục**. Nó thường là số lượng, giá tiền, nhiệt độ, lượng mưa ... Do nó là giá trị liên tục nên chúng ta hoàn toàn không thể sử dụng **độ chính xác** để đo **performance** của mô hình được mà cần phải dùng một số loại độ đo khác. Dưới đây mình xin trình bày một vài độ đo cơ bản trong số đó.

#### **Mean Absolute Error - MAE**

**MAE** là một phương pháp đo lường sự khác biệt giữa hai biến liên tục. Giả sử rằng *X* và *Y* là hai biến liên tục thể hiện kết quả dự đoán của mô hình và kết quả thực tế. chúng ta có độ đo **MAE** được tính theo công thức sau:

![](https://wikimedia.org/api/rest_v1/media/math/render/svg/3ef87b78a9af65e308cf4aa9acf6f203efbdeded)

Chúng ta có thể cài đặt một đoạn code đơn giản bằng Python sử dụng thư viện Sklearn để tính toán độ đo này như sau:

```python
from sklearn.metrics import mean_absolute_error
expected = [0.0, 0.5, 0.0, 0.5, 0.0]
predictions = [0.2, 0.4, 0.1, 0.6, 0.2]
mae = mean_absolute_error(expected, predictions)
print('MAE: %f' % mae)

>>>  MAE: 0.140000
```

Độ đo này thường được sử dụng để đánh giá sự sai khác giữa mô hình dự đoán và tập dữ liệu testing trong các bài toán hồi quy. Chỉ số này càng nhỏ thì mô hình học máy càng chính xác.

#### **Mean squared error - MSE**

**MSE** của một phép ước lượng là trung bình của **bình phương của sai số**, tức là sự khác biệt giữa các giá trị được mô hình dự đoán và gía trị thực. MSE là một **hàm rủi ro**, tương ứng với giá trị kỳ vọng của sự mất mát sai số bình phương hoặc mất mát bậc hai. **MSE** là **moment bậc hai** (về nguồn gốc) của sai số là moment bậc hai (về nguồn gốc) của sai số

![](https://wikimedia.org/api/rest_v1/media/math/render/svg/c1abbbe5e9a537dceaf5cbb197fa3cbf387dcf77)

#### Root Mean Squared Error - RMSE

**RMSE** là căn bậc hai của **MSE**, giúp đưa đơn vị của sai số về lại đúng đơn vị của biến mục tiêu ban đầu (vì MSE đã bình phương lên nên đơn vị bị "bình phương" theo). Nhờ vậy RMSE dễ diễn giải hơn MSE trong thực tế.

```python
from sklearn.metrics import mean_squared_error
rmse = mean_squared_error(expected, predictions, squared=False)
```

#### R² (Hệ số xác định - Coefficient of Determination)

**R²** đo lường tỷ lệ phương sai của biến mục tiêu có thể được giải thích bởi mô hình, nhận giá trị tối đa là 1 (mô hình dự đoán hoàn hảo). R² có thể âm nếu mô hình dự đoán tệ hơn cả việc chỉ lấy trung bình cộng của dữ liệu thực tế.

### Bổ sung cho bài toán Classification

#### Confusion Matrix (Ma trận nhầm lẫn)

Là bảng thống kê chi tiết kết quả dự đoán so với thực tế, gồm 4 thành phần:

- **True Positive (TP):** Dự đoán đúng là lớp dương.

- **True Negative (TN):** Dự đoán đúng là lớp âm.

- **False Positive (FP):** Dự đoán sai thành lớp dương (còn gọi là lỗi loại I).

- **False Negative (FN):** Dự đoán sai thành lớp âm (còn gọi là lỗi loại II).

Từ đây suy ra công thức: Precision = TP / (TP + FP), Recall = TP / (TP + FN).

#### ROC-AUC

**ROC Curve** biểu diễn mối quan hệ giữa True Positive Rate và False Positive Rate khi thay đổi ngưỡng phân loại (threshold). **AUC (Area Under Curve)** là diện tích dưới đường cong này — AUC càng gần 1 thì mô hình phân loại càng tốt, AUC = 0.5 tương đương với việc đoán ngẫu nhiên.
