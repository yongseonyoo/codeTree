n = input()
arr = n.split()
a, b = int(arr[0]), int(arr[1])

max_value = a if a > b else b

print(max_value)