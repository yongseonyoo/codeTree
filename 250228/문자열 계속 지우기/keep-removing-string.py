A = input()
B = input()

# Please write your code here.
a_arr = list(A)
for i in range(100):
    a = ''.join(a_arr)
    if B in a:
        B_index = a.index(B)
        a_arr.pop(B_index)
        a_arr.pop(B_index)

print(a)
