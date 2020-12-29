SMSStore = []
unreadMessage = []
class SMSMessage(object): # defining a class

    def __init__(self, hasBeenRead, messageText, fromNumber): # The constructor method is used to initialize data init
        self.hasBeenRead = hasBeenRead
        self.messageText = messageText # The argument to these functions is the word self
        self.fromNumber = fromNumber
        hasBeenRead = False

    def markAsRead(self, hasBeenRead):
        hasBeenRead = True

    def add_sms(self):
        newMessage = (self.hasBeenRead, self.messageText, self.fromNumber)
        return SMSStore.append(newMessage)

    def get_count():
        return len(SMSStore)

    def get_message(self, i):
        hasBeenRead = True
        return SMSStore[i][1]

    def get_unread_messages(i):
        for i in SMSStore:
            if SMSStore[i][0] == False:
                unreadMessage.append(SMSStore[i])
        print unreadMessage

    def remove(self, i):
        return SMSStore.remove(i)  

userChoice = ""

while userChoice != "quit":
    userChoice = raw_input("What would you like to do - read/send/quit?")
    if userChoice == "read":
        print len(SMSStore) #Place your logic here
    elif userChoice == "send":
        messageText = raw_input("Please type in your message: ")
        fromNumber = raw_input("Please type in the number it was sent from ")
        newObject = SMSMessage(False, messageText, fromNumber)
        newObject.add_sms()
        print SMSStore #Place your logic here
    elif userChoice == "quit":
        print "Goodbye"
    else:
        print "Oops - incorrect input"
