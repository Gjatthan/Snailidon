import pygame as p
from random import randint
import Snailidon as s

class Select_Hero():
    def __init__(self):
        p.init()
        self.win=p.display.set_mode((800,500))
        self.hero1=p.transform.smoothscale(p.image.load(r'E:\backup 28.12.22\E\hero13.png'),(130,200))
        self.hero2=p.transform.smoothscale(p.image.load(r'E:\backup 28.12.22\E\hero23.png'),(130,200))
        self.hero3=p.transform.smoothscale(p.image.load(r'E:\backup 28.12.22\E\hero33.png'),(130,200))
        self.back=p.surface.Surface((800,500))
        self.circle_panel=p.surface.Surface((250,350))
        self.back.fill('#ffffff')
        self.font=p.font.Font(r'E:\backup 28.12.22\E\nasalization-rg.otf',40)
        self.font1=p.font.Font(r'E:\backup 28.12.22\E\nasalization-rg.otf',25)
        self.txt=self.font.render("Select Character",False,"#000000")
        self.clock=p.time.Clock()
       
        
        self.display()
    def display(self):
        while True:
            self.win.blit(self.back,(0,0))
            #"#34efa3"
            for e in p.event.get():
                if e.type==p.QUIT:
                    exit(0)
            self.circle_panel.fill('#ffffff')
            for i in range(20):
                p.draw.circle(self.circle_panel,(randint(0,255),randint(0,255),randint(0,255)),(randint(20,150),randint(20,200)),randint(10,20))
            mouse_pos=p.mouse.get_pos()
            if self.hero1.get_rect(center=(200,250)).collidepoint(mouse_pos):
                self.win.blit(self.circle_panel,self.hero1.get_rect(center=(180,250)))
                self.win.blit(self.font1.render("Mr Green",False,(randint(0,255),randint(0,255),randint(0,255))),(130,390))
                if p.mouse.get_pressed()==(True,False,False):
                    s.Main(1)
            if self.hero2.get_rect(center=(400,250)).collidepoint(mouse_pos):
                self.win.blit(self.circle_panel,self.hero2.get_rect(center=(380,250)))
                self.win.blit(self.font1.render("Myztor",False,(randint(0,255),randint(0,255),randint(0,255))),(340,390))
                if p.mouse.get_pressed()==(True,False,False):
                    s.Main(2)
            if self.hero3.get_rect(center=(600,250)).collidepoint(mouse_pos):
                self.win.blit(self.circle_panel,self.hero3.get_rect(center=(580,250)))
                self.win.blit(self.font1.render("Evana",False,(randint(0,255),randint(0,255),randint(0,255))),(560,390))
                if p.mouse.get_pressed()==(True,False,False):
                    s.Main(3)
        
            self.win.blit(self.hero1,self.hero1.get_rect(center=(200,250)))
            self.win.blit(self.hero2,self.hero1.get_rect(center=(400,250)))
            self.win.blit(self.hero3,self.hero3.get_rect(center=(600,250)))
            self.win.blit(self.txt,(240,50))
            p.display.update()
            self.clock.tick(10)
            
