# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 23:49:44 2021

@author: Администратор
"""
import urllib
from io import BytesIO
import config
import telebot

url1 = 'https://animals.sandiegozoo.org/sites/default/files/2016-11/animals_hero_giraffe_1_0.jpg'
url2 = 'https://c.files.bbci.co.uk/E9DF/production/_96317895_gettyimages-164067218.jpg'
url3 = 'https://static.independent.co.uk/s3fs-public/thumbnails/image/2020/02/08/17/botswana-elephant.jpg?width=1200'
url4 = 'https://ichef.bbci.co.uk/news/976/cpsprodpb/1675A/production/_113249919_hi061718491.jpg'

TOKEN = config.token

bot = telebot.TeleBot(TOKEN)

commands = {  
    'start'       : 'Начать разговор с ботом',
    'help'        : 'Узнать, что может бот',
    'getPhoto'    : 'Попросить бота прислать картинку животного'
}
    
@bot.message_handler(commands=['start'])
def command_start(message):
    bot.send_message(message.chat.id, 
                     'Привет! Я NovyBot. Чтобы узнать, что я могу, напиши /help')
    
@bot.message_handler(commands=['help'])
def command_help(message):
    h_text = 'Вот что я умею: \n'
    for key in commands:  
        h_text += "/" + key + ": " 
        h_text += commands[key] + "\n"
    bot.send_message(message.chat.id, h_text)  
    
@bot.message_handler(commands=['getPhoto'])
def command_photo(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='Жираф', callback_data=7))
    markup.add(telebot.types.InlineKeyboardButton(text='Обезьяна', callback_data=8))
    markup.add(telebot.types.InlineKeyboardButton(text='Слон', callback_data=9))
    markup.add(telebot.types.InlineKeyboardButton(text='Тигр', callback_data=10))
    bot.send_message(message.chat.id, text = "Выбери, картинку какого животного тебе прислать?", reply_markup = markup)


@bot.callback_query_handler(func = lambda call: True)
def photo_select(call):
    #img = ''
    name = ''
    if call.data == '7':
        name = 'Жираф'
        img = BytesIO(urllib.request.urlopen(url1).read())
    elif call.data == '8':
        name = 'Обезьяна'
        img = BytesIO(urllib.request.urlopen(url2).read())
    elif call.data == '9':
        name = 'Слон'
        img = BytesIO(urllib.request.urlopen(url3).read())
    elif call.data == '10':
        name = 'Тигр'
        img = BytesIO(urllib.request.urlopen(url4).read())
        
    bot.send_message(call.message.chat.id, name)
    bot.send_photo(call.message.chat.id, img)
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

@bot.message_handler(func=lambda message: True, content_types=['text'])
def command_default(message):
    bot.send_message(message.chat.id, "Я не понимаю тебя. Напиши /start, чтобы начать общаться со мной")
       

bot.polling()


