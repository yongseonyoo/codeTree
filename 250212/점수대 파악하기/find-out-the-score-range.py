arr = list(map(int, input().split()))

for i in range(100, 9, -10):
    cnt = 0
    for j in arr:
        if j // i == 1 and (j - i) < 10:
            cnt += 1
        elif j == 0:
            break
    print(f"{i} - {cnt}")