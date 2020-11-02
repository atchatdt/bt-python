# Viết chương trình tìm tất cả các số chia hết cho 7 nhưng không phải bội số của 5, nằm trong đoạn 2000 và 3200 (tính cả 2000 và 3200). Các số thu được sẽ được in thành chuỗi trên một dòng, cách nhau bằng dấu phẩy.
from module import clear
clear()

listItem = []
for item in range(2000, 3200+1):
    if (item % 7 == 0) and (item % 5 != 0):
        listItem.append(str(item))

print(','.join(listItem))
