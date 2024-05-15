import pygame as p

class Settinng():
    def __init__(self):
        #p.init()
        self.window_fill=p.surface.Surface((120,170))
        self.window_fill.fill("#f2e3f2")
        self.icon=[]
        self.icon_rect=[]
        self.font=p.font.Font(r'E:\backup 28.12.22\E\nasalization-rg.otf',20)
        self.font2=p.font.Font(r'E:\backup 28.12.22\E\nasalization-rg.otf',13)
        self.resume=p.transform.scale(p.image.load(r'E:\backup 28.12.22\E\musicI5.png'),(30,30))
        for i in range(0,4):
            image=p.transform.scale(p.image.load(r'E:\backup 28.12.22\E\musicI'+str(i+1)+'.png'),(20,20))
            self.icon.append(image)
            self.icon_rect.append(image.get_rect(center=(80,50)))
        self.music=self.icon[0]
        self.sound=self.icon[3]
        self.m=0
        self.s=3

    def show(self,win,jBg,cBg,Bg):
        set_txt=self.font.render("Setting",False,'#00640f')
        music_txt=self.font2.render("Music",False,'#aa1414')
        sound_txt=self.font2.render("Sound",False,'#aa1414')
        win.blit(self.window_fill,(650,60))
        win.blit(self.resume,self.resume.get_rect(center=(715,200))) #resume button
        win.blit(set_txt,(675,70))
        win.blit(music_txt,(675,110))
        win.blit(sound_txt,(675,150))
        p.draw.rect(win,(0,0,0),(655,65,110,160),2)
        p.draw.rect(win,(0,0,0),(650,60,120,170),2)
        m=p.mouse.get_pos()
        if self.resume.get_rect(center=(715,200)).collidepoint(m) and p.mouse.get_pressed()==(True,False,False):
            return False
        if self.music.get_rect(center=((735,120))).collidepoint(m) and p.mouse.get_pressed()==(True,False,False):
            if self.m==0:
                self.m=2 #mute icon index
                Bg.set_volume(0)
            else:
                self.m=0 #unmute icon index
                Bg.set_volume(.2)
            self.music=self.icon[self.m]

        if self.sound.get_rect(center=(740,158)).collidepoint(m) and p.mouse.get_pressed()==(True,False,False):
            if self.s==3:
                self.s=1
                jBg.set_volume(0)
                cBg.set_volume(0)
            else:
                self.s=3
                jBg.set_volume(1)
                cBg.set_volume(1)
            self.sound=self.icon[self.s]

        win.blit(self.music,self.music.get_rect(center=((735,120))))
        win.blit(self.sound,self.sound.get_rect(center=(740,158)))
        return True
            