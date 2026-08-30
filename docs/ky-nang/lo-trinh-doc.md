# Lộ trình đọc bài báo & kiến thức nền

> Phương pháp đọc: [Cách đọc một bài báo khoa học](cach-doc-bai-bao.md)

> **🎯** Thứ tự dưới đây **không xếp theo năm xuất bản hay độ nổi tiếng**, mà theo **tốc độ đưa mình tới một câu hỏi nghiên cứu**. Mỗi đợt có một mục tiêu rõ ràng và một mốc tự kiểm tra ở cuối.

---

## Đợt 0 — Đã xong

- ✅ [Concept Bottleneck Models](https://arxiv.org/abs/2007.04612) (Koh et al., 2020) — bài nền của đề tài.
- ✅ [How to Read a Paper](https://www.cs.princeton.edu/courses/archive/fall18/cos561/papers/HowToRead05.pdf) (Keshav, 2007) — phương pháp đọc.
- 🔄 [Four Principles of Explainable Artificial Intelligence (NISTIR 8312)](https://nvlpubs.nist.gov/nistpubs/ir/2021/NIST.IR.8312.pdf) — đang đọc, còn mục 6–8.

---

## Đợt 1 — Hiểu vì sao CBM tồn tại và nó hỏng ở đâu

**Mục tiêu:** sau đợt này phải nói được *"CBM có 3 vấn đề, tôi quan tâm vấn đề số mấy"*. **Ước tính 2–3 tuần.**

> **⚠️ Đợt 1 là bắt buộc theo đúng thứ tự** — bốn bài này xây trên nhau. Đợt 2 và 3 thì linh hoạt hơn.

### 1. NIST IR 8312 (2021) — đọc nốt mục 6, 7, 8

Cho bộ từ vựng chuẩn (faithfulness, plausibility, knowledge limits) để đọc mọi bài sau đó.

**Kiến thức cần có trước:** [Tổng quan & Phân loại XAI](../xai/01-tong-quan.md)
**Đọc xong thì cập nhật vào:** [Đánh giá chất lượng lời giải thích](../xai/06-danh-gia.md)

### 2. TCAV — Kim et al., 2018

Tiền đề trực tiếp của CBM. Không đọc bài này thì không hiểu vì sao Koh et al. nghĩ ra tầng khái niệm. **Bắt buộc trích dẫn trong Related Work.**
→ [Interpretability Beyond Feature Attribution (TCAV)](https://arxiv.org/abs/1711.11279)

**Kiến thức cần có trước:** [Phương pháp dựa trên khái niệm (Concept-based)](../xai/03-concept-based.md) · khái niệm **CAV** trong [bảng Thuật ngữ](../glossary/all.md).

### 3. Promises and Pitfalls — Margeloiu et al., 2021

Bài đầu tiên **đo được concept leakage** một cách định lượng. Đọc sớm để mọi bài sau có chỗ bám.
→ [Promises and Pitfalls of Black-Box Concept Learning Models](https://arxiv.org/abs/2106.13314)

**Kiến thức cần có trước:** ba cách huấn luyện CBM (Independent / Sequential / Joint) — xem [CBM — Concept Bottleneck Models](../xai/04-cbm.md).

### 4. If Concept Bottlenecks are the Question... — 2026

Bài mới nhất và sắc nhất. Chứng minh hướng dùng VLM thay nhãn chuyên gia cho **nhãn đúng nhưng khái niệm sai**. Đọc ngay sau Margeloiu — hai bài nói cùng một bệnh ở hai thời điểm cách nhau 5 năm.
→ [If Concept Bottlenecks are the Question, are Foundation Models the Answer?](https://link.springer.com/article/10.1007/s10994-026-06999-y)

**Kiến thức cần có trước — quan trọng:** [CLIP & mô hình đa phương thức](../deep-learning/clip.md). Không nắm CLIP thì không đọc được bài này.

> **🛑 Mốc tự kiểm tra sau Đợt 1 — DỪNG LẠI tại đây.**
> Viết một đoạn ngắn dạng: *"CBM gặp vấn đề X. Các giải pháp hiện có là Y và Z. Chúng chưa giải quyết được W."*
> Nếu chưa viết được — **đừng đọc tiếp**, quay lại đọc kỹ hơn bài 3 và 4.

---

## Đợt 2 — Bản đồ toàn cảnh và các giải pháp đã có

**Mục tiêu:** biết ai đã thử gì, để không đề xuất lại thứ người ta làm rồi. **Ước tính 3–4 tuần.**

### 5. What's in the Bottle? (Survey) — TMLR 2026

Giờ mới đọc survey mới có ý nghĩa, vì đã có 4 bài làm mốc để định vị. **Nhảy thẳng tới taxonomy và open challenges.**
→ [What's in the Bottle? A Survey and Roadmap of Concept Bottleneck Models](https://arxiv.org/abs/2603.05629)

### 6. Rethinking CBM: From Pitfalls to Solutions — CVPR 2026

4 vấn đề nền tảng kèm giải pháp. Chú ý vấn đề *"nhiều CBM thực chất đi vòng qua tầng bottleneck"*.
→ [Rethinking Concept Bottleneck Models: From Pitfalls to Solutions](https://www.aimodels.fyi/papers/arxiv/rethinking-concept-bottleneck-models-pitfalls-solutions)

**Kiến thức cần có trước:** [Transformer & Vision Transformer (ViT)](../deep-learning/transformer-vit.md) — bài này phân tích tương tác giữa vision encoder và tập khái niệm.

### 7. Concept Embedding Models — Zarlenga et al., 2022

Giải pháp cho leakage: thay khái niệm vô hướng bằng **vector nhúng**.
→ [Concept Embedding Models](https://arxiv.org/abs/2209.09056)

**Kiến thức cần có trước:** khái niệm **[Latent Space](../deep-learning/latent-space.md)** và **Embedding**. Đây là chỗ kiến thức Autoencoder đã học nối vào đề tài CBM.

### 8. Label-free CBM — Oikarinen et al., 2023

**Đọc SAU bài 2026 chứ không trước.** Đọc sau thì tự nhìn ra chỗ yếu, thay vì bị thuyết phục rồi mới biết.
→ [Label-free Concept Bottleneck Models](https://arxiv.org/abs/2304.06129)

**Đọc xong cập nhật vào:** [Các biến thể & cải tiến của CBM](../xai/05-bien-the-cbm.md)

> **🛑 Mốc tự kiểm tra sau Đợt 2:** vẽ được một sơ đồ cây các nhánh CBM (gốc → CEM → Label-free → Post-hoc…) và chỉ ra được **mỗi nhánh vá điểm yếu nào**. Nếu vẽ được, bạn đã sẵn sàng viết phần Related Work.

---

## Đợt 3 — Chuẩn bị thực nghiệm và viết bài

**Đọc khi đã có câu hỏi nghiên cứu, không đọc trước.**

### 9. Measuring What Matters (Benchmark) — 2026

Công cụ đánh giá, dùng khi bắt đầu code. → [Measuring What Matters: Synthetic Benchmarks for Concept Bottleneck Models](https://arxiv.org/html/2606.04326)

**Kiến thức cần có trước:** [Bộ dữ liệu & Công cụ](../xai/07-du-lieu-cong-cu.md) · [Performance Measures](../ml-co-ban/performance-measures.md)

### 10. Post-hoc CBM — Yuksekgonul et al., 2023

Phương án dự phòng nếu thiếu GPU. → [Post-hoc Concept Bottleneck Models](https://arxiv.org/abs/2205.15480)

### 11. Sanity Checks for Saliency Maps — Adebayo et al., 2018

Dùng cho phần Mở đầu: biện minh vì sao chọn hướng intrinsic. → [Sanity Checks for Saliency Maps](https://arxiv.org/abs/1810.03292)

### 12. Grad-CAM — Selvaraju et al., 2017

Baseline so sánh trực quan. → [Grad-CAM: Visual Explanations from Deep Networks](https://arxiv.org/abs/1610.02391)

**Kiến thức cần có trước:** [CNN](../deep-learning/cnn.md) · [Các phương pháp hậu kỳ (Post-hoc)](../xai/02-post-hoc.md)

---

## Đọc thêm khi có thời gian

**13. β-VAE — Higgins et al., 2017** — chỉ ưu tiên nếu theo hướng disentanglement (dùng VAE sinh khái niệm không cần nhãn).
→ [β-VAE: Learning Basic Visual Concepts with a Constrained VAE](https://openreview.net/forum?id=Sy2fzU9gl)

**Kiến thức cần có trước:** [Variational Autoencoder (VAE)](../deep-learning/vae.md)

**14. Negative Results for SAE — DeepMind, 2025** — khác nhánh, đọc lấy bài học phương pháp luận.
→ [Negative Results for Sparse Autoencoders on Downstream Tasks](https://deepmindsafetyresearch.medium.com/negative-results-for-sparse-autoencoders-on-downstream-tasks-and-deprioritising-sae-research-6cadcfc125b9)

---

## Nhịp độ đọc — mỗi vòng cách nhau bao lâu, một ngày mấy bài?

### Có cần cách nhau 1 tuần không?

Keshav dẫn ý Andrew Simpson rằng phương pháp hiệu quả nhất khi **có khoảng cách dài giữa các vòng**. Nhưng cần phân biệt hai tình huống, vì lời khuyên đó viết cho **người bình duyệt đọc một lô bài**, không phải sinh viên đang học một lĩnh vực mới.

> **⏱️ Vòng 1 → Vòng 2 của CÙNG một bài: KHÔNG cần cách một tuần.**
> Với người đang học, làm liền trong ngày hoặc hôm sau là tốt nhất — ngữ cảnh còn tươi, không phải nạp lại từ đầu. Cách một tuần chỉ khiến bạn quên và phải đọc lại vòng 1.

> **📚 Khoảng cách phát huy tác dụng khi đọc theo LÔ (batch mode):**
> Làm vòng 1 cho **cả 4 bài của một đợt trong một buổi** → vài ngày tới 1 tuần sau mới làm vòng 2 lần lượt từng bài → vòng 3 để sau khi xong cả đợt.
> Lý do: sau khi đọc vòng 1 cả lô, bạn có bản đồ tổng thể; lúc làm vòng 2 sẽ hiểu mỗi bài trong tương quan với các bài khác — thứ mà đọc lẻ từng bài không có.

> **🧠 Vòng 3 THÌ NÊN cách xa.** Vòng này đòi hỏi kiến thức nền mà bạn chỉ có được sau khi đọc các bài khác. Làm vòng 3 quá sớm là lãng phí — bạn chưa đủ vốn để nhận ra giả định ngầm.

### Một ngày nên đọc mấy bài?

Khác nhau hoàn toàn tùy vòng:

| Vòng | Thời gian/bài | Số bài tối đa một buổi | Ghi chú |
|---|---|---|---|
| Vòng 1 | 5–10 phút | 3–5 bài (người mới) | Người quen tay làm được 8–10 |
| Vòng 2 | 45–60 phút | 1 bài/ngày | Hai bài vòng 2 trong một ngày thì bài sau sẽ hiểu rất kém |
| Vòng 3 | 4–5 giờ | 1 bài/tuần | Chỉ làm với 2–3 bài cốt lõi nhất của cả đề tài |

> **✅ Nhịp độ bền vững cho sinh viên còn đi học: 2–3 bài ở mức vòng 2 mỗi tuần.**
> Tức khoảng 10 bài/tháng — đủ để hoàn thành danh sách 14 bài trong khoảng 6 tuần. Đây là con số **bền**, quan trọng hơn con số cao.

### Ba lưu ý thực tế

**Bài đầu tiên luôn chậm gấp 2–3 lần.** Đọc tiếng Anh chuyên ngành, chưa quen thuật ngữ, chưa quen cấu trúc — hoàn toàn bình thường. **Đừng lấy tốc độ bài đầu để đánh giá bản thân.** Tới bài thứ năm bạn sẽ thấy nhanh hơn hẳn.

**Đọc đều đặn quan trọng hơn đọc nhiều.** Mỗi ngày 1 tiếng trong 5 ngày hiệu quả hơn nhiều so với dồn 5 tiếng vào cuối tuần. Kiến thức cần thời gian lắng.

**Không ghi chú thì coi như chưa đọc.** Sau 2 tuần bạn sẽ không nhớ gì. Ghi vào [Thư viện bài báo](../papers/index.md) ngay trong buổi đọc, đừng để hôm sau.

### Lịch mẫu một tuần

> **📅 Thứ 2:** vòng 1 cho 3–4 bài mới (1 tiếng) — quyết định bài nào đáng đọc tiếp.
> **Thứ 3, 4, 5:** mỗi ngày vòng 2 cho 1 bài (1 tiếng) + ghi chú ngay vào Notion (15 phút).
> **Thứ 6:** bổ sung thuật ngữ mới vào [Thuật ngữ Anh - Việt](../glossary/all.md), cập nhật nhật ký học tập.
> **Cuối tuần:** nghỉ, hoặc làm vòng 3 cho một bài cốt lõi nếu đang cần.

---

## Tìm bài báo — áp dụng mục 3 của Keshav

### Quy trình 3 bước của Keshav

**Bước 1.** Dùng Google Scholar hoặc Semantic Scholar với từ khóa chọn lọc để tìm **3–5 bài gần đây**. Làm **vòng 1** cho từng bài, rồi đọc phần **Related Work** của chúng — phần này thường tóm lược công trình gần đây và có thể chỉ tới một **survey**.

> **🎯 Nếu tìm được survey thì việc tìm kiếm KẾT THÚC** — chỉ cần đọc nó. Với đề tài CBM, bước này coi như đã xong (xem [What's in the Bottle?](https://arxiv.org/abs/2603.05629)).

**Bước 2.** Tìm các **trích dẫn lặp lại** và **tên tác giả xuất hiện nhiều lần** trong danh mục tham khảo — đó là **bài nền và nhà nghiên cứu chủ chốt**. Ghé trang web của họ xem công bố gần đây, từ đó biết **hội nghị hàng đầu** của lĩnh vực.

**Bước 3.** Vào trang các hội nghị đó, xem **kỷ yếu gần đây**. Làm **hai vòng** cho các bài tìm được. Nếu chúng cùng trích dẫn một bài nền mà bạn bỏ sót, tìm đọc rồi **lặp lại quy trình**.

### Cách săn bài survey

Trên Google Scholar hoặc arXiv, thêm các từ khóa này vào chủ đề của bạn:

`survey` · `review` · `systematic review` · `roadmap` · `taxonomy` · `a comprehensive study of` · `advances and challenges`

Ví dụ: `"concept bottleneck models" survey` hoặc `explainable AI taxonomy review`. Nhớ **lọc theo năm** (2024 trở lại đây) vì survey cũ hơn 2 năm trong lĩnh vực AI thường đã lạc hậu.

### Hội nghị và tạp chí uy tín cho đề tài của bạn

| Nhóm | Tên | Đặc điểm |
|---|---|---|
| Hội nghị ML hàng đầu | NeurIPS · ICML · ICLR | Nơi công bố CBM, CEM, Label-free CBM |
| Hội nghị thị giác máy tính | CVPR · ICCV · ECCV | Grad-CAM, Rethinking CBM đăng ở đây |
| Hội nghị AI tổng quát | AAAI · IJCAI | Uy tín, dễ vào hơn nhóm trên một chút |
| Chuyên về XAI / đạo đức AI | FAccT · AIES · xAI Conference | Rất hợp đề tài, cạnh tranh nhẹ hơn |
| Tạp chí | TPAMI · JMLR · TMLR · Machine Learning | TMLR và ML là nơi đăng 2 bài mới trong thư viện |
| Tạp chí liên ngành | Nature Machine Intelligence | Uy tín rất cao, nhiều bài XAI quan trọng |

> **⚠️ arXiv KHÔNG phải nơi công bố** — nó là kho tiền ấn (preprint), **chưa qua bình duyệt**. Không có nghĩa là sai, nhưng phải đọc hoài nghi hơn.
> **Luôn kiểm tra bài đó sau này có được đăng chính thức ở đâu không** bằng cách tra trên [dblp.org](http://dblp.org) hoặc **Semantic Scholar**. Khi trích dẫn, dùng bản chính thức nếu có.

### Công cụ nên dùng

**Google Scholar** — tìm kiếm rộng nhất, xem số trích dẫn, và quan trọng: nút **"Cited by"** để tìm các bài **mới hơn** đã trích dẫn bài này. Đây là cách đi xuôi dòng thời gian.

**Semantic Scholar** — tốt hơn Scholar ở chỗ có **Influential Citations** (lọc ra trích dẫn thực sự quan trọng, không phải trích dẫn cho có) và tóm tắt tự động.

**Connected Papers** — nhập một bài, nó vẽ **đồ thị các bài liên quan**. Cực kỳ hữu ích để nhìn thấy bản đồ một lĩnh vực trong 30 giây.

**Papers with Code** — tìm bài **kèm mã nguồn** và bảng xếp hạng trên từng benchmark. Dùng khi cần baseline để chạy lại.

[dblp.org](http://dblp.org) — tra cứu chính xác thông tin thư mục (venue, năm, trang) để trích dẫn đúng.

**OpenReview** — đọc được **cả phần bình duyệt** của ICLR, NeurIPS, TMLR. Đọc reviewer chê gì là cách nhanh nhất để học đọc phản biện.

### Cập nhật bài mới — đặt cảnh báo

**Google Scholar Alerts** — theo dõi từ khóa (`concept bottleneck model`) hoặc theo dõi một tác giả cụ thể. Có bài mới sẽ gửi email.

**arXiv** — đăng ký nhận danh sách hàng ngày của các mục `cs.LG` (Machine Learning), `cs.CV` (Computer Vision), `cs.AI`. Cảnh báo: rất nhiều bài mỗi ngày, chỉ đọc tiêu đề để lọc.

**Hugging Face Papers** — trang tuyển chọn bài nổi bật hàng ngày, đã lọc sẵn nên đỡ ngợp hơn arXiv.

**Theo dõi nhóm nghiên cứu** — tìm trang web hoặc Google Scholar của các tác giả chủ chốt (Koh, Kim, Zarlenga, Oikarinen với đề tài của bạn) và xem công bố mới của họ.

> **🚩 Dấu hiệu cần cảnh giác với một nguồn:** tạp chí không ai trong ngành nhắc tới; hứa hẹn xuất bản siêu nhanh có thu phí; không tìm thấy trên dblp; ban biên tập không có tên tuổi trong lĩnh vực. Khi nghi ngờ, kiểm tra xem **hội nghị/tạp chí đó có được xếp hạng trên CORE Ranking hoặc CSRankings** không, và hỏi giảng viên hướng dẫn.
