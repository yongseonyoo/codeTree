n = int(input())

prob = 0
for i in range(1, 101):
    prob += i
    if prob >= n:
        print(i)
        break