n = int(input())

cnt = n
for i in range(n):
    for j in range(i+1, 0, -1):
        print(cnt - j + 1, end=' ')
    print()