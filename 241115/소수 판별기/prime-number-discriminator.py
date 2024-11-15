n = int(input())

swi = False
for i in range(1, n+1):
    if n % i == 0:
        swi = True

if swi == True:
    print('P')
else:
    print('C')