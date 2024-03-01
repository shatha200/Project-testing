import pygame
class player(pygame.sprite.Sprite):
    color=(255,0,0)
    def _int_(self,x,y,width,height):
        self.rect=pygame.Rect(x,y,width,height)
        self.x_speed=0
        self.y_speed=0
        self.mask=None
        self.direction="left"
        self.animation_count=0
    
    def move(self,dx,dy):
        self.rect.x+=dx
        self.rect.y+=dy
    
    def move_left(self,speed):
        self.x_speed=-speed
        if self.direction!="left":
            self.direction="left"
            self.animation_count=0


    def move_right(self,speed):
        self.x_speed=speed 
        if self.direction!="right":
            self.direction="right"
            self.animation_count=0  

    def loop(self,FPS):
        self.move(self.x_speed,self.y_speed)
    
    def draw(self,win):
        pygame.draw.rect(win,self,self.color,self.rect)