n = int(input())

# Please write your code here.
def recursive(n):
    for i in range(n):
        print(i+1, end=' ')
    print()
    for j in range(n):
        print(n-j, end=' ')

recursive(n)