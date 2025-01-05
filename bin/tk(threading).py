import tkinter
from time import sleep
import threading
import os

import path
path.path=os.getcwd()

def clear(*masters):
    
    for master in masters:
        
        master.place_forget()

class create_tk:

    def __init__(self):

        self.win=tkinter.Tk()
        self.win.title('小球跑酷')
        self.win.iconbitmap(default='files\\icon.ico')
        self.win_width,self.win_height=450,300
        self.win_x,self.win_y=(self.win.winfo_screenwidth()-self.win_width)//2,(self.win.winfo_screenheight()-self.win_height)//2
        self.win.geometry('%sx%s+%s+%s'%(self.win_width,self.win_height,self.win_x,self.win_y))
        self.win.resizable(False,False)

        self.background=create_background(self.win,15,225,85).canvas
        main_win(self.win,self.background)

        self.win.mainloop()

    def close(self):

        self.win.quit
        self.win.destroy()

class main_win:

    def __init__(self,win,canvas):

        self.win=win
        self.canvas=canvas
        
        self.but_enter=tkinter.Button(self.win,text='开始',command=self.enter,font=('宋体',12,'bold'))
        self.but_key=tkinter.Button(self.win,text='按键',command=self.to_key,font=('宋体',12,'bold'))

        self.but_enter.place(x=175,y=60,width=100,height=40)
        self.but_key.place(x=175,y=120,width=100,height=40)

    def enter(self):

        clear(self.but_enter,self.but_key)
        self.enter_lab=tkinter.Label(self.win,text='正在进入游戏',font=('宋体',12,'bold'))
        self.enter_lab.place(x=175,y=80)

        #self.loop=threading.Thread(target=self.main_fun)
        #self.loop.start()

    def to_key(self):

        clear(self.but_enter,self.but_key)
        
        key_win(self.win,self.canvas)
    
    def ball_run(self):

        length=240
        speed=4

        for i in range(length//speed):
        
            try:
                self.canvas.move(2,speed,0)
            except:
                pass
            sleep(0.01)

    def main_fun(self):
        
        self.ball_run()

        import pygame
        import main
        import data
        
        try:
            
            self.win.withdraw()
            clear(self.enter_lab)
            
            pygame.init()
            main.game()

            if data.show_end:
                end_win(self.win,self.canvas)
                self.win.update()
                self.win.deiconify()
            else:
                self.win.quit
                self.win.destroy()

        except:
            
            pass

class key_win:
    
    def __init__(self,win,canvas):

        self.win=win
        self.canvas=canvas
        
        self.lab_key=tkinter.Label(self.win,text='< 向左\n> 向右\n︿ 向上\nesc 退出\nenter 重新开始',font=('宋体',12))
        self.but_back=tkinter.Button(self.win,text='返回',command=self.to_main,font=('宋体',12,'bold'))
        
        self.lab_key.place(x=125,y=20,width=200,height=100)
        self.but_back.place(x=175,y=120,width=100,height=40)
    
    def to_main(self):
        
        clear(self.lab_key,self.but_back)
        
        main_win(self.win,self.canvas)

class end_win:

    def __init__(self,win,canvas):

        import data

        self.win=win
        self.canvas=canvas

        self.lab_die_times=tkinter.Label(self.win,text='死亡次数：%s'%data.ball_die_times,font=('宋体',12,'bold'))
        self.but_ok=tkinter.Button(self.win,text='确定',command=self.to_main,font=('宋体',12,'bold'))

        self.lab_die_times.place(x=175,y=80)
        self.but_ok.place(x=175,y=120,width=100,height=40)

        self.loop=threading.Thread(target=self.ball_run)
        self.loop.start()

    def init_data(self):

        import data

        data.running=True
        data.show_end=True
        data.level=data.init_level
        data.ball_die_times=0
        
    def ball_run(self):

        self.canvas.move(2,-480,0)

        length=240
        speed=4

        for i in range(length//speed):
        
            try:
                self.canvas.move(2,speed,0)
            except:
                pass
            sleep(0.01)

    def to_main(self):

        self.init_data()
        
        clear(self.lab_die_times,self.but_ok)
        
        main_win(self.win,self.canvas)

class create_background:
    
    def __init__(self,win,ball_radius,ball_x,ball_y):
        
        self.win=win
        
        self.r=ball_radius
        self.x,self.y=ball_x,ball_y
        self.ball_color='#4BFF4B'
        self.ground_color='#FFFF78'
        
        self.canvas=tkinter.Canvas(self.win,width=450,height=150)
        self.canvas.pack(side='bottom')
        
        self.canvas.create_rectangle(0,100,450,150,outline=self.ground_color,fill=self.ground_color)
        self.canvas.create_oval(self.x-self.r,self.y-self.r,self.x+self.r,self.y+self.r,outline=self.ball_color,fill=self.ball_color)
