n, m = tuple(map(int, input().split()))

arr_2d = [
    [0 for _ in range(m)]
    for _ in range(n)
]

cnt = 1
for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            # print(i, j, '|', cnt)
            arr_2d[i][j] = cnt
            cnt += 1
        if i == 0 and j != 0:
            x, y = i, j
            for k in range(j+1):
                if x < n:
                    # print(x, y, '|', cnt)
                    arr_2d[x][y] = cnt
                    x += 1
                    y -= 1
                    cnt += 1
        if i != 0 and j == (m-1):
            x, y = i, j
            for k in range(j+1):
                if x < n:
                    # print('*', x, y, '|', cnt)
                    arr_2d[x][y] = cnt
                    x += 1
                    y -= 1
                    cnt += 1

for i in range(n):
    for j in range(m):
        print(arr_2d[i][j], end=' ')
    print()

# [0,0] [0,1] [0,2]
# [1,0] [1,1] [1,2]
# [2,0] [2,1] [2,2]
