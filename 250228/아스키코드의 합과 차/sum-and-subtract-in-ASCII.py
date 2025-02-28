a, b = tuple(map(str, input().split()))

a_int = ord(a)
b_int = ord(b)

if a_int > b_int:
    add = a_int + b_int
    minus = a_int - b_int
    print(add, minus)
else:
    add = a_int + b_int
    minus = b_int - a_int
    print(add, minus)