#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pygame
from pygame.draw import *
from random import randint
import os.path
import math
import time
from tabulate import tabulate

pygame.init()
#name=input()
FPS = 3
screen = pygame.display.set_mode((1200, 600))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

def new_ball():
    '''рисует новый шарик
       x,y:coordinates
       r:radius'''

    global x, y, r
    x = randint(100, 1100)
    y = randint(100, 500)
    r = randint(10, 100)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)
    pygame.display.update()

def another():
    '''рисует другую фигуру
    a,b:coordinates
       h:higher'''
    global a, b, h, b1, b2
    a = randint(100, 900)
    b = randint(100, 400)
    h = randint(20, 200)
    color = COLORS[randint(0, 5)]
    b1=b+int(h*math.tan(math.pi/6))
    b2=b-int(h*math.tan(math.pi/6))
    while (x-a)**2+(y-b)**2<(r+(h+b-b2))**2:
        a = randint(100, 900)
        b = randint(100, 400)
        h = randint(20, 200)
        b1 = b + int(h * math.tan(math.pi / 6))
        b2 = b - int(h * math.tan(math.pi / 6))

    polygon(screen,color,[(a,b),(a+h,b1),(a+h,b2)])
    pygame.display.update()

pygame.display.update()
clock = pygame.time.Clock()
finished = False
n = 0

while finished == False:
    strike = False
    clock.tick(FPS)
    new_ball()
    another()
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    if strike == False:
        '''координаты смещения'''
        x_change = randint(-15, 15)
        y_change = randint(-15, 15)
        a_change = randint(-15, 15)
        b_change = randint(-15, 15)
        color = COLORS[randint(0, 5)]
        while  strike == False:
            x+=x_change
            y+=y_change
            a+=a_change
            b+=b_change
            b1 = b + int(h * math.tan(math.pi/6))
            b2 = b - int(h * math.tan(math.pi/6))
            circle(screen, color, (x, y), r)
            polygon(screen, color, [(a, b), (a+h, b1), (a+h, b2)])
            pygame.display.update()
            screen.fill(BLACK)
            time.sleep(0.1)
            #movement of the first ball
            if (x + r) >= 1200 or (x - r) <= 0:
                x_change = 0 - x_change
            elif (y + r) >= 600 or (y - r) <= 0:
                y_change = 0 - y_change

            #movement of the another figure
            if (a+h)>=1200 or a <=0:
                a_change = 0 - a_change
            elif (b1)>=600 or (b2)<=0:
                b_change = 0 - b_change

            #about clicking these balls
            for event in pygame.event.get():
                if event.type == pygame.QUIT:

                    #print(n)
                    
                    finished = True
                    strike = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            if (abs(event.pos[0] - x))^2 + (abs(event.pos[1] - y))^2 <= r:
                                n += 1
                                strike = True
                            if (a <= event.pos[0] <= a+h) and (b2<=event.pos[1]<=b1) and  (
                               (b+(event.pos[0]-a)*math.tan(math.pi/6))>=event.pos[1] or (b-(event.pos[0]-a)*math.tan(math.pi/6))<=event.pos[1]):
                                n += 2
                                strike =True

    else:
        break

pygame.quit()

'''Запись в файл и отображение таблицы лучших игроков с помощью словарей.'''

print('Таблица лучших игроков\n')

g = n

#This dictionary is about the first player's data.

d1 = {'1-й игрок': str(g)}

#If the file doesn't exist, create a new one.

if not os.path.exists('1'):
    with open('1', 'w') as i:
        for key,val in d1.items():
            i.write('{}:{}\n'.format(key,val))
    nev = {}
    
#Write the first player's data to file.

    with open('1', 'r') as inp:
        for i in inp.readlines():
            key,val = i.strip().split(':')
            nev[key] = val
        print(tabulate(nev.items(), headers=['ИГРОК,№', 'БАЛЛЫ'], tablefmt="presto"))
        
#This dictionary will soon keep the information about players' results.

    dev = {}
    with open('2', 'w') as ha:
        for key,val in dev.items():
            ha.write('{}:{}\n'.format(key,val))
            
#Create a variable and save it to file. 
#This variable is needed to create dictionaries, containing data about other players (their numbers).

    p = 1
    ink = open('3', 'w')
    ink.write(str(p))
    ink.close
    
#If the file exists, then do the following tasks...

else:
    ink = open('3', 'r+')
    u = int(ink.readline())
    if u > 0:
        p = u + 1
    c = open('3','w')
    c.close()
    m = open('3','w')
    m.write(str(p))
    m.close()
    l = open('3','r')
    o = int(l.readline())
    l.close()
    
#Show the first player's data on the rating table

    nev = {}
    with open('1', 'r') as inp:
        for i in inp.readlines():
            key,val = i.strip().split(':')
            nev[key] = val
    print(tabulate(nev.items(), headers=['ИГРОК,№', 'БАЛЛЫ'], tablefmt="presto"))
    
#Show the other players' data on the rating table.

    zev = {}
    with open('2', 'r') as ing:
        for h in ing.readlines():
            key,val = h.strip().split(':')
            zev[key] = val
    zev[str(o) + '-й игрок'] = '      ' + str(n)
    with open('2', 'w') as ik:
        for key,val in zev.items():
            ik.write('{}:{}\n'.format(key,val))
    print(tabulate(zev.items(), tablefmt="presto"))


# In[ ]:





# In[ ]:





# In[ ]:




