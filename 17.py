# Câu hỏi:

# Viết một chương trình chấp nhận đầu vào là một câu, đếm chữ hoa, chữ thường.

# Giả sử đầu vào là: Quản Trị Mạng

# Thì đầu ra là:

# Chữ hoa: 3

# Chữ thường: 8

# Gợi ý:

# Trong trường hợp dữ liệu đầu vào được nhập vào chương trình nó nên được giả định là dữ liệu được người dùng nhập vào từ giao diện điều khiển


def countUpLowStr(myStr):
    countUpper = 0
    countLow = 0
    distStr = {'Upper': 0,'Lower': 0}
    for x in myStr:
        if x.isupper(): distStr['Upper'] +=1
        elif x.islower(): distStr['Lower'] +=1
    return distStr

print(countUpLowStr('Trần Thanh Tuấn'))
