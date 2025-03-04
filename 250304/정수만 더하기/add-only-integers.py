arr = list(input())

cnt = 0
for i in range(len(arr)):
    if arr[i].isdigit():
        cnt += int(arr[i])

print(cnt)