a, b = map(int, input().split())

# Please write your code here.
trg = ['3', '6', '9']

get_list = []

cnt = 0
for i in range(a, b+1):
    n = list(str(i))
    if i % 3 == 0:
        get_list.append(i)
    else:
        for j in n:
            if j in trg:
                get_list.append(i)

get_list = set(get_list)
print(len(get_list))