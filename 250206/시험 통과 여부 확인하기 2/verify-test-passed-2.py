n = int(input())

cnt = 0
for _ in range(n):
    arr = list(map(int, input().split()))
    sum_val = 0
    for j in arr:
        sum_val += j
    mean = sum_val / 4
    
    if mean >= 60:
        print("pass")
        cnt += 1
    else:
        print("fail")

print(cnt)