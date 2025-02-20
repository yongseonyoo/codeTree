sentence = input()
n = int(input())

for i in range(len(sentence)-1, len(sentence)-1-n, -1):
    print(sentence[i], end='')