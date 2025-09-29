from colorama import Fore, Back, init
import os
from openpyxl import Workbook, load_workbook
import pandas as pd
from pathlib import Path
import time

def is_data_none():
    wb=load_workbook(filename="ThongTinKhachHang.xlsx")
    sheet=wb.active
    
    for row in sheet.iter_rows(min_row=2, max_row=2, min_col=1, values_only=True):
        if all(cell is None for cell in row):
            return True
        else:
            return False
        
def is_recycle_bin():
    file_path = Path("Recycle Bin\ThongTinKhachHang.xlsx")
    if file_path.exists() and file_path.is_file():
        return True

def check_file():
    if is_recycle_bin() == True: #False
        return False
    elif os.path.exists("ThongTinKhachHang.xlsx") == False:
        return False
    elif os.path.exists("ThongTinKhachHang.xlsx") and is_data_none() == True:
        return False
    else:
        return True
        

def show_customer_information():
    # Load excel file
    wb=load_workbook(filename="ThongTinKhachHang.xlsx")
    sheet=wb.active

    #create header from first row
    header = [cell.value for cell in sheet[1]]

    #create list of dictionaries from excel file
    data_rows = []
    for row in sheet.iter_rows(min_row=2, values_only=True):
        data_rows.append(dict(zip(header, row)))
    #create dataframe from excel file
    df = pd.DataFrame(data_rows)
    return print(df)

def create_file():
    wb = Workbook()
    ws = wb.active
    ws['A1'] = 'Mã KH'
    ws['B1'] = 'Họ Tên'
    ws['C1'] = 'Số ĐT'
    ws['D1'] = 'Email'
    ws['E1'] = 'Địa Chỉ'
    
    wb.save("ThongTinKhachHang.xlsx")
    
def add_customer():
    new_customer = []
    #load excel file
    wb=load_workbook(filename="ThongTinKhachHang.xlsx")
    sheet=wb.active
    
    #get next row
    next_row = sheet.max_row + 1
    print(Fore.CYAN + Back.BLACK + "\n ----------THÊM KHÁCH HÀNG----------")
    ma_kh = input("Nhập mã khách hàng: ")
    ho_ten = input("Nhập họ tên khách hàng: ")
    so_dt = input("Nhập số điện thoại khách hàng: ")
    dia_chi = input("Nhập địa chỉ khách hàng: ")
    email = input("Nhập email khách hàng: ")
    new_customer.append(ma_kh)
    new_customer.append(ho_ten)
    new_customer.append(so_dt)
    new_customer.append(email)
    new_customer.append(dia_chi)
    
    for col, value in enumerate(new_customer, start=1):
        if value == "":
            return print(Fore.RED + Back.BLACK + "Vui lòng nhập đầy đủ thông tin khách hàng!!!")
        else:
            sheet.cell(row=next_row, column=col, value=str(value))
            
    wb.save("ThongTinKhachHang.xlsx")
    
    return print(Fore.GREEN + Back.BLACK + "Thêm khách hàng thành công.")
    
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
        if not os.path.exists("ThongTinKhachHang.xlsx"):
            print(Fore.YELLOW + Back.BLACK + "Chưa có file dữ liệu khách hàng. Đang tạo file...")
            time.sleep(1)
            create_file()
            print(Fore.GREEN + Back.BLACK + "Tạo file thành công.")
        elif os.path.exists("ThongTinKhachHang.xlsx") and is_data_none() == True:
            print(Fore.YELLOW + Back.BLACK + "File dữ liệu khách hàng hiện tại đang trống. Vui lòng thêm khách hàng.")
            add_customer()
        else:
            add_customer()
    elif choice == '2':
        if check_file() == False:
            print(Fore.RED + Back.BLACK + "Chưa có dữ liệu khách hàng. Vui lòng thêm khách hàng trước!!!")
        else:
            show_customer_information()
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