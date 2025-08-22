MAX_N = 5

codenames = []
scores = []
for _ in range(MAX_N):
    codename, score = input().split()
    codenames.append(codename)
    scores.append(int(score))

# Please write your code here.
class DB:
    def __init__(self, codename, score):
        self.codename = codename
        self.score = score

peoples = []
for i in range(MAX_N):
    peoples.append(DB(codenames[i], scores[i]))

min_people = ''
min_score = 100
for j in range(MAX_N):
    if peoples[j].score < min_score:
        min_score = peoples[j].score
        min_people = peoples[j].codename

print(min_people, min_score)
