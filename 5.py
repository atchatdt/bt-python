
# Định nghĩa một class có ít nhất 2 method:

# getString: để nhận một chuỗi do người dùng nhập vào từ giao diện điều khiển.

# printString: in chuỗi vừa nhập sang chữ hoa.

# Thêm vào các hàm hiểm tra đơn giản để kiểm tra method của class.

# Ví dụ: Chuỗi nhập vào là quantrimang.com thì đầu ra phải là: QUANTRIMANG.COM

from module import clear
clear()


class InputOutString:
    def __init__(self, stringIO=""):
        self.stringIO = stringIO

    def inputString(self):
        self.stringIO = input("Input string: ")

    def outputString(self):
        print(self.stringIO.upper())

ipop = InputOutString()
ipop.inputString()
ipop.outputString()