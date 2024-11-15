n = input()
arr = n.split()
a, b = int(arr[0]), int(arr[1])

prob = 1
for i in range(1, b+1):
    if i % a == 0:
        prob *= i

print(prob)