# HỆ THỐNG QUẢN LÝ KHÁCH HÀNG VỚI ĐĂNG NHẬP

## 🎯 Mô tả
Hệ thống quản lý khách hàng tích hợp đầy đủ với hệ thống đăng nhập phân quyền, sử dụng Flask và Excel để lưu trữ dữ liệu.

## 🔧 Cài đặt

### 1. Cài đặt thư viện
```bash
pip install flask openpyxl pandas colorama
```

### 2. Tạo dữ liệu mẫu
```bash
python create_sample_data.py
```

### 3. Chạy ứng dụng
```bash
python run_app.py
```

## 🔐 Hệ thống đăng nhập

### Tài khoản mẫu:
- **Admin**: `admin` / `123456` - Quyền FULL (Toàn quyền)
- **Manager**: `manager` / `654321` - Quyền READ_WRITE (Đọc & Ghi)
- **Staff1**: `staff1` / `111111` - Quyền READ_ONLY (Chỉ đọc)
- **Staff2**: `staff2` / `222222` - Quyền READ_ONLY (Chỉ đọc)

### Phân quyền:
- **FULL**: Toàn quyền - Có thể thêm, sửa, xóa tất cả dữ liệu và quản lý user
- **READ_WRITE**: Đọc & Ghi - Có thể xem và chỉnh sửa dữ liệu khách hàng
- **READ_ONLY**: Chỉ đọc - Chỉ có thể xem dữ liệu

## 📊 Dữ liệu

### File Excel:
- `userdatalogin.xlsx`: Chứa thông tin người dùng và phân quyền
- `ThongTinKhachHang.xlsx`: Chứa thông tin khách hàng

### Cấu trúc dữ liệu User:
| Username | Password | FullName | Level | Permission | Status | CreatedDate |
|----------|----------|----------|-------|------------|--------|-------------|
| admin    | 123456   | Admin    | 1     | FULL       | ACTIVE | 01/01/2024  |

### Cấu trúc dữ liệu Khách hàng:
| Mã KH | Họ Tên | Số ĐT | Email | Địa Chỉ | Tổng tiền mua | Ngày cuối mua |
|-------|--------|-------|-------|---------|---------------|---------------|
| KH001 | Nguyễn Văn An | 0901234567 | an@email.com | 123 ABC | 15,500,000đ | 15/09/2024 |

## 🌐 Giao diện Web

### Các trang chính:
- `/login` - Trang đăng nhập
- `/dashboard` - Dashboard chính
- `/customers` - Danh sách khách hàng
- `/customer-dashboard` - Chi tiết khách hàng
- `/orders` - Quản lý đơn hàng
- `/products` - Quản lý sản phẩm
- `/reports` - Báo cáo (cần quyền READ_WRITE)
- `/statistics` - Thống kê
- `/admin` - Quản trị hệ thống (cần quyền FULL)

### API Endpoints:
- `GET /api/dashboard-stats` - Lấy thống kê dashboard
- `GET /api/user-info` - Thông tin user hiện tại
- `GET /api/customers` - Danh sách khách hàng
- `GET /api/customers/<code>` - Chi tiết khách hàng
- `POST /api/customers` - Thêm khách hàng mới
- `PUT /api/customers/<code>` - Cập nhật khách hàng
- `DELETE /api/customers/<code>` - Xóa khách hàng

## 🔄 Tích hợp

### Files chính:
- `app_with_login.py` - Flask app chính với tích hợp đăng nhập
- `login_system.py` - Hệ thống đăng nhập (copy từ login-system.py)
- `run_app.py` - Script chạy ứng dụng
- `create_sample_data.py` - Script tạo dữ liệu mẫu
- `test_login_integration.py` - Script test tích hợp

### Templates:
- `login.html` - Giao diện đăng nhập
- `index.html` - Dashboard chính
- `customer_list.html` - Danh sách khách hàng
- `customer_dashboard.html` - Chi tiết khách hàng
- Các template khác...

## 🧪 Testing

### Chạy test tích hợp:
```bash
python test_login_integration.py
```

### Test các chức năng:
1. **Login System**: Test xác thực và phân quyền
2. **Flask Routes**: Test các route và API
3. **Data Integration**: Test tích hợp dữ liệu Excel

## 🚀 Sử dụng

### 1. Khởi động hệ thống:
```bash
python run_app.py
```

### 2. Truy cập ứng dụng:
- Mở trình duyệt: http://localhost:5000
- Đăng nhập bằng tài khoản mẫu
- Khám phá các chức năng theo quyền hạn

### 3. Quản lý người dùng (Admin):
- Truy cập `/admin` để quản lý user
- Thêm, sửa, xóa tài khoản
- Phân quyền cho từng user

### 4. Quản lý khách hàng:
- Xem danh sách khách hàng
- Thêm khách hàng mới (cần quyền READ_WRITE)
- Cập nhật thông tin khách hàng
- Xóa khách hàng (cần quyền FULL)

## 📝 Ghi chú

### Bảo mật:
- Mật khẩu được lưu dạng plain text (chỉ dùng cho demo)
- Trong production nên mã hóa mật khẩu
- Sử dụng HTTPS cho production

### Mở rộng:
- Có thể thay Excel bằng database (MySQL, PostgreSQL)
- Thêm các chức năng quản lý đơn hàng, sản phẩm
- Tích hợp email, SMS notification
- Thêm dashboard analytics nâng cao

### Lỗi thường gặp:
- Thiếu thư viện: `pip install flask openpyxl pandas colorama`
- File Excel bị khóa: Đóng Excel trước khi chạy app
- Port 5000 bị chiếm: Thay đổi port trong code

## 🎉 Kết luận

Hệ thống đã tích hợp thành công:
- ✅ Login system với phân quyền
- ✅ Flask web application
- ✅ Excel data integration
- ✅ Responsive UI với Bootstrap
- ✅ API endpoints đầy đủ
- ✅ Error handling và logging

Hệ thống sẵn sàng sử dụng và có thể mở rộng thêm nhiều tính năng khác!
