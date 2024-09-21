

class User:
    def __init__(self, id, name):
        self.Id = id
        self.Name = name
        self.followers = 0
        self.following = 0
        self.posts = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

    def post(self, user):
        self.posts += 1


user_1 = User(77, "yuvi")
user_2 = User(22, "abc")
user_1.follow(user_2)
user_1.post(user_1)
user_1.post(user_1)
print(user_1.following)
print(user_1.followers)
print("user 1 post :",user_1.posts)
print(user_2.following)
print(user_2.followers)
