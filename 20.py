# Câu hỏi:

# Viết chương trình tính số tiền thực của một tài khoản ngân hàng dựa trên nhật ký giao dịch được nhập vào từ giao diện điều khiển.

# Định dạng nhật ký được hiển thị như sau:

# D 100
# W 200

# (D là tiền gửi, W là tiền rút ra).

# Giả sử đầu vào được cung cấp là:

# D 300

# D 300

# W 200

# D 100

# Thì đầu ra sẽ là:

# 500

# Gợi ý:

# Trong trường hợp dữ liệu đầu vào được nhập vào chương trình nó nên được giả định là dữ liệu được người dùng nhập vào từ giao diện điều khiển.


from module import clear
clear()

totalMoney = 0

while True:
    s= input('\nNhấn:\nD: để gửi tiền\nW: để rút tiền\nS: để xem số hiện tại\nE: để thoát\nC: để clear màn hình\nChọn: ')
    s = s.lower()
    if s == 's': print('Số tiền hiện tại: {0}'.format(totalMoney))
    elif s == 'e': break
    elif s == 'c': clear()
    elif s == 'd' or s == 'w':
        dolla = int(input('Nhập số tiền: '))
        if s == 'd': totalMoney += dolla
        if s == 'w': 
            if totalMoney < dolla: print('Số tiền không đủ để rút')
            else: print('Đã rút thành công: {0}'.format(dolla))
    else:
        print('Lựa chọn sai')
