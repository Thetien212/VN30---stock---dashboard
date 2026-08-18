# VN30---stock---dashboard
Ứng dụng web thời gian thực hiển thị thông tin chi tiết và biểu đồ giá cho các cổ phiếu thuộc nhóm VN30, được xây dựng bằng Python và Streamlit.

## 🚀 Tính năng nổi bật
- **Hộp chọn linh hoạt**: Dễ dàng chuyển đổi qua lại giữa 30 mã cổ phiếu trong rổ VN30.
- **Bố cục 2 cột khoa học**: 
  - Cột trái: Hiển thị trọn vẹn Tên đầy đủ doanh nghiệp, Giá mở cửa, Giá đóng cửa, Khối lượng giao dịch (Volume) và tỷ lệ % thay đổi theo màu sắc xanh/đỏ trực quan.
  - Cột phải: Biểu đồ trực quan hóa biến động giá trong 1 tháng gần nhất.
- **Xử lý dữ liệu thông minh**: Tự động lọc bỏ các giá trị trống (`NaN`) trong khung giờ trước giờ giao dịch để đảm bảo số liệu luôn chính xác.

## 🛠️ Công nghệ sử dụng
- **Python** (Ngôn ngữ lập trình chính)
- **Streamlit** (Xây dựng giao diện Web Dashboard)
- **YFinance** (Kéo dữ liệu tài chính trực tiếp từ Yahoo Finance)
- **Pandas** (Xử lý, lọc và tính toán số liệu)
