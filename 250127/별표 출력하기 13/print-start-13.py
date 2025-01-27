n = int(input())

even, odd = 0, 0

for i in range(2 * n):
    if i % 2 == 0:
        print("* " * (n - even))
        even += 1
    else:
        print("* " * (odd + 1))
        odd += 1