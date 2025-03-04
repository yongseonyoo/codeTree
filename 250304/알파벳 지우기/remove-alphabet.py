n = input()
m = input()

s_n = ''
for i in n:
    if i.isdigit():
        s_n += i

s_m = ''
for j in m:
    if j.isdigit():
        s_m += j

print(int(s_n) + int(s_m))