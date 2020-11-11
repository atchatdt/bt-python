# Câu hỏi:

# Một Robot di chuyển trong mặt phẳng bắt đầu từ điểm đầu tiên (0,0). Robot có thể di chuyển theo hướng UP, DOWN, LEFT và RIGHT với những bước nhất định. Dấu di chuyển của robot được đánh hiển thị như sau:

# UP 5

# DOWN 3

# LEFT 3

# RIGHT 3

# Các con số sau phía sau hướng di chuyển chính là số bước đi. Hãy viết chương trình để tính toán khoảng cách từ vị trí hiện tại đến vị trí đầu tiên, sau khi robot đã di chuyển một quãng đường. Nếu khoảng cách là một số thập phân chỉ cần in só nguyên gần nhất.

# Ví dụ: Nếu tuple sau đây là input của chương trình:

# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2

# thì đầu ra sẽ là 2.

# Gợi ý:

# Trong trường hợp dữ liệu đầu vào được nhập vào chương trình nó nên được giả định là dữ liệu được người dùng nhập vào từ giao diện điều khiển.

from module import clear
clear()

import math
pos = [0,0]
while True:
    s = input('Input: ')
    if not s:
        break
    movement = s.split(" ")
    direction = movement[0]
    steps = int(movement[1])
    if direction=="UP":
        pos[1]+=steps
    elif direction=="DOWN":
        pos[1]-=steps
    elif direction=="LEFT":
        pos[0]-=steps
    elif direction=="RIGHT":
        pos[0]+=steps
    else:
        pass
# Bài tập Python 24 Code by Quantrimang.com
print (int(round(math.sqrt(pos[1]**2+pos[0]**2))))