n = int(input())

name = []
score1 = []
score2 = []
score3 = []

for _ in range(n):
    student_input = input().split()
    name.append(student_input[0])
    score1.append(int(student_input[1]))
    score2.append(int(student_input[2]))
    score3.append(int(student_input[3]))

# Please write your code here.
class f:
    def __init__(self, name, score1, score2, score3):
        self.name = name
        self.s1 = score1
        self.s2 = score2
        self.s3 = score3

database = []
for i in range(n):
    database.append(f(name[i], score1[i], score2[i], score3[i]))

database.sort(lambda x: x.s1 + x.s2 + x.s3)

for data in database:
    print(data.name, data.s1, data.s2, data.s3)