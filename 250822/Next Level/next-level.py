user2_id, user2_level = input().split()
user2_level = int(user2_level)

# Please write your code here.
class DB:
    def __init__(self, user_id='codetree', user_level=10):
        self.id = user_id
        self.lv = user_level

user1 = DB()
print('user', user1.id, 'lv', user1.lv)

user2 = DB(user2_id, user2_level)
print('user', user2.id, 'lv', user2.lv)
