n = input()
arr = n.split()
a, b = int(arr[0]), int(arr[1])

num_sum = 0
if a <= b:
    for i in range(a, b+1):
        if i % 5 == 0:
            num_sum += i
elif a > b:
    for i in range(b, a+1):
        if i % 5 == 0:
            num_sum += i

print(num_sum)