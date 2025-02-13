arr = list(map(int, input().split()))

max_val = 0
min_val = 999
for i in arr:
    if i == 999 or i == -999:
        break
    else:
        if i > max_val:
            max_val = i
        if i < min_val:
            min_val = i
    
print(max_val, min_val)