from datetime import datetime

def getCurrentTime():
    return datetime.now().strftime('%m-%d-%Y %H:%M:%S')
    
class Messenger:
    def __init__(self, listeners=[]):
        self.listeners = listeners
        
    def send(self, message, listener):
        #for listener in self.listeners:
        #    listener.receive(message)
        listener.receive(message)
    
    def receive(self, message):
        pass
    
class Listener(Messenger):
    def __init__(self, listeners=[]):
        super().__init__(listeners)
        self.messages = []          #clean messages
        
    def receive(self, message):
        self.messages.append({'message': message, 'time': getCurrentTime()})
    
    def printMessages(self):
        for msg in self.messages:
            print(f'Message: "{msg["message"]}" Time: {msg["time"]}')
        self.messages = []           #clean messages
    


listener1 = Listener()
listener2 = Listener()
sender = Messenger([listener1, listener2])

sender.send('Hey Listener One!', listener1)
sender.send('Hey Listener Two!', listener2)
sender.send('Can you save this message? Thanks!', listener1)
sender.send('How are you?', listener2)


listener1.printMessages()
listener2.printMessages()

