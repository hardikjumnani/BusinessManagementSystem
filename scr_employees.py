# design ref : https://github.com/Shobhit1338/Employee-Management-System
'''
* Employee Gender, DOB, Salary
'''

import pyautogui as pg
from customtkinter import *
from tkinter.ttk import Separator
from PIL import Image

from style_global import COLOR, fn_grid
from scr_emp_add import EmployeesPage_Add

SCREEN_WIDTH = pg.size()[0]
SCREEN_HEIGHT = pg.size()[1]

WINDOW_WIDTH = int(SCREEN_WIDTH * 0.5)
WINDOW_HEIGHT = int(SCREEN_HEIGHT * 0.55)
WINDOW_X = int(SCREEN_WIDTH * 0.16)
WINDOW_Y = int(SCREEN_HEIGHT * 0.1)

class StyleEmployeesPage:
    def __init__(self):
        self._lbl_title = {
            'text_color' : COLOR[4], 
            'fg_color' : COLOR[1], 
            'font' : ('Arial', 30, 'bold'),
            'corner_radius': 1,
            'width' : WINDOW_WIDTH,
            'height' : 60,
        }
        self._btn_employees_add = {
            'bg_color' : COLOR[1],
            'fg_color' : 'white',
            'hover_color' : 'lightgrey',
            'corner_radius' : 5,
            'width' : 10,
        }
style = StyleEmployeesPage()

class EmployeesPage:
    def __init__(self, root:CTk):
        self._root = root
        self._root.title('Employees')
        self._root.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{WINDOW_X}+{WINDOW_Y}')


        # ====== Widgets ======
        lbl_title = CTkLabel(self._root, text='Employees', **style._lbl_title)
        lbl_title.place(x=0, y=0)

        icon_add = CTkImage(dark_image=Image.open('AppData/icons/png/add.png'), size=(32, 32))
        btn_employees_add = CTkButton(self._root, text='', image=icon_add, command=self.win_emp_add, **style._btn_employees_add)
        btn_employees_add.place(relx=0.9, y=10)

        # ===== Employees Table =======
        frm_table = CTkFrame(self._root, fg_color='transparent')
        frm_table.place(x=20, y=70)

        lbl_top_line = CTkLabel(frm_table, text = '', fg_color='#303030', width=WINDOW_WIDTH-40, height=1, corner_radius=10)
        lbl_top_line.pack(fill=X)

        frm_headings = CTkFrame(frm_table, fg_color='transparent')
        frm_headings.pack(fill=X)

        lbl_srno = CTkLabel(frm_headings, text='SR NO').grid(**fn_grid(0, 0), padx=10)
        lbl_name = CTkLabel(frm_headings, text='NAME').grid(**fn_grid(0, 1), padx=50)
        lbl_id = CTkLabel(frm_headings, text='ID').grid(**fn_grid(0, 2), padx=10)
        lbl_contact1 = CTkLabel(frm_headings, text='CONTACT 1').grid(**fn_grid(0, 3), padx=20)
        lbl_working_status = CTkLabel(frm_headings, text='WORKING?').grid(**fn_grid(0, 4), padx=10)
        lbl_designation = CTkLabel(frm_headings, text='DESIGNATION').grid(**fn_grid(0, 5), padx=20)
        lbl_department = CTkLabel(frm_headings, text='DEPARTMENT').grid(**fn_grid(0, 6), padx=20)

        


    def win_emp_add(self):
        new_win = CTkToplevel(self._root)
        new_obj = EmployeesPage_Add(new_win)
        new_win.transient(self._root)


if __name__ == "__main__":
    root = CTk()
    obj = EmployeesPage(root)
    root.mainloop()