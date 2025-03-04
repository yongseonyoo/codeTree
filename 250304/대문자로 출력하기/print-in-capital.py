arr = list(input())

s = ''
for i in range(len(arr)):
    if arr[i].isalpha():
        s += arr[i].upper()

print(s)   