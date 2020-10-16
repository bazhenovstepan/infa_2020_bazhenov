#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pygame
from pygame.draw import *
import pygame.gfxdraw

pygame.init()

GRAY = (190,190,190)
BLACK = (0,0,0)
WHITE = (255,255,255)
YELLOW = (255,255,0)
RED = (255,0,0)

screen = pygame.display.set_mode((400,400))
screen.fill(GRAY)
tab1 = pygame.Surface((400,400))
tab1.fill(WHITE)
tab1.set_colorkey(WHITE)
rect(tab1, BLACK, (50,50,10,80), 0)

tab2 = pygame.Surface((400,400))
tab2.fill(WHITE)
tab2.set_colorkey(WHITE)
rect(tab2, (BLACK), (50,50,10,80),0)

circle(screen, YELLOW, [200,200], 100) 
pygame.gfxdraw.aacircle(screen, 200, 200, 100, BLACK)
circle(screen, RED, [152, 175], 25)
circle(screen, RED, [248,175], 20)
pygame.gfxdraw.aacircle(screen, 152, 175, 25, BLACK)
pygame.gfxdraw.aacircle(screen, 248, 175, 20, BLACK)
circle(screen, BLACK, [152,175], 10)
circle(screen, BLACK, [248,175], 10)
screen.blit(pygame.transform.rotate(tab1, 70), (45,-213))
screen.blit(pygame.transform.rotate(tab2,-72), (-55,66))

mouth = pygame.Surface((400,400))
mouth.fill(WHITE)
mouth.set_colorkey(WHITE)
rect(mouth, BLACK, (152,205,20,100),0)
screen.blit(pygame.transform.rotate(mouth, -90), (57,95))
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()


# In[6]:


import pygame
import pygame.gfxdraw
from pygame.draw import*

pygame.init()

WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (180,210,245)
GRAY = (180,180,180)
LIME = (160,255,130)
GREEN = (140,235,70)
YELLOW = (255,255,0)
PURPLE = (230, 130, 200)
RED = (255,0,0)
sc = pygame.display.set_mode((620, 760))

sc.fill(BLUE)

polygon(sc, GRAY, [(0,280), (80,80),(150,220), (230, 120), (370,360), (480, 100), (520, 140), (620, 20), (620, 430), (0,430), (0,280)], 0)
aalines(sc, BLACK, False, [(0,280), (80,80),(150,220), (230, 120), (370,360), (480, 100), (520, 140), (620, 20)])

back = pygame.Surface((620, 760))
back.fill(GRAY)
sc.blit(back, (0,430))

polygon(sc, LIME, [(0,455), (30,445), (60,440), (76,440), (136, 435), (300, 435), (307, 437), (310, 436), (312,440), (316,443), (316,460), (318,462), (318, 500), (325,502),(330,504),(620,504), (620,760), (0,760),(0,455)], 0)
aalines(sc, BLACK, False, [(0,455), (30,445), (60,440), (76,440), (136, 435), (300, 435), (307, 437), (310, 436), (312,440), (316,443), (316,460), (318,462), (318, 500), (325,502),(330,504),(620,504)])

circle(sc, GREEN, (540, 640), 90)

k = pygame.Surface((400,400))
k.fill(GREEN)
k.set_colorkey(GREEN)

a = 200
b = 200

d = a 
t = b - 35
pygame.gfxdraw.filled_ellipse(k,d,t,50,20,WHITE)
pygame.gfxdraw.aaellipse(k,d,t,50,20,BLACK)
    
d = a + 55
t = b - 20
pygame.gfxdraw.filled_ellipse(k,d,t,50,20,WHITE)
pygame.gfxdraw.aaellipse(k,d,t,50,20,BLACK)
    
d = a - 55
t = b - 25
pygame.gfxdraw.filled_ellipse(k,d,t,50,20,WHITE)
pygame.gfxdraw.aaellipse(k,d,t,50,20,BLACK)
    
pygame.gfxdraw.filled_ellipse(k,a,b,50,20,YELLOW)
    
d = a - 90
t = b + 5
pygame.gfxdraw.filled_ellipse(k,d,t,50,20,WHITE)
pygame.gfxdraw.aaellipse(k,d,t,50,20,BLACK)

pygame.gfxdraw.filled_ellipse(k,a,b,50,20,YELLOW)

d = a + 80
t = b
pygame.gfxdraw.filled_ellipse(k,d,t,50,20,WHITE)
pygame.gfxdraw.aaellipse(k,d,t,50,20,BLACK)
      
d = a - 40
t = b + 20
pygame.gfxdraw.filled_ellipse(k,d,t,50,20,WHITE)
pygame.gfxdraw.aaellipse(k,d,t,50,20,BLACK)
    
d = a + 40
t = b + 25
pygame.gfxdraw.filled_ellipse(k,d,t,50,20,WHITE)
pygame.gfxdraw.aaellipse(k,d,t,50,20,BLACK)

flower1 = pygame.transform.scale(k, (k.get_width()//4,k.get_height()//4))
flower2 = pygame.transform.scale(k, (k.get_width()//5,k.get_height()//5))

def flower_1(x,y,g):
    sc.blit(pygame.transform.rotate(flower1, g), (x,y)) 

flower_1(440,530,20)
flower_1(510,630,-10)

def flower_2(x,y,g):
    sc.blit(pygame.transform.rotate(flower2, g), (x,y))
    
flower_2(530,550, -30)
flower_2(450,600,20)
flower_2(520,590,-40)

pygame.gfxdraw.filled_ellipse(sc,180,580,60,25,WHITE)

neck = pygame.Surface((500,500))
neck.fill(GREEN)
neck.set_colorkey(GREEN)

horns = pygame.Surface((60,80))
horns.set_colorkey(BLACK)
horn1  = pygame.Surface((600,600))
horn1.fill(GREEN)
horn1.set_colorkey(GREEN)
polygon(horn1, WHITE, [(50,50),(54,58),(60,62),(68,64),(74,74),(70,74),(60,68),(56,64),(54,60),(52,56),(50,50)],0)
horn2 = horn1.copy()


horns.blit(horn1,(-30,-30))
horns.blit(horn2, (-40, -25))
sc.blit(horns,(199,421))

pygame.gfxdraw.filled_ellipse(neck,122,130,50,18,WHITE)

sc.blit(pygame.transform.rotate(neck,90),(100,150))

head = pygame.Surface((500,500))
head.fill(GREEN)
head.set_colorkey(GREEN)
pygame.gfxdraw.filled_ellipse(head,142,319,22,14,WHITE)
pygame.gfxdraw.filled_circle(head,140,317,9,PURPLE)
pygame.gfxdraw.filled_circle(head,143,316,4,BLACK)

sc.blit(head, (100,150))

eye = pygame.Surface((1200,700))
eye.fill(GREEN)
eye.set_colorkey(GREEN)
pygame.gfxdraw.filled_ellipse(eye,885,665,70,30,WHITE)
eyeball = pygame.transform.scale(eye, (eye.get_width()//16,eye.get_height()//16))

sc.blit(pygame.transform.rotate(eyeball,-30),(190,400))

leg = pygame.Surface((600,600))
leg.fill(GREEN)
leg.set_colorkey(GREEN)
pygame.gfxdraw.filled_ellipse(leg,88,63,24,10,WHITE)
pygame.gfxdraw.filled_ellipse(leg,107,37,24,10,WHITE)
pygame.gfxdraw.filled_ellipse(leg,88,120,24,10,WHITE)
pygame.gfxdraw.filled_ellipse(leg,107,100,24,10,WHITE)

pygame.gfxdraw.filled_ellipse(leg,46,63,20,10,WHITE)
pygame.gfxdraw.filled_ellipse(leg,65,37,20,10,WHITE)
pygame.gfxdraw.filled_ellipse(leg,46,120,20,10,WHITE)
pygame.gfxdraw.filled_ellipse(leg,65,100,20,10,WHITE)

sc.blit(pygame.transform.rotate(leg,90),(100,100))

foot = pygame.Surface((600,600))
foot.fill(GREEN)
foot.set_colorkey(GREEN)
pygame.gfxdraw.filled_ellipse(foot,21,160,10,7,WHITE)
pygame.gfxdraw.filled_ellipse(foot,84,160,10,7,WHITE)
pygame.gfxdraw.filled_ellipse(foot,47,179,10,7,WHITE)
pygame.gfxdraw.filled_ellipse(foot,104,179,10,7,WHITE)

sc.blit(foot, (120,500))
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()


# In[7]:


import pygame
import pygame.gfxdraw
from pygame.draw import*
import numpy

pygame.init()

WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (180,210,245)
GRAY = (180,180,180)
LIME = (160,255,130)
GREEN = (140,235,70)
YELLOW = (255,255,0)
PURPLE = (230, 130, 200)
RED = (255,0,0)
sc = pygame.display.set_mode((620, 760))

sc.fill(BLUE)

polygon(sc, GRAY, [(0,280), (80,80),(150,220), (230, 120), (370,360), (480, 100), (520, 140), (620, 20), (620, 430), (0,430), (0,280)], 0)
aalines(sc, BLACK, False, [(0,280), (80,80),(150,220), (230, 120), (370,360), (480, 100), (520, 140), (620, 20)])

back = pygame.Surface((620, 760))
back.fill(GRAY)
sc.blit(back, (0,430))

polygon(sc, LIME, [(0,455), (30,445), (60,440), (76,440), (136, 435), (300, 435), (307, 437), (310, 436), (312,440), (316,443), (316,460), (318,462), (318, 500), (325,502),(330,504),(620,504), (620,760), (0,760),(0,455)], 0)
aalines(sc, BLACK, False, [(0,455), (30,445), (60,440), (76,440), (136, 435), (300, 435), (307, 437), (310, 436), (312,440), (316,443), (316,460), (318,462), (318, 500), (325,502),(330,504),(620,504)])

flower = pygame.Surface((620,760))
flower.fill(RED)
flower.set_colorkey(RED)
circle(flower, GREEN, (520, 640), 90)

k = pygame.Surface((400,400))
k.fill(RED)
k.set_colorkey(RED)

a = 200
b = 200

d = a 
t = b - 35
pygame.gfxdraw.filled_ellipse(k,d,t,50,20,WHITE)
pygame.gfxdraw.aaellipse(k,d,t,50,20,BLACK)
    
d = a + 55
t = b - 20
pygame.gfxdraw.filled_ellipse(k,d,t,50,20,WHITE)
pygame.gfxdraw.aaellipse(k,d,t,50,20,BLACK)
    
d = a - 55
t = b - 25
pygame.gfxdraw.filled_ellipse(k,d,t,50,20,WHITE)
pygame.gfxdraw.aaellipse(k,d,t,50,20,BLACK)
    
pygame.gfxdraw.filled_ellipse(k,a,b,50,20,YELLOW)
    
d = a - 90
t = b + 5
pygame.gfxdraw.filled_ellipse(k,d,t,50,20,WHITE)
pygame.gfxdraw.aaellipse(k,d,t,50,20,BLACK)

pygame.gfxdraw.filled_ellipse(k,a,b,50,20,YELLOW)

d = a + 80
t = b
pygame.gfxdraw.filled_ellipse(k,d,t,50,20,WHITE)
pygame.gfxdraw.aaellipse(k,d,t,50,20,BLACK)
      
d = a - 40
t = b + 20
pygame.gfxdraw.filled_ellipse(k,d,t,50,20,WHITE)
pygame.gfxdraw.aaellipse(k,d,t,50,20,BLACK)
    
d = a + 40
t = b + 25
pygame.gfxdraw.filled_ellipse(k,d,t,50,20,WHITE)
pygame.gfxdraw.aaellipse(k,d,t,50,20,BLACK)

flower1 = pygame.transform.scale(k, (k.get_width()//4,k.get_height()//4))
flower2 = pygame.transform.scale(k, (k.get_width()//5,k.get_height()//5))

def flower_1(x,y,g):
    flower.blit(pygame.transform.rotate(flower1, g), (x,y)) 

flower_1(420,530,20)
flower_1(490,630,-10)

def flower_2(x,y,g):
    flower.blit(pygame.transform.rotate(flower2, g), (x,y))
    
flower_2(510,550, -30)
flower_2(430,600,20)
flower_2(500,590,-40)

animal = pygame.Surface((620,760))
animal.fill(RED)
animal.set_colorkey(RED)

body = pygame.Surface((620,760))
body.fill(RED)
body.set_colorkey(RED)
pygame.gfxdraw.filled_ellipse(body,180,580,60,25,WHITE)

neck = pygame.Surface((500,500))
neck.fill(GREEN)
neck.set_colorkey(GREEN)

horns = pygame.Surface((60,80))
horns.set_colorkey(BLACK)
horn1  = pygame.Surface((600,600))
horn1.fill(GREEN)
horn1.set_colorkey(GREEN)
polygon(horn1, WHITE, [(50,50),(54,58),(60,62),(68,64),(74,74),(70,74),(60,68),(56,64),(54,60),(52,56),(50,50)],0)
horn2 = horn1.copy()


horns.blit(horn1,(-30,-30))
horns.blit(horn2, (-40, -25))

#sc.blit(horns,(199,421))

pygame.gfxdraw.filled_ellipse(neck,122,130,50,18,WHITE)

#sc.blit(pygame.transform.rotate(neck,90),(100,150))

head = pygame.Surface((500,500))
head.fill(GREEN)
head.set_colorkey(GREEN)

pygame.gfxdraw.filled_ellipse(head,142,319,22,14,WHITE)
pygame.gfxdraw.filled_circle(head,140,317,9,PURPLE)
pygame.gfxdraw.filled_circle(head,143,316,4,BLACK)

#sc.blit(head, (100,150))

eye = pygame.Surface((1200,700))
eye.fill(GREEN)
eye.set_colorkey(GREEN)
pygame.gfxdraw.filled_ellipse(eye,885,665,70,30,WHITE)
eyeball = pygame.transform.scale(eye, (eye.get_width()//16,eye.get_height()//16))

#sc.blit(pygame.transform.rotate(eyeball,-30),(190,400))

leg = pygame.Surface((600,600))
leg.fill(GREEN)
leg.set_colorkey(GREEN)

pygame.gfxdraw.filled_ellipse(leg,88,63,24,10,WHITE)
pygame.gfxdraw.filled_ellipse(leg,107,37,24,10,WHITE)
pygame.gfxdraw.filled_ellipse(leg,88,120,24,10,WHITE)
pygame.gfxdraw.filled_ellipse(leg,107,100,24,10,WHITE)

pygame.gfxdraw.filled_ellipse(leg,46,63,20,10,WHITE)
pygame.gfxdraw.filled_ellipse(leg,65,37,20,10,WHITE)
pygame.gfxdraw.filled_ellipse(leg,46,120,20,10,WHITE)
pygame.gfxdraw.filled_ellipse(leg,65,100,20,10,WHITE)

#sc.blit(pygame.transform.rotate(leg,90),(100,100))

foot = pygame.Surface((600,600))
foot.fill(GREEN)
foot.set_colorkey(GREEN)

pygame.gfxdraw.filled_ellipse(foot,21,160,10,7,WHITE)
pygame.gfxdraw.filled_ellipse(foot,84,160,10,7,WHITE)
pygame.gfxdraw.filled_ellipse(foot,47,179,10,7,WHITE)
pygame.gfxdraw.filled_ellipse(foot,104,179,10,7,WHITE)

#sc.blit(foot, (120,500))

animal.blit(horns,(199,421))
animal.blit(pygame.transform.rotate(neck,90),(100,150))
animal.blit(head, (100,150))
animal.blit(pygame.transform.rotate(eyeball,-30),(190,400))
animal.blit(pygame.transform.rotate(leg,90),(100,100))
animal.blit(foot, (120,500))
animal.blit(body, (0,0))

animal1 = pygame.transform.scale(animal, (animal.get_width()*2, animal.get_height()*2))
animal2 = pygame.transform.scale(animal, (animal.get_width()//2, animal.get_height()//2))
animal3 = pygame.transform.scale(animal, (animal.get_width()//2, animal.get_height()//2))
animal4 = pygame.transform.scale(animal, (animal.get_width()//2, animal.get_height()//2))
animal5 = pygame.transform.scale(animal, (720,860))
animal6 = pygame.transform.flip(animal5,True,False)
animal7 = pygame.transform.flip(animal4,True,False)

bush1 = pygame.transform.scale(flower, (flower.get_width()//3, flower.get_height()//3))
bush2 = pygame.transform.scale(flower, (flower.get_width()//3, flower.get_height()//3))
bush3 = pygame.transform.scale(flower, (flower.get_width()//3, flower.get_height()//3))
bush4 = pygame.transform.scale(flower, (360,450))
bush5 = pygame.transform.scale(flower, (280, 350))
bush6 = pygame.transform.scale(flower, (420, 560))

#sc.blit(flower, (0,0))

sc.blit(bush1, (-152,261))
sc.blit(bush2, (270,323))
sc.blit(bush3, (450,520))
sc.blit(bush4, (180,300))
sc.blit(bush5, (360,200))
sc.blit(bush6, (260,150))

#sc.blit(animal, (0,0))

sc.blit(animal1, (-400,-350))
sc.blit(animal2, (160,130))
sc.blit(animal3, (80,220))
sc.blit(animal6, (115,-52))
sc.blit(animal7, (80,270))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()


# In[ ]:





# In[ ]:





# In[ ]:




