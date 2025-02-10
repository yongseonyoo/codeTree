arr = list(map(int, input().split()))

even_val = 0
multi_val = 0
multi_cnt = 0
for i in range(1, len(arr)+1):
    if i % 2 == 0:
        even_val += arr[i-1]
    if i % 3 == 0:
        multi_val += arr[i-1]
        multi_cnt += 1

multi_mean = multi_val / multi_cnt
print(f"{even_val} {multi_mean:.1f}")
