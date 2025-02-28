s = input()
if len(s) == 0:
    print(s)
else:
    s = s[1] + s[2:] + s[0]
print(s)