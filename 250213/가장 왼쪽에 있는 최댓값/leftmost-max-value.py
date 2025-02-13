n = int(input())
a = list(map(int, input().split()))

# Write your code here!
cnt = a[-1]
for _ in range(10):
    max_val = 0
    for i in range(cnt - 1):
        if max_val < a[i]:
            max_val = a[i]

    if max_val != 0:
        cnt = a.index(max_val) + 1

    print(cnt, end=' ')

    if cnt == 1:
        break
    
    # print('max_val:', max_val, 'cnt:', cnt)