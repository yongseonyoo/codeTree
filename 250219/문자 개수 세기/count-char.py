given_input = input()
given = input()

cnt = 0
for i in given_input:
    if i == given:
        cnt += 1

print(cnt)