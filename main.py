from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
from PIL import ImageTk, Image
import csv



conversations = [
    'Hi',
    'hey there how are you?',
    'how are you',
    'I am well and you?',
    'Hello how are you',
    'I am well thank you and you?',
    'I am well how about you?',
    'I am well thank you',
    'I am well thank you and you',
    'I am doing well thank you.',
    'What is your name?',
    "I am Apple's chatbot, I love assisting customers like you. What's your name?",
    'your name?',
    "I am Apple's chatbot, I love assisting customers like you. What's your name?",
    'name?',
    "I am Apple's chatbot, I love assisting customers like you. What's your name?",
    'may I ask you some questions?',
    "definitely!! Please do! that's what I am here for right",
    'what are your plans for the day?',
    'I am just going to help you figure out any apple products that you are interested in',

    #apple arcade
    "what is apple arcade?",
    "Apple arcade is our game subscription service that gives you unlimited access to 100+ games in one subscription",
    "what are the features of apple arcade?",
    '''
    We have some great features with apple arcade, 
    You have an all you can play subscription with no ads 
    and last but not the least, you can download to play online or offline
    ''',
   "what is the price of arcade subscription?",
    'we offer 4.99/month after free one month trial',
    'what is the mac lineup?',
    'we offer the mac book pro and mac book air in our lineup for macs',
    'what is the price of the mac book pro?',
    'the mac book pro starts at 1299$',
    'what is the price of the mac book air?',
    'the mac book air starts at 1099$',
    'tell me about the iphones',
    'we have 4 iphone models: iPhone 11 pro, iPhone 11, iPhone Xr, iPhone 8',
    'what is the price of the iphone 11 pro?',
    'the iphone11 pro starts at $999',
    'what is the price of the iphone 11?',
    'the iPhone 11 starts at $699',
    'price of iphone11?',
    'the iPhone 11 starts at $699',
    'what is the price of iphone xr?',
    'the iPhone xr starts at $599',
    'price of iphone xr?',
    'the iPhone xr starts at $599',
    'what is the price of iphone8?',
    'the iPhone 8 starts at 449',
    'what are some features of iphones?',
    'the features of iPhones are retina display and some of the iphones have fingersprint and face scanners',
    'features of iphones',
    'the features of iPhones are retina display and some of the iphones have fingersprint and face scanners',
    'what are the products that apple offers?',
    'We offer several products like notebooks, tablets, smartphones,and many high performance CPU devices',
    'products of apple?',
    'We offer several products like notebooks, tablets, smartphones,and many high performance CPU devices',
    'what is the current version of ios?',
    'iOS 13 is the current version that we are running',
    'version of ios?',
    'iOS 13 is the current version that we are running',
    'what is the current version of macos?',
    'the current version is macOS catalina',
    'version of current macOS?',
    'the current version is macOS catalina',
    'current version macOS?',
    'the current version is macOS catalina'

]

bot = ChatBot('Sriram')

trainer = ListTrainer(bot)
trainer.train(conversations)
def askFromBot():
    query = textField.get()
    answer = bot.get_response(query)
    messages.insert(END,"You:: "+query)
    messages.insert(END,"Bot:: "+str(answer))
    textField.delete(0,END)





mainWindow = Tk()

mainWindow.geometry("500x650")
mainWindow.title('my chat bot')

botImage = ImageTk.PhotoImage(Image.open('botImage.jpg'))
botImageLabel = Label(mainWindow, image = botImage)
botImageLabel.pack(pady=10)


frame = Frame(mainWindow)
scroll = Scrollbar(frame)
messages = Listbox(frame,width = 80, height = 20)
scroll.pack(side = RIGHT, fill = Y)
messages.pack(side=LEFT,fill=BOTH,pady=10)
frame.pack()

#creating text field
textField = Entry(mainWindow, font = ('Verdana',20))
textField.pack(fill=X, pady = 10)


askButton  = Button(mainWindow, text = "Enter",font = ('Verdana',20),command = askFromBot)
askButton.pack()

mainWindow.mainloop()

