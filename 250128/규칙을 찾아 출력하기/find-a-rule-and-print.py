n = int(input())

for i in range(n):
    if i == 0 or i == (n - 1):
        print("* " * n)
    else:
        for j in range(n):
            if j == 0 or j == (n - 1) or i > j:
                print("*", end=' ')
            else:
                print(" ", end=' ')
        print()