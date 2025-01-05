import pygame
import pymunk

from levels import level

class RectCollideError(Exception):
    pass

class sup_box(level.box):

    def __init__(self,win,space,rect,check_rect,color,is_body,if_show):

        super().__init__(win,space,rect,color,is_body)

        self.check_rect=check_rect
        self.if_show=if_show

        if all(check_rect) and pygame.Rect(check_rect[0]).colliderect(pygame.Rect(check_rect[1])):
            raise RectCollideError

    def check(self):

        if self.check_rect[0] and level.ball_enter_rect(self.check_rect[0]):
            self.appear()

        if self.check_rect[1] and level.ball_enter_rect(self.check_rect[1]):
            self.hide()

    def appear(self):

        self.if_show=True

    def hide(self):

        self.if_show=False

    def draw(self):

        self.check()
        if self.if_show:super().draw()

class sup_ground(sup_box):

    def __init__(self,win,space,rect,check_rect,if_show):

        super().__init__(win,space,rect,check_rect,level.data.ground_color,True,if_show)

        self.appear()
        if not if_show:
            self.hide()

    def appear(self):

        self.rect=pygame.Rect(self.rect)

        self.body=pymunk.Body(body_type=pymunk.Body.STATIC)
        self.shape=pymunk.Poly(self.body,[self.rect.topleft,self.rect.topright,self.rect.bottomright,self.rect.bottomleft])
        self.shape.elasticity=level.data.elasticity
        self.space.add(self.body,self.shape)

        super().appear()

    def hide(self):

        try:
            self.remove()
        except:
            pass

        super().hide()

class sup_lava(sup_box):

    def __init__(self,win,space,rect,check_rect,if_show):

        super().__init__(win,space,rect,check_rect,level.data.lava_color,if_show)

class create_level(level.level):

    def __init__(self,win,space):

        super().__init__(win,space)

        self.add(level.ground,rect=(0,500,120,100))
        self.add(level.ground,rect=(480,500,320,100))
        self.add(sup_ground,rect=(120,500,360,100),check_rect=(None,(120,0,40,600)),if_show=True)
        self.add(sup_ground,rect=(620,60,40,440),check_rect=((620,0,40,600),(480,100,40,40)),if_show=False)
        self.add(sup_ground,rect=(100,60,520,40),check_rect=((620,0,40,600),(480,100,40,40)),if_show=False)
        self.add(level.door)
