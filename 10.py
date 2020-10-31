#  Viết một chương trình có 2 chữ số, X, Y nhận giá trị từ đầu vào và tạo ra một mảng 2 chiều. Giá trị phần tử trong hàng thứ i và cột thứ j của mảng phải là i*j.

# Lưu ý: i=0,1,...,X-1; j=0,1,...,Y-1.

# Ví dụ: Giá trị X, Y nhập vào là 3,5 thì đầu ra là: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 

# Gợi ý:

# Viết lệnh để nhận giá trị X, Y từ giao diện điều khiển do người dùng nhập vào.


from module import clear
clear()

# input_str = input("Nhập X, Y: ")
# dimensions=[int(x) for x in input_str.split(',')]
# rowNum=dimensions[0]
# colNum=dimensions[1]
# multilist = [[0 for col in range(colNum)] for row in range(rowNum)]
# print(multilist)
#  # Viết bởi Quantrimang.com
# for row in range(rowNum):
#     for col in range(colNum):
#         multilist[row][col]= row*col

# print (multilist)


def createMatrix(x, y):
    multilist1 = []
    for i in range(x):
        listAppend = []
        print(i)
        for j in range(y):
            listAppend.append(i*j)
        multilist1.append(listAppend)
    return multilist1


x = int(input('Input x: '))
y = int(input('Input Y: '))
resultMatrix = createMatrix(x, y)
print(resultMatrix)
