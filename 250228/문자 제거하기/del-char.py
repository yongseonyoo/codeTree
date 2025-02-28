s = input()
n = len(s)
arr = list(s)
for i in range(20):
    if len(arr) == 1:
        break
    else:
        num = int(input())
        # print(num)
        if num < len(arr):
            arr.pop(num)
            f = ''.join(arr)
            print(f)
        else:
            arr.pop(-1)
            f = ''.join(arr)
            print(f)