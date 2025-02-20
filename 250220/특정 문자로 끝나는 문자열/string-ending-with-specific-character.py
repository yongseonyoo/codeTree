arr = []

for _ in range(10):
    word = input()
    arr.append(word)

w = input()

cnt = 0
for a in arr:
    if a[-1] == w:
        print(a)
        cnt += 1

if cnt == 0:
    print('None')
