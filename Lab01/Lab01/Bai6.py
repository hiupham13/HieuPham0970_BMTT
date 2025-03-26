kichThuoc = input("Nhập X, Y ")
mang = [int(x) for x in kichThuoc.split(',')]
rowNum = mang[0]
colNum = mang[1]
multilist = [[0 for col in range(colNum)] for row in range (rowNum)]
for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col] = row * col
print(multilist)