# Hướng dẫn bảo trì & cập nhật

Tài liệu này dành cho bạn (người quản lý repo), không phải người xem trang web. Có 2 phần: (A) đồng bộ dữ liệu **Glossary** tự động từ Notion, (B) cập nhật nội dung **kiến thức/bài báo** (bán tự động, cần nhờ Claude).

---

## Cấu trúc thư mục

```
nckh-wiki/
├── docs/                  Nội dung website (MkDocs quét thư mục này để build)
│   ├── index.md           Trang chủ
│   ├── toan/              Toán nền tảng
│   ├── ml-co-ban/         Machine Learning cơ bản
│   ├── deep-learning/     Autoencoder, VAE, CNN, Transformer, CLIP, Latent Space
│   ├── xai/               Explainable AI & CBM
│   ├── papers/            Thư viện bài báo (bibliography công khai)
│   ├── glossary/          Từ điển thuật ngữ Anh-Việt
│   └── ky-nang/           Kỹ năng nghiên cứu (cách đọc bài báo, lộ trình đọc)
├── scripts/               Script Python build & đồng bộ dữ liệu
│   ├── glossary_lib.py    Logic dùng chung để build trang glossary
│   ├── build_glossary.py  Build glossary từ data/raw_data.json (thủ công/offline)
│   ├── sync_and_push.py   Tự động lấy Notion -> build -> git push (script chính)
│   └── build_papers_page.py  Build trang thư viện bài báo từ data/papers_raw.json
├── data/                  Dữ liệu thô/xuất ra (không phải nội dung web trực tiếp)
│   ├── raw_data.json      Export thô database Glossary từ Notion
│   ├── papers_raw.json    Export thô database Thư viện bài báo từ Notion
│   ├── glossary.json      Glossary dạng máy đọc được (JSON)
│   └── glossary.csv       Glossary dạng máy đọc được (CSV)
├── .github/workflows/     GitHub Actions — tự build & deploy site khi push
├── mkdocs.yml             Cấu hình site (menu điều hướng, theme, plugin)
├── update_and_push.bat    Double-click để đồng bộ Glossary + push lên GitHub
├── requirements.txt       Thư viện Python cần cho sync_and_push.py
├── requirements-docs.txt  Thư viện Python cần để build/xem thử site (mkdocs serve)
└── .env                   Bí mật (Notion token) — KHÔNG bao giờ commit lên git
```

---

## Phần A — Đồng bộ Glossary tự động (đã hoạt động)

### Cài đặt lần đầu

```
cd C:\NCKH\nckh-wiki
pip install -r requirements.txt
pip install -r requirements-docs.txt
```

### Tạo Notion Integration Token (chỉ làm 1 lần)

1. Vào https://www.notion.so/my-integrations → **New integration** → đặt tên → **Submit**
2. Vào tab **Configuration**, copy **Internal Integration Secret** (bắt đầu bằng `secret_` hoặc `ntn_`)

### Share database với integration (bước hay quên nhất)

Mở database "Thuật ngữ Anh - Việt" trong Notion → nút **"..."** → **Connections** → chọn integration vừa tạo.

### Lấy Database ID

Mở database bằng trình duyệt, nhìn URL dạng `https://www.notion.so/.../<32-ký-tự>?v=...` — đoạn 32 ký tự đó là ID.

### Tạo file `.env`

Tại **thư mục gốc** project (`C:\NCKH\nckh-wiki\`, cùng cấp với `mkdocs.yml`), copy `.env.example` thành `.env`, điền:

```
NOTION_TOKEN=secret_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
NOTION_DATABASE_ID=4a41d94b-9d22-436a-9786-9a650f57bf2d
```

### Chạy

Double-click **`update_and_push.bat`** ở thư mục gốc. Script sẽ: lấy dữ liệu Notion mới nhất → build lại `data/glossary.json`, `data/glossary.csv`, và các trang `docs/glossary/*.md` → `git add` + `git commit -m "Auto update from Notion: <ngày giờ>"` + `git push`. GitHub Actions sẽ tự build lại site và cập nhật GitHub Pages.

### Lỗi thường gặp

- **`git push thất bại`**: SSH key/token đăng nhập GitHub hết hạn — chạy `git push` thủ công trong terminal để xem lỗi và xác thực lại.
- **`Notion API trả lỗi 401`**: token sai hoặc đã bị revoke — tạo lại token.
- **`Notion API trả lỗi 404`**: database ID sai, hoặc integration chưa được share vào database.
- **`'python' is not recognized`**: mở `update_and_push.bat` bằng Notepad, sửa dòng `set "PYTHON_EXE=..."` thành đường dẫn Python thật trên máy bạn (lấy bằng lệnh `where python` trong Anaconda Prompt).

---

## Phần B — Cập nhật nội dung kiến thức / bài báo (bán tự động)

Các trang trong `docs/toan/`, `docs/ml-co-ban/`, `docs/deep-learning/`, `docs/xai/`, `docs/ky-nang/` được chuyển thủ công từ Notion sang Markdown (Notion không có API đơn giản để tự động hóa hoàn toàn phần văn bản tự do như glossary). Quy trình hiện tại:

1. Bạn sửa/thêm nội dung trong Notion như bình thường.
2. Nhắn Claude: *"cập nhật lại trang [tên trang] từ Notion"* — Claude sẽ lấy lại nội dung, chuyển đổi định dạng, và ghi đè đúng file `.md` tương ứng vào máy bạn.
3. Chạy `git add . && git commit -m "Update [tên trang]" && git push` (hoặc dùng `update_and_push.bat` — nó cũng push mọi thay đổi khác đang có trong thư mục, không chỉ glossary).

Thư viện bài báo (`docs/papers/index.md`) tương tự — nhắn Claude cập nhật, Claude sẽ ghi lại `data/papers_raw.json` rồi chạy `scripts/build_papers_page.py`.

**Hướng nâng cấp trong tương lai (đã thảo luận, chưa triển khai):** viết một script Python tổng quát gọi thẳng Notion API + tự chuyển đổi block Notion sang Markdown (áp dụng đúng các quy tắc đã dùng thủ công: callout → blockquote, columns → phẳng, mention-page → link tương đối, giữ nguyên mermaid/LaTeX), tích hợp vào `update_and_push.bat` để không cần nhờ Claude mỗi lần nữa. Đây là một khối việc lớn, làm khi bạn sẵn sàng đầu tư thời gian.

---

## Xem thử site trước khi push

```
cd C:\NCKH\nckh-wiki
mkdocs serve
```

Mở `http://127.0.0.1:8000`. Nhấn `Ctrl+C` để dừng.

## Bật GitHub Pages (chỉ làm 1 lần)

1. Sửa 2 dòng `site_url` và `repo_url` trong `mkdocs.yml` thành đúng username/repo GitHub của bạn.
2. Push code lên nhánh `main` — GitHub Actions (`.github/workflows/deploy-docs.yml`) tự build và đẩy sang nhánh `gh-pages`.
3. Vào repo trên GitHub → **Settings** → **Pages** → **Source: Deploy from a branch** → chọn nhánh **`gh-pages`**, thư mục **`/ (root)`** → **Save**.
4. Site sẽ có tại `https://<username>.github.io/<tên-repo>/`.
