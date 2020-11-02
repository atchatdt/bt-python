# Câu hỏi:

# Sử dụng một danh sách để lọc các số lẻ từ danh sách được người dùng nhập vào.

# Giả sử đầu vào là: 1,2,3,4,5,6,7,8,9 thì đầu ra phải là: 1,3,5,7,9

# Gợi ý:

# Trong trường hợp dữ liệu đầu vào được nhập vào chương trình nó nên được giả định là dữ liệu được người dùng nhập vào từ giao diện điều khiển.

from module import clear
clear()

def filterOddNumber(strNumber):
    arrNumber = strNumber.split(',')
    arrResult = []
    for i in arrNumber:
        if int(i) % 2 != 0:
            arrResult.append(i)

    return ','.join(arrResult)

number = input('Enter a number: ')
result = filterOddNumber(number)
print(result)
