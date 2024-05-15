import pygame as p
import select_hero as s

class GUIStart():
    def __init__(self):
        p.init()
        self.window=p.display.set_mode((800,500))
        self.bg=p.transform.smoothscale(p.image.load(r'E:\backup 28.12.22\E\startBG1.png'),(800,500))
        self.str_rect=p.draw.ellipse(self.window,(100,255,200),(338,230,150,70),2)
        self.ext_rect=p.draw.ellipse(self.window,(100,255,200),(338,350,150,70),2)
        self.bg_music=p.mixer.Sound(r'E:\backup 28.12.22\E\startBG.mp3')
        self.bg_music1=p.mixer.Sound(r'E:\backup 28.12.22\E\startBG2.mp3')
        self.instr=p.image.load(r'E:\backup 28.12.22\E\instruction.png').convert_alpha()
        self.i_log=p.transform.smoothscale(p.image.load(r'E:\backup 28.12.22\E\ilog.png').convert_alpha(),(30,30))
        self.bg_music.set_volume(1)
        self.bg_music.play(-1)
        self.bg_music1.set_volume(1)
        self.bg_music1.play(-1)
        self.main()

    def mouse_move(self):
        m=p.mouse.get_pos()
        if self.str_rect.collidepoint(m):
            p.draw.ellipse(self.window,(100,255,200),(338,230,150,70),2)
            if p.mouse.get_pressed()==(True,False,False):
                self.bg_music.set_volume(0)
                self.bg_music1.set_volume(0)
                p.mouse.set_pos((0,0))
                s.Select_Hero()
        if self.ext_rect.collidepoint(m):
            p.draw.ellipse(self.window,(100,255,200),(338,350,150,70),2)
            if p.mouse.get_pressed()==(True,False,False):
                exit(0)
        
        if self.i_log.get_rect(center=(780,20)).collidepoint(m):
            self.window.blit(self.instr,self.instr.get_rect(center=(400,250)))
    def main(self):
        while True:
            for event in p.event.get():
                if event.type==p.QUIT:
                    exit(0)
            self.window.blit(self.bg,(0,0))
            self.window.blit(self.i_log,self.i_log.get_rect(center=(780,20)))
            self.mouse_move()
            p.display.update()
    
if __name__=='__main__':
    GUIStart()