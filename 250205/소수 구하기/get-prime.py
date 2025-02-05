n = int(input())

for i in range(1, n+1):
    cnt = 0
    for j in range(1, i+1):
        if i % j == 0:
            cnt += j
    if cnt == 1 + i:
        print(i, end=' ')