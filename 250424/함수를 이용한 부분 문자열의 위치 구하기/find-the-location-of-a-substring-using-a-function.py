text = input()
pattern = input()

# Please write your code here.
def hamsu(text, pattern):
    if pattern[0] in text:
        for i in range(len(text)-len(pattern)+1):
            cnt = 1
            if text[i] == pattern[0]:
                # print(text[i], pattern[0])
                for j in range(1, len(pattern)):
                    # print(text[i+j], pattern[j])
                    if text[i+j] == pattern[j]:
                        cnt += 1
                if cnt == len(pattern):
                    print(i)
                    break
    else:
        print(-1)

hamsu(text, pattern)