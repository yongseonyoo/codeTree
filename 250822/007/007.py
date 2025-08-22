secret_code, meeting_point, time = input().split()
time = int(time)

# Please write your code here.
class code_check:
    def __init__(self, secret_code, meeting_point, time):
        self.secret_code = secret_code
        self.meeting_point = meeting_point
        self.time = time
    
code = code_check(secret_code, meeting_point, time)

print("secret code :", code.secret_code)
print("meeting point :", code.meeting_point)
print("time :", code.time)