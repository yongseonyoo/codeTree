input_str, q = input().split()
q = int(q)
queries = [int(input()) for _ in range(q)]

# Please write your code here.
for i in queries:
    if i == 1:
        input_str = input_str[1:] + input_str[0]
        print(input_str)
    if i == 2:
        input_str = input_str[-1] + input_str[:-1]
        print(input_str)
    if i == 3:
        sub = ''
        for j in range(len(input_str)-1, -1, -1):
            sub += input_str[j]
        input_str = sub
        print(input_str)