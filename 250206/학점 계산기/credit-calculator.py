n = int(input())
arr = list(map(float, input().split()))

sum_val = 0
for i in range(n):
    sum_val += arr[i]

mean_val = round(sum_val/n, 1)

print(mean_val)

if mean_val >= 4.0:
    print("Perfect")
elif mean_val >= 3.0:
    print("Good")
else:
    print("Poor")