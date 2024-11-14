n = input()
arr = n.split()
a, b = int(arr[0]), int(arr[1])

num_sum = 0
for i in range(a, b+1):
    if i % 6 == 0 and i % 8 != 0:
        num_sum += i

print(num_sum)