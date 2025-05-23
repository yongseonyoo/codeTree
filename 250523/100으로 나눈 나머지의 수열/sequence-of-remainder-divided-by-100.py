N = int(input())

# Please write your code here.
def f(n):
    if n == 1:
        print(2)
    elif n == 2:
        print(4)
    else:
        a, b, c = 2, 4, 0
        for i in range(3, n+1):
            c = (a * b) % 100
            a, b = b, c
        print(c)

f(N)