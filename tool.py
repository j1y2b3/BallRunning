import pygame
import pymunk

import data

class create_text:

    def __init__(self,words,font,rect_center=(data.win_w>>1,data.win_h>>1)):

        self.text=font.render(words,True,data.text_color)
        self.rect=self.text.get_rect()
        self.rect.center=rect_center

    def draw(self,win,rect=None):

        if rect==None:
            rect=self.rect

        win.blit(self.text,rect)

def collide_color(win,rect,color):

    rect=pygame.Rect(rect).inflate(2,2)
    rect.y+=1
    rect.h-=1
    win_pixel=pygame.PixelArray(win)
    rect_pixel=win_pixel[rect.x:rect.x+rect.width,rect.y:rect.y+rect.height]
    pygame.PixelArray.close(win_pixel)

    if rect_pixel!=None:
        return color in rect_pixel
