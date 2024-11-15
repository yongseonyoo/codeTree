while True:
    n = input()
    arr = n.split()
    
    print(int(arr[0]) * int(arr[1]))

    if arr[2] == 'C':
        break