n = int(input())

for i in range(n):
    if i % 2 == 0:
        print('*')
    else:
        print("* " * (i + 1))
