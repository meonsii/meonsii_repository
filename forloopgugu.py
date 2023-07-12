for i in range(2, 10, 2):
    for j in range(1, 10, 1):
        print(f"{i}x{j}={i*j}")


# IF문을 작성해서 사용하는 방법

for i in range(1, 10):
    if i % 2 == 0:
        for j in range(1, 10):
            print(f"{i}x{j}={i*j}")


for i in range(1, 10):
    if i % 2 != 0:
        continue  # 포문을 실행하지말고 다음으로 넘어가라

    for j in range(1, 10):
        print(f"{i}x{j}={i*j}")


# crtl 누르고 ///누르면 #한것처럼 챱챱챱 할 수 있음!

for i in range(1, 10):
    print(f"#####{i}")
    if i % 2 == 0:
        break
        for j in range(1, 10):
            print(f"{i}x{j}={i*j}")
