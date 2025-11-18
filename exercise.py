# names = ["tina","akbar","asqar","sogol","samane","amini","fati"]

# listn = []

# for name in names:
#     if name[0] == "a":
#         listn.append(name)
        
# print(listn)


# exercise 2

# stored_password = "12345"

# entered_password = input("enter your password: ")

# if entered_password == stored_password:
#     print("oh cool your password is right!")
# else:
#     print("oh you are wrong") 


# exercise 3

# stored_password = "12345"
# entered_password = input("enter your password: ")

# while entered_password != stored_password:
#     entered_password = input("oh you are wrong, please enter another: ")
    
# print('oh cool correct password')

# exercise 4

# friends = ["amir","hesam","moji","ash"]

# m = "fmvfkvgf" in friends

# print(m)
# exercise 5

# users = {
#     "tina":"1234",
#     "asal":"5678",
#     "kim":"987"
# }
# entered_user = input("enter your username: ")
# entered_password = input("enter your password: ")

# if entered_user in users and users[entered_user] == entered_password:
#     print("oh cool you are loge in")
# else:
#     print("no please try again ! ")

# ex6

users = {
    "tina":"1234",
    "asal":"5678",
    "kim":"987"
}

entered_user = input("enter your username: ")
entered_password = input("enter your password: ")

while entered_user not in users or users[entered_user] != entered_password:
   print("your username or password is wrong")
   entered_user = input("enter your username again: ")
   entered_password = input("enter your password again: ")

print("oh cool you are log in")


