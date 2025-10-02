from colorama import Fore, Back, init
import os
import logging
from datetime import datetime
from openpyxl import Workbook, load_workbook
import pandas as pd
from pathlib import Path
import time
from typing import Dict, List, Optional, Union
import json

#Phan loai khach hang (WIP)
def phan_loai(): pass
    
#TrangThai (WIP)

#xuat tong tien tu hoa don (WIP)

#Cap nhap khach hang (WIP)
def update_customer():
    Workbook=load_workbook("ThongTinKhachHang.xlsx")
    ws=Workbook.active
    
    #quet dong tieu de
    header_row = ws[1]
    
    #tao dict
    col_index = {cell.value: cell.column for cell in header_row}
    
    #Lay col o cot Ma khach hang
    col_Ma_KH = col_index.get("Mã KH")
    
    #Update Thong tin khach hang
    Update_information = input ("Nhập mã khách hàng cần cập nhật thông tin: ")
    
    #list o cot ma khach hang
    list_ma_KH = [cell.value for cell in ws[col_Ma_KH]]
    
    #duyet tung phan tu trong ma khach hang
    for i in list_ma_KH:
        if Update_information == i:
            print("---------- CẬP NHẬT KHÁCH HÀNG ----------")
            KH_information = []

#generate ID khach hang   
def ID_kh():
    wb=load_workbook(filename="ThongTinKhachHang.xlsx")
    sheet=wb.active
    
    #Rut ra danh sach ma khach hang
    ma_kh_list = []
    for row in sheet.iter_rows(min_row=2, values_only=True):
        if row[0] is not None:
            ma_kh_list.append(row[0])
            
    #tim ma khach hang lon nhat
    if not ma_kh_list:
        ID_kh = "DLT" + "0"*4 + "1" #Neu khong co ID thi tao moi
        return ID_kh
    else:
        max_id = 0
        for ma_kh in ma_kh_list:
            try:
                num_part = int(ma_kh[3:])  # ma khach hang co dang DLT00001
                if num_part > max_id:
                    max_id = num_part
            except ValueError:
                continue  # Bỏ qua các mã không hợp lệ
        new_id_num = max_id + 1
        new_id = "DLU" + str(new_id_num).zfill(5)  # id luon co 5 chu so
        return new_id
    
def is_data_none(): #Kiem tra du lieu co bi rong khong
    wb=load_workbook(filename="ThongTinKhachHang.xlsx")
    sheet=wb.active
    
    for row in sheet.iter_rows(min_row=2, max_row=2, min_col=1, values_only=True):
        if all(cell is None for cell in row): #kiem tra xem value trong cell co gia tri rong khong
            return True
        else:
            return False
        
def is_recycle_bin(): #kiem tra xem co trong thung rac khong
    # Dùng Path join để tránh lỗi escape chuỗi trên Windows
    file_path = Path("Recycle Bin") / "ThongTinKhachHang.xlsx"
    if file_path.exists() and file_path.is_file():
        return True

def check_file():
    if is_recycle_bin() == True: 
        return False
    elif os.path.exists("ThongTinKhachHang.xlsx") == False:
        return False
    elif os.path.exists("ThongTinKhachHang.xlsx") and is_data_none() == True:
        return False
    else:
        return True
    
def show_customer_information(): #show danh sach khach hang
    # Load excel file
    wb=load_workbook(filename="ThongTinKhachHang.xlsx")
    sheet=wb.active #load sheet dau tien

    #create header from first row
    header = [cell.value for cell in sheet[1]]

    #create list of dictionaries from excel file
    data_rows = []
    for row in sheet.iter_rows(min_row=2, values_only=True): #xet tung row
        data_rows.append(dict(zip(header, row))) #ghep header + gia tri tung row
    #create dataframe from excel file
    df = pd.DataFrame(data_rows)
    return print(df)

def create_file(): #tao file moi neu chua co 
    wb = Workbook()
    ws = wb.active
    ws['A1'] = 'Mã KH'
    ws['B1'] = 'Họ Tên'
    ws['C1'] = 'Số ĐT'
    ws['D1'] = 'Email'
    ws['E1'] = 'Địa Chỉ'
    ws['F1'] = 'Nhóm khách hàng' #def phan loai khach hang
    ws['G1'] = 'Trạng thái' #def trang thai
    ws['H1'] = 'Lần cuối mua hàng' #dung date time
    ws['I1'] = 'Tổng tiền đã mua' #Lay data tu hoa don
    
    wb.save("ThongTinKhachHang.xlsx") #luu file
    
   
def add_customer(): #Them khach hang
    new_customer = []
    #load excel file
    wb=load_workbook(filename="ThongTinKhachHang.xlsx")
    sheet=wb.active
    
    #get next row
    next_row = sheet.max_row + 1
    print(Fore.CYAN + Back.BLACK + "\n ----------THÊM KHÁCH HÀNG----------")
    ma_kh = ID_kh()
    ho_ten = input("Nhập họ tên khách hàng: ")
    so_dt = input("Nhập số điện thoại khách hàng: ")
    dia_chi = input("Nhập địa chỉ khách hàng: ")
    email = input("Nhập email khách hàng: ")
    nhom_khach_hang = phan_loai()
    trang_thai = trang_thai()
    lan_cuoi_mua_hang = time.time()
    tong_tien_da_mua = data_hoa_don() 
    new_customer.append(ma_kh)
    new_customer.append(ho_ten)
    new_customer.append(so_dt)
    new_customer.append(email)
    new_customer.append(dia_chi)
    
    # Xử lý trường Email không bắt buộc - nếu để trống thì gán khoảng trắng
    if new_customer[3] == "" or new_customer[3].strip() == "":
        new_customer[3] = " "
    Ten_truong = ["Mã KH", "Họ Tên", "Số ĐT", "Email", "Địa Chỉ", "Nhóm khách hàng", "Trạng thái", "Lần cuối mua hàng", "Tổng tiền đã mua"]
    
    while True:
        # Chỉ kiểm tra các trường bắt buộc: Họ Tên (index 1), Số ĐT (index 2), Địa Chỉ (index 4)
        required_fields = [1, 2, 4]  # Chỉ kiểm tra Họ Tên, Số ĐT, Địa Chỉ
        validation_passed = True
        
        for i in required_fields:
            if new_customer[i] == "" or new_customer[i].strip() == "":
                print(Fore.RED + Back.BLACK + f"Trường '{Ten_truong[i]}' không được để trống. Vui lòng nhập lại.")
                validation_passed = False
                if Ten_truong[i] == "Họ Tên":
                    ho_ten = input("Nhập họ tên khách hàng: ")
                    new_customer[i] = ho_ten
                elif Ten_truong[i] == "Số ĐT":
                    so_dt = input("Nhập số điện thoại khách hàng: ")
                    new_customer[i] = so_dt
                elif Ten_truong[i] == "Địa Chỉ":
                    dia_chi = input("Nhập địa chỉ khách hàng: ")
                    new_customer[i] = dia_chi
        
        if validation_passed:
            break
    for col, value in enumerate(new_customer, start=1):
        sheet.cell(row=next_row, column=col, value=str(value)) #import value vao cell
            
    wb.save("ThongTinKhachHang.xlsx")
    
    return print(Fore.GREEN + Back.BLACK + "Thêm khách hàng thành công.")