n = input()
if chr(ord(n)+1) == '{':
    n = 'a'
else:
    n = chr(ord(n)+1)
print(n)