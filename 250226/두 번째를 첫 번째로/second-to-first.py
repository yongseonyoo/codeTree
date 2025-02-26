n = input()

word = ''
for i in range(len(n)):
    if n[i] == n[1]:
        word += n[0]
    else:
        word += n[i]

print(word)