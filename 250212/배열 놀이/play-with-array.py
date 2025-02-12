arr_1 = list(map(int, input().split()))
n, q = arr_1[0], arr_1[1]

arr_2 = list(map(int, input().split()))

# 1 a: a번째 원소를 출력합니다.

for i in range(q):
    arr_3 = list(map(int, input().split()))
    num, tar = arr_3[0], arr_3[1]
    if num == 1:
        print(arr_2[tar - 1])
    elif num == 2:
        for a2 in arr_2:
            if a2 == tar:
                print(arr_2.index(a2) + 1)
                break
    elif num == 3:
        s = arr_3[1]
        e = arr_3[2]
        for j in range(s, e+1):
            print(arr_2[j-1], end=' ')
        print()