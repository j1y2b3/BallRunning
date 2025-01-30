import pygame

running=True
show_end=True

test=False
test_start_level=11

error=None

win_icon=lambda win:pygame.image.load('files\\icon.ico').convert()
win_w,win_h=(800,600)#屏幕大小(宽,长)
win_color=(240,240,240)

FPS=60

NEXT_LEVEL=pygame.USEREVENT
init_level=level=1 if not test else test_start_level
levels_num=0

gravity=600#重力
damping=0.8#阻力
elasticity=0.5#弹性

game_font=lambda:pygame.font.Font('files\\msyh.ttc',15)
tk_font=('宋体',12)
tk_bold_font=('宋体',12,'bold')

text_color=(10,10,10)
ground_color=(255,255,120)
lava_color=(255,0,0)

door_w,door_h=(40,40)
door_color=(255,128,64)

ball_radius=20
ball_init_x,ball_init_y=(25,480)
ball_color=(75,255,75)
ball_die_times=0
ball_pass_times=0

force=[0,0]
jump_force=70#跳跃力
push_force=2#水平力
velocity_limit=300#跳跃速度限制
