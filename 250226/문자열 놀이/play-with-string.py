input_str, n = tuple(map(str, input().split()))

before_word = input_str
for _ in range(int(n)):
    cnt, a, b = tuple(map(str, input().split()))
    word = ''
    for i in range(len(input_str)):
        if cnt == '1':
            if i == (int(a)-1):
                word += before_word[int(b)-1]
            elif i == (int(b)-1):
                word += before_word[int(a)-1]
            else:
                word += before_word[i]
        elif cnt == '2':
            if before_word[i] == a:
                word += b
            else:
                word += before_word[i]
    
    print(word)

    before_word = word