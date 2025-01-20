n = int(input())

for i in range(n):
    # print(n-i-1, n-(n-i-1))
    print("  " * (n-i-1), end="")
    print("@ " * (n-(n-i-1)))

for i in range(n-1):
    # print(n-i-1)
    print("@ " * (n-i-1))