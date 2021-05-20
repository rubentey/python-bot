#!/bin/python
# Bot telegram @Proyecto_ASIR_Ruben_bot

import time
import os
import RPi.GPIO as GPIO
import telepot
from telepot.loop import MessageLoop

#from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

#def start (bot, update):
#  bot.sendMessage(chat_id=update.message.chat_id, text="Bienvenid@ al administrador de servicios on/off en RPi.")

#   al enviar un /start 
#def start(update, context):
#    update.message.reply_text('Saludos ma frei!')


def action(msg):
   message = "Bienvenid@"

   chat_id = msg['chat']['id']
   cmd = msg['text']
   print ('Recibido: %s' % cmd)

   if 'on' in cmd:
      message = "on "
      if 'cups' in cmd:
         message = message + "cups "
         os.system('sudo systemctl start cups')

      if 'ssh' in cmd:
         message = message + "ssh "
         os.system('sudo systemctl start ssh')

      message = message + "service"
      telegram_bot.sendMessage (chat_id, message)



   if 'off' in cmd:
      message = "off "
      if 'cups' in cmd:
         message = message + "cups "
         os.system('sudo systemctl stop cups')

      if 'ssh' in cmd:
         message = message + "ssh "
         os.system('sudo systemctl stop ssh')

      message = message + "service"
      telegram_bot.sendMessage (chat_id, message)




telegram_bot = telepot.Bot('1747202663:AAHuywvDSUHV51shJ8bq0bd40LkGEbzDf3I')
print (telegram_bot.getMe())

MessageLoop(telegram_bot, action).run_as_thread()
print ('Tamo ready....')

while 1:
   time.sleep(1)
