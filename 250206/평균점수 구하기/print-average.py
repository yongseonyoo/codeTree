arr = list(map(float, input().split()))

sum_val = 0
for i in arr:
    sum_val += i

mean_val = round(sum_val / len(arr), 1)

print(mean_val)