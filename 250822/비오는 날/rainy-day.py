n = int(input())
date = []
day = []
weather = []

for _ in range(n):
    d, dy, w = input().split()
    date.append(d)
    day.append(dy)
    weather.append(w)

# Please write your code here.
class server:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather

dates = []
for i in range(n):
    if server(date[i], day[i], weather[i]).weather == 'Rain':
        dates.append(server(date[i], day[i], weather[i]))

answer = []
for j in range(len(dates)):
    answer.append(dates[j].date)

answer.sort()
for k in range(len(dates)):
    if answer[0] == dates[k].date:
        print(dates[k].date, dates[k].day, dates[k].weather)