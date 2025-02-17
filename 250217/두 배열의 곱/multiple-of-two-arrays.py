n = 3
arr_2d_1 = [
    list(map(int, input().split()))
    for _ in range(n)
]

emp = input()

arr_2d_2 = [
    list(map(int, input().split()))
    for _ in range(n)
]

arr_2d_3 = [
    [0 for _ in range(n)]
    for _ in range(n)
]

for i in range(n):
    for j in range(n):
        arr_2d_3[i][j] = arr_2d_1[i][j] * arr_2d_2[i][j]

for i in range(n):
    for j in range(n):
        print(arr_2d_3[i][j], end=' ')
    print()