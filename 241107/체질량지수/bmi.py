n = input()
arr = n.split()
h, w = int(arr[0]), int(arr[1])

b = (10000 * w)//(h**2)

print(b)
if b > 25:
    print("Obesity")