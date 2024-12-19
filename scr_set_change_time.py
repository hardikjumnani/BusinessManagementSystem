# design ref : https://github.com/Shobhit1338/Employee-Management-System
'''
* Employee Gender, DOB, Salary
'''

import pyautogui as pg
from customtkinter import *
from tkinter.ttk import Separator
from PIL import Image

from style_global import COLOR, fn_grid

SCREEN_WIDTH = pg.size()[0]
SCREEN_HEIGHT = pg.size()[1]

WINDOW_WIDTH = int(SCREEN_WIDTH * 0.2)
WINDOW_HEIGHT = int(SCREEN_HEIGHT * 0.155)
WINDOW_X = int(SCREEN_WIDTH * 0.3)
WINDOW_Y = int(SCREEN_HEIGHT * 0.1)

class StyleChangeTimePage:
    def __init__(self):
        self._lbl_title = {
            'text_color' : COLOR[4], 
            'fg_color' : COLOR[1], 
            'font' : ('Arial', 30, 'bold'),
            'corner_radius': 1,
            'width' : WINDOW_WIDTH,
            'height' : 60,
        }
        self._btn_add = {
            'bg_color' : COLOR[1],
            'fg_color' : 'white',
            'hover_color' : 'lightgrey',
            'corner_radius' : 5,
            'width' : 10,
        }
        self._const_width = {
            'width' : 120,
        }
        self._btn = {
            'height' : 30,
            'fg_color' : COLOR[1],
        }
        self._txt = {
            'height' : 60,
            'text_color' : 'black',
            'fg_color' : COLOR[3],
            'font' : ('Calibra', 30, 'bold')
        }
style = StyleChangeTimePage()

class ChangeTimePage:
    def __init__(self, root:CTk, *time_data: list[int, int, str]):
        self._root = root
        self._root.title('Set Time')
        self._root.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{WINDOW_X}+{WINDOW_Y}')

        self.var_hour = 12
        self.var_min = 0
        self.var_meri = 'AM'
        # Above Vars are just for import purpose, use and throw
        
        if time_data:
            self.var_hour = time_data[0]
            self.var_min = time_data[1]
            self.var_meri = time_data[2]


        # ===== All Images ======
        icon_up = CTkImage(dark_image=Image.open('AppData/icons/png/up.png'), size=(22, 22))
        icon_down = CTkImage(dark_image=Image.open('AppData/icons/png/down.png'), size=(22, 22))

        # ====== Widgets ======

        frm_time = CTkFrame(self._root)
        frm_time.pack()
        # Hour
        frm_hours = CTkFrame(frm_time)
        frm_hours.pack(side=LEFT, padx=4)

        btn_hours_up = CTkButton(frm_hours, text='', image=icon_up, command=lambda: self.fn_increment(0), **style._const_width, **style._btn)
        btn_hours_up.pack()

        self.txt_hours = CTkLabel(frm_hours, text=f'{self.var_hour:02d}', **style._const_width, **style._txt)
        self.txt_hours.pack()

        btn_hours_down = CTkButton(frm_hours, text='', image=icon_down, command=lambda: self.fn_decrement(0), **style._const_width, **style._btn)
        btn_hours_down.pack()


        # Min
        frm_min = CTkFrame(frm_time)
        frm_min.pack(side=LEFT, padx=4)

        btn_min_up = CTkButton(frm_min, text='', image=icon_up, command=lambda: self.fn_increment(1), **style._const_width, **style._btn)
        btn_min_up.pack()

        self.txt_min = CTkLabel(frm_min, text=f'{self.var_min:02d}', **style._const_width, **style._txt)
        self.txt_min.pack()

        btn_min_down = CTkButton(frm_min, text='', image=icon_down, command=lambda: self.fn_decrement(1), **style._const_width, **style._btn)
        btn_min_down.pack()

        # Meri
        frm_meri = CTkFrame(frm_time)
        frm_meri.pack(side=LEFT, padx=4)

        btn_meri_up = CTkButton(frm_meri, text='', image=icon_up, command=lambda: self.fn_increment(2), **style._const_width, **style._btn)
        btn_meri_up.pack()

        self.txt_meri = CTkLabel(frm_meri, text=f'{self.var_meri}', **style._const_width, **style._txt)
        self.txt_meri.pack()

        btn_meri_down = CTkButton(frm_meri, text='', image=icon_down, command=lambda: self.fn_decrement(2), **style._const_width, **style._btn)
        btn_meri_down.pack()


        # Button Save
        btn_save = CTkButton(self._root, text='Save', fg_color=COLOR[1])
        btn_save.pack(pady=10)



    def fn_increment(self, data:int) -> None:
        if data == 0:  # Hour
            hour = (int(self.txt_hours.cget('text')) + 1) % 12 if (int(self.txt_hours.cget('text')) + 1) % 12 else 12
            self.txt_hours.configure(text=f"{hour :02d}")

        elif data == 1:  # Minute
            self.txt_min.configure(text=f"{(int(self.txt_min.cget('text')) + 1) % 60 :02d}")

        elif data == 2:  # Meri
            self.fn_toogle()
    
    def fn_decrement(self, data:int) -> None:
        if data == 0:  # Hour
            hour = (int(self.txt_hours.cget('text')) - 1) % 12 if (int(self.txt_hours.cget('text')) - 1) % 12 else 12
            self.txt_hours.configure(text=f"{hour :02d}")

        elif data == 1:  # Minute
            self.txt_min.configure(text=f"{(int(self.txt_min.cget('text')) - 1) % 60 :02d}")

        elif data == 2:  # Meri
            self.fn_toogle()
    
    def fn_toogle(self):
        if self.txt_meri.cget('text') == 'AM':
            self.txt_meri.configure(text='PM')
        else:
            self.txt_meri.configure(text='AM')

if __name__ == "__main__":
    root = CTk()
    obj = ChangeTimePage(root)
    root.mainloop()