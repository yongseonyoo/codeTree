n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def hamsu(n, arr):
    for i in range(n):
        if arr[i] % 2 == 0:
            arr[i] = arr[i] // 2
        print(arr[i], end=' ')

hamsu(n, arr)