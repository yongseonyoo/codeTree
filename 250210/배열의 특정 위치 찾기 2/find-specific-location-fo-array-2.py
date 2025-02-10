arr = list(map(int, input().split()))

odd_val = 0
even_val = 0
for i in range(len(arr)):
    if i % 2 != 0:
        odd_val += arr[i]
    if i % 2 == 0:
        even_val += arr[i]

if odd_val > even_val:
    print(odd_val - even_val)
else:
    print(even_val - odd_val)