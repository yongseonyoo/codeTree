n = int(input())

cnt = 0
while True:
    num = 2 ** cnt
    if num == n:
        print(cnt)
        break
    else:
        cnt += 1