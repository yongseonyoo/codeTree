a, b = map(int, input().split())

# Please write your code here.
trg = [3, 6, 9]

cnt = 0
for i in range(a, b+1):
    n = i // 10
    m = i - n * 10
    if i % 3 == 0:
        cnt += 1
    elif n in trg or m in trg:
        cnt += 1

print(cnt)