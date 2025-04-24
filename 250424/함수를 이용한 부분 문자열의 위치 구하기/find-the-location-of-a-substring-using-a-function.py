text = input()
pattern = input()

# Please write your code here.
def is_inside():
    for i in range(len(text)-len(pattern)+1):
        if text[i:i+len(pattern)] == pattern:
            return i
    return -1

print(is_inside())