n = 4
arr_2d = [
    list(map(int, input().split()))
    for _ in range(n)
]

add_val = 0
for i in range(n):
    for j in range(n):
        if i >= j:
            add_val += arr_2d[i][j]

print(add_val)