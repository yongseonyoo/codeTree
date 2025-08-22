n = int(input())
name = []
street_address = []
region = []

for _ in range(n):
    n_i, s_i, r_i = input().split()
    name.append(n_i)
    street_address.append(s_i)
    region.append(r_i)

# Please write your code here.
class server:
    def __init__(self, name, street_address, region):
        self.name = name
        self.street_address = street_address
        self.region = region

peoples = []
for i in range(n):
    peoples.append(server(name[i], street_address[i], region[i]))

name.sort()
people_idx = 0
for j in range(n):
    if name[-1] == peoples[j].name:
        people_idx = j

print("name", peoples[people_idx].name)
print("addr", peoples[people_idx].street_address)
print("city", peoples[people_idx].region)