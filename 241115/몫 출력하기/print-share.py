cnt = 0
for i in range(100):
    a = int(input())

    if a % 2 == 0:
        print(a // 2)
        cnt += 1
    
    if cnt == 3:
        break