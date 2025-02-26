def xoa(dictionary, key):
    if key in dictionary:
        del dictionary[key]
        return True
    else:
        return False
my_dict = {'a':1,'b':2,'c':3,'d':4}
key_delete = 'b'
ketQua = xoa(my_dict,key_delete)
if ketQua:
    print("Phần tử đã được xoá: ",my_dict)
else:
    print("Không tìm thấy phần tử đƯợc xoá: ")