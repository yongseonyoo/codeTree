n = input()
m = input()

cnt = 0
for i in range(len(n)):
    n = n[-1] + n[:-1]
    cnt += 1
    if n == m:
        break

if cnt == len(n):
    print(-1)
else:
    print(cnt)