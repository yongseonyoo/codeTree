n, m = map(int, input().split())

# Write your code here!

arr_2d = [
    [0 for _ in range(m)]
    for _ in range(n)
]

val = 0
for i in range(m):
    if i % 2 == 1:
        val += (n - 1)
        for j in range(n):
            arr_2d[j][i] = val
            val -= 1
    else:
        if i > 1:
            val += (n + 1)
            for j in range(n):
                arr_2d[j][i] = val
                val += 1
        else:
            for j in range(n):
                arr_2d[j][i] = val
                val += 1

for k in range(n):
    for l in range(m):
        print(arr_2d[k][l], end=' ')
    print()