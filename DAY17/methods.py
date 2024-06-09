class User:
    #constructor
    def __init__(self,user_id,user_name) :
        self.id=user_id
        self.user_name=user_name
        self.followers=0
        self.following=0
    
    def follow(self,user):
        user.followers+=1
        self.following+=1



user1=User("001","Ankush")
user2=User("002","Yash")

print(user1.following)

user1.follow(user2)
print(user1.following)
