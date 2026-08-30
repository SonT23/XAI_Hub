# Hướng dẫn: tự động đồng bộ Notion → GitHub

File này giải thích cách thiết lập `sync_and_push.py` để mỗi khi bạn cập nhật
database "Thuật ngữ Anh - Việt" trên Notion, chỉ cần chạy 1 file
(`update_and_push.bat`) là dữ liệu được lấy mới, build lại, và tự động
commit + push lên GitHub — với message commit là thời gian chạy.

## 1. Cài thư viện cần thiết (chỉ làm 1 lần)

Mở PowerShell/Command Prompt:

```
cd C:\NCKH\glossary-en-vi
pip install -r requirements.txt
```

## 2. Tạo Notion Integration Token (chỉ làm 1 lần)

1. Vào https://www.notion.so/my-integrations
2. Bấm **New integration**
3. Đặt tên (ví dụ "Glossary Sync"), chọn đúng Workspace của bạn, bấm **Submit**
4. Sau khi tạo xong, vào tab **Configuration**, copy giá trị **Internal Integration Secret**
   (bắt đầu bằng `secret_` hoặc `ntn_`) — đây chính là `NOTION_TOKEN`

## 3. Chia sẻ (share) database Notion với integration vừa tạo

Đây là bước hay bị quên nhất — nếu bỏ qua, script sẽ báo lỗi 401/403.

1. Mở database "Thuật ngữ Anh - Việt" trong Notion
2. Bấm nút **"..."** (ba chấm) ở góc trên bên phải trang → **Connections** (hoặc "Add connections")
3. Tìm và chọn integration bạn vừa tạo ở bước 2 (ví dụ "Glossary Sync")

## 4. Lấy Database ID

1. Mở database "Thuật ngữ Anh - Việt" bằng trình duyệt (bấm "Open as page" nếu đang xem dạng inline)
2. Nhìn vào URL, dạng: `https://www.notion.so/<workspace>/<DATABASE_ID>?v=...`
3. `DATABASE_ID` là chuỗi 32 ký tự (có thể có hoặc không có dấu gạch ngang `-`) ngay trước dấu `?v=`
4. Giá trị này hiện tại (đã dùng để build project ban đầu) là:
   `4a41d94b-9d22-436a-9786-9a650f57bf2d` — nhưng bạn nên tự kiểm tra lại URL thật
   để chắc chắn đúng.

## 5. Tạo file .env

Trong thư mục `C:\NCKH\glossary-en-vi\`, copy file `.env.example` thành `.env`,
rồi mở bằng Notepad, điền:

```
NOTION_TOKEN=secret_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
NOTION_DATABASE_ID=4a41d94b-9d22-436a-9786-9a650f57bf2d
```

**Quan trọng:** file `.env` chứa bí mật (token), đã được thêm vào `.gitignore`
nên sẽ KHÔNG bao giờ bị đưa lên GitHub. Đừng bao giờ tự tay `git add .env`.

## 6. Chạy thử lần đầu

```
cd C:\NCKH\glossary-en-vi
python sync_and_push.py
```

Nếu mọi thứ đúng, bạn sẽ thấy:

```
Đang lấy dữ liệu mới nhất từ Notion...
Lấy được 165 thuật ngữ.
Đã tạo lại glossary.json, glossary.csv, README.md (165 thuật ngữ).
Đã commit: "Auto update from Notion: 2026-08-30 16:20:00"
Đã push lên GitHub thành công.
```

## 7. Từ lần sau: chỉ cần double-click

Mỗi khi bạn sửa/thêm thuật ngữ trong Notion, chỉ cần double-click file
`update_and_push.bat` trong thư mục `C:\NCKH\glossary-en-vi\` — script sẽ tự
lấy dữ liệu mới, build lại, commit, và push. Không cần mở terminal, không cần
gõ lệnh git thủ công nữa.

## Xử lý lỗi thường gặp

- **`git push thất bại`**: có thể do SSH key/token đăng nhập GitHub đã hết
  hạn hoặc chưa cấu hình — chạy `git push` thủ công một lần trong terminal để
  xem lỗi chi tiết và xác thực lại.
- **`Notion API trả lỗi 401`**: token sai, hoặc đã bị revoke — tạo lại token
  ở bước 2.
- **`Notion API trả lỗi 404`**: database ID sai, hoặc integration chưa được
  share vào database (xem lại bước 3).
- **Không có thay đổi nào so với lần trước — không cần commit/push**: đây là
  thông báo bình thường, nghĩa là dữ liệu Notion chưa thay đổi gì kể từ lần
  chạy trước.
