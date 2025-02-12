arr = list(map(int, input().split()))
a, b = arr[0], arr[1]

val = 0
for i in range(a):
    a = arr[0]
    cnt = 0
    while a > 1:
        if a % b == i:
            cnt += 1
        a = a // b
    val += cnt ** 2

print(val)