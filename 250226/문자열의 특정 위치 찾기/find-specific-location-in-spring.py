a, b = tuple(map(str, input().split()))

if b in a:
    print(a.index(b))
else:
    print("No")