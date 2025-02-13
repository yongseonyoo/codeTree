n = int(input())
nums = list(map(int, input().split()))

# Write your code here!
max_val = nums[0]
for i in range(n):
    if max_val < nums[i]:
        max_val = nums[i]

cnt = 0
for num in nums:
    if num == max_val:
        cnt += 1

if cnt > 1:
    print(-1)
if cnt == 1:
    print(max_val)