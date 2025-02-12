a_cnt = 0
b_cnt = 0
c_cnt = 0
d_cnt = 0

cnt = 0
for _ in range(3):
    arr = input().split()
    flu, temp = arr[0], int(arr[1])
    if flu == 'Y' and temp >= 37:
        # print('A', end=' ')
        a_cnt += 1
    elif flu == 'N' and temp >= 37:
        # print('B', end=' ')
        b_cnt += 1
    elif flu =='Y' and temp < 37:
        # print('C', end=' ')
        c_cnt += 1
    else:
        # print('D', end=' ')
        d_cnt += 1

print(a_cnt, end=' ')
print(b_cnt, end=' ')
print(c_cnt, end=' ')
print(d_cnt, end=' ')
if a_cnt >= 2:
    print("E")

