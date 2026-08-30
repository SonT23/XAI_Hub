# Model Hyperparameter

Nếu như **Model parameter** được mô hình sinh ra từ chính tập dữ liệu huấn luyện thì **Model Hyperparameter** lại hoàn toàn khác. Nó hoàn toàn **nằm ngoài** mô hình và không phụ thuộc và tập dữ liệu huấn luyện. Như vậy mục đích của nó là gì? Thực ra chúng có một vài nhiệm vụ như sau:

- Được sử dụng trong quá trình huấn luyện, giúp mô hình tìm ra được các **parameters** hợp lý nhất
- Nó thường được lựa chọn thủ công bởi những người tham gia trong việc huấn luyện mô hình
- Nó có thể được định nghĩa dựa trên một vài chiến lược **heuristics**

Một vài ví dụ về **Model Hyperparameter**:

- Chỉ số **learning rate** khi training một mạng nơ ron nhân tạo
- Tham số *C* và *sigma* khi training một **Support Vector Machine**
    - C
    - sigma
- Hệ số *k* trong mô hình **k Nearest Neighbor**
    - k
