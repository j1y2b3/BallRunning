import pygame

import data
import tool

class ending:

    def __init__(self,win):

        self.win=win

        self.ground_rect=(0,data.win_h//6*5,data.win_w,data.win_h//6)
        self.ball_x=-data.ball_radius

        self.text_top_rect_center=(data.win_w//2,data.win_h//2-33)
        self.text_bottom_rect_center=(data.win_w//2,data.win_h//2+20)
        self.text_rect_center=(data.win_w//2,data.win_h//2-10)

        self.text_top=tool.create_text('死亡次数:%s'%data.ball_die_times,data.ending_top_font,self.text_top_rect_center)
        self.text_bottom=tool.create_text('点击屏幕进入结束页面',data.ending_bottom_font,self.text_bottom_rect_center)
        self.text=tool.create_text('游戏结束',data.ending_font,self.text_rect_center)

        data.running=True
        self.end=False
        self.clock=pygame.time.Clock()

        self.run()

    def run(self):

        while data.running and not data.close:

            self.check()
            self.update()

        pygame.quit()

    def check(self):

        for event in pygame.event.get():
            if event.type==pygame.QUIT or event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
                data.close=True
            if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                self.end=True

    def update(self):

        self.win.fill(data.win_color)

        pygame.draw.rect(self.win,data.ground_color,self.ground_rect)
        pygame.draw.circle(self.win,data.ball_color,(self.ball_x,data.ball_init_y),data.ball_radius)

        if self.ball_x>=data.win_w//2 and self.end:
            self.text.draw(self.win)
        elif self.end:
            self.ball_x+=5
            self.text.draw(self.win)
        else:
            self.text_top.draw(self.win)
            self.text_bottom.draw(self.win)

        pygame.display.flip()

        self.clock.tick(data.FPS)
