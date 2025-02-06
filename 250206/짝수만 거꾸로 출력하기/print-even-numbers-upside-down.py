n = int(input())
arr = list(map(int, input().split()))

even = list()
for i in arr:
    if i % 2 == 0:
        even.append(i)

for j in range(len(even)):
    print(even[len(even)-j-1], end=' ')