input_str = input()
target_str = input()

cnt = 0
for i in range(len(input_str)):
    if input_str[i:i+len(target_str)] == target_str:
        cnt += 1

print(cnt)