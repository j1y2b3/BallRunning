import pygame
import pymunk

import win
import space
import ball
import data
import levels
import log

class game:

    def __init__(self):

        log.log.record("'Have entered the game'")

        self.win=win.create_win()
        self.space=space.create_space()
        self.ball=ball.create_ball(self.win.win,self.space.space)
        self.run()
        self.space.close()

    def run(self):

        self.clock=pygame.time.Clock()
        
        self.level=levels.levels_list[data.level-1](self.win.win,self.space.space)
        
        while data.running:

            self.update()
            self.check()

        pygame.quit()

    def check(self):

        self.ball.check()

        for event in pygame.event.get():
            if event.type==pygame.QUIT or event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
                data.running=data.show_end=False
            if event.type==data.NEXT_LEVEL:
                self.level.close()
                data.level+=1
                if data.level>data.levels_num:
                    data.ball_pass_times+=1
                    log.log.record("f'Have passed the game,died {data.ball_die_times} times'")
                    data.running=False
                else:
                    self.level=levels.levels_list[data.level-1](self.win.win,self.space.space)

        keys=pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.ball.jump()

        if keys[pygame.K_LEFT]:
            self.ball.left()

        if keys[pygame.K_RIGHT]:
            self.ball.right()

        if keys[pygame.K_RETURN] and not(keys[pygame.K_LCTRL] or keys[pygame.K_RCTRL]):
            self.ball.die()
            data.ball_die_times=0
            pygame.event.post(pygame.event.Event(data.NEXT_LEVEL))
            data.level=0

        if keys[pygame.K_RETURN] and (keys[pygame.K_LCTRL] or keys[pygame.K_RCTRL]):
            self.ball.die()

    def update(self):

        self.win.update()
        self.ball.update()
        self.level.update()

        pygame.display.flip()

        self.space.space.step(1/data.FPS)
        self.clock.tick(data.FPS)
