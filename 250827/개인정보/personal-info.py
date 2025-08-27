n = 5
name = []
height = []
weight = []

for _ in range(n):
    n, h, w = input().split()
    name.append(n)
    height.append(int(h))
    weight.append(float(w))

# Please write your code here.
class f:
    def __init__(self, name, height, weight):
        self.name = name
        self.h = height
        self.w = weight

database = []
for i in range(5):
    database.append(f(name[i], height[i], weight[i]))

print("name")
database.sort(lambda x: x.name)
for data in database:
    print(data.name, data.h, data.w)
print()
print("height")
database.sort(lambda x: -x.h)
for data in database:
    print(data.name, data.h, data.w)