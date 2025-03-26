def daoNguocList(lst):
    return lst[::-1]
input_list = input("Nhập danh sách các số, các nhau bằng dấu phẩy: ")
numbers = list(map(int,input_list.split(',')))
listDaoNguoc = daoNguocList(numbers)
print("List sau khi đảo ngược: ", listDaoNguoc)