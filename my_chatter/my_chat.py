from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import os
import pyttsx3 #speech library for text to speech conversation

#chatterbot, pyttsx3, pypiwin32

bot = ChatBot('MyBot')
#conv = open('./data/chats.txt', 'r').readlines()
#train the bot
#bot.train(conv)


#set the trainer
bot.set_trainer(ListTrainer)

my_bot = pyttsx3.init() #initialize the engine
my_bot_v = my_bot.getProperty('voices')
my_bot.setProperty('voice', my_bot_v[1].id)
my_bot.setProperty('rate', 150)
my_bot.setProperty('volume', 5)
for _file in os.listdir('data'):
    chats = open('data/' + _file, 'r').readlines()

bot.train(chats)

while True:
    request = input('You: ')

    if request.strip() == 'Bye':
        print('Bot: '+ "Good Bye!")
        break

    response = bot.get_response(request)

    if response.confidence > 0.75:
        my_bot.say(response)
        print('Bot: ', response)
        my_bot.runAndWait()
    else:
        my_bot.say("I did not understand")
        my_bot.runAndWait()