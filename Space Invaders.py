import pygame
import sys
from pygame import mixer
import math
import random

mixer.init()
pygame.init()

surface=pygame.display.set_mode((1500,900))
pygame.display.set_caption('Space Invaders')

color=("black")

score=0
#scorefont
sfont=pygame.font.Font('freesansbold.ttf',25)
#gameoverfont
gfont=pygame.font.Font('freesansbold.ttf',80)

def showscore(x,y):
    stext=sfont.render("Score = "+str(score),True,"white")
    surface.blit(stext,(x,y))

#COLLISION
def collision(x1,x2,y1,y2):
    d=math.sqrt((math.pow(x1-x2,2))+(math.pow(y1-y2,2)))
    if d<50:
        return True
    else:
        return False
#showscore(20,20)

def showgameov(x,y):
    gtext=gfont.render("GAME OVER...",True,"red")
    surface.blit(gtext,(x,y))


#PLAYER  
px=600
pxd=0
py=670

p1=pygame.image.load("player1.png")
p1=pygame.transform.scale(p1,(300,300))

def player(x,y):
    surface.blit(p1,(x,y))

#BULLET
bx=700
by=700
byd=5
bstate="rest"
b1=pygame.image.load("bullet.png")
b1=pygame.transform.scale(b1,(150,200))

def bullet(x,y):
    global bstate
    bstate="fire"
    surface.blit(b1,(x,y))

#INVADERS
ic=10
invaders=[]
ix=[]
ixd=[]
iy=[]
iyd=[]

for i in range(ic):
    e1=pygame.image.load("enemy1.png")
    e1=pygame.transform.scale(e1,(100,100))
    #add image to list
    invaders.append(e1)
    #placing invaders in random positions
    ix.append(random.randint(20,1400))
    iy.append(random.randint(0,400))
    ixd.append(2)
    iyd.append(30)

def invader(x,y,i):
    #one at a time,
    surface.blit(invaders[i],(x,y))
    


#MUSIC
bg_music = pygame.mixer.Sound("bg music.mp3")
shoot_sound = pygame.mixer.Sound("shoot.wav")
game_over_sound = pygame.mixer.Sound("game over.wav")
bg_music.play(-1)

while True:
    surface.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                pxd = -2
            if event.key == pygame.K_d:
                pxd = 2
            if event.key == pygame.K_SPACE:
                if bstate == "rest":
                    bx = px + 75
                    by = py
                    bullet(bx, by)
                    shoot_sound.play()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                pxd = 0 

    
    for j in range(ic):
        ix[j] += ixd[j]
        if iy[j] > 600:
            if abs(px - ix[j]) < 20:
                for k in range(ic):
                    iy[k] = 1000
                game_over_sound.play()
                showgameov(500, 400)
                pygame.display.update()
                pygame.time.delay(2000)
                pygame.quit()
                sys.exit()

        if ix[j] < 20 or ix[j] > 1400:
            ixd[j] = -ixd[j]
            iy[j] += iyd[j]

        if collision(ix[j], bx, iy[j], by):
            score += 1
            by = 700
            bstate = "rest"
            ix[j] = random.randint(20, 1400)
            iy[j] = random.randint(0, 400)

        invader(ix[j], iy[j], j)

    px += pxd
    if px < -45:
        px = -45
    if px > 1285:
        px = 1285

    if bstate == "fire":
        by -= byd
        bullet(bx, by)
    if by <= 0:
        bstate = "rest"
        by = 700

    showscore(20, 20)
    player(px, py)
    pygame.display.update()
