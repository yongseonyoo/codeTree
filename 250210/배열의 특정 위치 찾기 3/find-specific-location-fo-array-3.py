arr = list(map(int, input().split()))

add_val = 0
for i in range(len(arr)):
    if arr[i] == 0:
        add_val = arr[i-1] + arr[i-2] + arr[i-3]
        break

print(add_val)