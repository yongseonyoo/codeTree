n = int(input())

swi = False

if n % 1 == 0 and n % n == 0:
    swi = True
    for i in range(1, n+1):
        if n % i == 0:
            swi = False

if swi == True:
    print('P')
else:
    print('C')