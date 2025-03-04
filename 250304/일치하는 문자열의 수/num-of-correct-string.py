n, trg = tuple(map(str, input().split()))
n = int(n)

cnt = 0
for _ in range(n):
    s = input()
    if s == trg:
        cnt += 1

print(cnt)