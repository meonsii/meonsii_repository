# an = 2n - 1
# an = 2n + 1

# 7, 5, 3, 1
# 2x4-1,2x3-1, ...
# 1, 2, 3, 45

n = 5
for i in range(1, n + 1):
    print((n - i) * " " + (2 * i - 1) * "*")

for i in range(n - 1, 0, -1):
    print(" " * (n - i) + (2 * i - 1) * "*")
