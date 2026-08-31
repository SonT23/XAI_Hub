# Cheat Sheet CNN (Stanford CS230)

> 🖼️ **4 ảnh gốc cho trang này (dán theo đúng thứ tự vào từng mục bên dưới):**
> 1364_cheatsheet-cnn-stanford-cs230-kien-truc-conv-pooli.jpg
>
> 1365_cheatsheet-cnn-pooling-padding-sieu-tham-so-bo-loc.jpg
>
> 1366_cheatsheet-cnn-receptive-field-relu-softmax.jpg
>
> 1367_cheatsheet-cnn-object-detection-iou-yolo-anchor-bo.jpg
>

Nguồn: Afshine Amidi & Shervine Amidi, *Super VIP Cheatsheet: Deep Learning*, Stanford CS230 (bản dịch tiếng Việt). Trang này tổng hợp lại 4 ảnh chụp phần **Mạng nơ-ron tích chập (CNN)**.

### 1. Kiến trúc CNN, các kiểu tầng (Conv, Pooling)

> 🖼️ Dán ảnh: `1364_cheatsheet-cnn-stanford-cs230-kien-truc-conv-pooli.jpg`

**Kiến trúc truyền thống của một mạng CNN** gồm chuỗi các tầng: Ảnh đầu vào → Tích chập (Conv) → Pooling → Kết nối đầy đủ (Fully Connected). Các tầng Conv và Pooling được điều chỉnh bằng các **siêu tham số (hyperparameters)**.

- **Tầng tích chập (CONV)**: dùng các bộ lọc (filter) trượt qua đầu vào $I$ để thực hiện phép tích chập theo mọi chiều. Siêu tham số của bộ lọc gồm kích thước bộ lọc $F$ và độ trượt (stride) $S$. Kết quả đầu ra $O$ gọi là feature map (hay activation map).

- **Pooling (POOL)**: là phép downsampling, thường dùng sau tầng tích chập để tăng tính bất biến không gian (spatial invariance). Có hai loại phổ biến:
    - **Max pooling**: lấy giá trị lớn nhất trong khu vực áp dụng — bảo toàn các đặc trưng đã phát hiện, được dùng thường xuyên.

    - **Average pooling**: lấy giá trị trung bình trong khu vực áp dụng — giúp giảm kích thước feature map, được dùng trong mạng LeNet.

> 💡 Lưu ý: phép tích chập có thể được khái quát hóa cả với trường hợp một chiều (1D) và ba chiều (3D), không chỉ 2D như ảnh minh họa.

- **Fully Connected (FC)**: tầng kết nối đầy đủ nhận đầu vào là dữ liệu đã được làm phẳng (flatten), mỗi phần tử đầu vào được nối với **mọi** neuron của tầng. Thường nằm ở cuối mạng CNN, dùng để tối ưu hóa mục tiêu của mạng (ví dụ độ chính xác phân loại).

### 2. Pooling, Padding, siêu tham số bộ lọc

> 🖼️ Dán ảnh: `1365_cheatsheet-cnn-pooling-padding-sieu-tham-so-bo-loc.jpg`

#### Stride và Zero-padding

- **Stride** $S$: đối với phép tích chập hoặc pooling, $S$ là số pixel mà cửa sổ (bộ lọc) di chuyển sau mỗi lần thực hiện phép tính.

- **Zero-padding**: quá trình thêm $P$ số 0 vào các biên của đầu vào. Có ba kiểu padding chính:

|   | Valid | Same | Full |
| --- | --- | --- | --- |
| **Giá trị** | $P=0$ | $P_{start}=\left\lfloor \dfrac{S\lceil I/S\rceil - I + F - S}{2} \right\rfloor$, $P_{end}=\left\lceil \dfrac{S\lceil I/S\rceil - I + F - S}{2} \right\rceil$ | $P_{start}\in[0,F-1]$, $P_{end}=F-1$ |
| **Mục đích** | Không dùng padding; bỏ phép tích chập cuối nếu số chiều không khớp | Làm feature map có kích thước $\lceil I/S\rceil$; thuận lợi về mặt toán học; còn gọi là 'half' padding | Padding tối đa để phép tích chập dùng được cả ở rìa đầu vào; bộ lọc 'thấy' được đầu vào từ đầu đến cuối |

> 💡 Trong nhiều trường hợp $P_{start}=P_{end}\triangleq P$, khi đó có thể thay $P_{start}+P_{end}$ bằng $2P$ trong các công thức.

#### Các chiều của một bộ lọc

Một bộ lọc kích thước $F\times F$ áp dụng lên đầu vào có $C$ kênh (channels) thì có kích thước tổng thể là $F\times F\times C$, thực hiện tích chập trên đầu vào kích thước $I\times I\times C$ và cho ra một feature map kích thước $O\times O\times 1$.

- Áp dụng $K$ bộ lọc kích thước $F\times F$ sẽ cho ra một feature map kích thước $O\times O\times K$.

#### Tính tương thích của tham số trong tầng tích chập

Gọi $I$ là độ dài kích thước đầu vào, $F$ là độ dài bộ lọc, $P$ là số lượng zero-padding, $S$ là stride, độ dài $O$ của feature map theo một chiều được tính:

$$O = \dfrac{I - F + P_{start} + P_{end}}{S} + 1$$

#### Độ phức tạp của mô hình (số tham số theo từng tầng)

|   | CONV | POOL | FC |
| --- | --- | --- | --- |
| **Kích thước đầu vào** | $I\times I\times C$ | $I\times I\times C$ | $N_{in}$ |
| **Kích thước đầu ra** | $O\times O\times K$ | $O\times O\times C$ | $N_{out}$ |
| **Số lượng tham số** | $(F\times F\times C+1)\cdot K$ | $0$ | $(N_{in}+1)\times N_{out}$ |
| **Lưu ý** | Một tham số bias cho mỗi bộ lọc; thường $S<F$; lựa chọn phổ biến cho $K$ là $2C$ | Pooling áp dụng theo từng kênh (channel-wise); thường $S=F$ | Đầu vào được làm phẳng; mỗi neuron có một tham số bias; số neuron phụ thuộc ràng buộc kiến trúc |

### 3. Trường thụ cảm (Receptive Field), ReLU, Softmax

> 🖼️ Dán ảnh: `1366_cheatsheet-cnn-receptive-field-relu-softmax.jpg`

#### Trường thụ cảm (Receptive field)

Trường thụ cảm tại tầng $k$ là vùng kích thước $R_k\times R_k$ của đầu vào mà các pixel của activation map thứ $k$ có thể "nhìn thấy". Gọi $F_j$ là kích thước bộ lọc của tầng $j$, $S_i$ là stride của tầng $i$ (quy ước $S_0=1$):

$$R_k = 1 + \sum_{j=1}^{k}(F_j-1)\prod_{i=0}^{j-1}S_i$$

Ví dụ: nếu $F_1=F_2=3$ và $S_1=S_2=1$ thì $R_2 = 1+2\cdot1+2\cdot1 = 5$.

#### Các hàm kích hoạt thường gặp

Mục đích của hàm kích hoạt $g$ là tăng tính phi tuyến cho mạng.

| ReLU | Leaky ReLU | ELU |
| --- | --- | --- |
| $g(z)=\max(0,z)$ | $g(z)=\max(\epsilon z,z)$ với $\epsilon\ll1$ | $g(z)=\max(\alpha(e^{z}-1),z)$ với $\alpha\ll1$ |
| Độ phức tạp phi tuyến tính có thể thông dịch được về mặt sinh học | Giải quyết vấn đề ReLU "chết" đối với các giá trị âm | Khả vi tại mọi nơi |

#### Softmax

Softmax là hàm logistic tổng quát, nhận đầu vào là một vector $x\in\mathbb{R}^n$ và trả về một vector xác suất $p\in\mathbb{R}^n$:

$$p=\begin{pmatrix}p_1\\ \vdots \\ p_n\end{pmatrix} \quad \text{với} \quad p_i=\dfrac{e^{x_i}}{\displaystyle\sum_{j=1}^{n}e^{x_j}}$$

### 4. Phát hiện vật thể (Object Detection): IoU, YOLO, Anchor Box

> 🖼️ Dán ảnh: `1367_cheatsheet-cnn-object-detection-iou-yolo-anchor-bo.jpg`

#### Các kiểu mô hình

Có 3 kiểu thuật toán nhận diện vật thể chính:

| Phân loại hình ảnh | Phân loại cùng khoanh vùng | Phát hiện |
| --- | --- | --- |
| Phân loại một tấm ảnh; dự đoán xác suất của một vật thể | Phát hiện một vật thể trong ảnh; dự đoán xác suất và định vị nó | Phát hiện nhiều vật thể trong cùng một tấm ảnh; dự đoán xác suất và định vị chúng |
| CNN cổ điển | YOLO đơn giản hóa, R-CNN | YOLO, R-CNN |

Hai phương pháp phát hiện chính:

| Phát hiện hộp giới hạn (bounding box) | Phát hiện landmark |
| --- | --- |
| Phát hiện phần trong ảnh có sự xuất hiện của vật thể. Hộp có tọa độ tâm $(b_x,b_y)$, chiều cao $b_h$ và chiều rộng $b_w$ | Phát hiện hình dạng/đặc điểm của đối tượng (vd: mắt), gồm nhiều điểm tương quan $(l_{1x},l_{1y}),\dots,(l_{nx},l_{ny})$ |

#### Intersection over Union (IoU)

IoU định lượng vị trí của hộp dự đoán $B_p$ so với hộp thực tế $B_a$:

$$IoU(B_p,B_a) = \dfrac{B_p\cap B_a}{B_p\cup B_a}$$

> 💡 Luôn có $IoU\in[0,1]$. Quy ước: hộp $B_p$ được coi là khá tốt nếu $IoU(B_p,B_a)\geq 0.5$.

#### Anchor boxes

Kỹ thuật dự đoán nhiều hộp giới hạn chồng lên nhau cùng lúc, mỗi dự đoán bị giới hạn theo một tập tính chất hình học (hình dạng hộp) cho trước — dự đoán đầu tiên có hình dạng khác dự đoán thứ hai, v.v.

#### Non-max suppression

Mục tiêu: loại bỏ các hộp giới hạn trùng lặp của cùng một đối tượng, chỉ giữ hộp đặc trưng nhất. Sau khi loại bỏ mọi hộp có xác suất dự đoán < 0.6, lặp lại:

- **Bước 1**: Chọn hộp có xác suất dự đoán lớn nhất.

- **Bước 2**: Loại bỏ những hộp có $IoU\geq0.5$ với hộp đã chọn.

#### YOLO (You Only Look Once)

Các bước thực hiện:

- **Bước 1**: Phân chia ảnh đầu vào thành lưới $G\times G$.

- **Bước 2**: Với mỗi ô lưới, chạy một mạng CNN dự đoán $y$ có dạng:

$$y=\big[p_c,\,b_x,\,b_y,\,b_h,\,b_w,\,\underbrace{c_1,c_2,\dots,c_p,\dots}_{\text{lặp lại }k\text{ lần}}\big]^{T}\in\mathbb{R}^{G\times G\times k\times(5+p)}$$

trong đó $p_c$ là xác suất dự đoán được một vật thể, $b_x,b_y,b_h,b_w$ là các thuộc tính của hộp giới hạn được dự đoán, $c_1,\dots,c_p$ là biểu diễn one-hot của lớp nào trong $p$ lớp được dự đoán, và $k$ là số lượng anchor box.

- **Bước 3**: Chạy thuật toán non-max suppression để loại bỏ các hộp giới hạn có khả năng bị trùng lặp.
