n = int(input())

status = False
for i in range(2, n):
    if n % i == 0:
        status = True

if status == True:
    print('C')
else:
    print('N')