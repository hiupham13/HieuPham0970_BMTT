def demSo(lst):
    count = {}
    for item in lst:
        if item in count:
            count[item] += 1
        else:
            count[item] = 1
    return count
input_str = input("Nhập danh sách các từ: ")
word = input_str.split()
soLan = demSo(word)
print("Số lần xuất hiện của các phần tử: ", soLan)