# Docker cơ bản: Khái niệm, kiến trúc & cài đặt

> 🖼️ **7 ảnh gốc cho trang này (dán theo đúng thứ tự vào từng mục bên dưới):**
> 1388_ghi-chu-docker-la-gi-vi-sao-nen-dung-docker.jpg
>
> 1389_so-sanh-docker-containers-va-virtual-machines.jpg
>
> 1390_kien-truc-docker-client-daemon-registry.jpg
>
> 1391_ghi-chu-docker-images-va-containers-so-do-minh-hoa.jpg
>
> 1392_huong-dan-cai-dat-docker-tren-windows-mac-linux.jpg
>
> 1393_huong-dan-tao-container-docker-dau-tien-hello-worl.jpg
>
> 1394_danh-sach-cac-lenh-docker-can-thiet-co-ban.jpg
>

### 1. Docker là gì? Vì sao nên dùng Docker

> 🖼️ Dán ảnh: `1388_ghi-chu-docker-la-gi-vi-sao-nen-dung-docker.jpg`

**Docker là gì?**

- Docker là một nền tảng (**platform**) giúp bạn **build, package và run** các ứng dụng bên trong **containers**.

- Một **container** giống như một chiếc hộp nhẹ, chứa mọi thứ ứng dụng của bạn cần để chạy.

- Nó hoạt động giống nhau trên mọi hệ thống — laptop, server hay cloud của bạn.

**Vì sao nên dùng Docker?**

- **Consistent Environment**: Chạy giống nhau ở mọi nơi, bất kể bạn deploy ở đâu.

- **Lightweight**: Containers có kích thước nhỏ và dùng ít tài nguyên hệ thống hơn.

- **Easy to Share**: Bạn có thể chia sẻ ứng dụng với người khác qua container image.

- **Faster Deployment**: Build một lần, chạy ở bất cứ đâu.

- **Better Isolation**: Mỗi container chạy độc lập, không ảnh hưởng lẫn nhau.

> 💡 Ghi chú thêm: "Build, package, run" là quy trình tổng quát khi làm việc với Docker — build image từ mã nguồn, đóng gói (package) mọi phụ thuộc cần thiết vào image đó, rồi run (chạy) image thành container thực thi.

### 2. So sánh Docker Containers và Virtual Machines

> 🖼️ Dán ảnh: `1389_so-sanh-docker-containers-va-virtual-machines.jpg`

Cả Docker và Virtual Machines (VMs) đều giúp chạy ứng dụng trong môi trường cách ly (**isolated**), nhưng hoạt động theo cách khác nhau.

<table header-row="true"><tr><td>Docker (Containers)</td><td>Virtual Machines (VMs)</td></tr><tr><td>Sử dụng OS-level virtualization</td><td>Sử dụng hardware-level virtualization</td></tr><tr><td>Dùng chung host OS kernel với tất cả các containers</td><td>Mỗi VM có guest OS và kernel riêng</td></tr><tr><td>Nhẹ (lightweight), khởi động chỉ trong vài giây</td><td>Nặng hơn (heavier), khởi động lâu hơn</td></tr><tr><td>Dùng ít hơn tài nguyên hệ thống</td><td>Dùng nhiều hơn tài nguyên hệ thống</td></tr><tr><td>Có thể chạy nhiều containers trên cùng một máy</td><td>Chỉ chạy được ít VMs hơn trên cùng một máy</td></tr><tr><td>Lý tưởng cho microservices và triển khai nhanh</td><td>Lý tưởng để chạy các OS khác nhau hoặc ứng dụng đầy đủ</td></tr></table>

> 💡 **Tóm lại:** Docker → Nhẹ, nhanh, dùng chung OS kernel. VMs → Nặng hơn, chậm hơn, mỗi VM có OS riêng.

### 3. Kiến trúc Docker (Client, Daemon, Registry)

> 🖼️ Dán ảnh: `1390_kien-truc-docker-client-daemon-registry.jpg`

Docker sử dụng kiến trúc **client-server**, gồm 3 thành phần chính:

- **Client**: Nơi bạn chạy các lệnh `docker`. Nó giao tiếp với Docker daemon.

- **Docker Host** — chứa:
    - **Docker Daemon**: Lắng nghe các lệnh Docker và quản lý các Docker objects (**Images** và **Containers**).
        - **Images**: Các template chỉ đọc (read-only) dùng để tạo containers.

        - **Containers**: Các instance đang chạy của images.

- **Registry**: Lưu trữ các Docker images. **Docker Hub** là một registry công khai (public) mà bạn có thể sử dụng.

**Cách hoạt động:**

- Bạn chạy một lệnh `docker` trong Client.

- Client gửi lệnh đến Docker Daemon.

- Daemon pull images từ Registry (nếu cần).

- Nó dùng các images đó để tạo và chạy Containers.

- Containers chạy ứng dụng của bạn trong môi trường cách ly.

> 💡 **Tóm lại:** Client đưa ra lệnh → Daemon thực hiện công việc → Images được sử dụng → Containers chạy ứng dụng.

### 4. Images và Containers (sơ đồ minh họa)

> 🖼️ Dán ảnh: `1391_ghi-chu-docker-images-va-containers-so-do-minh-hoa.jpg`

**Images**

- Image là một template nhẹ, chỉ đọc (**read-only**), chứa mọi thứ cần thiết để chạy một ứng dụng (code, runtime, libraries, tools, v.v.).

- Cấu trúc theo lớp (layer), từ dưới lên: **Base OS → Runtime → Libraries → Application Code**.

- Images được dùng để tạo containers.

- Images được lưu trong một registry (như Docker Hub) hoặc lưu cục bộ trên hệ thống của bạn.

**Containers**

- Container là một instance đang chạy của một image.

- Nó có mọi thứ ứng dụng cần để chạy, nhưng ở dạng **writable** (ghi được) và **isolated** (cách ly).

- Bạn có thể start, stop, remove và tạo nhiều containers từ cùng một image.

**Sự khác biệt chính**

- **Image** → Template tĩnh (read-only)

- **Container** → Instance đang chạy (read-write)

### 5. Hướng dẫn cài đặt Docker trên Windows, Mac, Linux

> 🖼️ Dán ảnh: `1392_huong-dan-cai-dat-docker-tren-windows-mac-linux.jpg`

Bạn có thể cài đặt **Docker Desktop** trên Windows, Mac hoặc Linux.

**1. Windows**

- Truy cập trang web chính thức của Docker: [https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop)

- Tải Docker Desktop cho Windows.

- Chạy file cài đặt và làm theo hướng dẫn thiết lập.

- Đảm bảo **WSL 2** đã được cài đặt và bật.

- Khởi động lại hệ thống nếu cần.

**2. Mac**

- Truy cập trang web chính thức của Docker.

- Tải Docker Desktop cho Mac (Intel hoặc Apple Silicon).

- Mở file `.dmg` vừa tải về.

- Kéo Docker vào thư mục Applications.

- Mở Docker và làm theo hướng dẫn thiết lập.

**3. Linux (Ví dụ với Ubuntu)**

- Mở terminal.

- Cập nhật hệ thống:

```bash
sudo apt update
```

- Cài đặt các package cần thiết:

```bash
sudo apt install ca-certificates curl gnupg
```

- Thêm GPG key chính thức của Docker:

```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
```

- Thêm Docker repository:

```bash
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list
```

- Cài đặt Docker:

```bash
sudo apt update
sudo apt install docker-ce docker-ce-cli containerd.io
```

- Khởi động Docker:

```bash
sudo systemctl start docker
sudo systemctl enable docker
```

**Sau khi cài đặt, kiểm tra bằng cách chạy:**

```bash
docker --version
```

### 6. Tạo container Docker đầu tiên (hello-world)

> 🖼️ Dán ảnh: `1393_huong-dan-tao-container-docker-dau-tien-hello-worl.jpg`

Cùng tạo và chạy container Docker đầu tiên của bạn bằng image `hello-world`.

**1. Pull Image** — Lệnh này tải image `hello-world` về từ Docker Hub.

```bash
docker pull hello-world
```

**2. Run Container** — Lệnh này tạo và chạy một container từ image. Bạn sẽ thấy một thông báo xác nhận Docker đang hoạt động bình thường.

```bash
docker run hello-world
```

**3. Kiểm tra Containers đang chạy** — Liệt kê tất cả containers đang chạy. Bạn sẽ không thấy `hello-world` ở đây vì nó dừng ngay sau khi chạy xong.

```bash
docker ps
```

**4. Kiểm tra tất cả Containers** — Liệt kê tất cả containers (kể cả những cái đã dừng).

```bash
docker ps -a
```

**5. Xóa Container** — Xóa container đã dùng.

```bash
docker rm <container_id_or_name>
```

> 💡 Note: Container `hello-world` sẽ exit ngay sau khi hiển thị thông báo, nên nó không chạy ngầm (background).

### 7. Danh sách các lệnh Docker cơ bản cần thiết

> 🖼️ Dán ảnh: `1394_danh-sach-cac-lenh-docker-can-thiet-co-ban.jpg`

Dưới đây là một số lệnh Docker cần thiết mà người mới bắt đầu nên biết:

1. Kiểm tra phiên bản Docker

```bash
docker --version
```

1. Pull một image từ Docker Hub

```bash
docker pull <image-name>
```

1. Liệt kê tất cả images đã tải về

```bash
docker images
```

1. Chạy một container

```bash
docker run <image-name>
```

1. Liệt kê tất cả containers đang chạy

```bash
docker ps
```

1. Liệt kê tất cả containers (kể cả đã dừng)

```bash
docker ps -a
```

1. Dừng một container đang chạy

```bash
docker stop <container-id-or-name>
```

1. Khởi động lại container đã dừng

```bash
docker start <container-id-or-name>
```

1. Restart một container

```bash
docker restart <container-id-or-name>
```

1. Xóa một container

```bash
docker rm <container-id-or-name>
```

1. Xóa một image

```bash
docker rmi <image-name>
```

1. Xem logs của container

```bash
docker logs <container-id-or-name>
```

1. Mở shell bên trong một container đang chạy

```bash
docker exec -it <container-id-or-name> /bin/bash
```
