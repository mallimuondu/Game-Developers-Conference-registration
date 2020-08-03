import datetime as time
from tinydb import TinyDB, Query
import sqlite3
conn = sqlite3.connect('main.db')
cone = sqlite3.connect('name.db')
d = cone.cursor()
c = conn.cursor()
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
        complete = True
    #        def activite():
    #            activite = print("""
    #            Welcome. These are the activities to do.
    #            a Adding a new person
    #            b Buying a new ticket
    #            c View all people
    #            d Exit the sytem
    #            """)
#        activite()
#        
#        if activities == "a":
def adding_new_person():

    name1 = input("Enter your first name:  ")
    name2 = input("Enter your second name:  ")
    global name3
    name3 = name1 + " " + name2
    if name1 == "":
        print("Please enter your two names")
        adding_new_person()
    else:
        d.execute('CREATE TABLE IF NOT EXISTS name(fName TEXT, sName Text)')
        d.execute("INSERT INTO name(fName, sName)VALUES(?,?)",(name1, name2))

#        global name3
#        name3 = dict(name1,name2)
#        f.write(name3)
#        f.write("\n")
    

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
    Golden ticket - 1500
    VIP ticket - 5000
    Ordinary ticket  - 500
    Which ticket do you want:  
    """)
    
    db = TinyDB('People.json')
    table1 = db.table('TicketsPeople.json')
    table1 = db.insert({name3:which_ticket})
    
    c.execute('CREATE TABLE IF NOT EXISTS golden_ticket(name TEXT, ticket TEXT)')
    c.execute('CREATE TABLE IF NOT EXISTS VIP_ticket(name TEXT, ticket TEXT)')
    c.execute('CREATE TABLE IF NOT EXISTS ordinary_ticket(name TEXT, ticket TEXT)')
    
    if which_ticket == "a" or which_ticket == "Golden ticket" or which_ticket == "golden ticket":
        print(name3 + " has bought a Golden ticket for 1000 sh")
        c.execute('INSERT INTO golden_ticket(name, ticket)VALUES(?,?)',(name3, which_ticket))

    elif which_ticket == "b" or which_ticket == "VIP ticket" or which_ticket == "V.I.P" or which_ticket == "V.I.P ticket":
        print(name3 + " has bought a VIP ticket for 5000 sh")
        
        c.execute('INSERT INTO VIP_ticket(name, ticket)VALUES(?,?)',(name3, which_ticket))
    elif which_ticket == "c" or which_ticket == "Ordinary ticket" or which_ticket == "ordinary ticket":
        print(name3 + " has bought an ordinary ticket for 5000 sh")
        
        c.execute('INSERT INTO ordinary_ticket(name, ticket)VALUES(?,?)',(name3, which_ticket))
buy_ticket()
#        elif activities == "c":
User = Query()
def view_tickets():
    what_to_view = input(""". These are the options available:
    a View all people in the conference with their tickets
    b All people with different tickets

    """) 
    if what_to_view == "View all people in the conference with their tickets" or what_to_view == "a":
        c.execute('SELECT * FROM golden_ticket')
        c.execute('SELECT * FROM VIP_ticket')
        c.execute('SELECT * FROM ordinary_ticket')
        c.execute('SELECT * FROM golden_ticket')
        data = c.fetchall()
        for kol in data:
            print(kol)
    elif what_to_view == "All people with different tickets" or what_to_view == "b":
        c.execute('SELECT * FROM golden_ticket')
        c.execute('SELECT * FROM VIP_ticket')
        c.execute('SELECT * FROM ordinary_ticket')
        c.execute('SELECT * FROM golden_ticket')
        data = c.fetchall()
        for kol in data:
            print(kol)
    else:
        print("Inputed the wrong input")
        view_tickets()
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