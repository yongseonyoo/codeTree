input_str = input()
target_str = input()

cnt = 0
# Please write your code here.
for i in range(len(input_str)):
    if input_str[i:i+len(target_str)] == target_str:
        # print(input_str[i:i+len(target_str)], target_str)
        cnt += i
        break

if cnt != 0:
    print(cnt)
else:
    if input_str[0] == target_str[0]:
        print(0)
    else:
        print(-1)