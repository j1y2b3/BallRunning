import pygame
import pymunk

import level

class unreal_ground(level.box):

    def __init__(self,win,space,rect):

        super().__init__(win,space,rect,(254,255,120),False)

class create_level(level.level):

    def __init__(self,win,space):

        super().__init__(win,space)

        self.add(level.ground,rect=(0,500,170,100))
        self.add(level.ground,rect=(630,500,170,100))
        self.add(level.ground,rect=(270,0,80,300))
        self.add(level.ground,rect=(270,400,80,200))
        self.add(level.ground,rect=(450,0,80,100))
        self.add(level.ground,rect=(450,200,80,400))
        self.add(unreal_ground,rect=(270,300,80,100))
        self.add(unreal_ground,rect=(450,100,80,100))
        self.add(level.door)
