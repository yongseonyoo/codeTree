n = input()
arr = n.split()
a, b = int(arr[0]), int(arr[1])

if a < b:
    for i in range(b, a-1, -1):
        print(i, end=' ')
elif a > b:
    for i in range(a, b-1, -1):
        print(i, end=' ')