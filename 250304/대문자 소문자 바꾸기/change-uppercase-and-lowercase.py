arr = list(input())

s = ''
for i in range(len(arr)):
    if arr[i].isupper():
        s += arr[i].lower()
    elif arr[i].islower():
        s += arr[i].upper()

print(s)