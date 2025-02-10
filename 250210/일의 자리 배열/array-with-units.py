arr = list(map(int, input().split()))

result = []
for i in range(10):
    if i == 0 or i == 1:
        result.append(arr[i])
    else:
        val = result[i - 1] + result[i - 2]
        val = val % 10
        result.append(val)
    
for j in result:
    print(j, end=' ')