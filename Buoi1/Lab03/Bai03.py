def taoTuple(lst):
    return tuple(lst)
input_list = input("Nhập danh sách các số, các nhau bằng dấu phẩy: ")
numbers = list(map(int,input_list.split(',')))
myTuple = taoTuple(numbers)
print("List: ",numbers)
print("Tuple từ list: ",myTuple)