n, m = tuple(map(str, input().split()))

s_n = ''
for i in n:
    if i.isdigit() == False:
        break
    else:
        s_n += i

s_m = ''
for j in m:
    if j.isdigit() == False:
        break
    else:
        s_m += j

print(int(s_n) + int(s_m))