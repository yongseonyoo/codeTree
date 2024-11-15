n = int(input())

prob = n
for i in range(1, n+1):
    prob /= i
    if prob <= 1:
        print(i)
        break