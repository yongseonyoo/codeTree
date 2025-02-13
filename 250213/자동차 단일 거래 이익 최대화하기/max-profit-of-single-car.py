n = int(input())
price = list(map(int, input().split()))

# Write your code here!
min_val = 2**31-1
for p in price:
    if p < min_val:
        min_val = p

cnt = price.index(min_val)
max_val = 0
for i in range(cnt+1, n):
    if price[i] > max_val:
        max_val = price[i]

# print('min_val:', min_val)
# print('max_val:', max_val)

if max_val == 0:
    print(0)
else:
    print(max_val - min_val)