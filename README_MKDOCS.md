# Hướng dẫn: trang tra cứu MkDocs + Material trên GitHub Pages

Trang này có ô tìm kiếm (search) và điều hướng theo chủ đề ở thanh bên,
tự động build lại và cập nhật lên mạng mỗi khi bạn push code lên GitHub —
không cần bạn tự build thủ công.

Cách hoạt động: `sync_and_push.py` (đã có sẵn) giờ tự sinh thêm các trang
Markdown trong thư mục `docs/` mỗi lần chạy. Khi bạn push code lên nhánh
`main`, GitHub Actions (`.github/workflows/deploy-docs.yml`) tự động build
các trang đó thành 1 trang web tĩnh bằng MkDocs Material, rồi publish sang
nhánh `gh-pages` — và GitHub Pages phục vụ nhánh đó công khai.

## 1. Sửa lại 2 dòng URL trong `mkdocs.yml`

Mở file `mkdocs.yml`, sửa 2 dòng:

```yaml
site_url: https://YOUR-GITHUB-USERNAME.github.io/glossary-en-vi/
repo_url: https://github.com/YOUR-GITHUB-USERNAME/glossary-en-vi
```

Thay `YOUR-GITHUB-USERNAME` bằng tên tài khoản GitHub thật của bạn, và
`glossary-en-vi` bằng đúng tên repo bạn đã tạo (nếu bạn đặt tên khác).

## 2. (Tùy chọn) Xem thử trên máy trước khi đưa lên mạng

```
cd C:\NCKH\glossary-en-vi
pip install -r requirements-docs.txt
mkdocs serve
```

Mở trình duyệt vào `http://127.0.0.1:8000` để xem trước. Nhấn `Ctrl+C`
trong terminal để dừng.

## 3. Push code lên GitHub

```
cd C:\NCKH\glossary-en-vi
git add .
git commit -m "Add MkDocs search site"
git push
```

(Hoặc đơn giản hơn: chạy `update_and_push.bat` như thường lệ — script vẫn
tự sinh `docs/` mới nhất từ Notion rồi push, bao gồm cả các file MkDocs bạn
vừa thêm.)

Sau khi push, vào tab **Actions** trên trang GitHub của repo, bạn sẽ thấy
workflow "Deploy MkDocs site to GitHub Pages" đang chạy (mất khoảng
1-2 phút). Khi nó chuyển sang dấu tick xanh, nhánh `gh-pages` đã có bản
build mới nhất.

## 4. Bật GitHub Pages (chỉ làm 1 lần)

1. Vào trang repo trên GitHub → **Settings** → **Pages** (menu bên trái)
2. Ở mục **Build and deployment** → **Source**, chọn **Deploy from a branch**
3. Ở mục **Branch**, chọn nhánh **`gh-pages`**, thư mục **`/ (root)`**, bấm **Save**
4. Đợi khoảng 1 phút, trang sẽ có tại:
   `https://<username-của-bạn>.github.io/glossary-en-vi/`

(Nhánh `gh-pages` chỉ xuất hiện trong danh sách sau khi GitHub Actions đã
chạy thành công ít nhất 1 lần ở Bước 3 — nếu chưa thấy, quay lại kiểm tra
tab Actions trước.)

## 5. Từ giờ về sau: hoàn toàn tự động

Quy trình đầy đủ giờ là:

```
Bạn sửa Notion
   → chạy update_and_push.bat (lấy Notion, build lại file + docs/, git push)
   → GitHub Actions tự động build MkDocs site
   → GitHub Pages tự động cập nhật trang tra cứu công khai
```

Bạn không cần làm gì thêm ngoài double-click `update_and_push.bat` mỗi khi
cập nhật thuật ngữ.

## Xử lý lỗi thường gặp

- **Tab Actions báo lỗi đỏ**: bấm vào lần chạy bị lỗi để xem log chi tiết —
  thường do `mkdocs.yml` có lỗi cú pháp (kiểm tra thụt lề YAML) hoặc thiếu
  file được khai báo trong mục `nav` (ví dụ bạn xóa nhầm 1 file trong
  `docs/glossary/`).
- **Trang GitHub Pages báo 404**: đợi thêm 1-2 phút sau khi bật Pages ở
  Bước 4, hoặc kiểm tra lại đã chọn đúng nhánh `gh-pages` chưa.
- **Có chủ đề mới xuất hiện trong Notion nhưng không thấy trên trang web**:
  MkDocs cần bạn khai báo thủ công trang mới vào mục `nav` trong
  `mkdocs.yml` (ví dụ nếu bạn thêm chủ đề "Reinforcement Learning", thêm
  dòng `Reinforcement Learning: glossary/reinforcement-learning.md` vào
  `nav`). Việc build file `.md` cho chủ đề mới thì `sync_and_push.py` đã tự
  làm — chỉ có bước thêm vào `nav` để nó hiện trên thanh điều hướng là cần
  làm thủ công 1 lần.
