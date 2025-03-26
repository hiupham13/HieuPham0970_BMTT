def truyCap(tuple_data):
    ptDau = tuple_data[0]
    ptCuoi = tuple_data[-1]
    return ptDau,ptCuoi
input_tuple = eval(input("Nhập tuple, ví dụ (1,2,3): "))
dau,cuoi = truyCap(input_tuple)
print("Phần tử đầu: ", dau)
print("Phần tử cuối: ", cuoi)