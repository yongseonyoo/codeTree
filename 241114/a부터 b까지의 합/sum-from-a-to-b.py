n = input()
arr = n.split()
a, b = int(arr[0]), int(arr[1])

sum_ab = 0
for i in range(a, b+1):
    sum_ab += i

print(sum_ab)