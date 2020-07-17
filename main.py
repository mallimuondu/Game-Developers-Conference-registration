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
user = {"Nesh" : "12", "Malli" : "67890","Dad":"258"}
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
        print(f"Password is not valid for . ")
        continue
    elif password == user[username]:
        print(f"Welcome {username} ")
        
        def activite():
            activite = print("""
            Welcome. These are the activities to do.
            a Adding a new person
            b Buying a new ticket
            c View all people
            d Exit the sytem
            """)
            asking2 = input("a Adding a new person. Enter the first name and second name:  ")
            print("You entered "+asking2)
            activities = input("Choose one of the above: ")
        activite()
#        
        if activities == "a":
            def adding_new_person():
                with open('main.txt','a') as f:
                        global asking2
                        asking2 = input("Enter the first and second name:  ")
                        f.write(asking2)
                        f.write("\n")
                repeating_input = input("Do you want to add another name: Yes(y) or No(n) ")
                if repeating_input == "y":
                    adding_new_person()
                else:
                    activite()
                        
            adding_new_person()
        elif activities == "b":
            def buy_ticket():
                which_ticket = input("""
                Hello
                There are the tickets we have.
                a Golden ticket
                b VIP ticket
                c Ordinary ticket  
                Which ticket do you want:  
                """)
                activite()
            buy_ticket()
        elif activities == "c":
            print("We will come to you soon")  
            exit()
        elif activities == "d":
            def close():
                press_e = input("Please enter E/e to exit the sytem:  ")
                if press_e == "E" or press_e == "e":
                    print("Good Bye.")
                    exit()
                else:
                    print("You have not pressed e/E. Please try again")
                    close()
                    
            close()
#        else:
#            print("You have inputed the wrong input")