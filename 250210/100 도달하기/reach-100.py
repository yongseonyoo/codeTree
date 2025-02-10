n = int(input())

val_list = []
for i in range(100):
    if i == 0:
        val_list.append(1)
    elif i == 1:
        val_list.append(n)
    else:
        val = val_list[i-2] + val_list[i-1]
        val_list.append(val)
        if val >= 100:
            break

for v in val_list:
    print(v, end=' ')