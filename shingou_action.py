from enum import Enum
class Shingou(Enum):
    RED = 1
    BLUE = 2
    YELLOW = 3


color = int(input("color1～3入力→"))
if(color == 1):
    print("とまれ")
elif(color == 2):
    print("すすめ")
elif(color == 3):
    print("注意")
else:
    print("信号機の色に対応してません")