a, b = map(int, input().split())
v = a / b
v = str(v)
one, two = v.split(".")
while len(two) < 20:
    two += "0"
print(f"{one}.{two[:20]}")