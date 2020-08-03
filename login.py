   
from tinydb import TinyDB
import datetime as time
now = time.datetime.now()
hour = now.hour
if hour < 12:
    print("Good morning")
elif hour > 12 and hour < 18:
    print("Good afternoon")
elif hour > 18 and hour < 19:
    print("Good evening")
else:
    print('Good night.')
user = {"Nesh" : "12", "Malli" : "67890" }
complete = False
while not complete:
    username = input("Please enter your usernmae: ")
    password = input("Please enter your password: ")
    if username == user and password == password:
        continue        
    elif username not in user:
        print("This is not a valid username, input username again!")
        continue
    elif password != user[username]:
        print(f"Password is not valid for {username}. ")
        continue
    elif password == user[username]:
        print(f"Welcome {username} ")
        complete = True
        
def adding_name():
    
    adding_name()
    