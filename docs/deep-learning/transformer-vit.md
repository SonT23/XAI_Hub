# Transformer & Vision Transformer (ViT)

> 🎯 **Vì sao phải học phần này cho đề tài XAI/CBM?** Bài báo CBM gốc (2020) dùng Inception-v3 — kiến trúc từ 2015. Nhưng **mọi bài CBM từ 2023 trở đi đều dựa trên ViT/CLIP**. Không nắm phần này thì không đọc được các bài mới nhất, cũng không làm được hướng label-free CBM.

> 🧭 **Cách đọc trang này:** Trang được viết lại theo hướng "không cần biết gì về AI trước cũng đọc hiểu được". Mỗi thuật ngữ học thuật mới (in **đậm** khi xuất hiện lần đầu) đều được giải thích bằng ví dụ đời thường **trước khi** đưa công thức toán. Nếu một đoạn có vẻ khó, hãy đọc phần ví dụ trước, bỏ qua công thức, rồi quay lại sau. Phần 0 bên dưới là kiến thức nền — nếu bạn thấy quen thuộc rồi thì bấm mở nhanh để kiểm tra lại, hoặc lướt thẳng xuống Phần 1.

### Phần 0 — Kiến thức nền cần có trước khi đọc (dành cho người mới hoàn toàn)

Transformer được xây trên một vài khái niệm Deep Learning cơ bản. Nếu bạn đã đọc [Cẩm nang Deep Learning: Nền tảng Neural Network](cam-nang-deep-learning-nen-tang-neural-network.md) thì có thể bỏ qua phần này. Nếu chưa, hãy mở từng mục dưới đây (bấm vào tam giác nhỏ để mở rộng) — mỗi mục chỉ mất 1–2 phút đọc.

<details markdown="1">
<summary>🔢 Vector là gì?</summary>

Vector đơn giản là **một dãy số có thứ tự**, ví dụ (2, 5, -1, 0.7). Trong AI, người ta dùng vector để "mã hoá" mọi thứ thành số — vì máy tính chỉ hiểu số, không hiểu chữ hay hình ảnh trực tiếp.

Ví dụ: một từ như "mèo" có thể được biểu diễn bằng một vector gồm vài trăm con số, ví dụ (0.12, -0.45, 0.88, ...). Những con số này không có ý nghĩa riêng lẻ, nhưng **khoảng cách và hướng** giữa các vector phản ánh mức độ liên quan về ý nghĩa: vector của "mèo" sẽ gần vector của "chó" hơn là gần vector của "máy bay".

Số lượng con số trong một vector gọi là **chiều** (dimension). Vector 3 số là vector 3 chiều, vector 768 số là vector 768 chiều — không thể vẽ ra giấy được nhưng máy tính xử lý bình thường.

</details>

<details markdown="1">
<summary>📐 Ma trận và phép nhân ma trận là gì?</summary>

Ma trận là một **bảng số** (nhiều hàng, nhiều cột) — có thể hình dung như một bảng Excel chỉ chứa số. Một vector thực chất là một ma trận có 1 hàng (hoặc 1 cột).

**Phép nhân ma trận** là cách toán học để "trộn" hoặc "biến đổi" các con số trong một vector/ma trận theo một quy tắc cố định. Trong Deep Learning, hầu hết các phép biến đổi (biến vector này thành vector khác) đều được thực hiện bằng cách nhân với một ma trận — ma trận đó chính là phần **kiến thức đã học được** của mô hình. Bạn không cần biết cách tính tay phép nhân ma trận để hiểu Transformer — chỉ cần biết: "nhân với một ma trận" = "chiếu/biến đổi vector này sang một không gian số khác, theo một công thức mô hình tự học được".

</details>

<details markdown="1">
<summary>🧠 Mạng nơ-ron nhân tạo (Neural Network), trọng số (weight), và việc "học"</summary>

Một mạng nơ-ron là một chuỗi các phép biến đổi số (chủ yếu là nhân ma trận, như ở trên) xếp nối tiếp nhau, xen giữa là các bước "phi tuyến" giúp mô hình học được các quy luật phức tạp chứ không chỉ quan hệ đường thẳng đơn giản.

Các con số bên trong những ma trận đó gọi là **trọng số** (weight) hoặc **tham số** (parameter) — đây chính là phần mô hình "học" được. Ban đầu các trọng số này là số ngẫu nhiên (mô hình chưa biết gì); qua quá trình **huấn luyện** (training) — cho mô hình xem rất nhiều ví dụ, so sánh dự đoán của nó với đáp án đúng, rồi chỉnh dần các trọng số theo hướng làm dự đoán đúng hơn (kỹ thuật này gọi là **gradient descent**, tạm hiểu là "dò từng bước nhỏ theo hướng giảm sai số") — các trọng số dần hội tụ về những giá trị giúp mô hình dự đoán tốt.

Một mô hình Transformer cỡ vừa có thể có **hàng trăm triệu** trọng số như vậy. Xem chi tiết đầy đủ hơn (perceptron, activation function, backpropagation, loss function) tại [Cẩm nang Deep Learning: Nền tảng Neural Network](cam-nang-deep-learning-nen-tang-neural-network.md).

</details>

<details markdown="1">
<summary>🔤 Token và Embedding</summary>

**Token** là một đơn vị nhỏ mà mô hình xử lý — với văn bản, một token có thể là một từ, một phần của từ, hoặc một ký tự (tuỳ cách chia). Câu "Con mèo ngồi" có thể bị chia thành 3 token: "Con", "mèo", "ngồi".

Nhưng mô hình không thể xử lý trực tiếp chữ "mèo" — nó cần một vector số. **Embedding** là bước biến mỗi token thành một vector (xem lại mục Vector ở trên). Bảng tra cứu này (token → vector) cũng là một phần được học trong quá trình huấn luyện, không phải quy tắc cố định.

</details>

<details markdown="1">
<summary>🎲 Xác suất và hàm Softmax</summary>

Nhiều bài toán AI cần mô hình đưa ra "mức độ tự tin" thay vì khẳng định chắc chắn — ví dụ "80% khả năng đây là ảnh con mèo, 15% là con chó, 5% là con khác". Đây là một **phân phối xác suất**: các con số đều nằm giữa 0 và 1, và cộng lại đúng bằng 1 (bằng 100%).

**Softmax** là một công thức toán học biến một dãy điểm số bất kỳ (có thể âm, có thể rất lớn) thành một phân phối xác suất hợp lệ như vậy — điểm số càng cao thì xác suất sau khi qua softmax càng lớn, nhưng luôn đảm bảo tổng bằng 1. Softmax được dùng liên tục trong Transformer, đặc biệt ở cơ chế attention (Phần 4).

</details>

<details markdown="1">
<summary>📉 Gradient, huấn luyện, và vì sao mô hình "học sâu" cần nhiều lớp</summary>

**Gradient** là một khái niệm từ giải tích, đại khái là "hướng và độ dốc thay đổi" — gradient của sai số theo một trọng số cho biết: nếu tăng trọng số đó một chút, sai số sẽ tăng hay giảm, và tăng/giảm nhanh cỡ nào. Quá trình huấn luyện dùng thông tin gradient để chỉnh từng trọng số theo hướng làm giảm sai số — gọi là **gradient descent**. Việc tính gradient cho hàng triệu trọng số cùng lúc, lan truyền từ đầu ra ngược trở lại đầu vào, gọi là **backpropagation** (lan truyền ngược).

Một vấn đề thường gặp: khi mạng có rất nhiều lớp xếp chồng, gradient có thể bị "teo nhỏ dần" khi lan truyền qua nhiều lớp (gọi là **vanishing gradient**) khiến các lớp đầu gần như không học được gì. Đây là một trong những vấn đề mà thiết kế của Transformer (cụ thể là **residual connection**, Phần 9) giải quyết.

</details>

---

## Phần A — Transformer (kiến trúc gốc, dùng cho văn bản)

### Phần 1: Bối cảnh và động lực ra đời Transformer

Trước năm 2017, các mô hình xử lý chuỗi (dịch máy, sinh văn bản...) chủ yếu dựa trên hai họ kiến trúc:

- **RNN / LSTM / GRU** (Recurrent Neural Network — mạng nơ-ron hồi quy): đọc dữ liệu **tuần tự từng phần tử một**, giống như đọc một câu từng chữ một và ghi nhớ dần trong đầu. Cách đọc này gây ra hai vấn đề: (1) không thể đọc song song — muốn hiểu từ thứ 10 thì bắt buộc phải xử lý xong 9 từ trước, khiến việc huấn luyện rất chậm; (2) thông tin từ những từ ở đầu câu dần "phai nhạt" khi mô hình đọc đến cuối câu dài (chính là hệ quả của vanishing gradient nhắc ở Phần 0), nên các câu dài, các mối liên hệ ở xa nhau rất khó nắm bắt.

- **CNN** (Convolutional Neural Network — mạng tích chập, vốn nổi tiếng với ảnh) áp dụng cho chuỗi: mỗi "lớp lọc" chỉ nhìn được một cửa sổ nhỏ xung quanh mỗi vị trí. Muốn liên kết hai từ ở cách xa nhau trong câu, phải xếp chồng rất nhiều lớp lọc để "vùng nhìn" mở rộng dần ra — tốn kém và vẫn gián tiếp.

Bài báo **"Attention Is All You Need"** (Vaswani và cộng sự, 2017) đề xuất **Transformer**: bỏ hẳn cách đọc tuần tự (recurrence) và cách nhìn cục bộ theo cửa sổ (convolution), thay bằng một cơ chế duy nhất gọi là **attention** ("phép chú ý" — sẽ giải thích cặn kẽ ở Phần 4), cho phép **mọi từ trong câu nhìn thấy và trao đổi thông tin trực tiếp với mọi từ khác, chỉ trong một bước tính toán duy nhất**, bất kể chúng cách nhau bao xa trong câu.

Điều này mang lại hai lợi ích cốt lõi:

1. **Song song hoá:** vì không phải chờ xử lý xong từ trước mới đến từ sau, toàn bộ câu được xử lý cùng lúc trên GPU — huấn luyện nhanh hơn rất nhiều so với RNN.

2. **Nắm bắt quan hệ xa tốt hơn:** vì mọi cặp từ đều có "đường nối trực tiếp", thông tin không bị phai nhạt dần như trong RNN.

> 💡 Ghi nhớ ngắn gọn: RNN đọc tuần tự (chậm, dễ quên xa); CNN nhìn cục bộ (phải chồng nhiều lớp mới nhìn xa); Transformer cho mọi từ nhìn thấy nhau ngay lập tức (nhanh, nhìn xa tốt) — đánh đổi là chi phí tính toán tăng theo bình phương độ dài câu (giải thích ở Phần 11).

### Phần 2: Kiến trúc tổng quan — Encoder và Decoder

Hãy hình dung một **phiên dịch viên** đang dịch một câu tiếng Việt sang tiếng Anh. Người này làm hai việc tách biệt: (1) đọc và **hiểu trọn vẹn** câu tiếng Việt trước, (2) rồi mới bắt đầu **nói ra** từng từ tiếng Anh, mỗi từ dựa trên cả câu gốc đã hiểu lẫn những từ tiếng Anh mình vừa nói ra trước đó. Transformer nguyên bản mô phỏng đúng hai vai trò này bằng hai khối:

- **Encoder** ("bộ mã hoá" — vai trò "hiểu"): nhận câu đầu vào, xử lý qua N lớp giống hệt nhau xếp chồng (bản gốc N=6), biến nó thành một tập hợp vector chứa đầy đủ ngữ cảnh — tạm hiểu là "bản tóm tắt số hoá" của toàn câu, mỗi từ một vector nhưng vector đó đã "biết" về các từ xung quanh.

- **Decoder** ("bộ giải mã" — vai trò "nói ra"): cũng N lớp xếp chồng, sinh ra từng từ đầu ra một, mỗi lần sinh một từ mới nó vừa nhìn vào kết quả của Encoder (câu gốc đã hiểu), vừa nhìn vào những từ nó đã tự sinh ra trước đó trong cùng câu trả lời.

Mỗi lớp Encoder gồm 2 khối con: **Multi-Head Self-Attention** (Phần 4–5) và **Feed-Forward Network** (Phần 8), mỗi khối con đều bọc bởi **residual connection** và **Layer Normalization** (Phần 9).

Mỗi lớp Decoder gồm 3 khối con: **Masked Multi-Head Self-Attention** (Phần 6, chỉ được nhìn các từ đã sinh trước đó), **Cross-Attention** (Phần 7, nhìn sang Encoder), và **Feed-Forward Network**.

> 📌 Nhiều mô hình nổi tiếng sau này chỉ dùng **một nửa** kiến trúc này: BERT chỉ dùng Encoder (phù hợp để "hiểu" văn bản — phân loại, tìm kiếm ngữ nghĩa); GPT chỉ dùng Decoder (phù hợp để "sinh" văn bản nối tiếp). **ViT** mà Phần B sẽ trình bày cũng chỉ dùng phần Encoder, vì bài toán phân loại ảnh chỉ cần "hiểu", không cần "sinh ra chuỗi".

### Phần 3: Input Embedding và Positional Encoding

#### 3.1. Input Embedding — biến từ thành vector

Đây chính là bước **Embedding** đã nhắc ở Phần 0: mỗi token (từ/subword) được tra trong một bảng đã học để lấy ra vector đại diện của nó, có số chiều cố định (bản gốc là 512 chiều, gọi là $d_{model}$).

#### 3.2. Vì sao cần thêm thông tin vị trí?

Đây là điểm rất phản trực giác của attention: bản thân phép tính attention (Phần 4) **không quan tâm thứ tự** các từ đưa vào — nếu bạn xáo trộn thứ tự các từ trong câu, kết quả tính toán của attention cũng chỉ xáo trộn tương ứng, bản thân phép toán không "biết" từ nào đứng trước từ nào. Điều này khác hẳn RNN (đọc tuần tự nên tự nhiên có thứ tự) hay CNN (có vị trí không gian cố định). Nhưng thứ tự từ rất quan trọng với ý nghĩa câu: "Con mèo đuổi con chuột" khác hẳn "Con chuột đuổi con mèo" dù dùng đúng những từ giống nhau. Vì vậy Transformer phải **chủ động cộng thêm thông tin vị trí** vào mỗi vector embedding.

#### 3.3. Positional Encoding — mã hoá vị trí

Bản gốc dùng một công thức cố định (không cần học) dựa trên hàm sin và cos:

$$PE(pos, 2i) = \sin\left(\frac{pos}{10000^{2i/d_{model}}}\right), \qquad PE(pos, 2i+1) = \cos\left(\frac{pos}{10000^{2i/d_{model}}}\right)$$

Trong đó $pos$ là vị trí của từ trong câu (từ đầu tiên, thứ hai, ...), $i$ là chỉ số một chiều trong vector. Bạn không cần nhớ công thức này — điều quan trọng cần hiểu là **ý tưởng**: mỗi chiều của vector vị trí dao động theo một "nhịp" (tần số) khác nhau, giống như kim giờ, kim phút, kim giây trên đồng hồ cùng quay nhưng với tốc độ khác nhau — tổ hợp các "kim" này tạo ra một dấu hiệu **duy nhất** cho mỗi vị trí, mà mô hình học được cách đọc dấu hiệu đó.

Vector vị trí này được **cộng trực tiếp** vào vector embedding của từ ở bước 3.1, để ra vector đầu vào cuối cùng cho Encoder.

> 📌 Các mô hình hiện đại hơn (BERT, GPT, và cả ViT ở Phần B) thường dùng **learned positional embedding**: thay vì công thức sin/cos cố định, dùng một bảng vector vị trí được học cùng lúc với toàn bộ mô hình — đơn giản hơn, nhưng phải nhìn thấy đủ nhiều mẫu ở mỗi vị trí trong lúc huấn luyện.

### Phần 4: Cơ chế Self-Attention — trái tim của Transformer

#### 4.1. Trực giác: tra cứu trong thư viện

Hãy hình dung việc tra cứu thông tin trong thư viện:

- **Query (Q, "câu hỏi/truy vấn"):** điều bạn đang muốn tìm — ví dụ "tôi cần tài liệu về loài chim".

- **Key (K, "khoá/nhãn"):** nhãn dán trên gáy mỗi cuốn sách, cho biết cuốn đó nói về gì.

- **Value (V, "giá trị/nội dung"):** nội dung thật sự bên trong mỗi cuốn sách.

Bạn so Query của mình với Key của từng cuốn sách để xem cuốn nào liên quan; cuốn càng liên quan thì bạn càng đọc kỹ nội dung (Value) của nó, cuốn không liên quan thì gần như bỏ qua. Kết quả cuối cùng là một bản tổng hợp thông tin, có trọng số theo mức độ liên quan.

Self-attention làm đúng việc này cho **mỗi từ trong câu**: mỗi từ tạo ra 3 vector Query, Key, Value của riêng nó (bằng cách nhân vector embedding của từ đó với 3 ma trận trọng số đã học, gọi là $W^Q, W^K, W^V$ — xem lại "phép nhân ma trận" ở Phần 0). Sau đó, Query của một từ được so với Key của **tất cả** các từ trong câu (kể cả chính nó), để quyết định nên "chú ý" bao nhiêu vào từng từ khi tổng hợp thông tin.

Gọi là "self" (tự) vì Query, Key, Value đều được tạo ra từ **cùng một câu** — mỗi từ vừa là người đi hỏi (Query) vừa là nguồn thông tin cho từ khác (Key/Value).

#### 4.2. Công thức: Scaled Dot-Product Attention

$$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$

Đọc từng bước:

1. $QK^T$: tính **độ tương đồng** giữa Query của mỗi từ với Key của mọi từ khác, bằng **tích vô hướng** (dot product — một phép tính nhân từng cặp số rồi cộng lại, cho ra một con số duy nhất thể hiện "hai vector giống hướng nhau đến đâu"). Hai vector càng "cùng hướng" thì tích vô hướng càng lớn, tức càng liên quan.

2. Chia cho $\sqrt{d_k}$ ($d_k$ là số chiều của vector Key): đây là một bước ổn định kỹ thuật thuần tuý — nếu không chia, khi $d_k$ lớn thì các điểm số dot-product có thể rất lớn, đẩy hàm softmax ở bước sau vào vùng gần như "tất cả hoặc không có gì", làm gradient (Phần 0) gần như bằng 0 và mô hình khó học tiếp.

3. **Softmax** (đã giải thích ở Phần 0): biến các điểm số thành một phân phối xác suất — gọi là **trọng số attention** — cho biết mỗi từ khác nên được "chú ý" bao nhiêu phần trăm.

4. Nhân với $V$: lấy **tổng có trọng số** của các vector Value theo đúng tỷ lệ vừa tính — từ nào có trọng số cao thì đóng góp nhiều vào kết quả, từ nào trọng số gần 0 thì gần như bị bỏ qua.

Kết quả: mỗi từ nhận về một vector biểu diễn **mới**, đã "hỏi ý kiến" toàn bộ câu và tổng hợp đúng phần thông tin liên quan đến nó.

> 🐱 **Ví dụ cụ thể:** Trong câu "Con mèo ngồi trên thảm vì nó mệt", để hiểu từ "nó" ám chỉ ai, self-attention cho phép Query của từ "nó" so trực tiếp với Key của mọi từ khác trong câu — kể cả từ "mèo" đứng cách đó khá xa — và gán trọng số attention cao cho "mèo", nhờ vậy vector kết quả của "nó" mang theo phần lớn thông tin của "mèo".

### Phần 5: Multi-Head Attention — nhiều "góc nhìn" chú ý song song

#### Vấn đề của một "đầu" attention duy nhất

Nếu chỉ dùng một phép attention duy nhất, mỗi từ chỉ nhận được **một** phân phối chú ý (một bộ trọng số) cho mỗi lượt tính. Nhưng một từ thường cần chú ý tới nhiều loại quan hệ khác nhau **cùng lúc**: quan hệ chủ ngữ – vị ngữ, quan hệ đồng tham chiếu ("nó" ám chỉ ai), quan hệ nguyên nhân – kết quả... Ép tất cả các loại quan hệ này vào một phân phối attention duy nhất sẽ làm chúng hoà trộn và làm mờ lẫn nhau.

#### Giải pháp: chia thành nhiều "đầu" (head)

Multi-Head Attention chạy **nhiều phép self-attention độc lập song song** (bản gốc dùng $h=8$ đầu), mỗi đầu có bộ ma trận $W^Q, W^K, W^V$ riêng và làm việc trên một không gian nhỏ hơn ($d_{model}/h$ chiều thay vì toàn bộ $d_{model}$ chiều). Vì mỗi đầu khởi tạo và học riêng biệt, chúng tự nhiên "phân công" nhau học các loại quan hệ khác nhau — giống như việc dùng nhiều bộ lọc khác nhau trong một lớp của mạng CNN, mỗi bộ lọc bắt một đặc điểm riêng.

$$\text{MultiHead}(Q,K,V) = \text{Concat}(\text{head}_1, ..., \text{head}_h)\,W^O, \qquad \text{head}_i = \text{Attention}(QW_i^Q, KW_i^K, VW_i^V)$$

Sau khi mỗi đầu ra kết quả riêng, các kết quả được **ghép nối** (concatenate — nối các vector lại thành một vector dài hơn) rồi nhân với một ma trận $W^O$ để đưa về đúng số chiều $d_{model}$ ban đầu, sẵn sàng cho bước tiếp theo.

### Phần 6: Masked Self-Attention — chỉ dùng trong Decoder

Decoder sinh ra câu trả lời **từng từ một, theo thứ tự** (giống người phiên dịch nói từng từ). Tại thời điểm sinh từ thứ 5, mô hình chỉ được phép biết 4 từ đã sinh ra trước đó — tuyệt đối không được "nhìn trộm" các từ thứ 6, 7... vì thực tế lúc suy luận, những từ đó còn chưa tồn tại.

Nhưng trong lúc **huấn luyện**, để tăng tốc, người ta vẫn đưa cả câu đúng (đáp án) vào cùng lúc và tính song song (kỹ thuật này gọi là **teacher forcing**, xem thêm Phần 10). Để làm được vậy mà không "gian lận", Masked Self-Attention che (mask) toàn bộ các vị trí ở tương lai: trước khi tính softmax, điểm số ứng với các từ chưa được phép nhìn thấy bị gán bằng $-\infty$, khiến sau softmax trọng số của chúng bằng đúng 0. Cơ chế này gọi là **causal mask** ("mặt nạ nhân quả").

### Phần 7: Cross-Attention — nơi Decoder "nhìn sang" Encoder

Ở khối con thứ hai của mỗi lớp Decoder, Query được lấy từ chính Decoder (những gì nó đã sinh ra), còn Key và Value được lấy từ **đầu ra cuối cùng của Encoder** (câu gốc đã được "hiểu" đầy đủ). Nhờ vậy, tại mỗi bước sinh từ, Decoder có thể "tra cứu" xem nên dựa vào phần nào của câu gốc — ví dụ khi dịch, để sinh ra đúng từ tiếng Anh tiếp theo, mô hình cần biết nên nhìn vào từ nào ở câu tiếng Việt gốc.

### Phần 8: Feed-Forward Network (FFN)

Sau khối attention, mỗi từ đã có một vector mới chứa thông tin ngữ cảnh (đã "hỏi han" các từ khác). Nhưng bản thân attention chỉ là các phép **tổng có trọng số** — về mặt toán học đây vẫn là phép biến đổi khá "thẳng" (tuyến tính). FFN bổ sung khả năng xử lý phi tuyến (non-linear — nghĩa là các quy luật phức tạp, không chỉ đơn giản là cộng trừ tỉ lệ) mà một mạng nơ-ron thực sự cần để học được các quy luật phức tạp (xem lại Phần 0, mục "Mạng nơ-ron").

$$\text{FFN}(x) = \max(0, xW_1+b_1)\,W_2 + b_2$$

FFN là 2 lớp fully-connected (mỗi neuron output nối với tất cả neuron input, một dạng mạng nơ-ron cơ bản nhất) với một hàm phi tuyến (ReLU, tức $\max(0,x)$ — hoặc GELU trong các mô hình mới hơn) ở giữa, thường có lớp ẩn ở giữa **rộng gấp 4 lần** so với $d_{model}$. Điểm quan trọng: FFN được áp dụng **độc lập cho từng từ** — không có sự trao đổi thông tin giữa các từ ở bước này (khác hẳn attention, nơi các từ trao đổi thông tin với nhau).

> 💡 Ghi nhớ ngắn gọn: **Attention = trộn thông tin giữa các từ** (theo chiều ngang, qua lại giữa các vị trí); **FFN = xử lý/tinh chỉnh thông tin trong từng từ** (theo chiều dọc, độc lập từng vị trí). Một lớp Transformer luôn xen kẽ hai kiểu xử lý này.

### Phần 9: Residual Connection và Layer Normalization

#### Residual Connection — "đường tắt" giữ thông tin gốc

Thay vì để một khối (attention hoặc FFN) hoàn toàn thay thế đầu vào của nó, Transformer **cộng thêm đầu vào gốc** vào kết quả:

$$\text{output} = x + \text{Sublayer}(x)$$

Nghĩa là khối con chỉ cần học phần "nên thêm/bớt gì" so với đầu vào, thay vì phải học lại từ đầu toàn bộ phép biến đổi. Lợi ích quan trọng nhất nằm ở việc huấn luyện: nhờ có "đường tắt" $x$ đi thẳng qua phép cộng, gradient (Phần 0) khi lan truyền ngược qua rất nhiều lớp không bị teo nhỏ dần (không bị vanishing gradient) — đây là kỹ thuật vay mượn trực tiếp từ mạng ResNet nổi tiếng trong xử lý ảnh, và là lý do Transformer có thể xếp chồng hàng chục, hàng trăm lớp mà vẫn huấn luyện ổn định.

#### Layer Normalization — giữ các con số trong tầm kiểm soát

Khi dữ liệu đi qua rất nhiều lớp tính toán liên tiếp, các con số có thể dần "phình to" hoặc "co nhỏ" một cách mất kiểm soát, khiến việc huấn luyện không ổn định. **Layer Normalization** giải quyết việc này bằng cách, với mỗi từ, tính trung bình và độ phân tán (variance) của toàn bộ các con số trong vector của chính từ đó, rồi co giãn lại sao cho trung bình về 0 và độ phân tán về 1 — sau đó nhân/cộng thêm hai tham số học được ($\gamma, \beta$) để mô hình có thể khôi phục lại độ lớn phù hợp nếu cần:

$$\text{LayerNorm}(x) = \gamma \cdot \frac{x-\mu}{\sqrt{\sigma^2+\epsilon}} + \beta$$

Điểm khác biệt với **Batch Normalization** (kỹ thuật chuẩn hoá phổ biến trong CNN): Batch Norm tính trung bình/độ phân tán trên nhiều mẫu khác nhau trong cùng một lô (batch) huấn luyện, còn Layer Norm tính trên chính các con số của **một** vector — không phụ thuộc vào các mẫu khác hay độ dài câu, nên phù hợp tự nhiên hơn với dữ liệu chuỗi có độ dài thay đổi.

Kết hợp lại, một khối con hoàn chỉnh trong Transformer hiện đại (kiểu Pre-LN, dùng trong GPT, ViT) trông như sau:

```javascript
x = x + MultiHeadAttention(LayerNorm(x))
x = x + FFN(LayerNorm(x))
```

### Phần 10: Một vài chi tiết khi huấn luyện

- **Teacher forcing:** khi huấn luyện Decoder, thay vì bắt mô hình tự sinh từng từ một (rất chậm), người ta đưa thẳng câu đáp án đúng vào làm đầu vào, kết hợp với Masked Self-Attention (Phần 6) để vẫn tôn trọng tính "không nhìn trộm tương lai" — nhờ vậy cả câu được xử lý song song trong một lượt.

- **Label smoothing:** thay vì bắt mô hình dự đoán "100% chắc chắn" cho từ đúng, người ta phân phối một phần xác suất rất nhỏ (ví dụ 10%) cho các từ khác, giúp mô hình bớt "tự tin thái quá" và tổng quát hoá tốt hơn trên dữ liệu mới.

- **Warm-up learning rate:** learning rate ($\eta$ trong Phần 0, mục Gradient — tốc độ điều chỉnh trọng số mỗi bước) được tăng dần trong giai đoạn đầu huấn luyện rồi mới giảm dần, giúp mô hình không "vọt" quá đà khi các trọng số còn ngẫu nhiên và chưa ổn định.

- **Dropout:** ngẫu nhiên "tắt" một số kết nối trong lúc huấn luyện (xem thêm trong trang Nền tảng Neural Network, mục Regularization) để giảm hiện tượng học vẹt dữ liệu huấn luyện (overfitting).

### Phần 11: Vì sao Transformer "tốn" tính toán khi câu dài?

Với một câu có $n$ từ và vector $d$ chiều: bước self-attention cần tính độ tương đồng giữa **mọi cặp từ**, tức khoảng $n \times n$ phép so sánh — chi phí tính toán và bộ nhớ tăng theo **bình phương** độ dài câu ($O(n^2)$). Bù lại, số bước phải làm **tuần tự** (không song song hoá được) chỉ là 1 bước duy nhất — đây chính là điểm mạnh cốt lõi so với RNN (vốn cần $n$ bước tuần tự). Khi $n$ rất lớn (văn bản dài, hoặc — như sẽ thấy ở Phần B — rất nhiều mảnh ảnh nhỏ), chi phí $O(n^2)$ trở thành nút thắt cổ chai, và là động lực cho nhiều biến thể attention "tiết kiệm" hơn (không nằm trong phạm vi trang này).

---

## Phần B — Từ Transformer đến Vision Transformer (ViT)

### Phần 12: Vì sao phải "chế biến" lại Transformer cho ảnh?

Transformer nguyên bản sinh ra để xử lý **chuỗi rời rạc** (câu = dãy từ). Ảnh là dữ liệu dạng **lưới 2 chiều liên tục** (mỗi điểm ảnh — pixel — là một hoặc vài con số thể hiện màu sắc, các pixel xếp thành hàng và cột). Một ảnh 224×224 điểm ảnh (kích thước phổ biến) có hơn 150.000 điểm ảnh. Nếu áp dụng self-attention (Phần 4) trực tiếp lên **từng pixel**, chi phí $O(n^2)$ (Phần 11) với $n \approx 150.000$ sẽ là một con số khổng lồ, hoàn toàn không thể tính nổi trên phần cứng hiện tại.

Bài báo **"An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale"** (Dosovitskiy và cộng sự, 2020 — gọi tắt là **ViT**) đưa ra một giải pháp rất trực tiếp, đúng như tên bài báo: chia ảnh thành các mảnh vuông nhỏ gọi là **patch** (ví dụ mỗi patch 16×16 pixel), và coi **mỗi patch như một "từ"** — từ đó có thể tái sử dụng gần như nguyên vẹn kiến trúc Transformer Encoder (Phần 2) vốn được thiết kế cho chuỗi từ.

### Phần 13: Kiến trúc ViT — từng bước

#### 13.1. Patch Embedding — biến ảnh thành "câu"

1. Ảnh đầu vào (ví dụ 224×224 pixel, 3 kênh màu Đỏ-Xanh lá-Xanh dương) được cắt thành các ô vuông nhỏ **không chồng lấp** kích thước 16×16, tạo ra $N = (224 \times 224)/(16 \times 16) = 196$ patch (mảnh).

2. Mỗi patch (16×16×3 = 768 con số) được "trải phẳng" thành một vector 1 chiều dài 768 số.

3. Vector này được nhân với một ma trận trọng số đã học (một phép nhân ma trận đơn giản như ở Phần 0) để chiếu sang vector có số chiều $D$ mong muốn (ví dụ D=768 cho phiên bản ViT-Base) — đây chính là bước **Patch Embedding**, tương đương với Input Embedding ở Phần 3.1 nhưng cho ảnh thay vì cho từ.

Kết quả: ảnh ban đầu (một lưới pixel) đã biến thành một **chuỗi gồm 196 vector**, đúng định dạng mà Transformer Encoder (Phần 2) đã quen xử lý.

#### 13.2. CLS Token — một "token đại diện" đặc biệt

Giống mô hình BERT, ViT thêm vào đầu chuỗi 196 patch một token đặc biệt gọi là **[CLS] token** ("class token" — token phân loại), không tương ứng với bất kỳ patch ảnh thật nào, mà là một vector học được, dùng làm "vùng chứa" tổng hợp. Qua các lớp self-attention (nơi mọi vị trí nhìn thấy mọi vị trí khác — Phần 4), token này dần "hấp thụ" thông tin từ toàn bộ 196 patch. Ở đầu ra cuối cùng, chỉ riêng vector của [CLS] token được lấy ra làm **đại diện cho toàn bộ ảnh**, đưa vào một lớp phân loại nhỏ để dự đoán nhãn (ví dụ "đây là ảnh con mèo").

#### 13.3. Positional Embedding cho ảnh

Giống lý do đã nêu ở Phần 3.2, self-attention không tự biết patch nào nằm ở đâu trong ảnh — ViT cộng thêm một vector vị trí học được (**learned positional embedding**, xem Phần 3.3) vào mỗi patch (và cả [CLS] token), để mô hình biết được cấu trúc không gian 2 chiều của ảnh gốc.

> 📌 Điều thú vị: bài báo ViT thử cả cách mã hoá vị trí phức tạp hơn (tách riêng toạ độ hàng và cột) nhưng thấy không tốt hơn đáng kể so với cách đơn giản này — cho thấy mô hình có thể tự học được cấu trúc 2 chiều từ dữ liệu, không cần ép buộc bằng kiến trúc.

#### 13.4. Transformer Encoder — lõi xử lý, giống hệt Phần A

Chuỗi gồm [CLS] + 196 patch (đã cộng vị trí) được đưa qua $L$ lớp Transformer Encoder — **đúng những gì đã trình bày ở Phần 2–9**: Multi-Head Self-Attention + Feed-Forward Network, mỗi khối có residual connection + Layer Normalization. Không có Decoder, không có mask, không có cross-attention — vì phân loại ảnh chỉ cần "hiểu" (Encoder), không cần "sinh chuỗi" (Decoder).

| Phiên bản | Số lớp (L) | Số chiều ẩn (D) | Số đầu attention | Số tham số |
| --- | --- | --- | --- | --- |
| ViT-Base | 12 | 768 | 12 | ~86 triệu |
| ViT-Large | 24 | 1024 | 16 | ~307 triệu |
| ViT-Huge | 32 | 1280 | 16 | ~632 triệu |

#### 13.5. MLP Head — lớp phân loại cuối

Vector [CLS] ở đầu ra lớp Encoder cuối cùng được đưa qua một mạng nhỏ (1–2 lớp fully-connected, xem Phần 0) để cho ra phân phối xác suất (qua Softmax, Phần 0) trên các nhãn cần phân loại.

### Phần 14: Inductive Bias — khác biệt cốt lõi giữa CNN và ViT

**Inductive bias** ("thiên kiến quy nạp") là một thuật ngữ nghe có vẻ khó nhưng ý tưởng đơn giản: đó là những **giả định có sẵn** được cài cứng vào kiến trúc mô hình, giúp nó học nhanh hơn khi giả định đó đúng với dữ liệu thực tế — đổi lại, mô hình sẽ bị "bó buộc" theo giả định đó dù đôi khi không cần thiết.

CNN có 2 giả định mạnh, cài cứng sẵn:

- **Tính cục bộ (locality):** mỗi neuron chỉ nhìn một vùng nhỏ xung quanh nó — hợp lý vì các pixel gần nhau trong ảnh thường liên quan chặt (cùng thuộc một cạnh, một hoạ tiết).

- **Bất biến khi dịch chuyển (translation equivariance):** cùng một bộ lọc được quét qua toàn ảnh, nên nếu vật thể dịch chuyển vị trí, đặc trưng nhận diện dịch chuyển theo tương ứng — mô hình không phải học lại từ đầu cho mỗi vị trí.

ViT gần như **không có** hai giả định này: ngay từ lớp đầu tiên, self-attention đã cho mọi patch nhìn thấy mọi patch khác trên toàn ảnh (toàn cục, không cục bộ), và không có cơ chế chia sẻ trọng số theo không gian như convolution. Thông tin không gian duy nhất mà ViT có là positional embedding học được.

**Hệ quả trực tiếp:** vì thiếu sẵn các giả định hữu ích này, ViT phải **tự học từ đầu**, bằng dữ liệu, những quy luật không gian mà CNN đã có sẵn trong kiến trúc — nên ViT cần một lượng dữ liệu huấn luyện **rất lớn** mới phát huy được sức mạnh. Trong bài báo gốc: huấn luyện trên ImageNet (khoảng 1,3 triệu ảnh — quy mô "vừa" trong ngành) thì ViT cho kết quả **kém hơn** ResNet (một kiến trúc CNN) cùng cỡ. Nhưng khi huấn luyện trước (pre-train) trên tập dữ liệu khổng lồ hơn nhiều (JFT-300M, 300 triệu ảnh), ViT lại **vượt trội** so với các CNN tốt nhất thời điểm đó. Nói cách khác: ViT mở rộng (scale) tốt hơn theo dữ liệu và tính toán, nhưng kém hiệu quả hơn CNN khi dữ liệu ít.

| Tiêu chí | CNN | ViT |
| --- | --- | --- |
| Phạm vi nhìn | Cục bộ, mở rộng dần theo độ sâu | Toàn cục ngay từ lớp đầu tiên |
| Inductive bias | Mạnh (tính cục bộ, bất biến tịnh tiến) | Yếu — phải tự học từ dữ liệu |
| Nhu cầu dữ liệu | Huấn luyện tốt với dữ liệu vừa | Cần dữ liệu rất lớn hoặc pre-training |
| Khả năng giải thích | Grad-CAM trên feature map | Attention map theo patch |

Đây cũng là động lực cho các nghiên cứu tiếp theo như **DeiT** (Data-efficient Image Transformer, 2021) — dùng kỹ thuật "học từ một mô hình thầy" (knowledge distillation) để huấn luyện ViT hiệu quả hơn chỉ với ImageNet, hay **Swin Transformer** — đưa lại tính cục bộ vào attention (chỉ tính attention trong từng cửa sổ nhỏ, dịch chuyển cửa sổ dần qua các lớp) để vừa giảm chi phí tính toán vừa cải thiện hiệu quả dữ liệu.

### Phần 15: So sánh trực tiếp Transformer (văn bản) và ViT

| Khía cạnh | Transformer gốc (văn bản) | ViT (ảnh) |
| --- | --- | --- |
| Đơn vị token | Từ / mảnh từ (subword) | Patch ảnh (ví dụ 16×16 pixel) |
| Bước tạo token | Tra bảng embedding | Trải phẳng patch rồi nhân ma trận (linear projection) |
| Mã hoá vị trí | Sin/cos cố định (bản gốc) | Learned embedding (học được) |
| Kiến trúc dùng | Encoder + Decoder | Chỉ Encoder |
| Token đặc biệt | Tuỳ tác vụ | [CLS] token để phân loại |
| Đầu ra | Chuỗi từ (sinh văn bản) | Một vector phân loại (từ [CLS]) |

### Phần 16: Tóm tắt toàn bộ luồng dữ liệu trong ViT

1. Ảnh → cắt thành N patch → trải phẳng → nhân ma trận (linear projection) → N vector.

2. Thêm [CLS] token vào đầu chuỗi.

3. Cộng thêm vector vị trí (positional embedding) vào từng vector.

4. Đưa qua L lớp Transformer Encoder (Multi-Head Self-Attention + FFN, có residual + Layer Norm).

5. Lấy riêng vector [CLS] ở đầu ra cuối cùng.

6. Đưa qua MLP Head → phân phối xác suất các nhãn.

> 💡 **Liên hệ với XAI:** Attention map của ViT (bản đồ trọng số attention chiếu lên các patch) trông rất giống một lời giải thích trực quan cho quyết định của mô hình, nhưng cộng đồng nghiên cứu đã chỉ ra **"Attention is not Explanation"** — trọng số attention cao không chứng minh được rằng đặc trưng đó thực sự quyết định đầu ra. Đây là một lập luận ủng hộ hướng đi intrinsic-interpretable (như CBM) thay vì chỉ dựa vào việc "đọc" attention.

---

### Nguồn học

#### Bài báo gốc

- [Attention Is All You Need – Vaswani et al., 2017](https://arxiv.org/abs/1706.03762) — bài khai sinh Transformer.

- [An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale – Dosovitskiy et al., 2020](https://arxiv.org/abs/2010.11929) — bài ViT gốc.

- [Attention is not Explanation – Jain & Wallace, 2019](https://arxiv.org/abs/1902.10186) — quan trọng cho phần lập luận XAI.

#### Giải thích trực quan (nên đọc trước bài báo gốc)

- [The Illustrated Transformer – Jay Alammar](https://jalammar.github.io/illustrated-transformer/) — tài liệu trực quan nổi tiếng nhất, giải thích Q/K/V bằng hình vẽ từng bước.

- [3Blue1Brown – Visualizing Attention (video)](https://www.youtube.com/watch?v=eMlx5fFNoYc) — giải thích toán học của attention bằng hình ảnh động.

- [Lil'Log – The Transformer Family](https://lilianweng.github.io/posts/2023-01-27-the-transformer-family-v2/) — tổng hợp hệ thống, chất lượng học thuật cao.

#### Thực hành và code

- [The Annotated Transformer – Harvard NLP](https://nlp.seas.harvard.edu/annotated-transformer/) — cài đặt Transformer từng dòng bằng PyTorch song song với bài báo.

- [Hugging Face – Transformers Course](https://huggingface.co/learn/nlp-course) — khoá miễn phí, thực hành trực tiếp.

- [timm – PyTorch Image Models](https://github.com/huggingface/pytorch-image-models) — thư viện chứa mọi biến thể ViT pre-trained, dùng được ngay làm backbone.

#### Bài giảng đại học

- [CS231n – Stanford (có phần Attention & Transformers)](https://cs231n.github.io/)

- [CS25: Transformers United – Stanford](https://web.stanford.edu/class/cs25/) — khoá chuyên sâu riêng về Transformer, có video công khai.
