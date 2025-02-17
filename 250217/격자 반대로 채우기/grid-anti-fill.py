n = int(input())

arr_2d = [
    [0 for _ in range(n)]
    for _ in range(n)
]

cnt = n ** 2

if n % 2 == 0:
    for i in range(n):
        if i % 2 == 0:
            cnt -= (n - 1)
            for j in range(n):
                arr_2d[j][i] = cnt
                cnt += 1
        else:
            cnt -= (n + 1)
            for j in range(n):
                arr_2d[j][i] = cnt
                cnt -= 1
else:
    for i in range(n):
        if i % 2 == 0:
            if i > 0:
                cnt -= (n + 1)
            for j in range(n):
                arr_2d[j][i] = cnt
                cnt -= 1
        else:
            cnt -= (n - 1)
            for j in range(n):
                arr_2d[j][i] = cnt
                cnt += 1

for i in range(n):
    for j in range(n):
        print(arr_2d[i][j], end=' ')
    print()
