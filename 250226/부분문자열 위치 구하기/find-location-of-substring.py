input_str = input()
target_str = input()

cnt = 0
# Please write your code here.
for i in range(len(input_str)):
    if target_str not in input_str:
        cnt = -1
        break
    if input_str[i:i+len(target_str)] == target_str:
        # print(input_str[i:i+len(target_str)], target_str)
        cnt = i
        break


print(cnt)