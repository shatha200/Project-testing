import os
from os import listdir
from os.path import isfile, join
import player
import pygame
pygame.init()
W,H=1000,800
win = pygame.display.set_mode((W,H))
pygame.display.set_caption("classic game")
FPS=60
speed=5

def get_bg():
    img=pygame.image.load(join("Data/sprites/background/1.png"))
    _,_,width,height =img.get_rect()
    tiles=[]

    for i in range (W//width+1):
        for j in range (H//height+1):
            P=(i*width,j*height)
            tiles.append(P)
    return tiles,img

def draw(win,background,bg_image):
    for tile in background:
        win.blit(bg_image,tuple(tile))
   
    pygame.display.update()



def main (win):
    run = True
    clock=pygame.time.Clock()
    background,bg_img=get_bg()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:
             run = False 
        draw(win,background,bg_img)
    pygame.quit() 

main(win)


