# #Creating  a class
# class StarCookie:
#     #Adding an attribute which is gonna be accessible for both class and object
#     milk = 0.1
#    #this pass keyword is gonna just let the lines get passed
#    #init function takes new objects and intializies attributes to them.
#     def __init__(self,color,weight) -> None:
#         self.color = color
#         self.weight = weight

# #Creating an object
# star_cookie1 = StarCookie("Red" , 20)
# star_cookie2 = StarCookie("Blue" , 25)
# #When individual global varibale is changing then in dict it updates value and displays it
# star_cookie2.milk = 0.3

# #dict function - It sends a type of dictinary which has a key value pair where the key is the attribute and the value is the value of the attribute.
# print(star_cookie1.__dict__)
# print(star_cookie2.__dict__)
# print(StarCookie.__dict__)


# print(star_cookie1.milk)
# print(star_cookie2.milk)
# print(StarCookie.milk)

#Another Youtube Example - Class
class Youtube:
    #Adding a default value
    def __init__(self , username , subscribers=0 , subscriptions = 0) -> None:
        #Adding Attributes 
        self.username = username
        self.subscribers = subscribers
        self.subscriptions = subscriptions
    #Adding Methods
    def subscribe(self , user):
        user.subscribers += 1
        self.subscriptions += 1
#Adding Methods
user1 = Youtube("Sandeep")
user2 = Youtube("Anuska")
user1.subscribe(user2)
print(f"{user1.username} subscribers: {user1.subscribers}")
print(f"{user1.username} subscriptions: {user1.subscriptions}")
print(f"{user2.username} subscribers: {user2.subscribers}")
print(f"{user2.username} subscriptions: {user2.subscriptions}")