n = int(input())
a = list(map(int, input().split()))

# Write your code here!
max_val = 0
for i in range(n):
    if max_val < a[i]:
        max_val = a[i]

a.pop(a.index(max_val))

max_two = 0
if max_val not in a:
    for j in range(n-1):
        if max_two < a[j]:
            max_two = a[j]

print(max_val, max_two)