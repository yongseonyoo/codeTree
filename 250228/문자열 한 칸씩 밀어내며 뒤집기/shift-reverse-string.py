input_str, q = input().split()
q = int(q)
queries = [int(input()) for _ in range(q)]

# Please write your code here.
for i in queries:
    if i == 1:
        input_str = input_str[1:] + input_str[0]
        print(input_str)
    elif i == 2:
        input_str = input_str[-1] + input_str[:-1]
        print(input_str)
    elif i == 3:
        print(input_str[-1:-len(input_str)-1:-1])