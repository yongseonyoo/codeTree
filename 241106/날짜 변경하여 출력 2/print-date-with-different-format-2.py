time = input()

arr = time.split("-")
m, d, y = arr[0], arr[1], arr[2]

print(f"{y}.{m}.{d}")