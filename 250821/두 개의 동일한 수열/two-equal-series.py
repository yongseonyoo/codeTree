n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
A.sort()
B.sort()

cnt = 0
for i in range(n):
    if A[i] == B[i]:
        cnt += 1

if cnt == n:
    print('Yes')
else:
    print('No')