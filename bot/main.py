#-*-coding: utf-8-*-
from chatterbot import ChatBot #import the chatbot
from chatterbot.trainers import ChatterBotCorpusTrainer
import os


bot= ChatBot('Bot')
trainer = ChatterBotCorpusTrainer(bot)

corpus_path='C:/Users/Asus-Pc/Desktop/chatterbot-corpus-master/chatterbot_corpus/data/french/'

for file in os.listdir(corpus_path):trainer.train(corpus_path + file)

while True:
 message = input('You:')
 print(message)
 if message.strip() == 'Bye':
   print('ChatBot: Bye')
   break
 else:
  reply = bot.get_response(message)
  print('ChatBot:', reply)