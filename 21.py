# Câu hỏi:

# Một website yêu cầu người dùng nhập tên người dùng và mật khẩu để đăng ký. Viết chương trình để kiểm tra tính hợp lệ của mật khẩu mà người dùng nhập vào.

# Các tiêu chí kiểm tra mật khẩu bao gồm:

# 1. Ít nhất 1 chữ cái nằm trong [a-z]
# 2. Ít nhất 1 số nằm trong [0-9]
# 3. Ít nhất 1 kí tự nằm trong [A-Z]
# 4. Ít nhất 1 ký tự nằm trong [$ # @]
# 5. Độ dài mật khẩu tối thiểu: 6
# 6. Độ dài mật khẩu tối đa: 12

# Chương trình phải chấp nhận một chuỗi mật khẩu phân tách nhau bởi dấu phẩy và kiểm tra xem chúng có đáp ứng những tiêu chí trên hay không. Mật khẩu hợp lệ sẽ được in, mỗi mật khẩu cách nhau bởi dấu phẩy.

# Ví dụ mật khẩu nhập vào chương trình là: ABd1234@1,a F1#,2w3E*,2We3345

# Thì đầu ra sẽ là: ABd1234@1

# Gợi ý:

# Trong trường hợp dữ liệu đầu vào được nhập vào chương trình nó nên được giả định là dữ liệu được người dùng nhập vào từ giao diện điều khiển.

import re
from module import clear
clear()


def checkPass(strPassword):
    letP = len(strPassword)
    if letP < 6 or letP > 12: return False
    if not re.search('[a-z]',strPassword): return False
    if not re.search('[0-9]', strPassword): return False
    if not re.search('[A-Z]',strPassword): return False
    if not re.search('[$#@]',strPassword): return False
    return True

def checkPasswordList(strPassword):
    arrPass = strPassword.split(',')
    arrResult = []
    for item in arrPass:
        if checkPass(item): arrResult.append(item)
    return arrResult

passwordList = input('Input password: ')
result = checkPasswordList(passwordList)
print(result)

    
