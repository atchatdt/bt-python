# Câu hỏi:

# Viết một chương trình chấp nhận đầu vào là một câu, đếm số chữ cái và chữ số trong câu đó. Giả sử đầu vào sau được cấp cho chương trình: hello world! 123

# Thì đầu ra sẽ là:

# Số chữ cái là: 10
# Số chữ số là: 3

# Gợi ý:

# Trong trường hợp dữ liệu đầu vào được nhập vào chương trình nó nên được giả định là dữ liệu được người dùng nhập vào từ giao diện điều khiển.
from module import clear
clear()
def countCharAndNumber(strinput):
    char = 0
    number = 0
    for i in strinput:
        if i.isdigit(): number += 1
        if i.isalpha(): char += 1
    return {'Number': number, 'Char': char}

strIp = input('Input string: ')

print(countCharAndNumber(strIp))
