n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def gcd(a, b):
    if a % b == 0:
        return b
    elif b == 0:
        return a
    else:
        return gcd(b, a % b)

# lcm(a,b)=(a*b)//gcd(a,b)

def f(arr):
    if len(arr) == 2:
        lcm = (arr[-2]*arr[-1])//gcd(arr[-2],arr[-1])
        return lcm
    else:
        lcm = (arr[-2]*arr[-1])//gcd(arr[-2],arr[-1])
        arr.remove(arr[-2])
        arr.remove(arr[-1])
        arr.append(lcm)
        return f(arr)

print(f(arr))