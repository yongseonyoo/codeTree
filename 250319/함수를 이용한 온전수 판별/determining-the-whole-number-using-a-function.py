a, b = map(int, input().split())

# Please write your code here.
def formula(a, b):
    cnt = 0
    for i in range(a, b+1):
        num = i - (i // 10) * 10
        if i % 2 == 0:
            pass
        elif num == 5:
            pass
        elif i % 3 == 0 and i % 9 != 0:
            pass
        else:
            cnt += 1
    print(cnt)

formula(a, b)