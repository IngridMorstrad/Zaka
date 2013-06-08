##TO FIX:
##    Contiguous Zaka glitch
##    COMMIT
##    Refactor Zaka into functions
##    Better graphics for Zaka
##    High score display
##    Comment/format whole code
##    Admin mode to change/reset high scores
##    Fix high score name entry (uppercase chars)
##    Better music...
##    Better sounds
##    COMMIT - Adjustable speed
##    Customizable Zaka (Colour)
##    Customizable screen size
##    Correct Zaka size (customizable?)
##    Separate music and sound toggle


def NewZaka():
    return [0,0,0,0,0,[[0,0]]]

def HighScore(score):
    """Screen displayed when a new high score is set"""
    ## Make t1 image
    t1 = menufont.render("Enter your name", True, (255,255,255))
    PName=""
    pygame.key.set_repeat(500,50)
    permKeys = range(48,58)+range(97,123)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if pygame.key.name(event.key)=='return':
                    pygame.key.set_repeat()
                    HSS.Wscore(PName, score)
                    return
                elif pygame.key.name(event.key) == 'backspace':
                    PName=PName[:-1]
                elif event.key == 32: ## Space
                    PName=PName+" "
                elif event.key in permKeys:
                    ## 48: '0' 57: '9' 97: 'a' 122: 'z'
                    ## Only numbers, space and smallcase letters allowed.
                    PName=PName+pygame.key.name(event.key)
                    ## print pygame.key.name(event.key), event.key, pygame.key.get_mods()
        screen.fill((0,0,0))
        screen.blit(t1, (0,0))
        img=menufont.render(PName, True,(255,255,255))
        screen.blit(img,(0,t1.get_height()+10))
        pygame.display.update()

def DispHighScore():
    """Displays high scores"""
    [names,scores]=HSS.Sscore()
    screen.fill((0,0,0))
    for i,name in enumerate(names):
        name="%s %s %s" %(i+1,name,scores[i])
        img=menufont.render(name,True,(255,255,255))
        screen.blit(img,(0,i*img.get_height()+10))
    pygame.display.update()                          
    while True:
        for event in pygame.event.get():
            if event.type==KEYDOWN:
                ## Add mouse-back??
                if event.key==K_r:
                    return
                elif event.key == K_s:
                    SToggle()
                elif event.key == K_q or event.key == K_ESCAPE:
                    pygame.quit()
                    exit()

def HSLimit():
    [names,scores]=HSS.Sscore()
    if len(scores)>9:
        return int(scores[-1])
    return 0

def getfood():
    return [random.randint(0+w,SCREEN_WIDTH-w),random.randint(0+h,SCREEN_HEIGHT-h)]

def mainmenu():
    MC=(100,150,150)
    WHITE=(255,255,255)
    while True:
        j=0
        bg=pygame.image.load('pics/background.jpg')
        screen.blit(bg, (0,0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_n:
                    j=1                
                elif event.key == K_h:
                    DispHighScore()
                elif event.key == K_s:
                    SToggle()
                elif event.key == K_q or event.key == K_ESCAPE:
                    pygame.quit()
                    exit()
            if event.type == MOUSEBUTTONDOWN:
                (a,b)=pygame.mouse.get_pos()
                ## IMAGE SPECIFIED BUTTON HEIGHTS/WIDTHS
                if (pygame.Rect(275,235,162,50).collidepoint((a,b))):
                    j=1
                if (pygame.Rect(275,300,162,50).collidepoint((a,b))):
                    ## TO ADD INSTRUCTIONS
                    pass
                if (pygame.Rect(275,365,162,50).collidepoint((a,b))):
                    DispHighScore()
                if (pygame.Rect(275,425,162,50).collidepoint((a,b))):
                    pygame.quit()
                    exit()
        pygame.display.update()
        if j==1:
            break

def SStop():
    pygame.mixer.music.set_volume(0.0)

def SToggle():
    global SoundsWanted
    SoundsWanted = not SoundsWanted 
    if SoundsWanted:
        pygame.mixer.music.set_volume(1.0)
    else:
        SStop()

def endSounds():
    SStop()
    endSound.play(0,0)

def updateZaka(zetas):
    global fdx, fdy
    new_zetas=[]
    for zeta in zetas:
        x,y,move_x,move_y,points,blitpos=zeta
        ## REMOVING TIME DEPENDENCY
        ##x+=min(int(move_x*tps),w)
        ##y+=int(move_y*tps)
        x+=move_x
        y+=move_y
        ENDGAME=False
        if (x>SCREEN_WIDTH-w or x<0 or y<0 or y>SCREEN_HEIGHT-h):
            ENDGAME=True
        for z in blitpos[1:]:
            if (pygame.Rect(z[0],z[1],w,h).collidepoint(x+5,y+5)):
                ENDGAME=True
        if ENDGAME:
            endgame(zetas)
            for z in zetas:
                new_zetas.append(NewZaka())
            return new_zetas
        blitpos=[[x,y]]+blitpos[:-1]
        if (pygame.Rect(x,y,w,h).colliderect(pygame.Rect(fdx,fdy,imw,imh))):
               fdx,fdy=getfood()
               if SoundsWanted:
                   eatSound.play(0,0)
               points+=10
               blitpos.append([-25,-25])
        zeta=[x,y,move_x,move_y,points,blitpos]
        new_zetas.append(zeta)
    return new_zetas

def endgame(zetas):
    endSounds()
    if len(zetas)==1:
        points=zetas[0][4]
        if(points>HSLimit()):
            HighScore(points)
    ## Convert to image
    name_surface = my_font.render("Game over", True, (255,255,255))
    screen.fill((0,0,0))
    screen.blit(name_surface, (screen.get_rect().centerx-name_surface.get_width()/2,screen.get_rect().centery-name_surface.get_height()/2))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_q or event.key == K_ESCAPE:
                    pygame.quit()
                    exit()
                elif event.key == K_n:
                    SToggle()
                    SToggle()
                    return 
                elif event.key == K_r or pygame.key.name(event.key)=='return':
                    SToggle()
                    SToggle()
                    mainmenu()
                    return

def displayZaka(zetas):
    screen.fill((0, 0, 0))
    for zeta in zetas:
        x,y,move_x,move_y,points,blitpos=zeta
        # Have to change for more than one zeta
        name_surface = my_font.render(repr(points), True, (0, 255, 0), (0, 0, 0))
        screen.blit(name_surface, (screen.get_width()/2,screen.get_height()/2))
        for [a,b] in blitpos:
            ## Change colour for other Zakas
            screen.fill((240,240,240),(a,b,w,h))
    screen.blit(food, (fdx,fdy))
    pygame.display.update()

def keyPress(zetas):
    new_zetas=[]
    for zeta in zetas:
        move_x=zeta[2]
        move_y=zeta[3]
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == KEYDOWN:
                ## Statements commented, remove time dependency
                ## To fix, have to work with appending to Zaka
                ## when food is eaten
                if (event.key == K_LEFT and move_x==0) :
                    ##move_x = -w*speed
                    move_x = -w
                    move_y = 0
                elif (event.key == K_RIGHT and move_x==0):
                    ##move_x = +w*speed
                    move_x = +w
                    move_y = 0
                elif (event.key == K_UP and move_y==0):
                    ##move_y = -h*speed
                    move_y = -h
                    move_x = 0
                elif (event.key == K_DOWN and move_y==0):
                    ##move_y = +h*speed
                    move_y = +h
                    move_x = 0
                elif event.key == K_s:
                    SToggle()
                elif event.key == K_q or event.key == K_ESCAPE:
                    pygame.quit()
                    exit()
            zeta[2]=move_x
            zeta[3]=move_y
        new_zetas.append(zeta)
    return new_zetas


import pygame, random, time, math
import HSS
from pygame.locals import *
from sys import exit

pygame.init()
## Refactor into one function
SCREEN_WIDTH=700
SCREEN_HEIGHT=500
clock=pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
my_font = pygame.font.SysFont("Trebuchet MS", 28)
menufont = pygame.font.SysFont("Verdana", 16)
eatSound=pygame.mixer.Sound('sounds/eat.wav')
endSound=pygame.mixer.Sound('sounds/awh_man.wav')
food=pygame.image.load('pics/food.jpg').convert()
pygame.mixer.music.load('sounds/rhbattle.mid')
pygame.mixer.music.play(-1)
SoundsWanted=True
imw=food.get_width()
imh=food.get_height()
w=10
h=10
fdx,fdy=getfood()
frate=30
speed=30
mainmenu()
zetas=[]
zetas.append(NewZaka())
name_surface = my_font.render(repr(0), True, (0, 255, 0), (0, 0, 0))
## Refactor to NEWGAME function
while True:
    zetas=keyPress(zetas)
    time_passed=clock.tick(frate)
    tps=time_passed/1000.0
    zetas=updateZaka(zetas)
    displayZaka(zetas)

