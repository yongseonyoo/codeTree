n1, n2 = tuple(map(int, input().split()))

a = list(map(int, input().split()))
b = list(map(int, input().split()))

# print(n1, n2)
# print(a, b)

if b[0] not in a:
    print('No')
else:
    result = []
    for i in range(n1):
        if a[i] == b[0]:
            a_list = []
            for j in range(i, n1):
                a_list.append(a[j])
            
            # print(a_list, b)
            
            cnt = 0
            for k in range(n2):
                if len(a_list) >= len(b):
                    if a_list[k] == b[k]:
                        cnt += 1
                else:
                    cnt = 0
            # print(cnt)
            
            if cnt == n2:
                result.append('Yes')
                break
            else:
                result.append('No')
    
    if 'Yes' in result:
        print('Yes')
    else:
        print('No')