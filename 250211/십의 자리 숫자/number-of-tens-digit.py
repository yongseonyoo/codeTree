arr = list(map(int, input().split()))

for i in range(1, 10):
    cnt = 0
    for j in arr:
        if j // 10 == i:
            cnt += 1
    print(f"{i} - {cnt}") 