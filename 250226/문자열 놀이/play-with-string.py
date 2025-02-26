input_str, n = tuple(map(str, input().split()))
for _ in range(int(n)):
    cnt, a, b = tuple(map(str, input().split()))
    word = ''
    for i in range(len(input_str)):
        if cnt == '1':
            if i == (int(a)-1):
                word += input_str[int(b)-1]
            elif i == (int(b)-1):
                word += input_str[int(a)-1]
            else:
                word += input_str[i]
    print(word)