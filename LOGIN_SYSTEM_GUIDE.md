# 📚 HƯỚNG DẪN SỬ DỤNG HỆ THỐNG ĐĂNG NHẬP ĐƠN GIẢN

## 📋 Mục lục
- [Giới thiệu](#-giới-thiệu)
- [Cài đặt](#-cài-đặt)
- [Cấu trúc hệ thống](#-cấu-trúc-hệ-thống)
- [Tài khoản mặc định](#-tài-khoản-mặc-định)
- [Hướng dẫn sử dụng](#-hướng-dẫn-sử-dụng)
- [API Functions](#-api-functions)
- [Ví dụ thực tế](#-ví-dụ-thực-tế)
- [Tích hợp với Flask](#-tích-hợp-với-flask)
- [Troubleshooting](#-troubleshooting)

---

## 🚀 Giới thiệu

Hệ thống đăng nhập đơn giản được thiết kế với các đặc điểm:
- ✅ **Dễ hiểu và sử dụng** - Code đơn giản, comment đầy đủ
- ✅ **Lưu trữ Excel** - Dữ liệu người dùng trong file `.xlsx`
- ✅ **Phân quyền linh hoạt** - 3 cấp độ quyền truy cập
- ✅ **Tích hợp Flask** - Decorators sẵn sàng cho web app

---

## 📦 Cài đặt

### 1. Cài đặt thư viện cần thiết
```bash
pip install openpyxl flask
```

### 2. Import hệ thống
```python
from login_system import *
```

### 3. Khởi tạo hệ thống
```python
# Tải dữ liệu người dùng
load_users()
```

---

## 🏗️ Cấu trúc hệ thống

### File dữ liệu: `userdatalogin.xlsx`
| Cột | Tên | Mô tả |
|-----|-----|-------|
| A | Username | Tên đăng nhập (duy nhất) |
| B | Password | Mật khẩu (plain text) |
| C | FullName | Họ tên đầy đủ |
| D | Level | Cấp bậc (1=Admin, 2=Manager, 3=Staff) |
| E | Permission | Quyền (FULL/READ_WRITE/READ_ONLY) |
| F | Status | Trạng thái (ACTIVE/INACTIVE) |
| G | CreatedDate | Ngày tạo tài khoản |

### Phân cấp quyền truy cập
```
FULL (1)        → Quyền đầy đủ (Admin)
READ_WRITE (2)  → Quyền đọc và ghi (Manager)  
READ_ONLY (3)   → Chỉ quyền đọc (Staff)
```

---

## 👤 Tài khoản mặc định

| Username | Password | Họ tên | Cấp bậc | Quyền | Trạng thái |
|----------|----------|---------|---------|-------|------------|
| `admin` | `123456` | Admin | 1 | FULL | ACTIVE |
| `manager` | `654321` | Manager | 2 | READ_WRITE | ACTIVE |
| `staff1` | `111111` | Staff1 | 3 | READ_ONLY | ACTIVE |
| `staff2` | `222222` | Staff2 | 3 | READ_ONLY | ACTIVE |
| `demo` | `demo123` | Demo User | 3 | READ_ONLY | INACTIVE |

---

## 📖 Hướng dẫn sử dụng

### 1. Khởi tạo hệ thống lần đầu
```python
# Import hệ thống
from login_system import *

# Tạo file dữ liệu (nếu chưa có)
create_userdata_file()

# Tải dữ liệu vào bộ nhớ
load_users()
```

### 2. Xác thực đăng nhập
```python
# Đăng nhập thành công
user_info = authenticate_user("admin", "123456")
if user_info:
    print(f"Chào mừng {user_info['FullName']}!")
    print(f"Quyền: {user_info['Permission']}")
else:
    print("Đăng nhập thất bại!")
```

### 3. Kiểm tra quyền truy cập
```python
# Kiểm tra quyền cụ thể
if check_permission("admin", "FULL"):
    print("Admin có quyền đầy đủ")

if check_permission("staff1", "READ_WRITE"):
    print("Staff có quyền ghi")  # Sẽ không in vì staff chỉ có READ_ONLY

# Kiểm tra cấp bậc
if check_user_level("manager", 2):
    print("Manager có cấp bậc đủ điều kiện")
```

### 4. Quản lý người dùng
```python
# Thêm người dùng mới
success = add_new_user(
    username="newuser",
    password="password123", 
    full_name="Nguyen Van New",
    level=3,
    permission="READ_ONLY"
)

if success:
    print("Tạo tài khoản thành công!")

# Hiển thị danh sách người dùng
print_all_users()
```

---

## 🔧 API Functions

### 📁 Quản lý file Excel
```python
create_userdata_file()          # Tạo file Excel với dữ liệu mẫu
load_users()                    # Tải dữ liệu từ Excel vào bộ nhớ  
save_users()                    # Lưu dữ liệu từ bộ nhớ vào Excel
```

### 🔐 Xác thực và đăng nhập
```python
authenticate_user(username, password)  # Xác thực đăng nhập
get_user_info(username)               # Lấy thông tin người dùng
is_user_active(username)              # Kiểm tra tài khoản có hoạt động
```

### 🛡️ Kiểm tra quyền truy cập
```python
check_permission(username, permission)  # Kiểm tra quyền cụ thể
check_user_level(username, min_level)   # Kiểm tra cấp bậc tối thiểu
```

### 👥 Quản lý người dùng
```python
add_new_user(username, password, full_name, level, permission)  # Thêm user mới
print_all_users()                                              # In danh sách users
get_user_by_id(user_id)                                        # Lấy user theo ID
```

### 🧪 Test và demo
```python
test_simple_login_system()  # Chạy test toàn bộ hệ thống
main()                      # Hàm main khởi động và demo
```

---

## 💡 Ví dụ thực tế

### Ví dụ 1: Hệ thống đăng nhập cơ bản
```python
from login_system import *

def login_example():
    # Khởi tạo hệ thống
    load_users()
    
    # Nhập thông tin đăng nhập
    username = input("Username: ")
    password = input("Password: ")
    
    # Xác thực
    user_info = authenticate_user(username, password)
    
    if user_info:
        print(f"✅ Đăng nhập thành công!")
        print(f"Chào mừng: {user_info['FullName']}")
        print(f"Cấp bậc: {user_info['Level']}")
        print(f"Quyền: {user_info['Permission']}")
        return user_info
    else:
        print("❌ Đăng nhập thất bại!")
        return None

# Sử dụng
user = login_example()
```

### Ví dụ 2: Kiểm tra quyền trước khi thực hiện hành động
```python
def delete_customer(username, customer_id):
    """Xóa khách hàng - chỉ Admin mới được phép"""
    
    # Kiểm tra quyền FULL
    if not check_permission(username, "FULL"):
        print("❌ Bạn không có quyền xóa khách hàng!")
        return False
    
    # Thực hiện xóa
    print(f"✅ Đã xóa khách hàng ID: {customer_id}")
    return True

def edit_customer(username, customer_id):
    """Sửa khách hàng - Manager trở lên mới được phép"""
    
    # Kiểm tra quyền READ_WRITE
    if not check_permission(username, "READ_WRITE"):
        print("❌ Bạn không có quyền sửa khách hàng!")
        return False
    
    # Thực hiện sửa
    print(f"✅ Đã sửa khách hàng ID: {customer_id}")
    return True

# Sử dụng
delete_customer("admin", "KH001")    # ✅ Thành công
delete_customer("staff1", "KH001")   # ❌ Không có quyền

edit_customer("manager", "KH002")    # ✅ Thành công  
edit_customer("staff1", "KH002")     # ❌ Không có quyền
```

### Ví dụ 3: Tạo tài khoản hàng loạt
```python
def create_multiple_users():
    """Tạo nhiều tài khoản cùng lúc"""
    
    new_users = [
        ("user1", "pass1", "Nguyen Van A", 3, "READ_ONLY"),
        ("user2", "pass2", "Tran Thi B", 2, "READ_WRITE"),
        ("user3", "pass3", "Le Van C", 3, "READ_ONLY"),
    ]
    
    success_count = 0
    for username, password, full_name, level, permission in new_users:
        if add_new_user(username, password, full_name, level, permission):
            success_count += 1
    
    print(f"✅ Đã tạo thành công {success_count}/{len(new_users)} tài khoản")

# Sử dụng
create_multiple_users()
```

---

## 🌐 Tích hợp với Flask

### 1. Sử dụng Decorators
```python
from flask import Flask, render_template, request, session, redirect, url_for
from login_system import *

app = Flask(__name__)
app.secret_key = 'your-secret-key'

# Khởi tạo hệ thống
load_users()

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user_info = authenticate_user(username, password)
        if user_info:
            session['username'] = username
            session['user_info'] = user_info
            return redirect(url_for('dashboard'))
        else:
            flash('Đăng nhập thất bại!', 'error')
    
    return render_template('login.html')

@app.route('/admin')
@require_permission('FULL')
def admin_page():
    """Trang admin - chỉ user có quyền FULL mới truy cập được"""
    return render_template('admin.html')

@app.route('/manager')  
@require_level(2)
def manager_page():
    """Trang manager - chỉ cấp bậc 2 trở lên mới truy cập được"""
    return render_template('manager.html')

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    user_info = session.get('user_info')
    return render_template('dashboard.html', user=user_info)
```

### 2. Middleware kiểm tra quyền
```python
def check_access_permission(required_permission):
    """Middleware kiểm tra quyền truy cập"""
    
    if 'username' not in session:
        return False, "Chưa đăng nhập"
    
    username = session['username']
    
    if not is_user_active(username):
        return False, "Tài khoản bị khóa"
    
    if not check_permission(username, required_permission):
        return False, "Không có quyền truy cập"
    
    return True, "OK"

# Sử dụng trong route
@app.route('/delete_customer/<customer_id>')
def delete_customer_route(customer_id):
    has_access, message = check_access_permission('FULL')
    
    if not has_access:
        flash(message, 'error')
        return redirect(url_for('dashboard'))
    
    # Thực hiện xóa khách hàng
    return f"Đã xóa khách hàng {customer_id}"
```

---

## 🔧 Troubleshooting

### ❓ Lỗi thường gặp

#### 1. ImportError: No module named 'openpyxl'
```bash
# Giải pháp: Cài đặt thư viện
pip install openpyxl flask
```

#### 2. File Excel không tồn tại
```python
# Hệ thống sẽ tự động tạo file, hoặc tạo thủ công:
create_userdata_file()
```

#### 3. Không thể đăng nhập
```python
# Kiểm tra tài khoản có hoạt động không
print(is_user_active("username"))

# Kiểm tra thông tin user
user_info = get_user_info("username") 
print(user_info)
```

#### 4. Quyền truy cập bị từ chối
```python
# Kiểm tra quyền hiện tại của user
user_info = get_user_info("username")
print(f"Quyền hiện tại: {user_info['Permission']}")
print(f"Cấp bậc: {user_info['Level']}")

# Kiểm tra quyền cụ thể
print(check_permission("username", "FULL"))
```

### 🛠️ Debug và kiểm tra

#### 1. Hiển thị tất cả users
```python
print_all_users()
```

#### 2. Test toàn bộ hệ thống
```python
test_simple_login_system()
```

#### 3. Kiểm tra cấu trúc dữ liệu
```python
# Xem dữ liệu trong bộ nhớ
print("Dữ liệu users:", users_data)

# Xem cấu hình quyền
print("Cấp độ quyền:", PERMISSION_LEVELS)
```

---

## 📝 Lưu ý quan trọng

### 🔒 Bảo mật
- ⚠️ **Mật khẩu lưu dạng plain text** - Trong production nên mã hóa
- ⚠️ **File Excel không được mã hóa** - Cần bảo vệ file dữ liệu
- ✅ **Sử dụng HTTPS** khi deploy web application

### 🚀 Performance  
- ✅ **Dữ liệu load vào RAM** - Truy cập nhanh
- ⚠️ **Phù hợp với < 1000 users** - Với nhiều user hơn nên dùng database
- ✅ **Tự động save khi thay đổi** - Đảm bảo dữ liệu không mất

### 🔄 Backup và Recovery
```python
# Backup file dữ liệu
import shutil
shutil.copy('userdatalogin.xlsx', 'backup_userdatalogin.xlsx')

# Restore từ backup
shutil.copy('backup_userdatalogin.xlsx', 'userdatalogin.xlsx')
load_users()  # Tải lại dữ liệu
```

---

## 📞 Hỗ trợ

Nếu gặp vấn đề, hãy:
1. 📖 Đọc lại hướng dẫn này
2. 🧪 Chạy `test_simple_login_system()` để kiểm tra
3. 🔍 Kiểm tra file `userdatalogin.xlsx` có tồn tại không
4. 📋 Xem log lỗi để debug

---

**🎉 Chúc bạn sử dụng hệ thống thành công!**
