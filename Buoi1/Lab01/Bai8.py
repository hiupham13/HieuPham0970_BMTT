def chiaHet5(soNhiPhan):
    soThapPhan = int(soNhiPhan,2)
    if (soThapPhan % 5 == 0):
        return True
    else:
        return False
chuoiNhiPhan = input("Nhập chuỗi số nhị phân (phân tách bởi dấu phẩy): ")

listSoNhiPhan = chuoiNhiPhan.split(',')
chiaHet5 = [so for so in listSoNhiPhan if chiaHet5(so)]
if len(chiaHet5) > 0:
    ketQua = ','.join(chiaHet5)
    print("Các số nhị phân chia hết cho 5 là: ",ketQua)
else:
    print("Không có số nhị phân nào chia hết cho 5 trong chuỗi đã nhập")
