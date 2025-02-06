arr = list(map(int, input().split()))

get_list = list()
for i in arr:
    if i == 0:
        break
    else:
        get_list.append(i)

cnt = 0
sum_val = 0
for j in get_list:
    if j % 2 == 0:
        cnt += 1
        sum_val += j

print(cnt, sum_val)