a, b = map(int, input().split())

# Please write your code here.
def hamsu(a, b):
    if a > b:
        a *= 2; b += 10
        print(a, b)
    else:
        b *= 2; a += 10
        print(a, b)

hamsu(a, b)