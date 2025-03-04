for _ in range(10):
    s = input()
    if s == 'END':
        break
    else:
        a = ''
        for i in range(len(s)-1, -1, -1):
            a += s[i]
        print(a)