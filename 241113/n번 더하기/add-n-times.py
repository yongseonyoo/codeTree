inp = input()
arr = inp.split()
a, n = int(arr[0]), int(arr[1])

for i in range(n):
    a += n
    print(a)