# Câu hỏi:

# Viết một chương trình tính giá trị của a+aa+aaa+aaaa với a là số được nhập vào bởi người dùng.

# Giả sử a được nhập vào là 1 thì đầu ra sẽ là: 1234

# Gợi ý:

# Trong trường hợp dữ liệu đầu vào được nhập vào chương trình nó nên được giả định là dữ liệu được người dùng nhập vào từ giao diện điều khiển.
from module import clear
clear()

def converToN(number):
    resut = 0
    for i in range(1, 5):
        resut += int(number*i)
    return resut


number = input('Enter number: ')

result = converToN(number)
print(result)
