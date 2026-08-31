# Docker nâng cao: Images, Dockerfile, Volumes & Compose

> 🖼️ **7 ảnh gốc cho trang này (dán theo đúng thứ tự vào từng mục bên dưới):**
> 1395_ghi-chu-lam-viec-voi-docker-images-pull-inspect-ta.jpg
>
> 1396_ghi-chu-ve-dockerfile-va-cac-instructions-pho-bien.jpg
>
> 1397_huong-dan-build-mot-docker-image-bang-docker-build.jpg
>
> 1398_ghi-chu-docker-port-mapping-vi-du-nginx.jpg
>
> 1399_ghi-chu-docker-volumes-luu-tru-du-lieu-lau-dai.jpg
>
> 1400_ghi-chu-docker-compose-file-yaml-multi-container.jpg
>
> 1401_cac-use-case-pho-bien-cua-docker-ban-trung.jpg
>

### 1. Làm việc với Docker Images

> 🖼️ Dán ảnh: `1395_ghi-chu-lam-viec-voi-docker-images-pull-inspect-ta.jpg`

Docker images là các template chỉ đọc (read-only) dùng để tạo containers.

#### 1. Pull một Image

- Tải một image từ Docker Hub.

```bash
docker pull <image-name>[:tag]
```

Ví dụ:

```bash
docker pull nginx:latest
```

#### 2. Liệt kê tất cả Images

- Hiển thị tất cả images được lưu cục bộ.

```bash
docker images
```

#### 3. Kiểm tra chi tiết Image (Inspect)

- Xem thông tin chi tiết về một image.

```bash
docker inspect <image-name>[:tag]
```

#### 4. Xóa một Image

- Xóa một image khỏi hệ thống của bạn.

```bash
docker rmi <image-name>[:tag]
```

#### 5. Xóa các Images không dùng đến

- Xóa tất cả images dangling (không còn dùng đến).

```bash
docker image prune
```

#### 6. Gắn Tag cho Image

- Tạo một tag mới cho image đã có.

```bash
docker tag <source-image>[:tag] <new-image>[:tag]
```

Ví dụ:

```bash
docker tag nginx:latest my-nginx:web
```

#### 7. Tìm kiếm Image

- Tìm kiếm images trên Docker Hub.

```bash
docker search <image-name>
```

### 2. Dockerfile và các Instructions phổ biến

> 🖼️ Dán ảnh: `1396_ghi-chu-ve-dockerfile-va-cac-instructions-pho-bien.jpg`

#### Dockerfile là gì?

- Dockerfile là một file văn bản (text file) chứa các instructions để tự động build một Docker image.

#### Vì sao nên dùng Dockerfile?

- Tự động hóa việc tạo image.

- Giúp việc tạo image lặp lại được (repeatable) và nhất quán (consistent).

- Chia sẻ cấu hình ứng dụng của bạn với người khác.

#### Cấu trúc cơ bản

- Một Dockerfile được tạo từ các instructions. Mỗi instruction tạo ra một layer trong image cuối cùng.

#### Các Instructions phổ biến

- **FROM**: Thiết lập base image.

- **RUN**: Chạy các lệnh trong image.

- **COPY**: Copy files từ máy của bạn vào image.

- **WORKDIR**: Thiết lập working directory bên trong image.

- **EXPOSE**: Mở một port.

- **CMD**: Chỉ định lệnh mặc định sẽ chạy khi container khởi động.

#### Ví dụ về Dockerfile

```docker
FROM python:3.11-slim        # Base image
WORKDIR /app                 # Thiết lập working directory
COPY . .                     # Copy toàn bộ files hiện tại vào /app
RUN pip install -r requirements.txt   # Cài đặt dependencies
EXPOSE 5000                  # Expose port 5000
CMD ["python", "app.py"]     # Lệnh để chạy ứng dụng
```

#### Build một Image

- Chạy lệnh này trong thư mục chứa Dockerfile:

```bash
docker build -t my-image:latest .
```

### 3. Hướng dẫn build một Docker Image bằng docker build

> 🖼️ Dán ảnh: `1397_huong-dan-build-mot-docker-image-bang-docker-build.jpg`

Chúng ta dùng một Dockerfile để build Docker image của riêng mình. Lệnh để build một image là `docker build`.

#### 1. Lệnh cơ bản

- Chạy lệnh này trong thư mục chứa Dockerfile của bạn.

```bash
docker build -t <image-name>:<tag> .
```

Ví dụ:

```bash
docker build -t my-app:1.0 .
```

- `-t`: Gắn tag cho image với tên và phiên bản.

- `.`: Báo cho Docker tìm Dockerfile trong thư mục hiện tại.

#### 2. Điều gì xảy ra khi bạn build

- Docker đọc các instructions trong Dockerfile theo từng bước và tạo ra các layers.

- Mỗi instruction thêm một layer vào image.

- Cuối cùng, Docker gộp tất cả các layers thành một image duy nhất.

#### 3. Kiểm tra Image của bạn

- Liệt kê tất cả images để xem image vừa build.

```bash
docker images
```

#### 4. Build với Dockerfile khác (Tùy chọn)

- Nếu Dockerfile của bạn có tên hoặc vị trí khác, dùng `-f` để chỉ định file.

```bash
docker build -f <Dockerfile-name> -t <image-name>:<tag> .
```

Ví dụ:

```bash
docker build -f Dockerfile.dev -t my-app:dev .
```

> 💡 Note: Build một image không có nghĩa là chạy nó. Nó chỉ tạo ra image mà thôi.

### 4. Port Mapping (ví dụ Nginx)

> 🖼️ Dán ảnh: `1398_ghi-chu-docker-port-mapping-vi-du-nginx.jpg`

Port mapping cho phép bạn access một service đang chạy bên trong container từ host machine của bạn.

#### 1. Port Mapping là gì?

- Containers có network nội bộ riêng. Port mapping (`-p`) sẽ ánh xạ (map) một port trên host sang một port bên trong container.

#### 2. Cú pháp cơ bản

```bash
docker run -p <host-port>:<container-port> <image-name>
```

- `<host-port>` → Port trên host machine của bạn

- `<container-port>` → Port trên container

#### 3. Ví dụ

- Chạy một nginx container và map port 8080 trên host sang port 80 trong container.

```bash
docker run -d -p 8080:80 nginx
```

- Giờ mở trình duyệt và truy cập: `http://localhost:8080`

- Bạn sẽ thấy trang chào mừng (welcome page) của nginx.

#### 4. Một ví dụ khác

- Nếu ứng dụng của bạn chạy trên port 5000 bên trong container, hãy map nó sang port 3000 trên host.

```bash
docker run -d -p 3000:5000 my-app
```

- Truy cập tại: `http://localhost:3000`

> 💡 Note: Bạn có thể map bất kỳ host port nào sang bất kỳ container port nào. Chỉ cần đảm bảo host port đó chưa được sử dụng.

### 5. Docker Volumes - lưu trữ dữ liệu lâu dài

> 🖼️ Dán ảnh: `1399_ghi-chu-docker-volumes-luu-tru-du-lieu-lau-dai.jpg`

Docker volumes là cách tốt nhất để lưu trữ lâu dài (persist) dữ liệu được tạo ra và sử dụng bởi Docker containers.

#### 1. Docker Volume là gì?

- Docker volume là một vị trí đặc biệt nằm ngoài filesystem của container.

- Dữ liệu trong volumes vẫn tồn tại (persist) ngay cả khi container bị dừng hoặc bị xóa.

- Volumes được Docker quản lý và dễ dàng back up cũng như chia sẻ.

#### 2. Vì sao nên dùng Volumes?

- Lưu trữ dữ liệu lâu dài, vượt ngoài vòng đời (lifecycle) của container.

- Chia sẻ dữ liệu giữa nhiều containers.

- Hiệu năng tốt hơn bind mounts đối với các tác vụ I/O nặng.

- Dễ dàng back up và migrate.

#### 3. Cú pháp cơ bản

```bash
docker run -v <volume-name>:<container-path> <image-name>
```

- `<volume-name>` → Tên của volume trên host.

- `<container-path>` → Đường dẫn bên trong container nơi volume được mount.

- `<image-name>` → Docker image sẽ sử dụng.

#### 4. Ví dụ

- Tạo và sử dụng một volume

```bash
docker run -v mydata:/app/data nginx
```

- Sử dụng volume với đường dẫn cụ thể trong container

```bash
docker run -v mydata:/var/lib/mysql mysql
```

- Volume chỉ đọc (read-only)

```bash
docker run -v mydata:/app/data:ro nginx
```

#### 5. Quản lý Volumes

- Liệt kê tất cả volumes

```bash
docker volume ls
```

- Kiểm tra chi tiết một volume

```bash
docker volume inspect <volume-name>
```

- Xóa một volume

```bash
docker volume rm <volume-name>
```

### 6. Docker Compose - file YAML multi-container

> 🖼️ Dán ảnh: `1400_ghi-chu-docker-compose-file-yaml-multi-container.jpg`

Docker Compose là một công cụ (tool) để định nghĩa và chạy các ứng dụng Docker multi-container bằng một file YAML duy nhất.

#### 1. Docker Compose là gì?

- Nó cho phép bạn cấu hình nhiều containers, networks, volumes và services trong một file duy nhất.

- Chỉ với một lệnh, bạn có thể tạo và khởi động tất cả các services cùng lúc.

- Rất phù hợp cho local development và testing.

#### 2. File Compose

- Docker Compose sử dụng một file YAML tên là `docker-compose.yml` theo mặc định.

- Nó định nghĩa:
    - **services** → Các containers cần chạy

    - **images** → Các Docker images sử dụng

    - **ports** → Port mapping

    - **volumes** → Lưu trữ dữ liệu lâu dài

    - **networks** → Giao tiếp giữa các containers

Ví dụ (docker-compose.yml):

```yaml
version: '3'
services:
  web:
    image: nginx
    ports:
      - "8080:80"
  db:
    image: mysql:8
    environment:
      MYSQL_ROOT_PASSWORD: root
```

#### 3. Các lệnh thường dùng

- `docker compose up` → Build (nếu cần) và khởi động services

- `docker compose up -d` → Khởi động services ở chế độ detached (nền)

- `docker compose down` → Dừng và xóa containers, networks và volumes

- `docker compose ps` → Liệt kê các services đang chạy

- `docker compose logs` → Xem logs của services

- `docker compose build` → Build hoặc rebuild lại services

#### 4. Vì sao nên dùng Docker Compose?

- Quản lý các ứng dụng multi-container một cách dễ dàng.

- Tiết kiệm thời gian nhờ chỉ dùng một file và các lệnh đơn giản.

- Đảm bảo tất cả services hoạt động cùng nhau một cách nhất quán.

### 7. Các Use Case phổ biến của Docker

> 🖼️ Dán ảnh: `1401_cac-use-case-pho-bien-cua-docker-ban-trung.jpg`

Docker được sử dụng trong rất nhiều lĩnh vực. Dưới đây là một số use case phổ biến nhất:

#### 1. Môi trường Development nhất quán

- Docker đảm bảo ứng dụng của bạn chạy giống nhau trên máy của mọi developer.

- Không còn tình trạng "chạy được trên máy tôi" (works on my machine) nữa.

#### 2. Deploy ứng dụng dễ dàng

- Đóng gói ứng dụng và toàn bộ dependencies vào một container.

- Deploy nhanh chóng lên bất kỳ server hay cloud platform nào.

#### 3. Kiến trúc Microservices

- Chạy mỗi service trong container riêng của nó.

- Dễ dàng scale, update và quản lý từng service riêng lẻ.

#### 4. CI/CD Pipelines

- Docker phù hợp hoàn hảo với các CI/CD workflows.

- Build, test và deploy ứng dụng nhanh hơn và đáng tin cậy hơn.

#### 5. Testing cách ly

- Test ứng dụng của bạn trong một môi trường cách ly (isolated).

- Không xung đột với các project khác hay cấu hình hệ thống.

#### 6. Hỗ trợ ứng dụng Legacy

- Chạy các ứng dụng cũ cùng dependencies của chúng mà không cần thay đổi host system.

- Giữ cho các hệ thống legacy vận hành trơn tru.

#### 7. Portable trên mọi nền tảng

- Build một lần và chạy ở mọi nơi – laptop, server hay cloud.

- Hoạt động trên Windows, macOS và Linux.
