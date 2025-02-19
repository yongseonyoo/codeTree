max_len = 0
min_len = 20

for _ in range(3):
    given_input = input()
    if len(given_input) > max_len:
        max_len = len(given_input)
    if len(given_input) < min_len:
        min_len = len(given_input)
    
print(max_len - min_len)