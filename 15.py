# 
# Câu hỏi:

# Viết một chương trình tìm tất cả các số trong đoạn 1000 và 3000 (tính cả 2 số này) sao cho tất cả các chữ số trong số đó là số chẵn. In các số tìm được thành chuỗi cách nhau bởi dấu phẩy, trên một dòng.

# Gợi ý:

# Trong trường hợp dữ liệu đầu vào được nhập vào chương trình nó nên được giả định là dữ liệu được người dùng nhập vào từ giao diện điều khiển.
# 

from module import clear
clear()
myList =[]

for item in range(1000,3001):
    kt = True
    for i in str(item):
        if int(i) % 2 != 0:
            kt = False
            break
    if kt: myList.append(item)

print(','.join(myList))