n = int(input())
a = list(map(int, input().split()))

# Write your code here!
cnt = n
for _ in range(1000):
    max_val = 0
    for i in range(cnt):
        if max_val < a[i]:
            max_val = a[i]

    if max_val != 0:
        cnt = a.index(max_val)

    print(cnt+1, end=' ')

    if cnt == 0:
        break
    
    # print('max_val:', max_val, 'cnt:', cnt)