n = int(input())
a = list(map(int, input().split()))

# Write your code here!
max_val = -2**31-1
for i in range(n):
    if max_val < a[i]:
        max_val = a[i]

a.pop(a.index(max_val))

max_two = -2**31-1
if max_val not in a:
    for j in range(n-1):
        if max_two < a[j]:
            max_two = a[j]
else:
    max_two = max_val

print(max_val, max_two)