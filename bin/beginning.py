import pygame

import data
import tool

class beginning:

    def __init__(self,win):

        self.win=win

        self.ground_rect=(0,data.win_h//6*5,data.win_w,data.win_h//6)
        self.ball_x=data.win_w//2

        self.text_top_rect_center=(data.win_w//2,data.win_h//2-33)
        self.text_bottom1_rect_center=(data.win_w//2,data.win_h//2+20)
        self.text_bottom2_rect_center=(data.win_w//2,data.win_h//2+50)
        self.text_rect_center=(data.win_w//2,data.win_h//2-10)

        self.text_top=tool.create_text('小球跑酷',data.begnning_top_font,self.text_top_rect_center)
        self.text_bottom1=tool.create_text('点击屏幕开始游戏',data.begnning_bottom_font,self.text_bottom1_rect_center)
        self.text_bottom2=tool.create_text('游戏关卡中可按ctrl+g获取玩法',data.begnning_bottom_font,self.text_bottom2_rect_center)
        self.text=tool.create_text('游戏开始',data.begnning_font,self.text_rect_center)

        data.running=True
        self.begin=False
        self.clock=pygame.time.Clock()

        self.run()

    def run(self):

        while data.running and not data.close:

            self.check()
            self.update()

    def check(self):

        for event in pygame.event.get():
            if event.type==pygame.QUIT or event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
                data.close=True
            if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                self.begin=True

    def update(self):

        self.win.fill(data.win_color)

        pygame.draw.rect(self.win,data.ground_color,self.ground_rect)
        pygame.draw.circle(self.win,data.ball_color,(self.ball_x,data.ball_init_y),data.ball_radius)

        if self.ball_x>=data.win_w+data.ball_radius and self.begin:
            data.running=False
        elif self.begin:
            self.ball_x+=10
            self.text.draw(self.win)
        else:
            self.text_top.draw(self.win)
            self.text_bottom1.draw(self.win)
            self.text_bottom2.draw(self.win)

        pygame.display.flip()

        self.clock.tick(data.FPS)
