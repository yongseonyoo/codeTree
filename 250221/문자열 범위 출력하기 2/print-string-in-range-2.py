sentence = input()
n = int(input())

cnt = n
for i in range(len(sentence)-1, -1, -1):
    print(sentence[i], end='')
    
    cnt -= 1
    if cnt == 0:
        break