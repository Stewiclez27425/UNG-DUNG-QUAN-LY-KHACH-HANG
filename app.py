from colorama import Fore, Back, init
import os
from openpyxl import Workbook, load_workbook

#Create Excel
wb=Workbook()
wb.active.title="KhachHang"
ws=wb.active

wb["A1"]="Mã KH"
wb["B1"]="Họ Tên"
wb["C1"]="Số ĐT"
wb["D1"]="Địa Chỉ"
wb["E1"]="Email"

if not os.path.exists("KhachHang.xlsx"):
    wb.save("KhachHang.xlsx")
def main():
    
    init(autoreset=False)
    print(Fore.YELLOW + Back.BLACK + "\n ----------QUẢN LÝ KHÁCH HÀNG----------")
    print("1. Thêm khách hàng")
    print("2. Hiển thị khách hàng")
    print("3. Tìm kiếm khách hàng")
    print("4. Cập nhật khách hàng")
    print("5. Xóa khách hàng")
    print("0. Thoát")
    print(Fore.CYAN + Back.BLACK)
    choice = input("Nhập lựa chọn của bạn: ")
    
    if choice == '1':
        pass
    elif choice == '2':
        pass
    elif choice == '3':
        pass
    elif choice == '4':
        pass
    elif choice == '5':
        pass
    elif choice == '0':
        print(Fore.WHITE + Back.BLACK + "Thoát chương trình.")
        exit()
    else: print(Fore.RED + Back.BLACK + "Lựa chọn không hợp lệ. Vui lòng thử lại!!!")
    
if __name__ == "__main__":
    while True:
        main()