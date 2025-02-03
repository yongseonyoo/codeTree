n = int(input())

cnt = 1
for i in range(n):
    for j in range(n):
        if i <= j:
            print(cnt, end=' ')
            if cnt == 9:
                cnt = 1
            else:
                cnt += 1
        else:
            print(' ', end=' ')
    print()