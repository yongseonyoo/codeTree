# Write your code here!

cnt = 1
for i in range(1, 20):
    for j in range(1, 20):
        print(f"{i} * {j} = {i * j}", end='')

        if j == 19:
            cnt = 2

        if cnt == 1:
            print(' / ', end='')
            cnt += 1
        elif cnt == 2:
            cnt = 1
            print()