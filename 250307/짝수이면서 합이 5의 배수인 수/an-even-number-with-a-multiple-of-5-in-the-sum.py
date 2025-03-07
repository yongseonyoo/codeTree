n = int(input())

# Please write your code here.
a = n // 10
b = n - a * 10

if (a + b) % 5 == 0:
    print('Yes')
else:
    print('No') 