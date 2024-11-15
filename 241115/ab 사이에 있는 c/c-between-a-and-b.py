n = input()
arr = n.split()
a, b, c = int(arr[0]), int(arr[1]), int(arr[2])

result = False
for i in range(a, b+1):
    if i % c == 0:
        result = True

if result == True:
    print('YES')
else:
    print('NO')