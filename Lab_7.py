#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pygame
from pygame.draw import *
from random import randint
import math
import time

pygame.init()
name=input()
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

                    print(n)
                    
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
'''запись в файл'''
out = open('table.txt', 'w')
out.write('\n'+ name + '=' + str(n))
out.close()
inp = open('table.txt', 'r')
s = inp.read()
inp.close()


# In[ ]:





# In[ ]:




