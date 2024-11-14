n = input()
arr = n.split()
a, b = int(arr[0]), int(arr[1])

num_sum = 0
cnt = 0

for i in range(a, b+1):
    if i % 5 == 0 or i % 7 == 0:
        num_sum += i
        cnt += 1

print(f"{num_sum} {num_sum/cnt:.1f}")