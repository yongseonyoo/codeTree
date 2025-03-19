a, o, c = input().split()
a = int(a)
c = int(c)

# Please write your code here.
def formula(a, o, c):
    val = 0
    if o == "+":
        val = a + c
        print(f"{a} {o} {c} = {val}")
    elif o == '-':
        val = a - c
        print(f"{a} {o} {c} = {val}")
    elif o == '/':
        val = a / c
        print(f"{a} {o} {c} = {val}")
    elif o == '*':
        val = a * c
        print(f"{a} {o} {c} = {val}")
    else:
        print(False)

formula(a, o, c)