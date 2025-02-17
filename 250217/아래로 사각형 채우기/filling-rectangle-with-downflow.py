n = int(input())

arr_2d = [
    [0 for _ in range(n)]
    for _ in range(n)
]

cnt = 1
for i in range(n):
    row_cnt = cnt
    for j in range(n):
        if cnt <= n:
            arr_2d[i][j] = row_cnt
        else:
            arr_2d[i][j] = row_cnt + n
        row_cnt += n
    cnt += 1

for i in range(n):
    for j in range(n):
        print(arr_2d[i][j], end=' ')
    print()