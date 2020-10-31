# 
# Câu hỏi:

# Viết một chương trình chấp nhận đầu vào là chuỗi các số nhị phân 4 chữ số, phân tách bởi dấu phẩy, kiểm tra xem chúng có chia hết cho 5 không. Sau đó in các số chia hết cho 5 thành dãy phân tách bởi dấu phẩy.

# Ví dụ đầu vào là: 0100,0011,1010,1001

# Đầu ra sẽ là: 1010

# Gợi ý:

# Trong trường hợp dữ liệu đầu vào được nhập vào chương trình nó nên được giả định là dữ liệu được người dùng nhập vào từ giao diện điều khiển.
# 

from module import clear
clear()

def BinDiv5(strInput):
    arrStr = strInput.split(',')
    arrResult = set()
    for item in arrStr:
        intNumber = int(item,2)
        if intNumber % 5 == 0:
            arrResult.add(item)
    return ','.join(arrResult)


strInput = input('Input: ')
result = BinDiv5(strInput)
print(result)