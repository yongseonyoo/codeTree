n = input()
arr = n.split()
a, b = int(arr[0]), int(arr[1])

cnt = b
for i in range(1, 10):
    for j in range(4):
        if cnt <= b and cnt >= a:
            print(f"{cnt} * {i} = {cnt * i}", end='')
            if cnt != a:
                print(' / ', end ='')
            cnt -= 2
    cnt = b
    print()
    