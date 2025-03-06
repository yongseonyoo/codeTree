a, b, c = map(int, input().split())

# Please write your code here.
def min_val(a, b, c):
    val = 100
    if a < val:
        val = a
    if b < val:
        val = b
    if c < val:
        val = c
    
    print(val)

min_val(a, b, c)