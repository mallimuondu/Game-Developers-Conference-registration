import datetime as time
from tinydb import TinyDB

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
#complete = False
#while not complete:
#    if username == user and password == password:
#        continue        
#    elif username not in user:
#        print("This is not a valid username, raw_input username again!")
#        continue
#    elif password != user[username]:
#        print("Password is not valid for . ")
#        continue
#    elif password == user[username]:
#        print("Welcome  " + username)

#def logic_login():
#    username = raw_input("Please enter your usernmae: ")
#    password = raw_input("Please enter your password: ")
#
#    complete = False
#    if username not in user.keys():
#        print("Username is invalid")
#        logic_login()
#    elif password != user.values():
#        print("Password is invalid")
#        logic_login()
#    else:
#        print("Welcome" + username)
#        complete = True
#        
#logic_login()
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

    name1 = raw_input("Enter your first name:  ")
    name2 = raw_input("Enter your second name:  ")
    name3 = name1 + name2
    if name1 == "":
        print("Please enter your two names")
        adding_new_person()
    else:
        print("You have added " + name3)
        f.write(name4)
        f.write("\n")
    global name4
    name4 = dict(name3)

#            repeating_raw_input = raw_input("Do you want to add another name: Yes(y) or No(n) ")
#            if repeating_raw_input == "y":
#                adding_new_person()
#            else:
#                break()repeating_raw_input = raw_input("Do you want to add another name: Yes(y) or No(n) ")
#            if repeating_raw_input == "y":
#                adding_new_person()
#            else:
#                break()

adding_new_person()
#        elif activities == "b":
def buy_ticket():
    which_ticket = raw_input("""
    There are the tickets we have.
    Golden ticket - 1500
    VIP ticket - 5000
    Ordinary ticket  - 500
    Which ticket do you want:  
    """)
    db = TinyDB('TicketsPeople.json')
    table1 = db.table('TicketsPeople.json')
    table1 = db.insert({name4:which_ticket})
    file.write(c)
    if which_ticket == "a" or which_ticket == "Golden ticket" or which_ticket == "golden ticket":
        print(name4 + " has bought a Golden ticket for 1000 sh")
        goldenfile = 'TicketsPeople.json'
        goldentable = goldenfile.table('Golden tickets')
        goldentable.insert({name4:which_ticket,"Sharon Gee":"Golden Ticket","Honey Bee":"Golden Ticket","Cow Milk":"Golden Ticket"})
    elif which_ticket == "b" or which_ticket == "VIP ticket" or which_ticket == "V.I.P" or which_ticket == "V.I.P ticket":
        print(name4 + " has bought a VIP ticket for 5000 sh")
        vipfile = 'TicketsPeople.json'
        viptable = goldenfile.table('VIP tickets')
        viptable.insert({name4:which_ticket,"Peter Jack":"VIP ticket","James Matenge":"VIP ticket","Moja Mujona":"VIP Ticket"})
    elif which_ticket == "c" or which_ticket == "Ordinary ticket" or which_ticket == "ordinary ticket":
        print(name4 + " has bought an ordinary ticket for 5000 sh")
        ordinaryfile = 'TicketsPeople.json'
        ordinarytable = goldenfile.table('Golden tickets')
        ordinarytable.insert({name4:which_ticket,"Peter Jack":"Original Ticket","Josh Mathanega":"Original Ticket","John Mop":"Original Ticket"})
buy_ticket()
#        elif activities == "c":
def view_tickets():
    what_to_view = raw_input(""". These are the options available:
    a View all people in the conference with their tickets
    b All people with different tickets

    """) 
    if what_to_view == "a" or what_to_view == "View all people in the conference with their tickets":
        file = open('differentPeopleTickets.js','r')
#        print()
        print(file)
    elif what_to_view == "b" or what_to_view == "All people with different tickets":
        e = file.read()
        print(e)
view_tickets()
#        elif activities == "d":
def close():
    press_e = raw_input("Please enter E/e to exit the sytem:  ")
    if press_e == "E" or press_e == "e":
        print("Good Bye.")
        exit()
    else:
        print("You have not pressed e/E. Please try again")
        close()

close()
#        else:
#            print("You have raw_inputed the wrong raw_input")