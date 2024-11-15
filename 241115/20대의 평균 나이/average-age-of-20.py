prob = 0
cnt = 0
while True:
    age = int(input())
    if age >= 30:
        print(f"{prob/cnt:.2f}")
        break
    else:
        prob += age
        cnt += 1