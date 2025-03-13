a, b = map(int, input().split())

# Please write your code here.
add_val = 0
for i in range(a, b+1):
    cnt = 0
    for j in range(2, i):
        if i % j == 0:
            cnt += 1
    if cnt == 0:
        add_val += i

print(add_val)