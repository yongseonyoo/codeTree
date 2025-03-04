n = int(input())

cnt = 0
for _ in range(n):
    a = int(input())
    cnt += a

print(str(cnt)[1:] + str(cnt)[0])