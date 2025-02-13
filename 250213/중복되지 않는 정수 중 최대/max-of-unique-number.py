n = int(input())
nums = list(map(int, input().split()))

# Write your code here!
while True:
    if len(nums) > 0:
        max_val = nums[0]
    else:
        break

    for i in nums:
        if max_val < i:
            max_val = i

    cnt = 0
    for j in nums:
        if j == max_val:
            cnt += 1

    if max_val not in nums:
        print(max_val)
        break
    else:
        if cnt == 1:
            print(max_val)
            break
        else:
            for k in range(cnt):
                nums.remove(max_val)

    
    if len(nums) == 0:
        print(-1)
        break