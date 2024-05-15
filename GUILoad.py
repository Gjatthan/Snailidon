import pygame as p
from random import randint
import GUIStart as g

class GUILoad(p.sprite.Sprite):
    def __init__(self,x):
        super().__init__()
        self.image=p.surface.Surface((13,40))
        self.image.fill((60,60,80))
        self.rect=self.image.get_rect(topleft=(100+x,400))

def main():   
    p.init()
    window=p.display.set_mode((800,500))
    title=p.image.load(r'E:\backup 28.12.22\E\title2.png')
    icon=p.image.load(r'E:\backup 28.12.22\E\snail1.png').convert_alpha()
    p.display.set_caption("")
    p.display.set_icon(icon)
    windowclr=p.surface.Surface((800,500))
    load_font=p.font.Font(r'E:\backup 28.12.22\E\nasalization-rg.otf',20)
    load=p.sprite.Group()
    x=0
    for _ in range(40):
        load.add(GUILoad(x))
        x+=15
    lis=load.sprites() #lis will contain 30 surface to illuminate the loading animation
    y=0 
    i=1 #to display ....
    while True:
        for event in p.event.get():
            if event.type==p.QUIT:
                exit(0)
        if y==randint(0,100):
            lis[y].image.fill('#12ef22')
            y+=1
            if y==40:
                break
        window.blit(windowclr,(0,0))
        load.draw(window)
        window.blit(title,(240,30))
        load_txt=load_font.render("L o a d i n g"+i*" . ",False,'#12ef22')
        i+=1
        if i==5: i=1
        window.blit(load_txt,(100,360))     
        p.display.update()
    g.GUIStart()

if __name__=='__main__':
    main()