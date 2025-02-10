arr = list(map(int, input().split()))

values = []
for i in range(10):
    if i == 0 or i == 1:
        values.append(arr[i])
        print(arr[i], end=' ')
    else:
        val = values[i-1] + 2 * values[i-2]
        values.append(val)
        print(val, end=' ')