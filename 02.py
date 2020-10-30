# Viết một chương trình có thể tính giai thừa của một số cho trước. Kết quả được in thành chuỗi trên một dòng, phân tách bởi dấu phẩy. Ví dụ, số cho trước là 8 thì kết quả đầu ra phải là 40320.
from module import clear
clear()


def giaThua(number):
    if number < 0:
        return -1
    if number == 0:
        return 1
    result = 1
    for item in range(1, number + 1):
        result *= item
    return result

def giaThua2(number):
    if number == 0: return 1
    if(number < 0): return -1
    return number * giaThua2(number-1)



number = int(input('Nhap so can tinh: '))

result = giaThua2(number)
print('{0}! = {1}'.format(number, result))
