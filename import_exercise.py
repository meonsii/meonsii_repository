# python module부르는 말
# python math factorial설치하기

import math

# 여기서 터미널이들어가 지지 않을/때
# math라는 파일이 있고, fctorial을 구현하는 함수 존재... 'from math import factorial'적음
# def factorial (n): -> math.factorial(5)라고 적음
# factorial 대신에 ft를 사용할 수 있음 -> as ft

help(math)
n = int(input("Enter:"))
res = math.factorial(n)
print(f"{n}!={res}")


import math
