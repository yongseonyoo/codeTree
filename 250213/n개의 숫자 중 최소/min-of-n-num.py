n = int(input())
a = list(map(int, input().split()))

# Write your code here!
min_val = 100
for i in range(n):
    if min_val > a[i]:
        min_val = a[i]

print(min_val, end=' ')

cnt = 0
for j in range(n):
    if a[j] == min_val:
        cnt += 1

print(cnt)