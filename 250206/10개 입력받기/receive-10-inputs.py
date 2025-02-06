arr = list(map(int, input().split()))

val = list()
for i in arr:
    if i == 0:
        break
    else:
        val.append(i)

sum_val = 0
for j in val:
    sum_val += j

mean_val = round(sum_val/len(val), 1)

print(sum_val, mean_val)