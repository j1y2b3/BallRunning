import pygame
import pymunk

import data

class box:

    def __init__(self,win,space,rect,color,is_body):

        self.win=win
        self.space=space
        self.rect=rect
        self.color=color
        self.is_body=is_body

    def draw(self):

        pygame.draw.rect(self.win,self.color,self.rect)

    def remove(self):

        self.space.remove(self.body,self.shape)

    def bind(self,check,fun):

        def wrapper():

            if check():
                fun()

        return wrapper

class ground(box):

    def __init__(self,win,space,rect):

        super().__init__(win,space,rect,data.ground_color,True)

        self.rect=pygame.Rect(self.rect)

        self.body=pymunk.Body(body_type=pymunk.Body.STATIC)
        self.shape=pymunk.Poly(self.body,[self.rect.topleft,self.rect.topright,self.rect.bottomright,self.rect.bottomleft])
        self.shape.elasticity=data.elasticity
        self.space.add(self.body,self.shape)

class lava(box):

    def __init__(self,win,space,rect):

        super().__init__(win,space,rect,data.lava_color,False)

class door(box):

    def __init__(self,win,space,rect=(700,460,40,40)):

        super().__init__(win,space,rect,data.door_color,False)

class level:

    def __init__(self,win,space):

        self.win=win
        self.space=space
        self.update_list=[]
        self.remove_list=[]

    def add(self,obj,**kwds):

        i=obj(self.win,self.space,**kwds)
        self.update_list.append(i)
        if i.is_body:self.remove_list.append(i)
        return i

    def update(self):

        tuple(map(lambda i:i.draw(),self.update_list))

    def close(self):

        tuple(map(lambda i:i.remove(),self.remove_list))
