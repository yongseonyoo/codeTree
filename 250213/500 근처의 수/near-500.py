arr = list(map(int, input().split()))

max_val = 0
min_val = 1000
for i in range(10):
    if arr[i] > max_val and arr[i] < 500:
        max_val = arr[i]
    if arr[i] < min_val and arr[i] > 500:
        min_val = arr[i]

print(max_val, min_val)