n = int(input())

arr = []

for _ in range(n):
    word = input()
    arr.append(word)

w = input()

add_val = 0
cnt = 0
for a in arr:
    if w == a[0]:
        add_val += len(a)
        cnt += 1

mean_val = add_val/cnt

print(f"{cnt} {mean_val:.2f}")
    