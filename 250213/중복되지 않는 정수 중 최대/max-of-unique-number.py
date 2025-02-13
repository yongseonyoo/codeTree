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

    # nums.pop(nums.index(max_val))
    nums.remove(max_val)
    if max_val in nums:
        # nums.pop(nums.index(max_val))
        nums.remove(max_val)
        if max_val in nums:
            nums.remove(max_val)
    elif max_val not in nums:
        print(max_val)
        break
    
    if len(nums) == 0:
        print(-1)
        break