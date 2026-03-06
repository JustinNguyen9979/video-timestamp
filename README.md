# Video Timestamp Inserter 🎥⏱️

Công cụ Python đơn giản giúp chèn dòng thời gian (Timestamp) chạy thực tế vào video. Rất hữu ích cho các video giám sát, hành trình hoặc ghi chép sự kiện cần mốc thời gian chính xác.

## ✨ Tính năng
- Chèn ngày/giờ vào video với hiệu ứng chữ có bóng (shadow) để dễ đọc trên mọi nền.
- Cho phép chọn mốc thời gian bắt đầu tùy ý.
- Tự động tăng thời gian theo từng giây tương ứng với tiến trình video.
- Giữ nguyên chất lượng video gốc (sử dụng codec H.264).

## 🛠 Yêu cầu hệ thống
Máy của anh cần cài đặt Python và một số thư viện sau:
- `moviepy`: Xử lý video.
- `Pillow` (PIL): Vẽ chữ và xử lý hình ảnh.
- `numpy`: Hỗ trợ mảng dữ liệu.

Cài đặt nhanh bằng lệnh:
```bash
pip install moviepy Pillow numpy
```

## 🚀 Cách sử dụng

1. **Chạy script:**
   Mở Terminal/Command Prompt và chạy lệnh:
   ```bash
   python timestamp.py
   ```

2. **Nhập File Video:**
   Khi chương trình hỏi `📂 Kéo thả file video vào đây`, anh chỉ cần kéo file video từ thư mục vào cửa sổ Terminal rồi nhấn **Enter**.

3. **Nhập thời gian bắt đầu:**
   Nhập ngày giờ theo định dạng: `Ngày/Tháng/Năm Giờ:Phút:Giây`.
   *Ví dụ:* `06/03/2026 14:30:00`

4. **Chờ xử lý:**
   Chương trình sẽ tiến hành ghép thời gian vào video. Sau khi chạy xong, file mới sẽ có tên dạng `[tên_gốc]_timestamp.mp4` nằm cùng thư mục với file gốc.

---

