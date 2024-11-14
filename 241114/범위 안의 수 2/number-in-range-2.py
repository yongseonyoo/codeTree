num_sum = 0
num_cnt = 0
for i in range(10):
    n = int(input())
    if 0 < n and n < 200:
        num_sum += n
        num_cnt += 1

print(f"{num_sum} {num_sum/num_cnt:.1f}")