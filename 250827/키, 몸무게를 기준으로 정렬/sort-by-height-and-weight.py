n = int(input())
name = []
height = []
weight = []
for _ in range(n):
    n_i, h_i, w_i = input().split()
    name.append(n_i)
    height.append(int(h_i))
    weight.append(int(w_i))

# Please write your code here.
class f:
    def __init__(self, name, height, weight):
        self.n = name
        self.h = height
        self.w = weight

database = []
for i in range(n):
    database.append(f(name[i], height[i], weight[i]))

database.sort(key=lambda x: (x.h, -x.w))

for data in database:
    print(data.n, data.h, data.w)