n = input()
arr = n.split()
a, b = int(arr[0]), int(arr[1])

while a <= b:
    if a % 2 == 1:
        print(a, end=' ')
        a *= 2
    else:
        print(a, end=' ')
        a += 3