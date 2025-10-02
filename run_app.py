#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script chạy ứng dụng web với hệ thống đăng nhập tích hợp
"""

import os
import sys
from pathlib import Path

# Thêm thư mục hiện tại vào Python path
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

def main():
    """Chạy ứng dụng web với hệ thống đăng nhập"""
    print("🚀 KHỞI ĐỘNG HỆ THỐNG QUẢN LÝ KHÁCH HÀNG VỚI ĐĂNG NHẬP")
    print("=" * 60)
    
    try:
        # Import và chạy ứng dụng
        from app_with_login import app, init_login_system
        
        # Khởi tạo hệ thống đăng nhập
        print("🔧 Khởi tạo hệ thống đăng nhập...")
        if not init_login_system():
            print("❌ Không thể khởi tạo hệ thống đăng nhập!")
            return
        
        print("✅ Hệ thống đăng nhập đã sẵn sàng!")
        print("\n📋 THÔNG TIN TÀI KHOẢN MẪU:")
        print("   👤 admin/123456 - Quyền FULL (Admin)")
        print("   👤 manager/654321 - Quyền READ_WRITE (Manager)")
        print("   👤 staff1/111111 - Quyền READ_ONLY (Staff)")
        print("   👤 staff2/222222 - Quyền READ_ONLY (Staff)")
        
        print("\n🌐 Ứng dụng đang chạy tại: http://localhost:5000")
        print("🔐 Trang đăng nhập: http://localhost:5000/login")
        print("\nNhấn Ctrl+C để dừng ứng dụng")
        print("=" * 60)
        
        # Chạy ứng dụng
        app.run(
            debug=True,
            host='0.0.0.0',
            port=5000
        )
        
    except ImportError as e:
        print(f"❌ Lỗi import: {e}")
        print("📦 Vui lòng cài đặt các thư viện cần thiết:")
        print("   pip install flask openpyxl pandas colorama")
        
    except KeyboardInterrupt:
        print("\n\n👋 Tạm biệt! Ứng dụng đã được dừng.")
        
    except Exception as e:
        print(f"❌ Lỗi không mong muốn: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
