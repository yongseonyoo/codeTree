arr = list(map(int, input().split()))

empty_list = list()
for i in arr:
    if i == 0:
        break
    else:
        empty_list.append(i)

for j in range(len(empty_list)):
    print(empty_list[len(empty_list)-j-1], end=' ')