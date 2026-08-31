# Cẩm nang PyTorch

> 🖼️ **9 ảnh gốc cho trang này (dán theo đúng thứ tự vào từng mục bên dưới):**
> 1355_bia-cam-nang-pytorch-tensor-va-mang-neural.jpg
>
> 1356_pytorch-tensor-va-cac-phep-toan-co-ban.jpg
>
> 1357_pytorch-data-pipeline-dataset-dataloader.jpg
>
> 1358_pytorch-xay-dung-model-voi-nn-module.jpg
>
> 1359_pytorch-training-loop-co-ban-loss-optimizer.jpg
>
> 1360_pytorch-mau-cnn-cho-computer-vision.jpg
>
> 1361_pytorch-transfer-learning-fine-tuning.jpg
>
> 1362_pytorch-training-luu-va-inference-tren-gpu.jpg
>
> 1363_pytorch-debugging-thuc-hanh-tot-nhat.jpg
>

Trang tổng hợp 9 ảnh cheat-sheet về **PyTorch** — từ tensor cơ bản đến training, transfer learning, inference trên GPU và debugging. Dùng làm tài liệu tra cứu nhanh khi triển khai các mô hình Deep Learning phục vụ NCKH về Explainable AI/CBM.

### 1. Trang bìa — Cẩm nang PyTorch

> 🖼️ Dán ảnh: `1355_bia-cam-nang-pytorch-tensor-va-mang-neural.jpg`

Trang bìa minh họa 3 trụ cột của cẩm nang: **code PyTorch cơ bản** (tạo tensor, áp dụng activation), **cấu trúc tensor 3D** (khối `torch.Tensor` với các chiều 3×4), và **mạng neural** kết nối tới biểu đồ **Loss giảm dần theo Epochs**. Đoạn code minh họa mở đầu:

```python
import torch
x = torch.randn(3, 4)
y = torch.nn.ReLU()
z = y(x)
z.shape  # (3, 4)
```

### 2. Tensor và các phép toán cơ bản

> 🖼️ Dán ảnh: `1356_pytorch-tensor-va-cac-phep-toan-co-ban.jpg`

**Tensor** là cấu trúc dữ liệu trung tâm của PyTorch — mảng đa chiều tương tự NumPy array nhưng hỗ trợ chạy trên GPU và autograd.

#### Tạo Tensor

```python
# Từ dữ liệu
x = torch.tensor([[1, 2, 3], [4, 5, 6]])

# Số 0 & số 1
z = torch.zeros((2, 3))
o = torch.ones((2, 3))

# Ngẫu nhiên
r = torch.randn(3, 4)

# Dải giá trị
a = torch.arange(0, 10)

# Ma trận đơn vị
I = torch.eye(3)
```

#### Kiểm tra thuộc tính

```python
x.shape       # vd (3, 4) — kích thước của từng chiều
x.dtype       # vd torch.float32 — kiểu dữ liệu của các phần tử
x.device      # vd cuda:0 hoặc cpu — thiết bị đang lưu tensor
x.ndim        # vd 2 — số chiều (rank)
x.size()      # vd torch.Size([3, 4]) — giống với shape
```

#### Reshape & các chiều

```python
x.view(-1, 1)             # reshape (dùng chung bộ nhớ)
x.reshape(2, 6)           # reshape (copy nếu cần)
x.unsquenese(0)           # thêm chiều tại vị trí 0
x.squeeze()               # bỏ các chiều có kích thước 1
x.permute(0, 2, 3, 1)     # sắp xếp lại chiều (không copy)
```

#### Các phép toán cơ bản

```python
x + y                     # cộng từng phần tử
x * y                     # nhân từng phần tử
torch.matmul(a, b)        # nhân ma trận
x.sum(dim=1)              # tổng theo chiều 1
x.mean()                  # trung bình tất cả phần tử
x.max(dim=1)              # giá trị lớn nhất & chỉ số
torch.cat([a, b], dim=0)  # nối các tensor
```

#### Tổng quan các chiều của Tensor

- **Scalar** — Rank 0, Shape: `[]` (vd: `7`)

- **Vector** — Rank 1, Shape: `[4]` (vd: `[1, 2, 3, 4]`)

- **Matrix** — Rank 2, Shape: `[3, 3]`

- **3D Tensor** — Rank 3, Shape: `[D, H, W]` (Sâu, Cao, Rộng)

> 💡 **Mẹo hay:**
> ✔ **Broadcasting** — PyTorch tự động broadcast các shape tương thích trong phép toán element-wise. (vd: [3, 1] + [1, 4] → [3, 4])
>
> ✔ **In-place Ops** — Dùng add_(), mul_(), v.v. để tiết kiệm bộ nhớ. Cẩn thận vì chúng làm thay đổi tensor gốc.
>
> ✔ **Giữ shape nhất quán** — Luôn kiểm tra shape của tensor khi xây dựng model để tránh lỗi ngầm.
>

### 3. Data Pipeline: Dataset & DataLoader

> 🖼️ Dán ảnh: `1357_pytorch-data-pipeline-dataset-dataloader.jpg`

Quy trình xử lý dữ liệu: **Raw data → Custom Dataset → Transform → DataLoader → Mini-batches → Model** (nạp, biến đổi và chia batch dữ liệu hiệu quả để training).

#### 1. Custom Dataset

```python
from torch.utils.data import Dataset

class MyDataset(Dataset):
    def __init__(self, data, labels, transform=None):
        self.data = data
        self.labels = labels
        self.transform = transform

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, idx):
        x = self.data[idx]
        y = self.labels[idx]
        if self.transform:
            x = self.transform(x)
        return x, y
```

#### 2. Tạo DataLoader

```python
from torch.utils.data import DataLoader

train_loader = DataLoader(
    train_ds,
    batch_size=32,
    shuffle=True,
    num_workers=4,
    pin_memory=True
)
```

#### 3. Các tham số chính

- **batch_size** — Số lượng mẫu trong mỗi mini-batch.

- **shuffle** — Xáo trộn dữ liệu mỗi epoch (True/False).

- **num_workers** — Số subprocess dùng để load dữ liệu.

- **pin_memory** — Truyền dữ liệu host → GPU nhanh hơn (dùng với CUDA).

- **drop_last** — Bỏ batch cuối nếu không đủ (True/False).

#### 4. Các transform hữu ích

- `Resize((224, 224))` — Resize ảnh

- `ToTensor()` — Chuyển thành tensor [C, H, W] trong [0, 1]

- `Normalize(mean, std)` — Chuẩn hóa theo mean & std

- `RandomHorizontalFlip(p=0.5)` — Lật ảnh với xác suất p

#### 5. Truy cập trong training loop

```python
for x_batch, y_batch in train_loader:
    # x_batch: [B, C, H, W] hoặc [B, D]
    # y_batch: [B] hoặc [B, ...]
    ...
```

> ⭐ **6. Thực hành tốt nhất:**
> ✔ **Chuẩn hóa đầu vào** — Giúp training nhanh hơn và ổn định hơn.
>
> ✔ **Giữ tiền xử lý trên CPU hiệu quả** — Dùng các phép toán vector hóa và transform hiệu quả.
>
> ✔ **Dùng num_workers hợp lý** — Bắt đầu với giá trị nhỏ (2-4) rồi tinh chỉnh theo hệ thống.
>
> ✔ **Tránh làm nghẽn GPU** — Đảm bảo DataLoader luôn cung cấp đủ dữ liệu cho GPU.
>

### 4. Xây dựng model với nn.Module

> 🖼️ Dán ảnh: `1358_pytorch-xay-dung-model-voi-nn-module.jpg`

Luồng dữ liệu qua model ví dụ: **Input (N,784) → Linear(784,128) → ReLU → Dropout(p=0.5) → Linear(128,10) → Output (N,10)**.

#### Tùy chỉnh nn.Module

```python
import torch
import torch.nn as nn

class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(784, 128)
        self.relu = nn.ReLU()
        self.drop = nn.Dropout(p=0.5)
        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.drop(x)
        x = self.fc2(x)
        return x
```

#### nn.Sequential (cách viết nhanh hơn)

```python
model = nn.Sequential(
    nn.Linear(784, 128),
    nn.ReLU(),
    nn.Dropout(p=0.5),
    nn.Linear(128, 10)
)
```

> ℹ️ `forward(self, x)`** dùng để làm gì?** Nó định nghĩa phép tính được thực hiện trên đầu vào x và trả về kết quả. PyTorch tự động gọi hàm này khi bạn chạy `model(x)`.

#### Các layer thông dụng

- **Linear** — `nn.Linear(in,out)` — Layer kết nối đầy đủ.

- **Conv2d** — `nn.Conv2d(in,out,kernel_size,...)` — Tích chập 2D.

- **ReLU** — `nn.ReLU()` — Hàm kích hoạt phi tuyến.

- **BatchNorm2d** — `nn.BatchNorm2d(C)` — Chuẩn hóa channel, giúp training ổn định.

- **Dropout** — `nn.Dropout(p)` — Ngẫu nhiên triệt tiêu activation.

- **MaxPool2d** — `nn.MaxPool2d(k)` — Giảm kích thước bằng cách lấy max.

- **Flatten** — `nn.Flatten()` — Làm phẳng thành 2D (N, -1).

- **Embedding** — `nn.Embedding(n,d)` — Ánh xạ index thành vector dense.

- **LSTM** — `nn.LSTM(in,hid)` — Model chuỗi (recurrent).

#### Tiện ích của model

- `model.parameters()` — Iterable chứa các parameter.

- `model.train()` — Bật chế độ training (bật dropout, BN).

- `model.eval()` — Bật chế độ eval (tắt dropout, BN).

- `print(model)` — In ra tóm tắt kiến trúc.

- **Summary** — Dùng `torchinfo.summary(model, input_size=(1, 784))` để xem chi tiết từng layer.

### 5. Training loop cơ bản: Loss & Optimizer

> 🖼️ Dán ảnh: `1359_pytorch-training-loop-co-ban-loss-optimizer.jpg`

Các thành phần cốt lõi của một vòng lặp training: **1. Batch → 2. Forward Pass → 3. Loss → 4. Zero Grad → 5. Backward → 6. Step → 7. Batch tiếp theo (lặp lại)**.

#### Training loop (ví dụ đầy đủ)

```python
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model.to(device)
criterion = torch.nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)

for epoch in range(num_epochs):
    model.train()                  # Bật chế độ train
    running_loss, running_correct = 0.0, 0
    total = 0
    for x, y in train_loader:
        x, y = x.to(device), y.to(device)
        optimizer.zero_grad()             # Xóa gradient
        outputs = model(x)                # Forward pass
        loss = criterion(outputs, y)      # Tính loss
        loss.backward()                   # Backward pass
        optimizer.step()                  # Cập nhật params
        running_loss += loss.item() * x.size(0)
        _, preds = outputs.max(1)
        running_correct += (preds == y).sum().item()
        total += y.size(0)

    epoch_loss = running_loss / total
    epoch_acc = running_correct / total
    print(f"Epoch {epoch+1}: loss={epoch_loss:.4f}, acc={epoch_acc:.4f}")
```

#### Validation loop

```python
model.eval()                       # Bật chế độ eval
val_loss, val_correct, total = 0.0, 0, 0
with torch.no_grad():
    for x, y in val_loader:
        x, y = x.to(device), y.to(device)
        outputs = model(x)
        loss = criterion(outputs, y)
        val_loss += loss.item() * x.size(0)
        _, preds = outputs.max(1)
        val_correct += (preds == y).sum().item()
        total += y.size(0)

val_loss /= total
val_acc = val_correct / total
model.train()  # Quay lại chế độ train
```

> ⭐ **Cần nhớ:**
> ✔ Zero gradient mỗi batch: `optimizer.zero_grad()`
>
> ✔ Chuyển dữ liệu & model sang device để tăng tốc
>
> ✔ Dùng `model.train()` khi training, `model.eval()` khi eval
>
> ✔ Dùng `torch.no_grad()` khi validation/test
>
> ✔ Theo dõi metric (loss, accuracy, v.v.) và log
>

#### Các hàm loss thông dụng

| Loss | Dùng khi | Input (Pred) | Target | Ghi chú |
| --- | --- | --- | --- | --- |
| CrossEntropyLoss | Phân loại đa lớp | Raw logits [N, C] | Class idx [N] | Đã gồm LogSoftmax |
| BCEWithLogitsLoss | Nhị phân / multi-label | Raw logits [N,1]/[N,C] | Nhãn 0/1 cùng shape | Đã gồm Sigmoid |
| MSELoss | Regression (liên tục) | Predictions [N, *] | Targets [N, *] | Mean Squared Error |

#### Các optimizer thông dụng

| Optimizer | Phù hợp với | Tham số chính | Ghi chú |
| --- | --- | --- | --- |
| SGD | Đa dụng, dataset lớn | lr=0.01, momentum=0.9, weight_decay=1e-4 | Đơn giản, nhanh |
| Adam | Đa số bài toán, hội tụ nhanh | lr=1e-3, betas=(0.9,0.999), weight_decay=0 | Học thích ứng |
| AdamW | Transformer / model sâu | lr=1e-3, betas=(0.9,0.999), weight_decay=1e-2 | Weight decay tách biệt |

### 6. Mẫu CNN cho Computer Vision

> 🖼️ Dán ảnh: `1360_pytorch-mau-cnn-cho-computer-vision.jpg`

Kiến trúc CNN mẫu: **Image (224×224×3) → Conv2d(3,32,3) → ReLU → MaxPool(2×2) → Conv2d(32,64,3) → ReLU → MaxPool(2×2) → Flatten → Linear(64*****56*****56, N) → Output (N classes)**.

```python
import torch.nn as nn

class SimpleCNN(nn.Module):
    def __init__(self, num_classes=10):
        super().__init__()
        self.features = nn.Sequential(
            nn.Conv2d(3, 32, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(2, 2),
            nn.Conv2d(32, 64, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(2, 2),
        )
        self.classifier = nn.Sequential(
            nn.Flatten(),
            nn.Linear(64 * 56 * 56, 128),
            nn.ReLU(inplace=True),
            nn.Linear(128, num_classes)
        )
    def forward(self, x):
        x = self.features(x)
        x = self.classifier(x)
        return x
```

#### Ghi chú về input shape

Input cho vision trong PyTorch có dạng: `[batch, channels, height, width]`. Ví dụ: `[32, 3, 224, 224]`.

#### Các layer chính

- **nn.Conv2d** — Học đặc trưng không gian bằng tích chập 2D.

- **nn.MaxPool2d** — Giảm kích thước không gian (thường 2×2).

- **nn.AdaptiveAvgPool2d** — Cho kích thước cố định (vd 1×1) dù input là gì.

- **nn.Flatten** — Chuyển feature map thành vector 1D cho fully connected.

#### Mẹo thực tế

- Chuẩn hóa ảnh (mean/std) để training nhanh và ổn định hơn.

- Bắt đầu nhỏ: có baseline để lặp nhanh.

- Dùng data augmentation để cải thiện khả năng tổng quát hóa.

- Theo dõi overfitting: so sánh metric giữa train và val.

#### Các augmentation thường dùng

- Random Horizontal Flip

- Random Crop

- Normalize

### 7. Transfer Learning & Fine-Tuning

> 🖼️ Dán ảnh: `1361_pytorch-transfer-learning-fine-tuning.jpg`

Tận dụng các pretrained model và điều chỉnh cho bài toán của bạn chỉ với lượng dữ liệu và compute tối thiểu. Quy trình 5 bước: **1. Load pretrained backbone → 2. Freeze các layer gốc → 3. Thay classifier head → 4. Train head → 5. Unfreeze layer cuối → Fine-tune**.

#### 1) Load pretrained backbone, thay head & freeze base

```python
import torch
import torch.nn as nn
from torchvision import models

num_classes = 10
model = models.resnet18(weights=models.ResNet18_Weights.DEFAULT)

in_features = model.fc.in_features
model.fc = nn.Linear(in_features, num_classes)   # classifier head mới

# Freeze tất cả layer trừ head mới
for name, param in model.named_parameters():
    if not name.startswith("fc."):
        param.requires_grad = False
    else:
        param.requires_grad = True
```

#### 2) Train head → sau đó fine-tune các layer sâu hơn

```python
# --- Giai đoạn 1: chỉ train head ---
optimizer = torch.optim.AdamW(model.fc.parameters(), lr=1e-3, weight_decay=1e-4)
criterion = nn.CrossEntropyLoss()

# training loop cho head-only (không hiển thị)
# ... chạy trong vài epoch ...

# --- Giai đoạn 2: unfreeze layer cuối & fine-tune ---
for name, param in model.named_parameters():
    if any(k in name for k in ["layer4.", "layer3."]):
        param.requires_grad = True

optimizer = torch.optim.AdamW(filter(lambda p: p.requires_grad,
        model.parameters()), lr=1e-4, weight_decay=1e-4)
# tiếp tục training với learning rate thấp hơn
```

#### Khi nào nên dùng

- **Dataset nhỏ** — Tổng quát hóa tốt hơn dù ít dữ liệu.

- **Compute hạn chế** — Training nhanh hơn, tốn ít tài nguyên hơn.

- **Hội tụ nhanh hơn** — Bắt đầu từ đặc trưng mạnh, có thể transfer.

#### Mẹo quan trọng

- **Dùng learning rate thấp hơn** — Fine-tuning cần LR nhỏ hơn (vd: 1e-4).

- **Áp dụng data augmentation** — Giúp tổng quát hóa tốt hơn trên dataset nhỏ.

- **Theo dõi validation accuracy** — Dừng khi metric validation không cải thiện thêm.

- **Lưu model tốt nhất** — Checkpoint tại điểm validation tốt nhất.

#### Các pretrained backbone phổ biến

- **ResNet (resnet18/34/50/101)** — Baseline mạnh cho hầu hết bài toán; biểu diễn đặc trưng tốt; có sẵn trong `torchvision.models`.

- **EfficientNet (b0–b7)** — Độ chính xác cao với ít tham số hơn; compound scaling giúp hiệu quả hơn; cân bằng tốt giữa accuracy và chi phí.

- **MobileNetV3 (small/large)** — Nhẹ & thân thiện với mobile; inference nhanh; lý tưởng để triển khai trên edge.

### 8. Training, lưu và inference trên GPU

> 🖼️ Dán ảnh: `1362_pytorch-training-luu-va-inference-tren-gpu.jpg`

Quy trình 6 bước: **1. Thiết lập Device → 2. Chuyển sang GPU → 3. Mixed Precision (tùy chọn) → 4. Lưu → 5. Nạp → 6. Inference**.

#### 1) Thiết lập device & chuyển sang GPU

```python
import torch

device = torch.device('cuda' if torch.cuda.is_available()
                       else 'mps' if torch.backends.mps.is_available()
                       else 'cpu')

model = MyModel()
model.to(device)

x = x.to(device)   # chuyển dữ liệu sang device
```

> ℹ️ Lưu ý khi training: Chuyển cả model và tensor sang cùng một device trước khi forward/backward.

#### 2) Lưu model (state_dict)

```python
import torch

torch.save(model.state_dict(), 'model.pt')
```

#### 3) Nạp model (state_dict)

```python
import torch
model = MyModel()
model.load_state_dict(torch.load('model.pt',
                       map_location=device))
model.to(device)
```

#### 4) Inference

```python
model.eval()                    # chuyển sang eval mode
with torch.no_grad():          # tắt gradient tracking
    preds = model(x)
```

#### 5) Mixed Precision (tùy chọn)

```python
scaler = torch.cuda.amp.GradScaler()

for x, y in loader:
    optimizer.zero_grad(set_to_none=True)
    with torch.cuda.amp.autocast():
        out = model(x)
        loss = criterion(out, y)

    scaler.scale(loss).backward()
    scaler.step(optimizer)
    scaler.update()
```

> ✨ **Ghi nhớ:**
> ✔ Lưu state_dict, không lưu cả model.
>
> ✔ Chuyển sang model.eval() khi inference.
>
> ✔ Dùng [torch.no](http://torch.no/)_grad() để tiết kiệm bộ nhớ và tăng tốc.
>
> ✔ Dùng map_location='cpu' khi load trên máy chỉ có CPU.
>

#### Các loại device

- **CUDA** (NVIDIA GPUs) — `torch.device('cuda')`, `torch.cuda.is_available()`

- **MPS** (Apple Silicon, macOS) — `torch.device('mps')`, `torch.backends.mps.is_available()`

- **CPU** (Dự phòng / Đa dụng) — `torch.device('cpu')`

### 9. Debugging & thực hành tốt nhất

> 🖼️ Dán ảnh: `1363_pytorch-debugging-thuc-hanh-tot-nhat.jpg`

#### Các lỗi thường gặp

- ☐ **Quên model.train()/eval()** — Set model.train() khi training, model.eval() khi validation/test.

- ☐ **Lỗi lệch shape (mismatch)** — Kiểm tra kỹ shape của tensor, dùng .shape hoặc .size()

- ☐ **Quên **[**optimizer.zero**](http://optimizer.zero/)**_grad()** — Gradient mặc định sẽ cộng dồn. Phải zero chúng mỗi step.

- ☐ **Lệch device (CPU và GPU)** — Đảm bảo model và tensor cùng nằm trên một device.

- ☐ **Thiếu **[**torch.no**](http://torch.no/)**_grad() khi inference** — Dùng [torch.no](http://torch.no/)_grad() để tiết kiệm bộ nhớ và tăng tốc.

#### Khả năng tái lập

```python
import torch, random, numpy as np
seed = 42
torch.manual_seed(seed)
torch.cuda.manual_seed_all(seed)
np.random.seed(seed)
random.seed(seed)

torch.backends.cudnn.deterministic = True
torch.backends.cudnn.benchmark = False
```

> 💡 Đảm bảo thí nghiệm cho kết quả giống nhau qua các lần chạy (đánh đổi một chút hiệu năng).

#### Mẹo về hiệu năng

- Dùng batch size lớn hơn nếu bộ nhớ cho phép.

- Set pin_memory=True trong DataLoader.

- Tinh chỉnh num_workers theo số nhân CPU.

- Dùng mixed precision (torch.cuda.amp) để tăng tốc & tiết kiệm bộ nhớ.

- Profile các điểm nghẽn bằng torch.profiler.

#### Ổn định khi training

- Clip gradient để tránh exploding gradient.

- Dùng learning-rate scheduler (StepLR, CosineAnnealingLR).

- Áp dụng early stopping để tránh overfitting.

- Theo dõi validation loss (không chỉ accuracy).

#### Các tiện ích hữu dụng

- `torch.nn.utils.clip_grad_norm_` — Clip gradient

- `torch.optim.lr_scheduler.StepLR` — Lên lịch learning rate

- `tqdm.auto.tqdm` — Thanh tiến trình

- `torch.utils.tensorboard.SummaryWriter` — Ghi log với TensorBoard

#### Vấn đề → cách khắc phục

| Vấn đề | Cách khắc phục |
| --- | --- |
| NaN loss | Giảm LR, kiểm tra normalization / gradient |
| Overfitting | Thêm dropout, augmentation, early stopping |
| Training chậm | Tăng batch size, bật AMP, tinh chỉnh DataLoader |
| Độ chính xác thấp | Kiểm tra nhãn, preprocessing, cân bằng dữ liệu |

> 🎯 Nắm vững training loop, phần còn lại sẽ dễ dàng hơn nhiều.
