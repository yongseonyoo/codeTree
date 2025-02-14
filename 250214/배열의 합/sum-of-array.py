for _ in range(4):
    arr = list(map(int, input().split()))
    add_val = 0
    for i in arr:
        add_val += i
    print(add_val)