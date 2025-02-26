n = input()

word = ''
for i in range(len(n)):
    if n[i] == n[0]:
        word += n[1]
    elif n[i] == n[1]:
        word += n[0]
    else:
        word += n[i]

print(word) 