n = int(input())

n_sum = 0
for i in range(1, n):
    if n % i == 0:
        n_sum += i
        if n_sum == n:
            print('P')

if n_sum != n:
    print('N')