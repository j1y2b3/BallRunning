import pygame
import pymunk

import level

class fan(level.box):

    def __init__(self,win,space,rect):

        super().__init__(win,space,rect,level.data.ground_color,True)

        self.w,self.h=self.rect

        self.body=pymunk.Body(body_type=pymunk.Body.KINEMATIC)
        self.body.position=(400,300)
        self.body.angular_velocity=1
        self.shape=pymunk.Poly(self.body,[(-self.w>>1,-self.h>>1),(-self.w>>1,self.h>>1),(self.w>>1,self.h>>1),(self.w>>1,-self.h>>1)])
        self.space.add(self.body,self.shape)

    def draw(self):

        topleft=self.body.local_to_world((-self.w>>1,-self.h>>1))
        topright=self.body.local_to_world((-self.w>>1,self.h>>1))
        bottomright=self.body.local_to_world((self.w>>1,self.h>>1))
        bottomleft=self.body.local_to_world((self.w>>1,-self.h>>1))

        pygame.draw.polygon(self.win,self.color,[topleft,topright,bottomright,bottomleft])

class create_level(level.level):

    def __init__(self,win,space):

        super().__init__(win,space)

        self.add(level.ground,rect=(0,500,170,100))
        self.add(level.ground,rect=(630,500,170,100))
        self.add(fan,rect=(400,40))
        self.add(fan,rect=(40,400))
        self.add(level.door)
