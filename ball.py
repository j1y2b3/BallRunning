import pygame
import pymunk

import data
import tool

class create_ball:

    def __init__(self,win,space):

        self.win=win
        self.space=space
        self.x=data.ball_init_x
        self.y=data.ball_init_y
        self.radius=data.ball_radius

        self.create()

    def create(self):

        self.ball_body=pymunk.Body(1,1,body_type=pymunk.Body.DYNAMIC)
        self.ball_body.position=self.x,self.y
        self.ball_shape=pymunk.Circle(self.ball_body,self.radius)
        self.ball_shape.elasticity=data.elasticity
        self.space.add(self.ball_body,self.ball_shape)

    def move(self,x,y):

        self.space.remove(self.ball_body,self.ball_shape)
        self.x,self.y=x,y
        self.create()

    def die(self):
        
        self.move(data.ball_init_x,data.ball_init_y)

    def jump(self):

        if tool.collide_color(self.win,self.rect,data.ground_color):
            data.force[1]-=data.jump_force

    def left(self):

        data.force[0]-=data.push_force

    def right(self):

        data.force[0]+=data.push_force

    def check(self):

        if tool.collide_color(self.win,self.rect,data.door_color):
            self.die()
            pygame.event.post(pygame.event.Event(data.NEXT_LEVEL))

        if tool.collide_color(self.win,self.rect,data.lava_color) or self.x<0 or self.x>data.win_w or self.y<0 or self.y>data.win_h+100:
            self.die()
            data.ball_die_times+=1

    def space_update(self):

        data.force[0]=int(data.force[0]/1.5)
        data.force[1]=int(data.force[1]/1.5)

        if self.ball_body.velocity.y<-data.velocity_limit:
            self.ball_body.velocity=(self.ball_body.velocity.x,-data.velocity_limit)
        
        self.ball_body.apply_impulse_at_local_point(tuple(data.force),(0,0))

    def win_update(self):

        self.x,self.y=self.ball_body.position
        self.rect=pygame.draw.circle(self.win,data.ball_color,(self.x,self.y),self.radius)

    def update(self):

        self.space_update()
        self.win_update()
