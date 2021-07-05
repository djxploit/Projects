# Spychat : A program to send and receive secret messages

from extra import User,add_friend,send_message,read_chat,read_message
from termcolor import colored

# ----Who are you ?------#

while True:
    check = raw_input(colored("Continue as a defaut user(Y/N) : ",'grey','on_white',attrs=['bold']))
    if check == 'Y' or check == 'y':
        from extra import Spy         # Importing default user
        break
    elif check == 'N' or check == 'n':

        # Details of a spy
        name = raw_input(colored("Name : ",'grey','on_white',attrs=['bold']))
        if len(name) == 0:
            print colored("Name length too short",'red')
            exit()
        spy_sal = raw_input(colored("Salutation : ",'grey','on_white',attrs=['bold']))
        name = spy_sal + ' ' + name

        # Error handling for string or other inputs(except int)
        while True:
            try:
                age = int(raw_input(colored("Age : ",'grey','on_white',attrs=['bold'])))
            except ValueError:
                print colored("Invalid input.Integers only",'red')
                continue
            break
        if age <= 12 or age >= 50:
            print colored("Age entered is inappropriate",'red')
            exit()

        # Error handling for inputs other than float
        while True:
            try:
                rating = float(raw_input(colored("Rating : ",'grey','on_white',attrs=['bold'])))
            except ValueError:
                print colored("Invalid input. Float only",'red')
                continue

        # Commenting on spy's rating
            if rating > 8 and rating <= 10:
                #print colored("__Elite spy__",'blue',attrs=['bold'])
                rank = "Elite Spy"
                break
            elif rating > 6 and rating <= 8:
                #print colored("__Pro spy__",'blue',attrs=['bold'])
                rank = "Pro Spy"
                break
            elif rating > 4 and rating <= 6:
                #print colored("__Semi-pro spy__",'blue',attrs=['bold'])
                rank = "Semi-pro Spy"
                break
            elif rating > 0 and rating <= 4:
                #print colored("__Rookie spy__",'blue',attrs=['bold'])
                rank = "Rookie Spy"
                break
            else:
                print colored("Invalid rating",'red')

        Spy = User(name, age, rating, True, rank)
        break
    else:
        print colored("Invalid input.",'red')


# Adding default friends
Friend1 = User(name="John",age=23,rating=7,stat=False,rank="Pro Spy")
Friend2 = User(name="Jack",age=25,rating=8.7,stat=True,rank="Elite Spy")
Spy.friends.append(Friend1)
Spy.friends.append(Friend2)

# Welcome message

print "\n\n\t\tWelcome to spy_chat \n"\
    "\t\t%s" % (Spy.name)
print "\t\tYour age :%d" % Spy.age
print "\t\tYour rating :%.1f (%s)" % (Spy.rating,Spy.rank)

# Main menu
current_stat="Empty"
while True:
    print colored("\n1. Status Update\n2. Add Friend\n"\
    "3. Send secret message \n4. Read secret message\n"\
    "5. Read chats \n6. Close application\n",'green',attrs=['bold'])
    choice = raw_input(colored("Please enter :",'grey','on_white',attrs=['bold']))

    # Status update
    if choice == '1':
        print "\n"
        print colored("Your current status is :%s" % current_stat,'white','on_grey',attrs=['bold'])
        while True:
            inp = raw_input(colored("\nChoose from :\n1. Older status\n2. Create new status\n3. Go to main menu\n",'grey',attrs=['bold']))
            if inp == '1':
                i = 1
                for mess in Spy.status:
                    print colored("%d. %s" % (i, mess),attrs=['bold'])
                    i = i + 1

                # Error handling for input other than integer
                while True:
                    try:
                        item = int(raw_input(colored("Choose message :",'grey','on_white',attrs=['bold'])))
                        if item>=i:
                            print colored("Index selected is invalid",'red')
                            continue
                    except ValueError:
                        print colored("Invalid input. Integers only",'red')
                        continue
                    break
                current_stat = Spy.status[item - 1]            # Updating current status
                print colored("Updated status : %s" % current_stat,'blue')
            elif inp == '2':
                current_stat = raw_input(colored("Type new status :",'grey','on_white',attrs=['bold']))
                Spy.status.append(current_stat)               # Appending new status to old status list
                print colored("Updated status : %s" % current_stat,'blue')
            elif inp == '3':
                break
            else:
                print colored("Invalid input",'red')
            continue


    # Add friend
    elif choice=='2':
        print '\n'
        tot_friend = add_friend()
        if tot_friend==0:
            print colored("\nFriend not added",'red',attrs=['bold'])
            tot_friend = len(Spy.friends)
        print colored("Total friend :%d" % tot_friend,'blue')

    # Send message
    elif choice=='3':
        send_message()

    elif choice=='4':
        read_message()

    elif choice=='5':
        read_chat()

    elif choice == '6':
        print "\nExiting"
        print colored("Spychat",'blue',attrs=['bold'])
        break

    else:
        print colored("Invalid input. Re-enter",'red')
