n = input()
arr = n.split()
a, b, c = int(arr[0]), int(arr[1]), int(arr[2])

swi = False
for i in range(a, b+1):
    if c % i == 0:
        swi = True

if swi == True:
    print('YES')
else:
    print('NO')