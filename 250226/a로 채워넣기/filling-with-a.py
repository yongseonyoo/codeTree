n = input()

word = ''
for i in range(len(n)):
    if i == 1 or i == len(n) - 2:
        word += 'a'
    else:
        word += n[i]

print(word)