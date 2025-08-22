unlock_code, wire_color, seconds = input().split()
seconds = int(seconds)

# Please write your code here.
class server:
    def __init__(self, unlock_code, wire_color, seconds):
        self.unlock_code = unlock_code
        self.wire_color = wire_color
        self.seconds = seconds

answer = server(unlock_code, wire_color, seconds)

print("code :", answer.unlock_code)
print("color :", answer.wire_color)
print("second :", answer.seconds)