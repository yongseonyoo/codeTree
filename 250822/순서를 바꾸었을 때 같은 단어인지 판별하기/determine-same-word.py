word1 = input()
word2 = input()

# Please write your code here.
if len(word1) != len(word2):
    print('No')
else:
    word1_li = sorted(list(word1))
    word2_li = sorted(list(word2))
    
    cnt = 0
    for i in range(len(word1)):
        if word1_li[i] == word2_li[i]:
            cnt += 1
    
    if cnt == len(word1):
        print('Yes')
    else:
        print('No')