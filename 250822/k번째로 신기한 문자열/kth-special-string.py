n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

# Please write your code here.

arr = sorted(str)
for i in range(n):
    if str[i][:2] != 'ap':
        arr.remove(str[i])

print(arr[k-1])