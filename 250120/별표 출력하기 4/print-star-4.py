n = int(input())

for i in range(n):
    print("* " * (n - i))

for i in range(n):
    if i != 0:
        print("* " * (i + 1))