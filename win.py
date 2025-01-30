import pygame

import data

class create_win:

    def __init__(self):

        self.win=pygame.display.set_mode((data.win_w,data.win_h),depth=8)
        pygame.display.set_caption('小球跑酷')
        pygame.display.set_icon(data.win_icon(self.win))
        self.win.fill(data.win_color)
        self.font=data.game_font()

    def show_data(self):

        level_text=self.font.render(f'关卡数:{data.level}/{data.levels_num}',True,data.text_color)
        level_text_rect=level_text.get_rect()
        self.win.blit(level_text,level_text_rect.move(5,5))

        die_times_text=self.font.render(f'死亡次数:{data.ball_die_times}',True,data.text_color)
        die_times_text_rect=die_times_text.get_rect()
        self.win.blit(die_times_text,die_times_text_rect.move(5,5+level_text_rect.h))

    def update(self):

        self.win.fill(data.win_color)
        self.show_data()
