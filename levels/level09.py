import pygame
import pymunk

import level

class movable_ground(level.box):

    def __init__(self,win,space,velocity,pos):

        self.velocity=velocity
        self.x,self.y=pos
        self.w,self.h=(44,20)
        self.mw,self.mh=(self.w>>1,self.h>>1)
        self.rect=pygame.Rect(self.x-self.mw,self.y-self.mh,self.w,self.h)
        self.can_turn=False

        super().__init__(win,space,self.rect,level.data.ground_color,True)

        self.body=pymunk.Body(1,1,body_type=pymunk.Body.KINEMATIC)
        self.body.position=self.rect.center
        self.body.velocity=(self.velocity,0)
        self.shape=pymunk.Poly(self.body,[(-self.mw,-self.mh),(self.mw,-self.mh),(self.mw,self.mh),(-self.mw,self.mh)])
        self.shape.elasticity=level.data.elasticity
        self.space.add(self.body,self.shape)

    def check(self):
        
        if self.can_turn and (self.rect.topleft[0]<170 or 630<self.rect.topright[0]):
            self.body.velocity=-self.body.velocity
            self.can_turn=False
        if 170<=self.rect.topleft[0] and self.rect.topright[0]<=630:
            self.can_turn=True

    def draw(self):
        
        self.rect.center=self.body.position

        super().draw()

        self.check()

class create_level(level.level):

    def __init__(self,win,space):

        super().__init__(win,space)

        self.add(level.ground,rect=(0,500,170,100))
        self.add(level.ground,rect=(630,500,170,100))
        self.add(level.ground,rect=(0,200,800,100))
        self.add(movable_ground,velocity=50,pos=(170,320))
        self.add(movable_ground,velocity=50,pos=(254,360))
        self.add(movable_ground,velocity=-50,pos=(338,400))
        self.add(movable_ground,velocity=50,pos=(422,440))
        self.add(movable_ground,velocity=-50,pos=(506,480))
        self.add(level.door)
