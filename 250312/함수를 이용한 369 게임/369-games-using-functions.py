a, b = map(int, input().split())

# Please write your code here.
trg = [3, 6, 9]

cnt = 0
for i in range(a, b+1):
    n = list(str(i))
    if i % 3 == 0:
        cnt += 1
    else:
        for j in n:
            if int(j) in trg:
                cnt += 1

print(cnt)