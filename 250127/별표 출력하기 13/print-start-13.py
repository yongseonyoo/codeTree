n = int(input())

odd = 0
even = 0
for i in range(n):
    if i % 2 == 0:
        print("* " * (n - even))
        even += 1
    else:
        print("* " * (odd + 1))
        odd += 1

odd = 0
even = 0
for i in range(n):
    if i % 2 == 0:
        print("* " * (even + 3))
        even += 1
    else:
        print("* " * (n - odd - 3))
        odd += 1