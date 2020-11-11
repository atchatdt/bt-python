# Câu hỏi:

# Viết chương trình sắp xếp tuple (name, age, score) theo thứ tự tăng dần, name là string, age và height là number. Tuple được nhập vào bởi người dùng. Tiêu chí sắp xếp là:

# Sắp xếp theo name sau đó sắp xếp theo age, sau đó sắp xếp theo score. Ưu tiên là tên > tuổi > điểm.

# Nếu đầu vào là:

# Tom,19,80
# John,20,90
# Jony,17,91
# Jony,17,93
# Json,21,85

# Thì đầu ra sẽ là:

# [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]

# Gợi ý:

# Trong trường hợp dữ liệu đầu vào được nhập vào chương trình nó nên được giả định là dữ liệu được người dùng nhập vào từ giao diện điều khiển.

# Sử dụng itemgetter để chấp nhận nhiều key sắp xếp.

from module import clear
from operator import itemgetter, attrgetter

clear()

myList = []
while True:
    s = input('\nNhập e để thoát\nNhập: ')
    if s.lower() == 'e':
        break
    myList.append(tuple(s.split(',')))

myList = sorted(myList, key=itemgetter(0, 1, 2))
print(myList)