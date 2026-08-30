# Ghi chú vận hành — Cách hoạt động của Wiki này

> **File này CHỈ ở trên máy bạn, KHÔNG lên GitHub** (đã thêm vào `.gitignore`). Đây là
> ghi chú cá nhân để bạn hiểu và tự vận hành hệ thống mà không cần hỏi lại Claude mỗi lần.
> `MAINTENANCE.md` (file public, có trên GitHub) vẫn là tài liệu tham chiếu chính thức
> cho phần kỹ thuật — file này chỉ giải thích thêm theo cách dễ hiểu, kèm "tại sao".

---

## 1. Bức tranh tổng thể: Notion → Git → Website

```
┌─────────────┐      chạy .bat       ┌──────────────┐    GitHub Actions   ┌─────────────────┐
│   Notion     │  ───────────────►   │  Máy bạn      │  ──────────────►   │  GitHub Pages    │
│ (nơi bạn ghi │   (kéo dữ liệu về,   │  C:\NCKH\     │   (tự build lại    │  (website công   │
│  chú hàng    │    build lại .md,    │  nckh-wiki\   │    trang từ file    │   khai, ai có     │
│  ngày)       │    commit + push)    │  (git repo)   │    .md, deploy)     │   link đều xem)  │
└─────────────┘                      └──────────────┘                     └─────────────────┘
```

Ba tầng, ba việc khác nhau:

1. **Notion = nơi soạn thảo.** Bạn viết/sửa như bình thường, không cần nghĩ gì đến kỹ thuật ở bước này.
2. **Git repo trên máy bạn (`C:\NCKH\nckh-wiki`) = kho lưu trữ trung gian + lịch sử.** Đây là nơi các file `.md` được sinh ra, và là nơi "chốt" một phiên bản (mỗi lần `git commit` là một mốc có thể quay lại được).
3. **GitHub Pages = bản công khai cuối cùng.** Chỉ đọc, tự build lại mỗi khi có commit mới trên GitHub — bạn không bao giờ sửa trực tiếp ở tầng này.

**Điều quan trọng nhất cần nhớ:** dữ liệu chỉ chảy **một chiều** — Notion → Git → Web.
Không bao giờ sửa trực tiếp file trong `docs/toan/`, `docs/xai/`, v.v. trên máy, vì lần đồng
bộ tiếp theo từ Notion sẽ **ghi đè mất** sửa đổi đó. Muốn sửa nội dung, luôn sửa trong Notion.

Ngoại lệ: các file bạn viết tay và script KHÔNG bao giờ đụng vào — an toàn để sửa trực tiếp:
`docs/index.md`, `docs/*/index.md` (trang tổng quan mỗi mục), `mkdocs.yml`, `README.md`,
`MAINTENANCE.md`, file này.

---

## 2. Có 2 cơ chế đồng bộ khác nhau — hiểu rõ để biết khi nào cần làm gì

### Cơ chế A — Glossary (từ điển thuật ngữ): quét **toàn bộ database**, không cần danh sách

`scripts/sync_and_push.py` gọi thẳng Notion API, hỏi "cho tôi toàn bộ hàng trong database
Thuật ngữ Anh-Việt", rồi build lại tất cả. Vì đây là 1 database, mọi hàng đều tự động được
gồm vào — **không cần thêm gì thủ công dù bạn thêm bao nhiêu thuật ngữ mới**. Đây là ý
nghĩa của "tự động hoàn toàn" cho phần glossary.

### Cơ chế B — Các trang kiến thức (Toán/ML/DL/XAI/Kỹ năng): theo **danh sách thủ công** (manifest)

Khác với glossary, các trang như "Autoencoder", "CNN"... là các trang Notion tự do (không
phải hàng trong database), nên **không có cách nào để Notion API tự biết trang nào bạn
"muốn" đưa lên web và trang nào không**. Vì vậy `scripts/pages_manifest.json` đóng vai trò
danh sách "được duyệt" — chỉ trang có tên trong này mới được đồng bộ.

**Hệ quả thực tế:**
- Sửa nội dung của 1 trang ĐÃ có trong danh sách → **100% tự động**, không cần làm gì thêm.
- Tạo 1 trang HOÀN TOÀN MỚI muốn đưa lên web → cần đúng **1 bước thủ công một lần**: thêm
  trang đó vào danh sách (xem mục 3 bên dưới). Sau bước đó, mọi lần sửa tiếp theo của
  đúng trang đó lại tự động hoàn toàn.

Đây không phải thiếu sót của script — mà là vì bản chất Notion không có khái niệm
"trang này công khai, trang kia là nháp riêng tư" trừ khi bạn tự định nghĩa ra (đây chính
là việc `pages_manifest.json` làm thay).

---

## 3. Quy trình đầy đủ khi bạn viết một trang kiến thức MỚI trong Notion

Ví dụ: bạn vừa viết xong 1 trang mới "Diffusion Models" trong Notion và muốn nó lên web.

**Bước 1 — Viết trong Notion như bình thường.** Không cần lo về format, chỉ cần viết đúng
theo Notion (dùng heading, callout, bảng, mermaid... của Notion — script sẽ tự chuyển đổi).

**Bước 2 — Đảm bảo integration "nhìn thấy" trang đó.** Nếu trang mới nằm **bên trong** một
trang/khu vực đã share với integration trước đó (ví dụ nó là trang con của "Deep Learning"),
thì **không cần làm gì** — quyền tự động lan xuống. Nếu là trang hoàn toàn độc lập
(không nằm trong cây trang nào đã share), cần "..." → Connections → chọn integration.

**Bước 3 — Lấy ID trang.** Mở trang bằng trình duyệt, copy 32 ký tự cuối trong URL.

**Bước 4 — Thêm 1 dòng vào `scripts/pages_manifest.json`**, trong mảng `"pages"`:
```json
{ "id": "abc123...", "output": "docs/deep-learning/diffusion-models.md" }
```
(Chọn đường dẫn `output` theo đúng thư mục con phù hợp trong `docs/`.)

**Bước 5 — Thêm vào menu điều hướng** trong `mkdocs.yml`, phần `nav:`, ví dụ:
```yaml
  - Deep Learning:
      - ...
      - Diffusion Models: deep-learning/diffusion-models.md
```
(Nếu quên bước này, trang vẫn được build ra file `.md`, chỉ là không hiện trên menu —
người xem không tìm thấy trừ khi có link trực tiếp.)

**Bước 6 — Chạy `update_and_push.bat`.** Xong — trang mới sẽ xuất hiện trên GitHub Pages
sau khi GitHub Actions build lại (~1-2 phút).

**Từ lần sau trở đi:** sửa nội dung trang "Diffusion Models" trong Notion → chạy
`update_and_push.bat` → tự động cập nhật, không cần lặp lại bước 3-5 nữa.

### Nếu bạn không tự làm bước 4-5 mà nhờ Claude

Cứ nhắn kiểu: *"Tôi vừa thêm trang [tên trang] trong Notion, thêm vào danh sách đồng bộ
giúp tôi"* — Claude sẽ tự lấy ID, sửa 2 file, gửi lại cho bạn.

---

## 4. Những thứ KHÔNG (chưa) tự động được — cần biết để tránh bất ngờ

- **Thư viện bài báo** (`docs/papers/index.md`): vẫn cần nhờ Claude cập nhật thủ công
  (chạy `scripts/build_papers_page.py` sau khi Claude query lại database). Lý do: đây là
  1 database nhưng có yêu cầu lọc riêng (ẩn trường "Trạng thái" cá nhân, bỏ dòng mẫu) mà
  hiện chưa viết thành script REST API riêng như glossary.
- **Video, audio, file đính kèm trong trang Notion**: bị bỏ qua âm thầm khi đồng bộ (không
  có gì hiện trên web, không báo lỗi). Nếu 1 trang có video quan trọng, nói với Claude để
  xử lý riêng (ví dụ tự thêm link YouTube thủ công vào trang `.md`).
- **Ảnh dán trực tiếp/upload lên Notion** (không phải link ảnh từ nơi khác): không nhúng
  được vì Notion chỉ cấp link tạm thời cho loại ảnh này (hết hạn sau vài giờ). Script sẽ
  hiện dòng chữ ghi chú thay vì ảnh hỏng. Cách né: dùng ảnh có link cố định (ví dụ upload
  lên Imgur/GitHub rồi dán link vào Notion dạng "external").
- **Bảng có ký tự `|` trong nội dung ô**: có thể làm lệch cấu trúc bảng khi ra Markdown.
  Hiếm gặp với tiếng Việt/công thức toán thông thường, nhưng nếu thấy bảng bị vỡ trên web,
  kiểm tra xem ô nào có dấu `|` không.
- **Trang tạo mới hoàn toàn**: luôn cần bước thủ công 1 lần (mục 3) — không có cách nào
  tránh được việc này trừ khi đổi toàn bộ Notion sang cấu trúc database (không khuyến khích,
  sẽ gò bó cách bạn ghi chú tự do).

---

## 5. Khi có gì đó không chạy đúng — kiểm tra theo thứ tự này

1. Chạy `python scripts\sync_pages.py` riêng (không commit/push) để xem lỗi cụ thể, không
   sợ làm hỏng gì vì lệnh này chỉ ghi file `.md`, không đụng git.
2. Lỗi `404 Not Found` → integration chưa được share vào trang đó (xem mục Bước 2 ở trên).
3. Lỗi `401` → token trong `.env` sai/hết hạn.
4. Trang lên web nhưng thiếu 1 phần nội dung → khả năng cao là loại block chưa được hỗ trợ
   (xem mục 4) — chụp ảnh phần bị thiếu trong Notion gửi Claude để bổ sung.
5. `mkdocs build --strict` báo lỗi khi bạn tự chạy thử → thường là do thiếu file trong
   `nav` của `mkdocs.yml` (đã xóa trang khỏi manifest nhưng quên xóa khỏi `nav`, hoặc
   ngược lại).

---

## 6. Lịch sử: trang thử nghiệm đã dùng để kiểm tra hệ thống

Ngày 30/08/2026, đã tạo 1 trang test "🧪 Trang thử nghiệm đồng bộ" trong Notion để kiểm tra
toàn bộ luồng (danh sách, bảng, callout, toggle, mermaid, công thức, mention-link, video).
Qua đó phát hiện và sửa 1 lỗi thật: nội dung Markdown lồng bên trong khối toggle (`<details>`)
không được xử lý đúng — đã sửa bằng cách thêm `markdown="1"` vào thẻ và bật extension
`md_in_html` trong `mkdocs.yml`. Trang test này đã được xóa khỏi `pages_manifest.json` và
`mkdocs.yml`; bạn cần tự xóa thủ công trong Notion (Claude không có quyền xóa trang Notion)
và xóa thư mục `docs/test/` trên máy nếu còn sót lại.
