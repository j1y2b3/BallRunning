import pygame
import pymunk

import level

class create_level(level.level):

    def __init__(self,win,space):

        super().__init__(win,space)

        self.add(level.ground,rect=(0,500,170,100))
        self.add(level.ground,rect=(630,500,170,100))
        self.add(level.ground,rect=(170,400,44,20))
        self.add(level.ground,rect=(254,300,44,20))
        self.add(level.ground,rect=(338,500,44,20))
        self.add(level.ground,rect=(422,260,44,20))
        self.add(level.ground,rect=(506,460,44,20))
        self.add(level.ground,rect=(590,360,44,20))
        self.add(level.door)
