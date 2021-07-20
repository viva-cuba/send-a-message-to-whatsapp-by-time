# win 7 64 bit//python 3.7.6//vivacuba
# алгоритм отправки сообщения на WhatsApp
# написал код для себя, чтобы утром и вечером посылать сообщение маме. задать можно любое время.
# ОБЯЗАТЕЛЬНО: установленный WhatsApp на компьютере, сообщение кому отсылаете, должно быть закреплено на первой позиции в списке, можно ещё добавить день месяца "%d", тогда сообщение будет отправленно в заданный день и время,  ну и вроде всё...пользуйтесь на здоровье...
# P.S. есть какая-то библиотека для отправки сообщений по времени на WhatsApp, но захотелось чего-то своего...

import os
import datetime
from time import strftime
import time
import keyboard as ked
import random

def mama_message():
# рандомно посылает одно сообщение
    message_list = random.choice(['привет мамунь, как дела?', 'привет. всё нормально?', 'как у тебя дела?', 'как самочувствие?', 'у тебя всё хорошо?'])
# задаём свой путь к файлу
    os.startfile("C:/Users/dmitrycubahp/AppData/Local/WhatsApp/WhatsApp.exe")
# время задержки для открытия мессенджера с запасом (время задержки установите в зависимости от скорости открытия вашего приложения, но лучше сделать с запасом)
    time.sleep(20)
    ked.send("Tab")
    time.sleep(1)
    ked.send("down")
    time.sleep(1)
    ked.send("enter")
    time.sleep(1)
    ked.write(message_list, delay=0.25)
    ked.send("enter")
    time.sleep(2)
    ked.send("Alt + F4") 
    
now = strftime("%H:%M") 
print('сейчас '+ now)
# задаём время отправки. таймеры можно добавить или убрать по усмотрению.
set_the_time = '08:00'
set_the_time1 = '21:00'
print(set_the_time)
print(set_the_time1)

while True:
    now = datetime.datetime.now()
    time.sleep(30)
    now = strftime("%H:%M")
    if  now == set_the_time:
# звуковой сигнал, любой файл поместить в папку с проектом
        os.startfile('apple.mp3')
        mama_message()
    if  now == set_the_time1:
        os.startfile('apple.mp3')
        mama_message()
        exit()