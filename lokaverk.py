import pygame
import random
import os

WIDTH=800
HEIGHT=600
FPS=60

BLACK=(0,0,0)
WHITE=(255,255,255)

#slóð til að ná í myndir
game_folder=os.path.dirname(__file__)
img_folder=os.path.join(game_folder, "myndir")

pygame.init()
pygame.mixer.init()

#stillingar á glugganum og hversu hraður leikurin á að vera
skjar=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Khaled's tomb")
klukka=pygame.time.Clock()

#bý til klasa fyr spilarann
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #set myndina inn
        self.image= pygame.image.load(os.path.join(img_folder, "flaug/flaug.png")).convert()
        self.image.set_colorkey(BLACK)
        #Set flaugina á byrjunar stað og hraða á 0
        self.rect=self.image.get_rect()
        self.rect.centerx=WIDTH/2
        self.rect.bottom=HEIGHT-20
        self.speedy=0

    def update(self):
        #stilli keybindings
        self.speedy=0
        keystate=pygame.key.get_pressed()
        if keystate[pygame.K_UP]:
            self.speedy=-8
        if keystate[pygame.K_w]:
            self.speedy = -8
        if keystate[pygame.K_DOWN]:
            self.speedy = 8
        if keystate[pygame.K_s]:
            self.speedy = 8

        self.speedx=0
        if keystate[pygame.K_LEFT]:
            self.speedx=-8
        if keystate[pygame.K_a]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        if keystate[pygame.K_d]:
            self.speedx = 8
        self.rect.x +=self.speedx
        self.rect.y +=self.speedy

        #stillingar svo ekki sé hægt að fara af skjánum
        if self.rect.right > WIDTH:
            self.rect.right=WIDTH
        if self.rect.left < 0:
            self.rect.left=0
        if self.rect.top < 0:
            self.rect.top=0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom=HEIGHT

#klasi fyrir loftsteinana
class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #fæ randomtölur úr for lykkjuni til að segja hvora myndinna á að nota
        for x in range(FPS):
            randomtala=random.randint(1, 2)
            if randomtala ==1:
                self.image=pygame.image.load(os.path.join(img_folder, "Fljúgandi hlutir/grjót4.png")).convert()
                self.rect=self.image.get_rect()
                self.image.set_colorkey(WHITE)
                #stilli hraða og staðsetningu
                self.rect.x=random.randrange(WIDTH - self.rect.width)
                self.rect.y=random.randrange(-100, -40)
                self.speedy=random.randrange(1, 8)
                self.speedx=random.randrange(-4, 4)
            else:
                self.image=pygame.image.load(os.path.join(img_folder, "Fljúgandi hlutir/grjót1.png")).convert()
                self.rect=self.image.get_rect()
                self.image.set_colorkey(WHITE)
                self.rect.x=random.randrange(WIDTH - self.rect.width)
                self.rect.y=random.randrange(-100, -40)
                self.speedy=random.randrange(1, 8)
                self.speedx=random.randrange(-4, 4)

    def update(self):
        self.rect.y+=self.speedy
        self.rect.x += self.speedx
        #færir loftsteinana aftur upp eftir að þeir fara út af skjánum
        if self.rect.top > HEIGHT+10 or self.rect.left <-100 or self.rect.right > WIDTH + 80:
            self.rect.x=random.randrange(WIDTH - self.rect.width)
            self.rect.y=random.randrange(-100, -40)
            self.speedy=random.randrange(1, 8)

background=pygame.image.load(os.path.join(img_folder, "background/geimur.png")).convert()
background_rect=background.get_rect()

skip=pygame.sprite.Group()
loftsteinn=pygame.sprite.Group()
player=Player()
skip.add(player)
#býr til 8 loftsteina
for x in range(8):
    s=Mob()
    skip.add(s)
    loftsteinn.add(s)
run=True
while run:
    klukka.tick(FPS)
    for event in pygame.event.get():
        #stoppar leikinn
        if event.type==pygame.QUIT:
            run=False

    #update-ar og stillir backgroundið
    skip.update()
    skjar.fill(BLACK)
    skjar.blit(background, background_rect)
    skip.draw(skjar)
    pygame.display.flip()

pygame.quit()
