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
        print("Password is not valid for . ")
        continue
    elif password == user[username]:
        print("Welcome  " + username)

        
#        def #        activite():
#            activite = print("""
#            Welcome. These are the activities to do.
#            a Adding a new person
#            b Buying a new ticket
#            c View all people
#            d Exit the sytem
#            """)
        #        #        activite()
#        
#        if activities == "a":
        def adding_new_person():
            with open('main.txt','a') as f:
                name1 = input("Enter your first name:  ")
                name2 = input("Enter your second name:  ")
                global name3
                name3 = name1 + " " + name2
                
                if name1 == "":
                    print("Please enter your two names")
                    adding_new_person()
                else:
                    print("You have added " + name3)
                    f.write(name3)
                    f.write("\n")
#            repeating_input = input("Do you want to add another name: Yes(y) or No(n) ")
#            if repeating_input == "y":
#                adding_new_person()
#            else:
#                break()repeating_input = input("Do you want to add another name: Yes(y) or No(n) ")
#            if repeating_input == "y":
#                adding_new_person()
#            else:
#                break()
                        
        adding_new_person()
#        elif activities == "b":
        def buy_ticket():
            which_ticket = input("""
            There are the tickets we have.
            a Golden ticket - 1500
            b VIP ticket - 5000
            c Ordinary ticket  - 500
            Which ticket do you want:  
            """)
            c = name3 + "has a " + which_ticket
            file = open('differentPeopleTickets.txt','a')
            file.write(c)
            if which_ticket == "a" or which_ticket == "Golden ticket" or which_ticket == "golden ticket":
                print(name3 + " has bought a Golden ticket for 1000 sh")
                
            elif which_ticket == "b" or which_ticket == "VIP ticket" or which_ticket == "V.I.P" or which_ticket == "V.I.P ticket":
                print(name3 + " has bought a VIP ticket for 5000 sh")
                
            elif which_ticket == "c" or which_ticket == "Ordinary ticket" or which_ticket == "ordinary ticket":
                print(name3 + " has bought a VIP ticket for 5000 sh")
            
        buy_ticket()
#        elif activities == "c":
        def view_tickets():
            what_to_view = input(""". These are the options available:
            a View all people in the conference with their tickets
            b All people with different tickets
            
            """) 
            if what_to_view == "a" or what_to_view == "View all people in the conference with their tickets":
                file = open('differentPeopleTickets.txt','r')
                e = file.read()
                print(e)
            elif what_to_view == "b" or what_to_view == "All people with different tickets":
                file = open('TicketsPeople.txt','r')
                e = file.read()
                print(e)
        view_tickets()
#        elif activities == "d":
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