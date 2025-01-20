n = int(input())

for i in range(n):
    # print(i, (2 * (n - i) - 1))
    print("  " * i, end="")
    print("* " * (2 * (n - i) - 1), end="")
    print("  " * i)

for i in range(n - 1):
    # print((n - 2 - i), (2 * (i + 2) - 1))
    print("  " * (n - 2 - i), end="")
    print("* " * (2 * (i + 2) - 1), end="")
    print("  " * (n - 2 - i))