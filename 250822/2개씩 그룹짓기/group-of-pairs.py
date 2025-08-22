n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
nums.sort()

max_num = 0
for i in range(n):
    add_num = nums[i] + nums[2*n-i-1]
    if add_num > max_num:
        max_num = add_num

print(max_num)