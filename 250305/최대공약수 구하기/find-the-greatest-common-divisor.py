n, m = map(int, input().split())

# Please write your code here.
max_num = 0
num = 1
for i in range(100):
    if n % num == 0 and m % num == 0:
        if max_num < num:
            max_num = num
    num += 1

print(max_num)