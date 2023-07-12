# 1001
a, b = [int(x) for x in input().split()]
print(a - b)

A, B = input().split()
print(int(A) - int(B))


# 2475 검증수
# 1
sum_val = 0
for i in range(5):
    sum_val += int(input()) ** 2
res = sum_val % 10
print(res)
# 2
data = list()  # []
for i in range(5):
    num = int(input())
    data.append(num)


# 기본입출력 for문을 이용해서
arr = list(map(int, input().split))
r = 0
for i in arr:  # for문을 사용해서 arr에 들어있는 값을 넣어준다는 의미
    r *= 1**2
print(r % 10)


# 2741

# range함수를 활용해서 하는 것/받았던 문자를 range안에 넣어놓고 input에 받아놓고 intro로 감싸서
# range(N)에서 하나만 들어오면 ->0~N-1출력
# range(start,stop,step) 그냥 python이 이렇게 만들어 진것임,,,

n = int(input())
for i in range(1, n + 1):
    print(i)

help(range)
# abs ->절댓값으로 많이 쓰이는 것
