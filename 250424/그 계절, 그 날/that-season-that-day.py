Y, M, D = map(int, input().split())

# Please write your code here.
leap_year = False

if Y % 4 == 0:
    if Y % 100 == 0:
        if Y % 400 == 0:
            leap_year = True
    else:
        leap_year = True

day = False
if M <= 7:
    if M % 2 == 1:
        if D <= 31:
            day = True
    else:
        if M == 2 
            if leap_year == True and D <= 29:
                day = True
            elif leap_year == False and D <= 28:
                day = True
        if D <= 30:
            day = True
elif M > 7 and M <= 12:
    if M % 2 == 0:
        if D <= 31:
            day = True
    else:
        if D <= 30:
            day = True


if day == True:
    if M >= 3 and M <= 5:
        print('Spring')
    elif M >= 6 and M <= 8:
        print('Summer')
    elif M >= 9 and M <= 11:
        print('Fall')
    else:
        print('Winter')
else:
    print(-1)