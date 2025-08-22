n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

# Please write your code here.

arr = sorted(str)
for i in range(n):
    if str[i][:len(t)] != t:
        arr.remove(str[i])

print(arr[k-1])