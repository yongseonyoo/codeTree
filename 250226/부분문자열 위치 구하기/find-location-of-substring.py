input_str = input()
target_str = input()

cnt = 0
# Please write your code here.
for i in range(len(input_str)):
    if input_str[i:i+len(target_str)] == target_str:
        print(input_str[i:i+len(target_str)], target_str)
        cnt += input_str.index(target_str[0])
        break

if cnt != 0:
    print(cnt)
else:
    print(-1)