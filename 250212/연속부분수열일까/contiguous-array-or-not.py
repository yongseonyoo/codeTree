n1, n2 = tuple(map(int, input().split()))

a = list(map(int, input().split()))
b = list(map(int, input().split()))

cnt = a.index(b[0])
for i in range(len(b)):
    # print(a[cnt], b[i])
    if a[cnt] == b[i]:
        cnt +=1
    else:
        cnt = 0

if (cnt - a.index(b[0])) == len(b):
    print('Yes')
else:
    print('No')