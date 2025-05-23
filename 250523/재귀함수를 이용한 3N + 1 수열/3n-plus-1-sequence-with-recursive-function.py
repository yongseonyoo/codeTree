n = int(input())

# Please write your code here.
cnt = 0
def f(n, cnt):
    if n == 1:
        print(cnt)
    else:
        if n % 2 == 0:
            n = n // 2
        elif n % 2 == 1:
            n = n * 3 + 1
        cnt += 1
        return f(n, cnt)

f(n, cnt)