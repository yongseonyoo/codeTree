start, end = map(int, input().split())

# Write your code here!
cnt = 0
for i in range(start, end+1):
    count = 0
    for j in range(1, i+1):
        if i % j == 0:
            count += 1
    if count == 3:
        cnt += 1
    
print(cnt)