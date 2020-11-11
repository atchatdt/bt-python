# Câu hỏi:

# Xác định một class với generator có thể lặp lại các số nằm trong khoảng 0 và n, và chia hết cho 7.

# Gợi ý:
# Sử dụng yield.
from module import clear
clear()
def putNumbers(n):
    i = 0
    while i < n:
        j=i
        i += 1
        if j % 7 == 0:
            yield j

for i in putNumbers(10):
    print(i)
