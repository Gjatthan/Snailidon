import pygame as p
from random import randint,choice
import GUIStart as g
import Setting as s

class Hero(p.sprite.Sprite):    #inherits Sprite class
    def __init__(self,jump_bg,hero_type):
        super().__init__()
        self.hero_list=[]       #stores hero movement
        self.hero_index=0
        self.gravity=200
        self.jump=False
        self.jump_bg=jump_bg
        self.jump_bg.set_volume(1)  #1-full vlm 0-mute

        for _ in range(4):          #loads hero movement
            path=r'E:\backup 28.12.22\E\hero'+f'{hero_type}'+f'{_+1}'+'.png'
            hero=p.transform.smoothscale(p.image.load(path).convert_alpha(),(60,80))
            self.hero_list.append(hero)
        self.image=self.hero_list[self.hero_index]  #image is member of super class that contains the image surface
        self.rect=self.image.get_rect(bottomleft=(20,460))  #mem of super class store the image rect
    
    def hero_animation(self):
        self.hero_index+=0.1    #animating is slow; if set to 1 then hero will move rapidly
        if self.hero_index>=3: self.hero_index=0    #if index=3 then index=0
        self.image=self.hero_list[int(self.hero_index)]

    def hero_jump(self):
        if self.jump:   #jump=true whem up arrow key is pressed
            self.gravity+=4#incrementing gravity by 2 and assigning it to hero rect y value
            self.rect.y=self.gravity
            if self.gravity>=380:   #if gravity reaches ground then jump=false and hero image will changes to normal one
                self.jump=False
                self.gravity=200
                self.image=self.hero_list[0]
    
    def hero_movement(self,tobj,sobj): #tobj is tree object and sobj is stone object
        keys=p.key.get_pressed() #gives all the pressed keys
        if keys[p.K_LEFT] and self.rect.x>=0: #keys[p.K_LEFT] return true if left key is pressed
            self.rect.x-=1.5
            self.hero_animation()
        elif keys[p.K_RIGHT] and self.rect.x<=750:
            if self.rect.right<=750:
                self.rect.x+=1.5
            self.hero_animation()
            tobj.update() #stone and tree will move only when hero moves forward
            sobj.update()
        elif keys[p.K_UP]:
            if not self.jump: #if jump=True then not jump becomes false
                self.jump_bg.play() #plays jump music
                self.jump=True
                self.rect.y=self.gravity  #player will moved up to 270
                self.image=self.hero_list[3] 
        elif not self.jump:
            self.image=self.hero_list[2]
    def update(self,tobj,sobj): #overiding the method of Sprite class so that all the methods can be called once in one method
        #if not self.jump: #hero will animated only when he is on the ground
        #    self.hero_animation()
        self.hero_movement(tobj,sobj) #passing tree and stone object
        self.hero_jump()

class Coin(p.sprite.Sprite):
    def __init__(self,type): #type is a type of coin to be generated and its decided when timer triggers
        super().__init__()
        self.image=p.transform.smoothscale(p.image.load(r'E:\backup 28.12.22\E\coin'+f'{type}'+'.png').convert_alpha(),(25,25))
        if type==1:
            self.rect=self.image.get_rect(center=((randint(850,1250),240)))
        elif type==2:
            self.rect=self.image.get_rect(center=((randint(870,1100),330)))
        elif type==3:
            self.rect=self.image.get_rect(center=((randint(850,990),400)))
        elif type==4:
            self.rect=self.image.get_rect(center=((randint(760,1140),430)))
        
    def coin_movement(self):
        self.rect.x-=2
        if self.rect.x<=-2: #if coin moves out of the frame it will be removed
            self.kill() #kill is the method of Sprite class that kills the object
    
    def update(self):
        self.coin_movement()

class Enemy(p.sprite.Sprite):
    def __init__(self,type): #type of enemy to be generated and each object will allocated different memory so each enemy will be an object
        super().__init__()
        self.enemy_list=[] #it contain the either bird or snail animation image depending on type
        self.animation_idx=0
        if type==1 or type==2: #if type is 1 or 2 snail will be generated
            self.enemy_list.append(p.transform.smoothscale(p.image.load(r'E:\backup 28.12.22\E\snail'+f'{type}'+'.png').convert_alpha(),(30,30))) #here we are not animating snail so list conatins only one snail either green one or blue one
            self.image=self.enemy_list[0] #image store the initial image that to be displayed
            self.rect=self.image.get_rect(bottomright=(choice([randint(810,900),randint(1010,1100),randint(1200,1300)]),460)) #since we r generating multiple snails so assigning different x value
        else: #if type is not 1 or 2 bird will generated
            for _ in range(3): #bird have animation 
                path=r'E:\backup 28.12.22\E\bird'+f'{_+1}'+'.png'
                enemy=p.transform.smoothscale(p.image.load(path).convert_alpha(),(40,30))
                self.enemy_list.append(enemy) #different flying bird image will be appended for single bird object
            self.image=self.enemy_list[self.animation_idx]
            self.rect=self.image.get_rect(center=(randint(810,900),randint(100,300))) #assigning different x and y value
    
    def animation(self):
        if self.rect.bottom==460: #assigning different animation speed for different enemy if object is snail it wont be animated bcs we have only one snail image 
            self.animation_idx+=.01 #snail animation index incr
        else:
            self.animation_idx+=.1 #bird animation
        if self.animation_idx>=len(self.enemy_list): self.animation_idx=0
        self.image=self.enemy_list[int(self.animation_idx)]

    def enemy_movement(self):
        if self.rect.bottom==460:
            self.rect.x-=1 #snail movement
        else:
            self.rect.x-=2 #bird movement
        if self.rect.x<=-50: self.kill() #if enemy moves out of frame then dlt obj

    def update(self):
        self.animation()
        self.enemy_movement()

class Cloud(p.sprite.Sprite):
    def __init__(self,type):
        super().__init__()
        self.image=p.transform.smoothscale(p.image.load(r'E:\backup 28.12.22\E\cloud'+f'{type}'+'.png').convert_alpha(),(randint(140,160),randint(50,70)))
        self.rect=self.image.get_rect(center=(randint(-700,-10),randint(30,150)))
    def cloud_movement(self):
        self.rect.x+=1
        if self.rect.x>=850: self.kill()
    def update(self):
        self.cloud_movement()

class Trees(p.sprite.Sprite):
    def __init__(self,no):
        super().__init__()
        self.image=p.transform.smoothscale(p.image.load(r'E:\backup 28.12.22\E\tree'+f'{no}'+'.png').convert_alpha(),(100,randint(190,250)))
        self.rect=self.image.get_rect(bottomright=(randint(900,1200),457))
    
    def tree_move(self):
        self.rect.x-=1
        if self.rect.x<=-50: 
            self.kill()
    def update(self):
        self.tree_move()

class Stone(p.sprite.Sprite):
    def __init__(self,type):
        super().__init__()
        self.image=p.transform.smoothscale(p.image.load(r'E:\backup 28.12.22\E\stone'+f'{type}'+'.png').convert_alpha(),(randint(60,70),randint(30,70)))
        self.rect=self.image.get_rect(bottomleft=(randint(820,1000),457))
    def stone_move(self):
        self.rect.x-=1
        if self.rect.x<=-50: self.kill()
    def update(self):
        self.stone_move()

class Main():
    def __init__(self,hero_type):
        p.init()
        self.screen=p.display.set_mode((800,500))
        p.display.set_caption("")
        self.game_active=True #detect whether game is active or not
        self.game_lost=False #used to display lost msg
        self.clock=p.time.Clock() 
        self.set=s.Settinng() #creating the object of setting GUI class
        self.jump_bg=p.mixer.Sound(r'E:\backup 28.12.22\E\jumpbg.mp3')
        self.bgmusic=p.mixer.Sound(r'E:\backup 28.12.22\E\BGMusic.mp3')
        self.lost_bg=p.mixer.Sound(r'E:\backup 28.12.22\E\lost.wav')
        self.lost_bg.set_volume(1)
        #self.score=0
        self.coin_display=[] #stores coins to be displayed on the top
        self.coin_rect=[]   #and their rect
        
        self.font=p.font.Font(r'E:\backup 28.12.22\E\nasalization-rg.otf',20)
        self.score_text=self.font.render("0",False,(50,50,50))
        
        self.score_list=[0,0,0,0,0] #stores collection of different coins and used to calculate total
        x=0
        for i in range(1,5):
            self.coin_display.append(p.transform.smoothscale(p.image.load(r'E:\backup 28.12.22\E\coin'+f'{i}'+'.png').convert_alpha(),(25,25)))
            self.coin_rect.append(self.coin_display[i-1].get_rect(center=(50+x,30)))
            x+=70
        self.coin_display.append(p.transform.smoothscale(p.image.load(r'E:\backup 28.12.22\E\snail1.png').convert_alpha(),(25,25)))
        self.coin_rect.append(self.coin_display[4].get_rect(center=(50+x,30)))

        self.sky=p.surface.Surface((800,450))
        self.sky.fill((135,206,235))
        self.ground=p.surface.Surface((800,50))
        self.ground.fill((10,160,10))
        self.ground1=p.surface.Surface((800,50))
        self.ground1.fill((10,200,20))
        self.setting=p.transform.scale(p.image.load(r'E:\backup 28.12.22\E\setting.png'),(40,40))
        self.coin_bg=p.mixer.Sound(r'E:\backup 28.12.22\E\coinColect.mp3')
        self.coin_bg.set_volume(1)
        
        self.cloud_event=p.USEREVENT+1 #creating user defined event +1 indicate the no of Udefined event 
        p.time.set_timer(self.cloud_event,60) #assigning timer to trigger in milisec
        self.enemy_timer=p.USEREVENT+2
        p.time.set_timer(self.enemy_timer,2000)
        self.coin_timer=p.USEREVENT+3
        p.time.set_timer(self.coin_timer,1500)
        self.tree_timer=p.USEREVENT+4
        p.time.set_timer(self.tree_timer,100)

        self.heroS=p.sprite.GroupSingle() #Since we r using sprite, and hero is only one we r creating the obj of sprite.GroupSingle
        self.heroS.add(Hero(self.jump_bg,hero_type)) #we are adding one instance of hero class
        self.coinS=p.sprite.Group() #since we r creating multiple instance of coin class we have to create container for them using Group() class
        self.enemyS=p.sprite.Group()
        self.cloudS=p.sprite.Group()
        self.treeS=p.sprite.Group()
        self.stoneS=p.sprite.Group()

        self.state=False #detect whether setting icon is clicked or not
        self.bgmusic.set_volume(1)
        self.bgmusic.play(-1)
        self.main_loop()

    def main_loop(self):
        while True:
            if self.game_active: #True if hero is not collided with enemies
                self.event() 
                self.screen.blit(self.sky,(0,0)) #blitting sky on main screen
                self.screen.blit(self.ground1,(0,445))
                self.treeS.draw(self.screen) #since treeS contains the group of obj of tree(), draw() method is used to draw all of them one a screen at a time
                self.stoneS.draw(self.screen)
                self.screen.blit(self.ground,(0,455))
                self.heroS.draw(self.screen) 
                self.coinS.draw(self.screen)
                self.cloudS.draw(self.screen)
                self.enemyS.draw(self.screen)
                self.screen.blit(self.setting,self.setting.get_rect(center=(760,40)))

                pos=p.mouse.get_pos()
               
                if self.setting.get_rect(center=(750,30)).collidepoint(pos): #checking whether mouse is on setting icon
                    p.draw.circle(self.screen,(170,240,220),(763,40),30,4)
                    if p.mouse.get_pressed()==(True,False,False): #true is right click is made on icon
                        self.state=self.set.show(self.screen,self.jump_bg,self.coin_bg,self.bgmusic) #display the setting menu and return True, to continueous display of setting menu
                elif self.state==True: #id true when user click on setting icon
                    self.state=self.set.show(self.screen,self.jump_bg,self.coin_bg,self.bgmusic) #self.state becomes false if user click on resume button
                else:
                    self.heroS.update(self.treeS,self.stoneS) #it will call the update method of hero class
                    self.coinS.update() #each object of coin class in the CoinS object will cl Update method
                    self.enemyS.update()
                    self.cloudS.update()
                    colide_list=p.sprite.spritecollide(self.heroS.sprite,self.coinS,True) #this method will check whether hero is colliding with the obj in the coinS, True will dlt the coin when collides
                    #heroS.sprite will give the single obj that is stored in heroS obj
                    if colide_list: #True if hero collide with coin
                        self.score_count(colide_list) #we r passing the rect of the coins that collide
                        self.coin_bg.play()
                    list=p.sprite.spritecollide(self.heroS.sprite,self.enemyS,False) 
                    if list:
                        if self.heroS.sprite.rect.bottom==(list[0].rect.top+2) : #if hero jump on the snail then snail will be killed
                            self.score_list[4]+=1 #scorelist[4] contains the count of snails killed
                            list[0].kill() #kill method will kill the collided snail obj
                        else: #otherwise game comes to an end and all the spride will be dlt or formated
                            self.coinS.empty()
                            self.enemyS.empty()
                            self.cloudS.empty()
                            #self.score=0
                            self.game_active=False #game ative becomes falls 
                            self.game_lost=True #now it wont come out of the screen but it wont blite or generate any thing but display the lost info
                            self.bgmusic.set_volume(0) #bg music will stop
                            self.lost_bg.play(0) #lost bg music will play once
                x=70
                for i in range(0,5): #displaying coins and its count
                    self.screen.blit(self.coin_display[i],self.coin_rect[i])
                    self.score_text=self.font.render(str(self.score_list[i]),False,(0,0,0))
                    self.screen.blit(self.score_text,(x,20))
                    x+=70
                  
            elif self.game_lost: #display lost info
                for event in p.event.get(): #its required other will mouse pos will not be generated
                    if event.type==p.QUIT:
                        p.quit()
                        exit(0)
                #pos=p.mouse.get_pos()
                self.game_lost=self.lostMsg()
            else: #when user press home button in lost info then it will display start GUI andcome out of main loop
                self.bgmusic.set_volume(0)
                g.GUIStart()
            p.display.update() #update the screen
            self.clock.tick(60) #run while loop 60 times per second
    
    def event(self):
        for event in p.event.get():
            if event.type==p.QUIT:
                p.quit()
                exit()
            if event.type==p.KEYDOWN and event.key==p.K_SPACE:
                self.game_active=True
            if event.type==self.enemy_timer and not self.state: #enemy will not be generated when user clicked on setting menu
                self.enemyS.add(Enemy(randint(1,5))) #it will create the object of enemy() class and add it to enemyS object
            if event.type==self.cloud_event and not self.state:
                self.cloudS.add(Cloud(randint(1,4)))
                p.time.set_timer(self.cloud_event,5000)
            if event.type==self.coin_timer and not self.state:
                self.coinS.add(Coin(randint(1,4)))
            if event.type==self.tree_timer and not self.state:
                self.stoneS.add(Stone(randint(1,3)))
                self.treeS.add(Trees(randint(1,4)))
                p.time.set_timer(self.tree_timer,10000)
    def score_count(self,colide_list):
        for i in colide_list:
            if i.rect.bottom==253:
                self.score_list[0]=self.score_list[0]+1
            elif i.rect.bottom==343:
                self.score_list[1]=self.score_list[1]+1
            elif i.rect.bottom==413:
                self.score_list[2]=self.score_list[2]+1
            elif i.rect.bottom==443:
                self.score_list[3]=self.score_list[3]+1
    def lostMsg(self):
        window=p.surface.Surface((200,200))
        window.fill((0,0,10))
        
        home=p.transform.smoothscale(p.image.load(r'E:\backup 28.12.22\E\homeicon.png').convert_alpha(),(50,50))
        home_rect=home.get_rect(center=(400,310))
        total=(self.score_list[0]*20)
        total+=(self.score_list[1]*15)
        total+=(self.score_list[2]*10)
        total+=(self.score_list[3]*5)
        total+=(self.score_list[4]*25)
        score_txt=self.font.render("Total Score : "+str(total),False,(255,255,255))
        if total>1000:
            reward=p.transform.smoothscale(p.image.load(r'E:\backup 28.12.22\E\excellent.png').convert_alpha(),(100,70))
        elif total>=800:
            reward=p.transform.smoothscale(p.image.load(r'E:\backup 28.12.22\E\amaging.png').convert_alpha(),(100,65))
        elif total>=250:
            reward=p.transform.smoothscale(p.image.load(r'E:\backup 28.12.22\E\avg.png').convert_alpha(),(100,70))
        else:
            reward=p.transform.smoothscale(p.image.load(r'E:\backup 28.12.22\E\bad.png').convert_alpha(),(100,60))
        pos=p.mouse.get_pos()
        if home_rect.collidepoint(pos):
            p.draw.rect(window,(255,225,250),(65,134,70,50),100)
            if p.mouse.get_pressed()==(True,False,False):
                return False 
        window.blit(score_txt,(15,100))
        p.draw.rect(window,(255,0,0),(5,5,190,190),3)
        window.blit(reward,(50,20)) #reward is bad amaging excellent ......
        self.screen.blit(window,(300,150))
        self.screen.blit(home,home_rect)
        
        return True 
        #returns true if user not press home icon


if __name__=='__main__':
    Main(1)