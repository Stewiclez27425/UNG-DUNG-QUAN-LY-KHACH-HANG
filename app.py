from colorama import Fore, Back, init
import os
from openpyxl import Workbook, load_workbook
import pandas as pd

def load_data():
    # Load excel file if exists, else create a new workbook
    wb=load_workbook(filename="ThongTinKhachHang.xlsx") if os.path.exists("ThongTinKhachHang.xlsx") else Workbook()
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
        load_data()
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