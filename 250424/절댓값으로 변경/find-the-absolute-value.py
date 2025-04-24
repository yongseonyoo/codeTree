n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def hamsu(n, arr):
    for i in range(n):
        if arr[i] < 0:
            arr[i] *= -1
        print(arr[i], end=' ')

hamsu(n, arr)