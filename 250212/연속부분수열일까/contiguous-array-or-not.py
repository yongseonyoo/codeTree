n1, n2 = tuple(map(int, input().split()))

a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(n1, n2)
print(a, b)

if b[0] not in a:
    print('No')
else:
    n1_list = []
    for i in a:
        if i in b:
            n1_list.append(i)
    print(n1_list)