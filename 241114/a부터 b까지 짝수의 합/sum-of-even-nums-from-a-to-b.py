n = input()
arr = n.split()
a, b = int(arr[0]), int(arr[1])

even_sum = 0
for i in range(a, b+1):
    if i % 2 == 0:
        even_sum += i

print(even_sum)