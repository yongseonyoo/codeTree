n = int(input())
name = []
korean = []
english = []
math = []

for _ in range(n):
    student_info = input().split()
    name.append(student_info[0])
    korean.append(int(student_info[1]))
    english.append(int(student_info[2]))
    math.append(int(student_info[3]))

# Please write your code here.
class f:
    def __init__(self, name, korean, english, math):
        self.nam = name
        self.kor = korean
        self.eng = english
        self.mat = math

database = []
for i in range(n):
    database.append(f(name[i], korean[i], english[i], math[i]))

database.sort(lambda x: (-x.kor, -x.eng, -x.mat))

for data in database:
    print(data.nam, data.kor, data.eng, data.mat)