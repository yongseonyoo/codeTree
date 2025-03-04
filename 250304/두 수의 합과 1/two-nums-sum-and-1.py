a, b = tuple(map(int, input().split()))

add_val = a + b

cnt = 0
for i in str(add_val):
    if i == '1':
        cnt += 1

print(cnt)