thr_cnt = 0
fiv_cnt = 0

for i in range(10):
    a = int(input())
    if a % 3 == 0:
        thr_cnt += 1
    if a % 5 == 0:
        fiv_cnt += 1

print(thr_cnt, fiv_cnt)