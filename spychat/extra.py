# ----helper file(extra.py)-----

from datetime import datetime
from termcolor import colored

# Spy class
class User:
    def __init__(self, name, age, rating, stat, rank):
        self.name = name
        self.age = age
        self.rating = rating
        self.online = stat
        self.status = ['Life for country', 'I am a spy', 'Sneaky life']
        self.rank = rank
        self.friends = []     # Friend list
        self.chats = []       # Chat list

# Default user
name = "Mr DJ"
age = 21
rat = 3.2
stat = True
rank = "Rookie Spy"
Spy = User(name,age,rat,stat,rank)

# Chat class
class chat:
    def __init__(self, mess, by_me):
        self.message = mess
        self.time = datetime.now()
        self.by_me = by_me
        self.av_words = 0  # Maintaining average words spoken by a friend

# Function for selecting a friend from friend list of the user
def sel_friend():
    i = 1
    for friend in Spy.friends:
        print colored("%d. %s" % (i,friend.name),attrs=['bold'])
        i = i + 1

    # Error handling for invalid index and strings
    while True:
        try:
            item = int(raw_input(colored("Choose friend :",'grey','on_white',attrs=['bold'])))
            if item>=i:
                print colored("Friend selected is invalid",'red')
                continue
        except ValueError:
            print colored("Invalid input. Integers only",'red')
            continue
        break
    return item - 1

# Sending message function
def send_message():
    index = sel_friend()
    image_name = raw_input(colored("Image name : ",'grey','on_white',attrs=['bold']))
    sec_message = raw_input(colored("Enter message : ",'grey','on_white',attrs=['bold']))
    from steganography.steganography import Steganography

    # Error handling for wrong file name
    try:
        print colored("\n...Loading...",attrs=['blink'])
        Steganography.encode(image_name, "output"+Spy.friends[index].name+".jpg", sec_message)
    except IOError:
        print colored("Invalid file name or path name",'red')

    cha = chat(sec_message, True)    # Creating new chat

    Spy.friends[index].chats.append(cha)    # Appending new chat to chat list of the friend

    print colored("Message saved",'blue')

# Adding friend
def add_friend():
    while True:
        name = raw_input(colored("Friend name : ",'grey','on_white',attrs=['bold']))
        if len(name) == 0:
            print colored("Name length too short",'red')
            continue
        break

    # Error handling for input except integer
    while True:
        try:
            age = int(raw_input(colored("Friend age : ",'grey','on_white',attrs=['bold'])))
            if age <= 12 or age >= 50:
                print colored("Age entered is inappropriate", 'red')
                return 0

        except ValueError:
            print colored("Invalid input. Integers only",'red')
            continue
        break

    # Error handling for input except float
    while True:
        try:
            rating = float(raw_input(colored("Friend rating : ",'grey','on_white',attrs=['bold'])))
            if rating >10:
                print colored("Invalid rating.Max. rating is 10.0",'red')
                return 0
        except ValueError:
            print colored("Invalid input. Float only",'red')
            continue
        break
    if rating<Spy.rating:
        print colored("%s has less rating than yours" % name,'red')
        return 0

    frn = User(name,age,rating,False)   # Creating new friend

    Spy.friends.append(frn)    # Appending new friend to user's friend list

    return len(Spy.friends)    # Returning length of friend list

# Reading message
def read_message():
    index = sel_friend()
    image_name = raw_input(colored("Image name(to be decoded) :",'grey','on_white',attrs=['bold']))
    from steganography.steganography import Steganography

    # Error handling for images which doesnot contain any message
    # And also for wrong file path or name
    try:
        print '\n'
        print colored("...Loading...",attrs=['blink'])
        sec_message = Steganography.decode(image_name)
    except IOError:
        print colored("Wrong file name",'red')
        return 0
    except TypeError:
        print colored("Image does not contain message ",'red')
        return 0

    # Checking for special words in the decoded message
    print "\n"
    if sec_message=="SOS":
        print colored("!!!Emergency!!!   SOS ",'green','on_red',attrs=['bold'])
    elif sec_message == 'SAVE ME':
        print colored("Need help  !!!SAVE HIM!!! ",'green','on_red',attrs=['bold'])
    elif sec_message == 'OP':
        print colored("!!Mission started!! ",'green','on_red',attrs=['bold'])
    else:
        print colored("Decoded message :%s" % sec_message,'magenta',attrs=['bold'])

    cha = chat(sec_message,False)    # creating new chat

    cha.av_words = len(sec_message.split())   # Storing av_word spoken by the friend

    Spy.friends[index].chats.append(cha)   # Appending new chat to chat list of the friend

    print colored("Message saved",'blue')

# Reading chat history of a friend
def read_chat():
    from termcolor import colored
    index = sel_friend()
    tot = 0
    for temp in Spy.friends[index].chats:
        print colored("Message :%s " % temp.message,'red'),
        print colored("Time :%s " % temp.time,'blue'),
        print colored("By_me :%s " % temp.by_me,'green')  # Message sent by me or read by me to or from a friend
        if temp.by_me==False:
            tot = tot + temp.av_words  # Total words spoken by spy's friend (not both spy and his friend)

    # Deleting a friend from the list who speaks more than 100 words
    if tot>100:
        print colored("Friend deleted(%s)" % Spy.friends[index].name,'red',attrs=['bold'])
        del Spy.friends[index]
