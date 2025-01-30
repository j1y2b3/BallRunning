import tkinter
from time import sleep
import threading
import pygame

import game
import data
import log

def clear(*masters):
    
    for master in masters:
        
        master.place_forget()

class create_tk:

    def __init__(self):

        log.log.record("'Have begun to run'")

        self.win=tkinter.Tk()
        self.win.title('小球跑酷')
        self.win.iconbitmap(default='files\\icon.ico')
        self.win_width,self.win_height=450,300
        self.win_x,self.win_y=(self.win.winfo_screenwidth()-self.win_width)>>1,(self.win.winfo_screenheight()-self.win_height)>>1
        self.win.geometry(f'{self.win_width}x{self.win_height}+{self.win_x}+{self.win_y}')
        self.win.resizable(False,False)
        
        self.win.bind_all('<Escape>',lambda event:self.close())

        self.background=create_background(self.win,15,225,85).canvas
        main_win(self.win,self.background)

        self.win.mainloop()

        log.log.record("f'Have ended running successfully,passed the game {data.ball_pass_times} times'")

    def close(self):

        self.win.quit
        self.win.destroy()

class main_win:

    def __init__(self,win,canvas):

        self.win=win
        self.canvas=canvas

        self.t=0
        self.dt=10

        self.x=240
        self.dx=4
        
        self.but_enter=tkinter.Button(self.win,text='开始',command=self.enter,font=data.tk_bold_font)
        self.but_key=tkinter.Button(self.win,text='按键',command=self.to_key,font=data.tk_bold_font)

        self.but_enter.place(x=175,y=60,width=100,height=40)
        self.but_key.place(x=175,y=120,width=100,height=40)

        self.win.bind('<Return>',lambda event:self.enter())
        self.win.bind('<Control-k>',lambda event:self.to_key())

    def enter(self):

        self.win.unbind('<Return>')
        self.win.unbind('<Control-k>')

        clear(self.but_enter,self.but_key)
        self.enter_lab=tkinter.Label(self.win,text='正在进入游戏',font=data.tk_bold_font)
        self.enter_lab.place(x=175,y=80)
        
        self.after_id=self.win.after(self.dt,self.main_fun)

    def to_key(self):

        self.win.unbind('<Return>')
        self.win.unbind('<Control-k>')

        clear(self.but_enter,self.but_key)
        
        key_win(self.win,self.canvas)
    
    def ball_run(self):
        
        self.t+=self.dt

        try:
            self.canvas.move(2,self.dx,0)
        except:
            pass

    def main_fun(self):
        
        if self.t<self.x//self.dx*self.dt:
            
            self.ball_run()

            self.after_id=self.win.after(self.dt,self.main_fun)
            
        else:

            pygame.init()
            
            self.win.withdraw()
            clear(self.enter_lab)
            
            try:
                game.game()
            except Exception as error:
                data.error=error

            if data.show_end:
                end_win(self.win,self.canvas)
                self.win.update()
                self.win.deiconify()
            else:
                self.win.quit
                self.win.destroy()

            self.win.after_cancel(self.after_id)

class key_win:
    
    def __init__(self,win,canvas):

        self.win=win
        self.canvas=canvas
        
        self.lab_key=tkinter.Label(self.win,text='游戏内：\n< 向左\n> 向右\n︿ 向上\nesc 退出\nenter 重新开始',font=data.tk_font)
        self.but_back=tkinter.Button(self.win,text='返回',command=self.to_main,font=data.tk_bold_font)
        
        self.lab_key.place(x=125,y=10,width=200,height=100)
        self.but_back.place(x=175,y=120,width=100,height=40)

        self.win.bind('<Return>',lambda event:self.to_main())
    
    def to_main(self):

        self.win.unbind('<Return>')
        
        clear(self.lab_key,self.but_back)
        
        main_win(self.win,self.canvas)

class end_win:

    def __init__(self,win,canvas):

        self.win=win
        self.canvas=canvas

        self.t=0
        self.dt=10

        self.x=240
        self.dx=4

        self.lab_die_times=tkinter.Label(self.win,text=f'死亡次数：{data.ball_die_times}',font=data.tk_bold_font)
        self.but_ok=tkinter.Button(self.win,text='确定',command=self.to_main,font=data.tk_bold_font)

        self.lab_die_times.place(x=175,y=80)
        self.but_ok.place(x=175,y=120,width=100,height=40)

        self.canvas.move(2,-480,0)
        self.after_id=self.win.after(self.dt,self.main_fun)

        self.win.bind('<Return>',lambda event:self.to_main())

    def init_data(self):

        data.running=True
        data.show_end=True
        data.level=data.init_level
        data.ball_die_times=0
        
    def ball_run(self):

        self.t+=self.dt
        
        try:
            self.canvas.move(2,self.dx,0)
        except:
            pass

    def main_fun(self):

        if self.t<self.x//self.dx*self.dt:

            self.ball_run()

            self.after_id=self.win.after(self.dt,self.main_fun)

        else:

            self.win.after_cancel(self.after_id)

    def to_main(self):

        self.win.unbind('<Return>')

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

