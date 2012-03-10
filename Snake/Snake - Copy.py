##BUGS:
##Snake collision with itself to be detected

class Zaka():
    def __init__ (self):
        self.x=0
        self.y=0
        self.move_x=0
        self.move_y=0
        self.points=0
        self.length=0
        self.blitpos=[[0,0]]
        self.name_surface = my_font.render(repr(self.points), True, (0, 255, 0), (0,0,0))

    def reset(self):
        self.x=0
        self.y=0
        self.move_x=0
        self.move_y=0
        self.points=0
        self.length=0
        self.blitpos=[[0,0]]
        self.name_surface = my_font.render(repr(self.points), True, (0, 255, 0), (0,0,0))

def HighScore(score):
    t1 = menufont.render("Enter your name", True, (255,255,255))
    j=True
    PName=""
    while j:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if pygame.key.name(event.key)=='return':
                    j = not j
                elif pygame.key.name(event.key) == 'backspace':
                    PName=PName[:len(PName)-1]
                else:
                    PName=PName+pygame.key.name(event.key)
        screen.fill((0,0,0))
        screen.blit(t1, (0,0))
        img=menufont.render(PName, True,(255,255,255))
        screen.blit(img,(0,t1.get_height()+10))
        pygame.display.update()
    HSS.Wscore(PName, repr(score))

def DispHighScore():
    [names,scores]=HSS.Sscore()
    i=0
    screen.fill((0,0,0))
    j=True
    for name in names:
        if i==10:
            break
        name=name[:len(name)-2]+" "+scores[i][:len(scores[i])-2]
        img=menufont.render(name,True,(255,255,255))
        screen.blit(img,(0,i*img.get_height()+10))
        i=i+1
    pygame.display.update()                          
    while j:
        for event in pygame.event.get():
            if event.type==KEYDOWN:
                if event.key==K_r:
                    j=False

def HSLimit():
    [names,scores]=HSS.Sscore()
##    temp=scores[0]
##    temp=int(temp[:len(temp)-2])
##    for score in scores:
##        if (int(score[:len(score)-2])<temp):
##            temp=int(score[:len(score)-2])
    return int(scores[9])

def getfood():
    return [random.randint(0+w,640-w),random.randint(0+h,480-h)]

def mainmenu():
    HSS.sort()
    MC=(100,150,150)
    WHITE=(255,255,255)
    while True:
        j=0
        bg=pygame.image.load('bg1.jpg')
        #t1=pygame.image.load('t1.jpg').convert_alpha()
        t1 = my_font.render("Zaka", True, (255, 185, 205), WHITE)
        t2 = menufont.render("New Game", True, MC, WHITE)
        t3 = menufont.render("Instructions", True, MC, WHITE)
        t4 = menufont.render("High Scores", True, MC, WHITE)
        t5 = menufont.render("Exit", True, MC, WHITE)
        #screen.fill((0,0,0))
        screen.blit(bg, (0,0))
        sx=screen.get_rect().centerx
        screen.blit(t1, (sx-t1.get_width()/2,20))
        screen.blit(t2, (sx-t2.get_width()/2,80))
        screen.blit(t3, (sx-t3.get_width()/2,140))
        screen.blit(t4, (sx-t4.get_width()/2,200))
        screen.blit(t5, (sx-t5.get_width()/2,260))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_n:
                    j=1                
            if event.type == MOUSEBUTTONDOWN:
                (a,b)=pygame.mouse.get_pos()
                if (t2.get_rect().collidepoint((a-sx+t2.get_width()/2,b-80))):
                    j=1
                if (t3.get_rect().collidepoint((a-sx+t3.get_width()/2,b-140))):
                    t6=my_font.render("I pity the foo'!", True, WHITE, MC)
                    screen.blit(t6, (sx-t6.get_width()/2,480-t6.get_height()))
                    pygame.display.update((sx-t6.get_width()/2,480-t6.get_height(),t6.get_width(),t6.get_height()))
                    time.sleep(2)
                if (t4.get_rect().collidepoint((a-sx+t4.get_width()/2,b-200))):
                    DispHighScore()
                if (t5.get_rect().collidepoint((a-sx+t5.get_width()/2,b-260))):
                    pygame.quit()
                    exit()
        pygame.display.update()
        if j==1:
            break

def MToggleOn():
    pygame.mixer.music.play(-1,0.0)

def MToggleOff():
    pygame.mixer.music.stop()
    
def gameend():
    MToggleOff()
    while True:
        j=0
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
                    j=1
                if event.key == K_m:
                    j=2
        pygame.display.update()
        if j!=0:
            MToggleOn()
            if j==2:
                mainmenu()
            break

def newgame():
    zeta.reset()
    HSS.sort()

import pygame, random, time
import HSS
from pygame.locals import *
from sys import exit
pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)
###background = pygame.image.load(bg).convert()
food=pygame.image.load('food.jpg').convert()
w=10
h=10
clock=pygame.time.Clock()
##x, y = 0, 0
##move_x, move_y = 0, 0
[fdx,fdy]=getfood()
##points =0
##length=0
frate=30
speed=10
##blitpos=[[0,0]]
my_font = pygame.font.SysFont("Analog", 32)
menufont = pygame.font.SysFont("Verdana", 16)
##name_surface = my_font.render(repr(points), True, (0, 255, 0), (0,0,0))
pygame.mixer.music.load('rhbattle.mid')
MToggleOn()
mainmenu()
zeta=Zaka()
eatSound=pygame.mixer.Sound('eat.wav')
endSound=pygame.mixer.Sound('awh_man.wav')
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
            elif event.key == K_m:
                if(pygame.mixer.music.get_busy()):
                    MToggleOff()
                else:
                    MToggleOn()
            elif event.key == K_q or event.key == K_ESCAPE:
                pygame.quit()
                exit()
    time_passed=clock.tick(frate)
    tps=time_passed/1000.0
    ###x= min((640-w),max(0,x+move_x*tps))
    zeta.x=zeta.x+zeta.move_x*tps
    zeta.y=zeta.y+zeta.move_y*tps
    if (zeta.x>640-w or zeta.x<0 or zeta.y<0 or zeta.y>480-h):
        endSound.play(0,0.0)
        if(zeta.points>HSLimit()):
                HighScore(zeta.points)
        gameend()
        newgame()
        continue
    for i in range(zeta.length,0,-1):
        if (pygame.Rect(zeta.blitpos[i][0],zeta.blitpos[i][1],w,h).collidepoint(zeta.x+2,zeta.y+2)):
            endSound.play(0,0.0)
            if(zeta.points>HSLimit()):
                HighScore(zeta.points)
            gameend()
            newgame()
            continue
    ###y= min((480-h),max(0,y+move_y*tps))
    for i in range(zeta.length,0,-1):   
        zeta.blitpos[i]=zeta.blitpos[i-1]
    zeta.blitpos[0]=[int(zeta.x),int(zeta.y)]
##    if (int(zeta.x+w/2) in range(fdx-w/2,fdx+w/2) and int(zeta.y+h/2) in range(fdy-h/2, fdy+h/2)):
    if(fdx in range(zeta.x,zeta.x+w) and fdy in range(zeta.y,zeta.y+h)):
           [fdx,fdy]=getfood()
           eatSound.play(0,0.0)
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

