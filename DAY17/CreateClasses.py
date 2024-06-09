class User:
    #constructor
    def __init__(self,user_id,user_name) :
        self.id=user_id
        self.user_name=user_name
        
    

# user_1=User() #object
# user_1.id="001"
# user_1.username="Ankush"/
user1=User("001","Ankush")
print(user1.user_name)
print(user1.id) 