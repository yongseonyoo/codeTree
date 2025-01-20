n = int(input())
num_space = (2 * n - 1) // 2 + 1

for i in range(n):
    num_star = 2 * i + 1
    num_space -= 1
    print("  " * num_space, end="")
    print("* " * num_star)
