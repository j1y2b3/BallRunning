import pygame
import pymunk

import level

class unreal_lava(level.box):

    def __init__(self,win,space,rect):

        super().__init__(win,space,rect,(254,0,0),False)

class create_level(level.level):

    def __init__(self,win,space):

        super().__init__(win,space)

        self.add(level.ground,rect=(0,500,800,100))
        self.add(level.lava,rect=(360,460,40,40))
        self.add(unreal_lava,rect=(360,0,40,460))
        self.add(level.door)

        
