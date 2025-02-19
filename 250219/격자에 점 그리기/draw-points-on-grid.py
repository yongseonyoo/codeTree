n, m = tuple(map(int, input().split()))

arr_2d = [
    [0 for _ in range(n)]
    for _ in range(n)
]

cnt = 1
for _ in range(m):
    x, y = tuple(map(int, input().split()))
    arr_2d[x-1][y-1] = cnt
    cnt += 1

for i in range(n):
    for j in range(n):
        print(arr_2d[i][j], end=' ')
    print()