prob = 0
for i in range(1,101):
    age = int(input())
    if age >= 30:
        print(f"{prob/(i-1):.2f}")
        break
    prob += age