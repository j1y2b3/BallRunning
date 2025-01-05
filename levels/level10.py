import pygame
import pymunk
import random

import level

class random_lava(level.box):

    def __init__(self,win,space):

        super().__init__(win,space,pygame.Rect(360,460,80,40),level.data.lava_color,False)
        
        self.time=0
        self.on_time,self.off_time=(level.data.FPS//3,level.data.FPS//12)
        self.if_on=False

    def update(self):

        self.time+=1
        self.time%=self.off_time if self.if_on else self.on_time

    def check(self):

        if not self.time:
            self.if_on=not self.if_on
            if self.if_on:
                self.rect.x=random.randrange(150,570,5)

    def draw(self):

        self.update()
        self.check()

        if self.if_on:
            super().draw()

class create_level(level.level):

    def __init__(self,win,space):

        super().__init__(win,space)

        self.add(level.ground,rect=(0,500,800,100))
        self.add(random_lava)
        self.add(level.door)
