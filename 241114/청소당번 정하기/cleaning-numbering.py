n = int(input())

cls_cnt = 0
hal_cnt = 0
toi_cnt = 0

for i in range(n+1):
    if i != 0:
        if i % 12 == 0:
            toi_cnt += 1
        elif i % 3 == 0:
            hal_cnt += 1
        elif i % 2 == 0:
            cls_cnt += 1

print(cls_cnt, hal_cnt, toi_cnt)