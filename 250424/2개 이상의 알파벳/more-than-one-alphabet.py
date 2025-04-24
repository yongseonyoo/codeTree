A = input()

# Please write your code here.
def hamsu(arr):
    arr = set(list(A))
    if len(arr) > 1:
        print('Yes')
    else:
        print('No')

hamsu(A)