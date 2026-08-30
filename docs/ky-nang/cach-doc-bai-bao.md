# Cách đọc một bài báo khoa học / báo cáo học thuật

> **⚡ Nguyên tắc quan trọng nhất:** không bao giờ đọc bài báo từ trên xuống dưới như đọc tiểu thuyết. Bài báo được **viết để tra cứu**, không phải để đọc tuyến tính. Phải đọc **nhiều vòng**, mỗi vòng sâu hơn.

---

## Phần 1 — Trước khi đọc

### 1.1. Xác định mục đích đọc

Trước khi mở file PDF, trả lời: **mình đọc bài này để làm gì?** Mỗi mục đích dẫn tới cách đọc khác nhau:

| Mục đích | Cách đọc | Thời gian |
|---|---|---|
| Khảo sát xem có liên quan không | Chỉ vòng 1 | 5–10 phút |
| Viết Related Work | Vòng 1 + 2 | 1 giờ |
| Tái hiện lại kết quả / làm baseline | Cả 3 vòng | 4–6 giờ trở lên |
| Tìm khe hở nghiên cứu | Vòng 2 + đọc kỹ phần Hạn chế | 2 giờ |

### 1.2. Kiểm tra độ tin cậy trước khi đầu tư thời gian

- **Venue (nơi công bố):** hội nghị hàng đầu về AI/CV gồm NeurIPS, ICML, ICLR, CVPR, ICCV, ECCV, AAAI. Bài đăng ở đây đã qua bình duyệt nghiêm ngặt.
- **arXiv là tiền ấn (preprint), CHƯA qua bình duyệt.** Không có nghĩa là sai, nhưng phải đọc với thái độ hoài nghi hơn. Luôn kiểm tra xem bài đó sau này có được đăng chính thức ở đâu không.
- **Số trích dẫn:** tra trên Google Scholar hoặc Semantic Scholar. Nhưng nhớ: bài mới ra 3 tháng thì ít trích dẫn là bình thường.
- **Nhóm tác giả:** họ có các bài khác cùng hướng không? Một nhóm theo đuổi một vấn đề nhiều năm thường đáng tin hơn.
- **Có code công khai không?** Có GitHub là dấu hiệu tốt về tính tái lập.

---

## Phần 2 — Phương pháp 3 vòng

Phương pháp chuẩn trong giới nghiên cứu, do S. Keshav đề xuất: **How to Read a Paper** (ACM SIGCOMM CCR, Vol. 37 No. 3, tháng 7/2007, tr. 83–84).

### Vòng 1 — Nhìn tổng thể (5–10 phút)

**Mục tiêu:** quyết định có đọc tiếp hay không.

Đọc theo đúng thứ tự này:

1. **Tiêu đề, tác giả, nơi công bố, năm**
2. **Abstract (tóm tắt)**
3. **Các tiêu đề mục** — lướt qua để nắm cấu trúc
4. **Hình và bảng** — đọc cả phần chú thích bên dưới
5. **Kết luận**
6. **Lướt danh mục tài liệu tham khảo** — đánh dấu bài nào mình đã đọc

> **✅ Tiêu chí dừng vòng 1 — Năm chữ C của Keshav:** (1) **Category** — bài thuộc loại gì? (2) **Context** — liên quan tới bài nào, dựa trên nền tảng lý thuyết nào? (3) **Correctness** — giả định có hợp lý không? (4) **Contributions** — đóng góp chính là gì? (5) **Clarity** — bài có được viết tốt không?

Sau vòng 1, **phần lớn bài báo sẽ bị loại** — đó là điều bình thường và cần thiết. Không ai đủ thời gian đọc kỹ mọi bài.

### Vòng 2 — Nắm nội dung (45–60 phút)

**Mục tiêu:** hiểu được bài báo làm gì và kết quả ra sao, **nhưng chưa cần hiểu chi tiết chứng minh**.

- Đọc kỹ phần thân bài nhưng **bỏ qua các chứng minh toán học chi tiết**.
- **Tập trung mạnh vào hình và bảng.** Kiểm tra: trục có nhãn đúng không? có thanh sai số không? kết quả có ý nghĩa thống kê không?
- **Ghi ra từ khóa lạ** nhưng **đừng dừng lại để tra ngay** — tra một lượt sau khi hết mục, kẻo mất mạch.
- **Đánh dấu tài liệu tham khảo cần đọc thêm.**

> **✅ Tiêu chí dừng vòng 2:** tóm tắt được bài báo cho người khác nghe, **kèm bằng chứng chính**. Nếu không làm được: hoặc bài quá khó (thiếu nền tảng, phải đi đọc bài nền trước), hoặc bài viết tệ, hoặc mình đang mệt.

### Vòng 3 — Tái dựng (4–5 giờ với người mới, ~1 giờ với người có kinh nghiệm)

**Mục tiêu:** hiểu sâu tới mức có thể **tự làm lại** công trình đó.

Chỉ làm vòng này với các bài **cốt lõi** của đề tài — không phải mọi bài.

Cách làm: **đọc với giả định rằng mình là người viết bài đó.** Tự tái tạo từng bước lập luận, tự dựng lại công thức, tự hỏi "nếu là mình thì mình làm khác chỗ nào". So sánh cách tái dựng của mình với của tác giả — **chỗ lệch nhau chính là chỗ họ có giả định ngầm** mà bài báo không nói ra.

---

## Phần 3 — Giải phẫu một bài báo

Từng phần có vai trò khác nhau, và **không phải phần nào cũng đáng tin như nhau**.

**Title & Abstract** — phiên bản "quảng cáo" của bài. Đọc để sàng lọc. **Thường bị thổi phồng** — đừng tin hoàn toàn.

**Introduction** — nêu vấn đề, động lực, và danh sách đóng góp. Đoạn cuối thường liệt kê rõ 3–4 đóng góp — **đây là đoạn đáng giá nhất để đọc nhanh**.

**Related Work** — bản đồ lĩnh vực. Với người mới, đây là **mỏ vàng** để tìm các bài nền cần đọc. Nhưng nhớ: tác giả luôn trình bày công trình trước theo hướng **làm nổi bật đóng góp của họ**.

**Method / Approach** — trái tim của bài. Đọc kỹ ở vòng 2 và 3.

**Experiments** — **phần cần đọc hoài nghi nhất.** Kiểm tra: baseline có công bằng không? có được tinh chỉnh kỹ như phương pháp mới không? chạy bao nhiêu seed? có độ lệch chuẩn không?

**Ablation Study** — chứng minh từng thành phần thực sự đóng góp. **Bài không có ablation là dấu hiệu đáng ngờ.**

**Limitations** — **phần quan trọng nhất với người đang tìm đề tài.** Đây là nơi tác giả tự chỉ ra khe hở. Rất nhiều đề tài sinh ra từ đoạn này.

**Conclusion & Future Work** — tác giả gợi ý hướng tiếp theo. Đọc kỹ, nhưng nhớ rằng họ thường đang tự làm những hướng đó rồi.

**References** — dùng để lần theo **citation trail**: bài nào được nhắc đi nhắc lại trong nhiều bài thì đó là bài nền bắt buộc phải đọc.

---

## Phần 4 — Báo cáo kỹ thuật và survey khác gì?

Không phải tài liệu học thuật nào cũng có cấu trúc IMRaD (Introduction – Method – Results – Discussion).

**Báo cáo kỹ thuật (technical report)** — ví dụ NIST IR 8312. Đặc điểm: **không có thực nghiệm, không đề xuất mô hình mới**, mục tiêu là **định khung khái niệm** hoặc đưa chuẩn. Cách đọc: tìm **các định nghĩa và phân loại**, đọc không theo thứ tự, bắt đầu từ mục cốt lõi nhất.

**Survey / Review** — tổng hợp toàn cảnh một lĩnh vực. Cách đọc: **đừng đọc tuần tự**. Đọc phần **taxonomy** để định vị những gì mình đã biết, rồi nhảy thẳng tới **open challenges / future directions**. Đó là nơi các khe hở nghiên cứu được liệt kê sẵn.

**Blog nghiên cứu (DeepMind, Anthropic, OpenAI)** — không qua bình duyệt nhưng thường rất mới và thẳng thắn. **Không dùng làm nguồn trích dẫn chính** trong bài báo, nhưng rất tốt để nắm xu hướng.

---

## Phần 5 — Đọc phản biện

> **🔍** Đây là phần phân biệt **"đã đọc"** với **"đã hiểu"**. Người mới thường đọc để tiếp thu; người làm nghiên cứu đọc để **tìm chỗ yếu**.

Bốn câu hỏi luôn đặt ra sau khi đọc:

**1. Giả định nào đang được ngầm chấp nhận?** Mọi phương pháp đều dựa trên giả định. Bài báo tốt nói ra; bài báo yếu giấu đi.

**2. Kết quả có đủ chứng minh cho kết luận không?** Thường gặp: kết luận rộng hơn nhiều so với phạm vi thực nghiệm.

**3. Baseline có công bằng không?** Kiểm tra baseline có được tinh chỉnh kỹ như phương pháp mới không. Đây là chỗ "gian lận hợp pháp" phổ biến nhất.

**4. Nếu mình là reviewer, mình sẽ hỏi gì?** Tập tư duy như người bình duyệt — đây là kỹ năng quan trọng nhất để sau này tự viết bài tốt.

---

## Phần 6 — Ghi chú khi đọc

> **✍️ Quy tắc vàng:** mọi ghi chú phải viết **bằng lời của mình**. Copy-paste abstract không phải là ghi chú — đó là sao chép. Nếu không diễn đạt lại được thì nghĩa là chưa hiểu.

**Phép thử thành thật nhất:** gấp tài liệu lại, tự nói thành lời nội dung vừa đọc. Nói không được tức là chưa hiểu — đọc lại.

**Một câu tóm tắt.** Sau mỗi bài, viết **đúng một câu**: bài này làm gì, bằng cách nào, kết quả ra sao. Không viết nổi câu này nghĩa là chưa thực sự nắm bài.

**Tách bạch lời tác giả và ý của mình.** Trong ghi chú, luôn đánh dấu rõ đâu là nội dung bài báo, đâu là suy nghĩ riêng. Sau 3 tháng bạn sẽ không nhớ nổi câu nào là của ai.

**Ghi số trang.** Khi viết bài cần trích dẫn chính xác, không phải mò lại cả bài.

**Lưu BibTeX ngay** lúc đọc, đừng để đến lúc viết bài.

---

## Phần 7 — Lỗi thường gặp của người mới

| Lỗi | Cách sửa |
|---|---|
| Đọc tuần tự từ trang 1 | Dùng phương pháp 3 vòng |
| Dừng lại tra từng thuật ngữ lạ | Ghi ra danh sách, tra một lượt sau khi hết mục |
| Cố hiểu 100% ngay lần đầu | Chấp nhận 60% ở bài đầu tiên; phần còn lại sẽ sáng ra khi đọc bài thứ hai, thứ ba |
| Bỏ qua hình và bảng | Hình và bảng chứa nhiều thông tin nhất trên mỗi đơn vị thời gian đọc |
| Tin hoàn toàn vào bài báo | Luôn hỏi: kết quả này đã được kiểm chứng độc lập chưa? |
| Đọc nhiều bài nhưng không ghi chú | Không ghi chú thì sau 2 tuần coi như chưa đọc |
| Bỏ qua phần Limitations | Đây là phần giá trị nhất để tìm đề tài |

---

## Phần 8 — Checklist sau khi đọc xong một bài

- [ ] Viết được tóm tắt 1 câu bằng lời của mình
- [ ] Nêu được vấn đề bài báo giải quyết
- [ ] Nêu được ý tưởng cốt lõi của phương pháp
- [ ] Biết dataset, baseline, metric được dùng
- [ ] Nêu được ít nhất 1 hạn chế của bài
- [ ] Biết bài này dùng được gì cho đề tài của mình
- [ ] Đã ghi các thuật ngữ mới vào bảng Thuật ngữ
- [ ] Đã đánh dấu các bài cần đọc tiếp
- [ ] Đã cập nhật Trạng thái trong Thư viện bài báo

---

## Nguồn tham khảo

- [S. Keshav — *How to Read a Paper* (ACM SIGCOMM CCR, 2007)](https://web.stanford.edu/class/ee384m/Handouts/HowtoReadPaper.pdf) — nguồn gốc của phương pháp 3 vòng, chỉ 3 trang, nên đọc bản gốc.
- [Andrew Ng — Advice on reading research papers (CS230, Stanford)](https://cs230.stanford.edu/) — hướng dẫn đọc nhiều bài cùng lúc để nắm một lĩnh vực mới.

---

> **🧭 Áp dụng vào đề tài cụ thể:** thứ tự các bài nên đọc, kiến thức nền cần có trước mỗi bài, nhịp độ đọc và cách tìm bài mới — xem [Lộ trình đọc bài báo & kiến thức nền](lo-trinh-doc.md).
