M, D = map(int, input().split())

# Please write your code here.
if M < 13:
    if M <= 7:
        if M % 2 == 0 and M != 2:
            if D <= 30:
                print('Yes')
            else:
                print('No')
        elif M == 2:
            if D <= 28:
                print('Yes')
            else:
                print('No')
        else:
            if D <= 31:
                print('Yes')
            else:
                print('No')
    elif M >= 8:
        if M % 2 == 0 and M != 2:
            if D <= 31:
                print('Yes')
            else:
                print('No')
        else:
            if D <= 30:
                print('Yes')
            else:
                print('No')
else:
    print("No")