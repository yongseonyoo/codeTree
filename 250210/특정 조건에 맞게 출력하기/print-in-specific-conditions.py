arr = list(map(int, input().split()))

val = []
for i in range(len(arr)):
    if arr[i] == 0:
        for j in val:
            if j % 2 == 1:
                print(j+3, end=' ')
            else:
                print(j//2, end=' ')
    else:
        val.append(arr[i])