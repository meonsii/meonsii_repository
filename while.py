n = 5
result = 1  # (res)는 result

while True:
    if n == 0:
        break

    result *= n
    n -= 1

print(result)


n = 5
result = 1
while n > 0:  # while n이 0보다 클 동안에
    result *= n
    n -= 1

    print(result)


# while 문을 사용하여 1부터 10까지의 합구하기

result = 0
n = 1
while n < 11:
    result += n
    n += 1

    print(result)

    #################

    result = 0
    n = 1
    while True:
        if n > 10:
            break
        result += n
        n += 1

        print(result)
