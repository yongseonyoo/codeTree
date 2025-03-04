cnt = 0
final = list()
for i in range(200):
    a = input()
    if a == '0':
        break
    else:
        if i % 2 == 0:
            final.append(a)
        cnt += 1
        
print(cnt)
for j in final:
    print(j)