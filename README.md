# Phân loại ung thư vú từ ảnh X-quang bằng CNN

## Giới thiệu

Đây là cấu trúc khởi đầu cho dự án học máy phân loại bất thường liên quan đến
ung thư vú từ ảnh X-quang tuyến vú (mammogram) bằng mạng nơ-ron tích chập
(CNN).

Hiện tại repository **chưa có mã nguồn CNN, pipeline huấn luyện hoặc kết quả
thực nghiệm**. File `week1.py` được giữ nguyên như một bài tập Python độc lập
về precision, recall và F1-score.

> **Tuyên bố y tế:** Dự án này chỉ phục vụ mục đích học tập và nghiên cứu.
> Kết quả mô hình (khi được bổ sung) không phải là chẩn đoán y khoa, không
> thay thế bác sĩ hoặc quy trình khám chữa bệnh, và không được sử dụng để đưa
> ra quyết định chăm sóc người bệnh.

## Dữ liệu

- **Tên bộ dữ liệu:** `[ĐIỀN TÊN DATASET]`
- **Liên kết nguồn:** `[ĐIỀN LINK DATASET]`
- **Giấy phép sử dụng:** `[ĐIỀN THÔNG TIN LICENSE]`

Không đưa ảnh bệnh nhân, dữ liệu nhận dạng cá nhân hoặc dữ liệu y tế nhạy cảm
vào Git repository. Lưu dữ liệu cục bộ trong `data/raw/` và kiểm tra điều
khoản sử dụng của dataset trước khi tải hoặc chia sẻ.

## Cấu trúc dự kiến

```text
.
├── data/
│   ├── raw/              # Ảnh và nhãn gốc, không commit vào Git
│   └── processed/        # Dữ liệu sau tiền xử lý, không commit vào Git
├── models/               # Checkpoint và model đã huấn luyện, không commit
├── notebooks/            # Notebook khám phá và thử nghiệm
├── reports/              # Biểu đồ, bảng và báo cáo đánh giá
├── src/                  # Mã nguồn tiền xử lý, huấn luyện và đánh giá
├── tests/                # Kiểm thử
├── week1.py              # Bài tập precision/recall/F1 hiện có
├── requirements.txt      # Phụ thuộc Python của mã nguồn hiện tại
└── README.md
```

## Cài đặt

Yêu cầu Python `[ĐIỀN PHIÊN BẢN PYTHON]`.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

`requirements.txt` hiện chưa khai báo thư viện bên thứ ba vì mã nguồn đang
được theo dõi không có import bên thứ ba. Hãy cập nhật file này cùng với mã
CNN thực tế khi pipeline được triển khai.

## Huấn luyện

Pipeline huấn luyện chưa được triển khai. Sau khi bổ sung mã nguồn, cập nhật
lệnh dưới đây:

```powershell
python -m src.train --data-dir data/raw --output-dir models
```

## Đánh giá

Pipeline đánh giá chưa được triển khai. Sau khi bổ sung mã nguồn, cập nhật
lệnh dưới đây:

```powershell
python -m src.evaluate --data-dir data/processed --model models/[TEN_MODEL].pt
```

## Kết quả

- **Accuracy:**
- **Precision:**
- **Recall:**
- **F1-score:**
- **AUC:**
- **Ghi chú thí nghiệm:**

## Trạng thái dự án

- [ ] Chọn và ghi rõ dataset, nguồn và license
- [ ] Xây dựng pipeline tiền xử lý
- [ ] Triển khai CNN
- [ ] Huấn luyện và lưu cấu hình thí nghiệm
- [ ] Đánh giá trên tập kiểm tra độc lập
- [ ] Bổ sung phân tích giới hạn, sai lệch và khả năng tổng quát hóa
