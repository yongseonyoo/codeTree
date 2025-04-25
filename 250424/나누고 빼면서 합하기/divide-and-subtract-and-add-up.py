n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.
def matrix(n, m, A):
    val = 0
    while m != 0:
        val += A[m-1]
        # print(m, A[m-1])
        if m % 2 == 1:
            m -= 1
        else:
            m //= 2
    print(val)

matrix(n, m, A)