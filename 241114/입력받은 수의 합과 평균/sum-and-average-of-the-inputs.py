n = int(input())

n_num = 0
for i in range(n):
    num = int(input())
    n_num += num

print(f"{n_num} {n_num/n:.1f}")