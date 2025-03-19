n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Please write your code here.
for i in range(n1):
    if a[i] == b[0]:
        cnt = 0
        for j in range(n2):
            if a[i+j] == b[j]:
                cnt += 1
        if cnt == n2:
            print('Yes')
        else:
            print('No')
            
