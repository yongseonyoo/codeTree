a, b = tuple(map(str, input().split()))

word = ''
for i in range(len(b)):
    if i == 0 or i == 1:
        word += a[i]
    else:
        word += b[i]

print(word)