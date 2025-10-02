# UNG-DUNG-QUAN-LY-KHACH-HANG
Ứng dụng quản lý khách hàng được xây dựng với Python để tạo ra các hàm logic và xử lý data cùng Flask 3.0+ và hỗ trợ cả giao diện web và CLI.

## Tính năng chính

### Web Interface
- Dashboard tổng quan với thống kê KPI
- Quản lý danh sách khách hàng
- Xem chi tiết thông tin khách hàng
- API RESTful cho CRUD operations
- Export dữ liệu Excel
- Responsive design

### CLI Interface
- Thêm khách hàng mới
- Hiển thị danh sách khách hàng
- Tìm kiếm khách hàng
- Cập nhật thông tin khách hàng
- Xóa khách hàng

## Cài đặt

### Yêu cầu hệ thống
- Python 3.8+
- pip

### Cài đặt dependencies
```bash
pip install -r requirements.txt
```

### Cấu hình môi trường
1. Copy file cấu hình mẫu:
```bash
cp env.example .env
```

2. Chỉnh sửa file `.env` theo nhu cầu:
```env
FLASK_ENV=development
FLASK_DEBUG=True
FLASK_HOST=0.0.0.0
FLASK_PORT=5000
SECRET_KEY=your-secret-key-here
```

## Sử dụng

### Chạy Web Application
```bash
# Cách 1: Sử dụng biến môi trường
export RUN_WEB=1
python app.py

# Cách 2: Chạy trực tiếp web app
python web_app.py
```

Truy cập ứng dụng tại: http://localhost:5000

### Chạy CLI Application
```bash
python app.py
```

### API Endpoints

#### Khách hàng
- `GET /api/customers` - Lấy danh sách tất cả khách hàng
- `GET /api/customers/<code>` - Lấy thông tin khách hàng theo mã
- `POST /api/customers` - Tạo khách hàng mới
- `PUT /api/customers/<code>` - Cập nhật thông tin khách hàng
- `DELETE /api/customers/<code>` - Xóa khách hàng

#### Thống kê
- `GET /api/dashboard-stats` - Lấy thống kê KPI
- `GET /api/stats` - Lấy thống kê khách hàng

#### Utility
- `GET /api/health` - Health check
- `GET /api/export/customers` - Export danh sách khách hàng

### Ví dụ sử dụng API

#### Tạo khách hàng mới
```bash
curl -X POST http://localhost:5000/api/customers \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Nguyễn Văn A",
    "phone": "0123456789",
    "email": "nguyenvana@example.com",
    "address": "123 Đường ABC, Quận 1, TP.HCM"
  }'
```

#### Lấy danh sách khách hàng
```bash
curl http://localhost:5000/api/customers
```

## Cấu trúc dự án

```
UNG-DUNG-QUAN-LY-KHACH-HANG-main/
├── app_with_login.py          # Flask app chính với đăng nhập
├── app.py                     # App gốc (CLI)
├── login_system.py            # Hệ thống đăng nhập
├── run_app.py                 # Script chạy ứng dụng
├── create_sample_data.py      # Tạo dữ liệu mẫu
├── config.py                  # Cấu hình
├── defined.py                 # Định nghĩa functions
├── validators.py              # Validation
├── requirements.txt           # Dependencies
├── README_INTEGRATION.md      # Hướng dẫn tích hợp
├── LOGIN_SYSTEM_GUIDE.md      # Hướng dẫn login
├── ThongTinKhachHang.xlsx     # Dữ liệu khách hàng
├── userdatalogin.xlsx         # Dữ liệu user
├── templates/                 # Templates HTML
├── static/                    # CSS, JS, images
└── uploads/                   # Thư mục upload
```

## Production Deployment

### Sử dụng Gunicorn
```bash
gunicorn -w 4 -b 0.0.0.0:5000 web_app:app
```

### Sử dụng Passenger
Cấu hình Passenger để sử dụng `passenger_wsgi.py` làm entry point.

## Validation

Ứng dụng có hệ thống validation mạnh mẽ:
- Kiểm tra định dạng số điện thoại Việt Nam
- Kiểm tra định dạng email
- Kiểm tra tên khách hàng (hỗ trợ tiếng Việt)
- Sanitization dữ liệu đầu vào
- Giới hạn độ dài các trường

## Logging

Ứng dụng ghi log vào:
- Console (development)
- File `app.log` (production)
- File `web_app.log` (web app)
- File `passenger.log` (Passenger deployment)

## Các file chính

- app.py - File ứng dụng chính
- config.py - File cấu hình
- login-system.py - Hệ thống đăng nhập
- run_with_login.py - Chạy app với login
- web_app.py & web_app_with_login.py - Web applications
- validators.py - Validation logic
- requirements.txt - Dependencies
- app.log - Log file
- Thư mục static/ - CSS và assets
- Thư mục templates/ - HTML templates
- Thư mục uploads/ - Upload folder
- ThongTinKhachHang.xlsx & userdatalogin.xlsx - Data files
- __pycache__/ - Python cache

