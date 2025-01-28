n = int(input())

for i in range(n):
    if i == 0:
        print('* ' * n)
    else:
        for j in range(n):
            if (j % 2 == 1) and (i <= j) :
                print("*", end=' ')
            else:
                print(" ", end=' ')
        print()