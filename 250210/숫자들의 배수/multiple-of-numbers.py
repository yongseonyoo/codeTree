n = int(input())

cnt = 0
for i in range(100):
    val = n * (i+1)
    print(val, end=' ')
    if val % 5 == 0:
        cnt += 1
    if cnt == 2:
        break
