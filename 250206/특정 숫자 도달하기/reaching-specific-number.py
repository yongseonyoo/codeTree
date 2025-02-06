arr = input().split()

num_list = list()
for i in arr:
    i = int(i)
    if i >= 260:
        break
    else:
        num_list.append(i)

add = 0
for j in num_list:
    add += j

mean = add / len(num_list)

print(add, mean)