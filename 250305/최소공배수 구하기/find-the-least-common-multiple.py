n, m = map(int, input().split())

# Please write your code here.
def find_lcm(n, m):
    save_val = 10000
    min_val = 9999
    for i in range(10000):
        if min_val > 0 and min_val % n == 0 and min_val % m == 0:
            if save_val > min_val:
                save_val = min_val
        min_val -= 1
    print(save_val)

find_lcm(n, m)