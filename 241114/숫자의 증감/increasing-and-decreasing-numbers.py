inp = input()
arr = inp.split()
c, n = arr[0], int(arr[1])

if c == 'A':
    for i in range(1, n+1):
        print(i, end=' ')
        i += 1
elif c == 'D':
    for i in range(n, 0, -1):
        print(i, end=' ')