n = input()
arr = n.split()
a, b = int(arr[0]), int(arr[1])

prob = 1
for i in range(b):
    prob *= a

print(prob)