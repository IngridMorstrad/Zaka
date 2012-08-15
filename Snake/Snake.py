##TO FIX:
##    Contiguous snake glitch
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
##    Customizable snakes (Colour)
##    Customizable screen size
##    Correct snake size (customizable?)
##    Separate music and sound toggle

class Zaka():
    """Class that defines the Zaka"""
    def __init__ (self):
        """Initialize a new Zaka to the top left of the screen"""
        self.x=0
        self.y=0
        self.move_x=0
        self.move_y=0
        self.points=0
        self.length=0
        self.blitpos=[[0,0]]
        self.name_surface = my_font.render(repr(self.points), True, (0, 255, 0), (0,0,0))

    def reset(self):
        """Resets the Zaka's position to the top left of the screen"""
        self.x=0
        self.y=0
        self.move_x=0
        self.move_y=0
        self.points=0
        self.length=0
        self.blitpos=[[0,0]]
        self.name_surface = my_font.render(repr(self.points), True, (0, 255, 0), (0,0,0))

def HighScore(score):
    """Screen displayed when a new high score is set"""
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
                ## Add escape
                ## Add mouse-back
                if event.key==K_r:
                    return
                elif event.key == K_s:
                    SToggle()
                elif event.key == K_q or event.key == K_ESCAPE:
                    pygame.quit()
                    exit()

def HSLimit():
    [names,scores]=HSS.Sscore()
##    temp=scores[0]
##    temp=int(temp[:len(temp)-2])
##    for score in scores:
##        if (int(score[:len(score)-2])<temp):
##            temp=int(score[:len(score)-2])
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
                    ## TO ADD
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
    
def gameend():
    while True:
        name_surface = my_font.render("Game over", True, (255,255,255))
        screen.fill((0,0,0))
        screen.blit(name_surface, (screen.get_rect().centerx-name_surface.get_width()/2,screen.get_rect().centery-name_surface.get_height()/2))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_q or event.key == K_ESCAPE:
                    pygame.quit()
                    exit()
                if event.key == K_n:
                    SToggle()
                    SToggle()
                    return
                if event.key == K_r or pygame.key.name(event.key)=='return':
                    SToggle()
                    SToggle()
                    mainmenu()
                    return
        pygame.display.update()

def newgame():
    zeta.reset()

import pygame, random, time, math
import HSS
from pygame.locals import *
from sys import exit
pygame.init()
SCREEN_WIDTH=700
SCREEN_HEIGHT=500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
###background = pygame.image.load(bg).convert()
food=pygame.image.load('pics/food.jpg').convert()
imw=food.get_width()
imh=food.get_height()
w=10
h=10
clock=pygame.time.Clock()
##x, y = 0, 0
##move_x, move_y = 0, 0
[fdx,fdy]=getfood()
##points =0
##length=0
frate=30
speed=30
##blitpos=[[0,0]]
my_font = pygame.font.SysFont("Analog", 32)
menufont = pygame.font.SysFont("Verdana", 16)
##name_surface = my_font.render(repr(points), True, (0, 255, 0), (0,0,0))
pygame.mixer.music.load('sounds/rhbattle.mid')
pygame.mixer.music.play(-1)
eatSound=pygame.mixer.Sound('sounds/eat.wav')
endSound=pygame.mixer.Sound('sounds/awh_man.wav')
SoundsWanted=True
mainmenu()
zeta=Zaka()
newgame()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if (event.key == K_LEFT and zeta.move_x==0) :
                zeta.move_x = -w*speed
                zeta.move_y = 0
            elif (event.key == K_RIGHT and zeta.move_x==0):
                zeta.move_x = +w*speed
                zeta.move_y = 0
            elif (event.key == K_UP and zeta.move_y==0):
                zeta.move_y = -h*speed
                zeta.move_x = 0
            elif (event.key == K_DOWN and zeta.move_y==0):
                zeta.move_y = +h*speed
                zeta.move_x = 0
            elif event.key == K_s:
                SToggle()
            elif event.key == K_q or event.key == K_ESCAPE:
                pygame.quit()
                exit()
    time_passed=clock.tick(frate)
    tps=time_passed/1000.0
    ###x= min((SCREEN_WIDTH-w),max(0,x+move_x*tps))
    zeta.x=zeta.x+min(int(zeta.move_x*tps),w)
    zeta.y=zeta.y+min(int(zeta.move_y*tps),h)
    if (zeta.x>SCREEN_WIDTH-w or zeta.x<0 or zeta.y<0 or zeta.y>SCREEN_HEIGHT-h):
        endSounds()
        if(zeta.points>HSLimit()):
            HighScore(zeta.points)
        gameend()
        newgame()
        continue
    for i in range(zeta.length,0,-1):
        if (pygame.Rect(zeta.blitpos[i][0],zeta.blitpos[i][1],w,h).collidepoint(zeta.x+5,zeta.y+5)):
            if(zeta.points>HSLimit()):
                HighScore(zeta.points)
            gameend()
            newgame()
            continue
    ###y= min((SCREEN_HEIGHT-h),max(0,y+move_y*tps))
    for i in range(zeta.length,0,-1):   
        zeta.blitpos[i]=zeta.blitpos[i-1]
    zeta.blitpos[0]=[zeta.x,zeta.y]
    if (pygame.Rect(zeta.x,zeta.y,w,h).colliderect(pygame.Rect(fdx,fdy,imw,imh))):
           [fdx,fdy]=getfood()
           if SoundsWanted:
               eatSound.play(0,0)
           zeta.points+=10
           zeta.name_surface = my_font.render(repr(zeta.points), True, (0, 255, 0), (0, 0, 0))
           ###blitpos.append([int(x-move_x/10*(length+1)),int(y-move_y/10*(length+1))])
           zeta.blitpos.append([-25,-25])
           zeta.length+=1
    screen.fill((0, 0, 0))
    screen.blit(zeta.name_surface, (screen.get_width()/2,screen.get_height()/2))
    screen.blit(food, (fdx,fdy))
    for [a,b] in zeta.blitpos:
        screen.fill((240,240,240),(a,b,w,h))
    pygame.display.update()

