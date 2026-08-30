# Model Parameter

**Model Parameter** là các giá trị của model được sinh ra từ dữ liệu huấn luyện giúp thể hiện mối liên hệ giữa các đại lượng trong dữ liệu

khi chúng ta nói **tìm được mô hình tốt nhất cho bài toán** thì nên ngầm hiểu rằng chúng ta đã tìm ra được các **Model parameter** phù hợp nhất cho bài toán trên tập dữ liệu hiện có. Nó có một số đặc điểm như sau:

- Nó được sử dụng để dự đoán đối với dữ liệu mới

- Nó thể hiện sức mạnh của mô hình chúng ta đang sử dụng. Thường được thể hiện bằng tỷ lệ **accuracy** hay chúng ta gọi là độ chính xác

- Được **học** trực tiếp từ tập dữ liệu huấn luyện

- Thường **không** được đặt thủ công bởi con người

**Model paramter** có thể bắt gặp trong một số dạng như là các trọng số trọng mạng nơ ron, các **support vectors** trong SVM hay các **coefficients** trong các giải thuật linear regression hoặc logistic regression...
