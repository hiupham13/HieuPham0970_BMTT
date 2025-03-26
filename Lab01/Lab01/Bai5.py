soGioLam = float(input("Nhập số giờ làm mỗi tuần: "))
luongGio = float(input("Nhập thù lao trên mỗi giờ làm tiêu chuẩn: "))
gioTieuChuan = 44
gioVuotChuan = max(0,soGioLam - gioTieuChuan)
thuNhap = gioTieuChuan * luongGio + gioVuotChuan * luongGio * 1.5
print(f"Số tiền lương của bạn là: ",thuNhap)