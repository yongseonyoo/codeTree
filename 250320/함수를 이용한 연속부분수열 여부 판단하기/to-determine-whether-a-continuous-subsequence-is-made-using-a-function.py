n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Please write your code here.
if b[0] in a:
    if b[0] != a[-1]:
        cnt = 0
        for i in range(a.index(b[0]), a.index(b[0])+n2):
            if a[i] == b[i-a.index(b[0])]:
                # print(a[i], b[i-a.index(b[0])])
                cnt += 1
        if cnt == n2:
            print("Yes")
        else:
            print("No")
    elif len(a) == len(b) and a[0] == b[0]:
        print("Yes")
    else:
        print("No")
else:
    print("No")