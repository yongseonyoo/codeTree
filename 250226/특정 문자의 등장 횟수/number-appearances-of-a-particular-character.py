n = input()

ee_cnt = 0
eb_cnt = 0
for i in range(len(n)):
    if 'ee' == n[i:i+2]:
        ee_cnt += 1
    if 'eb' == n[i:i+2]:
        eb_cnt += 1

print(ee_cnt, eb_cnt)
    

