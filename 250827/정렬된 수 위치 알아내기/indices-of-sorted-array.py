n = int(input())
sequence = list(map(int, input().split()))

# Please write your code here.
index = sorted(sequence)

idx = [(i+1, index[i]) for i in range(n)]

if len(set(sequence)) == 1:
    for i in range(n):
        print(i+1, end=' ')
else:
    for seq in sequence:
        for i in idx:
            if i[1] == seq:
                print(i[0], end=' ')
                idx.remove(i)