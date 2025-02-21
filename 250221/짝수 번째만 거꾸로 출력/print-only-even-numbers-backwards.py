sent = input()

n = len(sent)

for i in range(n):
    if (n-i-1) % 2 == 1:
        print(sent[n-i-1], end='')