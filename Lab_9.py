#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pygame
from pygame.draw import *
from random import randint
import math
import pygame.freetype
pygame.init()
FPS = 3
screen = pygame.display.set_mode((1200, 600))

RIGHT = "to the right"
LEFT = "to the left"
STOP = "stop"
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

class Target:
    '''заждает параметры начальной мишени'''
    def __init__(self):
        self.x = randint(600, 780)
        self.y = randint(300, 550)
        self.r = randint(15, 50)
        self.color = COLORS[randint(0, 5)]
        circle(screen, self.color, (self.x, self.y),self.r )

    def new_target(self):
        """Координаты мишени"""
        circle(screen,(0,0,0), (self.x, self.y), self.r)
        x = self.x = randint(600, 780)
        y = self.y = randint(300, 550)
        r = self.r =  randint(15,50)
        color=self.color = COLORS[randint(0, 5)]
        circle(screen,color,(x,y),r)
        pygame.display.update()
class Target1:
    def __init__(self):
        self.x = randint(600, 780)
        self.y = randint(300, 550)
        self.l = 50
        self.h = 30
        self.color = COLORS[randint(0, 5)]
        rect(screen, self.color, (self.x, self.y, self.l, self.h))
        pygame.display.update()
    def new_target1(self):
        rect(screen, (0,0,0), (self.x, self.y, self.l, self.h))
        self.x = randint(600, 780)
        self.y = randint(300, 550)
        self.color = COLORS[randint(0, 5)]
        rect(screen, self.color, (self.x, self.y, self.l, self.h))
        pygame.display.update()


class Ball:
    '''задает параметры шара'''
    def __init__(self,x, y):
        self.x = x
        self.y = y
        self.r = 10
        self.color=COLORS[randint(0, 5)]
        circle(screen,self.color,(self.x,self.y),self.r)
        pygame.display.update()
    def move(self,x_change,y_change):
        '''задает движение шара'''
        circle(screen,(0,0,0),(self.x,self.y),self.r)
        self.x+=x_change
        self.y+=y_change
        circle(screen, self.color, (self.x, self.y), self.r)
        pygame.display.update()
class Ball2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = 30
        self.color = COLORS[randint(0, 5)]
        circle(screen, self.color, (self.x, self.y), self.r)
        pygame.display.update()

    def move(self, x_change, y_change):
        '''задает движение шара'''
        circle(screen, (0, 0, 0), (self.x, self.y), self.r)
        self.x += x_change
        self.y += y_change
        circle(screen, self.color, (self.x, self.y), self.r)
        pygame.display.update()
class Tank:
    '''Задает параметры танка и пушки'''
    def __init__(self,x=120,y=440,x1=150,w=10,x2=40,y2=460,l2=160,h2=80,x3=100,y3=440,l3=40,h3=20):
        self.x = x
        self.y = y
        self.w = w
        self.x1 = x1
        self.y1 = y
        self.x2 = x2
        self.y2 = y2
        self.l2 = l2
        self.h2 = h2
        self.x3 = x3
        self.y3 = y3
        self.l3 = l3
        self.h3 = h3
        self.color = COLORS[randint(0, 5)]
        self.color2 = COLORS[randint(0, 5)]
        self.color3 = COLORS[randint(0, 5)]
        rect(screen, self.color2, (self.x2, self.y2, self.l2, self.h2))
        rect(screen, self.color3, (self.x3, self.y3, self.l3, self.h3))
        line(screen, self.color,(self.x,self.y),(self.x1,self.y1),self.w)
        pygame.display.update()
    def Gun_aim(self,x,y):
        '''движение пушки'''
        line(screen, (0,0,0), (self.x, self.y), (self.x1, self.y1), self.w)
        self.y1 = y
        self.x1 = x
        line(screen, self.color, (self.x, self.y), (self.x1,self.y1), self.w)
        pygame.display.update()
    def tank_move(self,a):
        line(screen, (0, 0, 0), (self.x, self.y), (self.x1, self.y1), self.w)
        rect(screen, (0,0,0), (self.x2, self.y2, self.l2, self.h2))
        rect(screen, (0,0,0), (self.x3, self.y3, self.l3, self.h3))
        self.x += a
        self.x2 += a
        self.x3 += a
        rect(screen, self.color2, (self.x2, self.y2, self.l2, self.h2))
        rect(screen, self.color3, (self.x3, self.y3, self.l3, self.h3))
        pygame.display.update()
    def tank_update(self):
        line(screen, (0, 0, 0), (self.x, self.y), (self.x1, self.y1), self.w)
        rect(screen, (0, 0, 0), (self.x2, self.y2, self.l2, self.h2))
        rect(screen, (0, 0, 0), (self.x3, self.y3, self.l3, self.h3))
        rect(screen, self.color2, (self.x2, self.y2, self.l2, self.h2))
        rect(screen, self.color3, (self.x3, self.y3, self.l3, self.h3))
        pygame.display.update()
def display_score(count):
    FONT = pygame.freetype.Font(None, 50)
    FONT.render_to(screen, (50, 50), "Игра началась, счёт: " + str(count-1), (0, 0, 0))
    FONT.render_to(screen, (50, 50), "Игра началась, счёт: " + str(count), (70, 70, 0))
    pygame.display.update()
def display_score1(count):
    FONT = pygame.freetype.Font(None, 50)
    FONT.render_to(screen, (50, 50), "Игра началась, счёт: " + str(count-2), (0, 0, 0))
    FONT.render_to(screen, (50, 50), "Игра началась, счёт: " + str(count), (70, 70, 0))
    pygame.display.update()
pygame.display.update()
clock = pygame.time.Clock()
finished = False
screen.fill(BLACK)
New_target=Target()
New_target1=Target1()
new_tank=Tank()
count=0
display_score(count)
while finished == False:
    strike = False
    click = False
    clock.tick(FPS)
    h=30
    while strike == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('Пушка попала',str(count),'раза')
                #pygame.quit()
                finished = True
                strike = True
            elif event.type == pygame.MOUSEMOTION:
                x2 = event.pos[0]
                y2 = event.pos[1]
                tg_angle = (new_tank.y-y2)/(x2-new_tank.x)
                alpha = math.atan(tg_angle)
                coordinate_Gun_x= int(new_tank.x+h*math.cos(alpha))
                coordinate_Gun_y= int(new_tank.y-h * math.sin(alpha))
                new_tank.Gun_aim(coordinate_Gun_x,coordinate_Gun_y)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    a = -5
                    new_tank.tank_move(a)
                elif event.key == pygame.K_RIGHT:
                    a = 5
                    new_tank.tank_move(a)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x = event.pos[0]
                    y = event.pos[1]
                    tg_angle = (new_tank.y - y) / (x - new_tank.x)
                    alpha = math.atan(tg_angle)
                if  event.button == 3:
                    coordinate_Gun_x = int(new_tank.x + h * math.cos(alpha))
                    coordinate_Gun_y = int(new_tank.y - h * math.sin(alpha))
                    new_tank.Gun_aim(coordinate_Gun_x, coordinate_Gun_y)
                    if h<=60:
                        h+=5

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    coordinate_ball_x = int(new_tank.x + h * math.cos(alpha))
                    coordinate_ball_y = int(new_tank.y - h * math.sin(alpha))
                    New_ball = Ball(coordinate_ball_x,coordinate_ball_y)
                    x_change=int(h*math.cos(alpha))
                    y_change=-int(20 * math.sin(alpha))
                    while New_ball.y<=600 and New_ball.x<=1200 and (
                            (New_target.x-New_ball.x)**2 + (New_target.y-New_ball.y)**2) > ((New_target.r+New_ball.r)**2) and (
                            ((New_target1.x + New_target1.l / 2 - New_ball.x) ** 2 + (
                                    New_target1.y + New_target1.h / 2 - New_ball.y) ** 2) > (
                                    (int(math.sqrt(New_target1.l ** 2 + New_target1.h ** 2) / 2) + New_ball.r) ** 2)):
                        clock.tick(40)
                        New_ball.move(x_change,y_change)
                        y_change+=1
                        if ((New_target.x-New_ball.x)**2 + (New_target.y-New_ball.y)**2) < ((New_target.r+New_ball.r)**2):
                            count+=1
                            display_score(count)
                        elif ((New_target1.x+New_target1.l/2 - New_ball.x) ** 2 + (New_target1.y+New_target1.h/2 - New_ball.y) ** 2) <= (
                            (int(math.sqrt(New_target1.l**2+New_target1.h**2)/2) + New_ball.r) ** 2):
                            count+=2
                            display_score1(count)
                    else:
                        while New_ball.y <= 600 and New_ball.x <= 1200:
                            clock.tick(40)
                            New_ball.move(x_change, y_change)
                            y_change += 1
                        circle(screen,(0,0,0),(New_ball.x,New_ball.y),10)
                    new_tank.tank_update()
                    strike=True
                elif event.button == 2:
                    coordinate_ball_x = int(new_tank.x + h * math.cos(alpha))
                    coordinate_ball_y = int(new_tank.y - h * math.sin(alpha))
                    New_ball2 = Ball2(coordinate_ball_x, coordinate_ball_y)
                    x_change = int(h * math.cos(alpha))
                    y_change = -int(20 * math.sin(alpha))
                    while New_ball2.y <= 600 and New_ball2.x <= 1200 and (
                            (New_target.x - New_ball2.x) ** 2 + (New_target.y - New_ball2.y) ** 2) > (
                            (New_target.r + New_ball2.r) ** 2) and (((New_target1.x+New_target1.l/2 - New_ball2.x) ** 2 + (New_target1.y+New_target1.h/2 - New_ball2.y) ** 2) > (
                            (int(math.sqrt(New_target1.l**2+New_target1.h**2)/2) + New_ball2.r) ** 2)):
                        clock.tick(40)
                        New_ball2.move(x_change, y_change)
                        y_change += 1
                        if ((New_target.x - New_ball2.x) ** 2 + (New_target.y - New_ball2.y) ** 2) < (
                                (New_target.r + New_ball2.r) ** 2):
                            count += 1
                            display_score(count)
                        elif ((New_target1.x+New_target1.l/2 - New_ball2.x) ** 2 + (New_target1.y+New_target1.h/2 - New_ball2.y) ** 2) < (
                            (int(math.sqrt(New_target1.l**2+New_target1.h**2)/2) + New_ball2.r) ** 2):
                            count += 2
                            display_score1(count)
                    else:
                        while New_ball2.y <= 600 and New_ball2.x <= 1200:
                            clock.tick(40)
                            New_ball2.move(x_change, y_change)
                            y_change += 1
                        circle(screen, (0, 0, 0), (New_ball2.x, New_ball2.y), 30)
                    new_tank.tank_update()
                    strike = True
    New_target.new_target()
    New_target1.new_target1()

pygame.quit()


# In[ ]:





# In[ ]:




