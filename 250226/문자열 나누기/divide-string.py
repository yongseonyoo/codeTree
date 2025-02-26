n = int(input())
arr = list(map(str, input().split()))

nums = ''
for i in range(n):
    nums += arr[i]

cnt = 0
for i in range(n):
    print(nums[cnt: cnt+5])
    cnt += 5