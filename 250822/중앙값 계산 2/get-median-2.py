n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
for i in range(n):
    if i % 2 == 0:
        pre_arr = arr[:i+1]
        j = len(pre_arr) // 2 + 1
        print(pre_arr[j-1], end=' ')
        