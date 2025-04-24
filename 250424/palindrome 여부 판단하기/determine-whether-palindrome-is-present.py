A = input()

# Please write your code here.
def palindrome(arr):
    mid_val = 0
    if len(arr) % 2 == 1:
        mid_val = (len(arr) // 2)
    else:
        mid_val = (len(arr) // 2) - 1
    
    cnt = 0
    for i in range(mid_val):
        if arr[i] == arr[-(i+1)]:
            cnt += 1
    
    if mid_val == cnt:
        print('Yes')
    else:
        print('No')

palindrome(A)