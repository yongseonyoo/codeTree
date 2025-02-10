arr = list(map(int, input().split()))

add_value = 0
for i in range(len(arr)):
    if i == 2 or i == 4 or i == 9:
        add_value += arr[i]

print(add_value)