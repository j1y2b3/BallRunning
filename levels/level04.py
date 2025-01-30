import pygame
import pymunk

import level

class create_level(level.level):

    def __init__(self,win,space):

        super().__init__(win,space)

        self.add(level.ground,rect=(0,500,800,100))
        self.add(level.ground,rect=(120,100,80,400))
        self.add(level.ground,rect=(300,0,80,400))
        self.add(level.ground,rect=(480,100,80,400))
        self.add(level.door)
