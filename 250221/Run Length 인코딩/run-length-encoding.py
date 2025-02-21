sent = input()

result = ''

cnt = 0
for i in range(len(sent)):
    if i == 0 or sent[i] != sent[i-1]:
        if i != 0:
            result += f"{sent[i-1]}{str(cnt)}"
        cnt = 1
    elif sent[i] == sent[i-1]:
        cnt += 1
        if i == (len(sent)-1):
            result += f"{sent[i]}{str(cnt)}"
    

print(len(result))
print(result)