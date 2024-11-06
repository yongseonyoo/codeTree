n = input()

arr = n.split()
a, b = int(arr[0]), int(arr[1])

print(f'{int(a//b)}...{int(a%b)}')