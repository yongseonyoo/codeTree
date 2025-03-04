arr = list(input())

s = ''
for i in range(len(arr)):
    if arr[i].isdigit():
        s += arr[i]
    elif arr[i].isalpha():
        s += arr[i].lower()

print(s)