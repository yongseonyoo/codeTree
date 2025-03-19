a, b = map(int, input().split())

# Please write your code here.
def formula(a, b):
    cnt = 0
    for i in range(a, b+1):
        flag = False
        for j in range(2, i):
            if i % j == 0:
                flag = True
        if flag == False:
            first_num = i - (i // 10) * 10
            sec_num = (i // 10)
            if (first_num + sec_num) % 2 == 0:
                cnt += 1
    print(cnt)

formula(a, b)