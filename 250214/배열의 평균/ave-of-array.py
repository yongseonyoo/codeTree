n = 2
arr_2d = [
    list(map(int, input().split()))
    for _ in range(n)
]

for i in range(n):
    row_add = 0
    for j in range(len(arr_2d[i])):
        row_add += arr_2d[i][j]
    row_mean = row_add // len(arr_2d[i])
    print(f"{row_mean:.1f}", end=' ')
print()


for i in range(len(arr_2d[0])):
    col_add = 0
    for j in range(n):
        # print(arr_2d[j][i], i, j)
        col_add += arr_2d[j][i]
    col_mean = col_add // n
    print(f"{col_mean:.1f}", end=' ')
print()

add_val = 0
cnt = 0
for i in range(n):
    for j in range(len(arr_2d[i])):
        add_val += arr_2d[i][j]
        cnt += 1
        
mean_val = add_val / cnt
print(f"{mean_val:.1f}", end=' ')