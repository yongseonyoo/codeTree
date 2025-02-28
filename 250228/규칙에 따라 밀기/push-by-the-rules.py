s = input()
arr = list(input())

for a in arr:
    if a == 'L':
        s = s[1:] + s[0]
    elif a == 'R':
        s = s[-1] + s[:-1]

print(s)