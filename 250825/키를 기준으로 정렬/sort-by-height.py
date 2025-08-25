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
class server:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight
    
database =[]
for i in range(n):
    database.append(server(name[i], height[i], weight[i]))

database.sort(key=lambda x:x.height)

for db in database:
    print(db.name, db.height, db.weight)