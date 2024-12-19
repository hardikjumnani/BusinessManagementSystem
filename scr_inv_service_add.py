import pyautogui as pg
from customtkinter import *
from PIL import Image

from style_global import COLOR, fn_grid

SCREEN_WIDTH = pg.size()[0]
SCREEN_HEIGHT = pg.size()[1]

WINDOW_WIDTH = int(SCREEN_WIDTH * 0.3)
WINDOW_HEIGHT = int(SCREEN_HEIGHT * 0.38)
WINDOW_X = int(SCREEN_WIDTH * 0.27)
WINDOW_Y = int(SCREEN_HEIGHT * 0.15)

class StyleInventoryPage_ServiceAdd:
    def __init__(self):
        self._lbl_title = {
            'text_color' : COLOR[4], 
            'fg_color' : COLOR[1], 
            'font' : ('Arial', 30, 'bold'),
            'corner_radius': 1,
            'width' : WINDOW_WIDTH,
            'height' : 50,
        }
        self._txt_form = {
            'border_width' : 0,
        }
        self._opt_balance = {
            'fg_color' : '#343638',
        }
        self._btn_save = {
            'width' : int(WINDOW_WIDTH/4), 
            'height' : 40,
        }
        self._btn_clear = {
            'width' : int(WINDOW_WIDTH/4), 
            'height' : 40, 
            'fg_color' : 'grey',
        }
        self._btn_add = {
            'anchor' : W,
            'width' : 10,
            'height' : 10,
        }
        self._btn_save = {
            'width' : int(WINDOW_WIDTH/5), 
        }
        self._btn_clear = {
            'width' : int(WINDOW_WIDTH/5), 
            'fg_color' : 'grey',
        }
style = StyleInventoryPage_ServiceAdd()


class InventoryPage_ServiceAdd:
    def __init__(self, root:CTk):
        self._root = root
        self._root.title('Add Service')
        self._root.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{WINDOW_X}+{WINDOW_Y}')

        # === Vars ====
        self.var_first_name = StringVar()


        # === Widgets === (code, name, price, expense)
        # === title ===
        lbl_title = CTkLabel(self._root, text='New Service', **style._lbl_title)
        lbl_title.place(x=0, y=0)

        # === Service image ===
        frm_service_img = CTkFrame(self._root)
        frm_service_img.place(x=20, y=70)

        jpg_default_image = CTkImage(dark_image=Image.open('AppData/icons/png/service_default.png'), size=(250, 250))
        lbl_service_img = CTkLabel(frm_service_img, image=jpg_default_image, text='')
        lbl_service_img.pack(fill=BOTH)

        # ===== Service Details =====
        # Frame 1 (Right)
        frm_details1 = CTkFrame(self._root, fg_color='transparent')
        frm_details1.place(x=int(WINDOW_WIDTH/2), y=70)

        # Row 1
        lbl_code = CTkLabel(frm_details1, text='Code')
        lbl_code.grid(**fn_grid(0, 0), sticky=W, padx=5)

        txt_code = CTkEntry(frm_details1, **style._txt_form)
        txt_code.grid(**fn_grid(1, 0), sticky=W, columnspan=2, padx=5, pady=(0, 4))

        # Row 3
        lbl_description = CTkLabel(frm_details1, text='Description')
        lbl_description.grid(**fn_grid(2, 0), sticky=W, padx=5)

        txt_description = CTkTextbox(frm_details1, width=int(WINDOW_WIDTH/2)-10, height=115, **style._txt_form)
        txt_description.grid(**fn_grid(3, 0), sticky=W, columnspan=4)

        # Row 4
        lbl_retail = CTkLabel(frm_details1, text='Retail*')
        lbl_retail.grid(**fn_grid(4, 0), sticky=W, padx=5)

        txt_retail_price = CTkEntry(frm_details1, placeholder_text='Retail Price', width=int(WINDOW_WIDTH/4), **style._txt_form)
        txt_retail_price.grid(**fn_grid(5, 0), columnspan=2, sticky=W, padx=(0, 2), pady=(0, 10))

        txt_unit_1 = CTkEntry(frm_details1, placeholder_text='Retail Unit', width=int(WINDOW_WIDTH/4)-20, **style._txt_form)
        txt_unit_1.grid(**fn_grid(5, 2), columnspan=2, sticky=W, padx=(2, 0), pady=(0, 10))

        # Row 6
        lbl_expense = CTkLabel(frm_details1, text='Expense')
        lbl_expense.grid(**fn_grid(6, 0), sticky=W, padx=5)

        self.icon_add = CTkImage(dark_image=Image.open('AppData/icons/png/add.png'), size=(15, 15))
        self.icon_subtract = CTkImage(dark_image=Image.open('AppData/icons/png/subtract.png'), size=(15, 15))
        self.btn_expense = CTkButton(frm_details1, text='', image=self.icon_add, command=self.fn_expense_toggle, fg_color='lightgreen', hover_color='green', **style._btn_add)
        self.btn_expense.grid(**fn_grid(6, 1), sticky=W)
        self.var_expense_active = False

        self.txt_expense_price = CTkEntry(frm_details1, placeholder_text='Expense Price', width=int(WINDOW_WIDTH/4)-10, **style._txt_form)
        # self.txt_expense_price.grid(**fn_grid(7, 0), columnspan=2, sticky=W, padx=(0, 2), pady=(0, 10))


        # Frame 2 (Left)
        frm_details2 = CTkFrame(self._root, fg_color='transparent')
        frm_details2.place(x=15, y=330)

        # Row 2
        txt_name = CTkEntry(frm_details2, placeholder_text='Service Name*', width=int(WINDOW_WIDTH/2.2), **style._txt_form)
        txt_name.grid(**fn_grid(0, 0), columnspan=4)

        # Row 3
        btn_save = CTkButton(frm_details2, text='Save', **style._btn_save)
        btn_save.grid(**fn_grid(1, 0), columnspan=2, pady=(10, 5))

        btn_clear = CTkButton(frm_details2, text='Clear', **style._btn_clear)
        btn_clear.grid(**fn_grid(1, 2), columnspan=2, pady=(10, 5))

        

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 

    def fn_save(self): ...
    def fn_clear(self): ...

    def fn_expense_toggle(self):
        if not self.var_expense_active:
            self.btn_expense.configure(image=self.icon_subtract, fg_color='tomato', hover_color='red')
            self.txt_expense_price.grid(**fn_grid(7, 0), columnspan=2, sticky=W, padx=(0, 2), pady=(0, 10))
            self.var_expense_active = True
        else:
            self.btn_expense.configure(image=self.icon_add, fg_color='lightgreen', hover_color='green')
            self.txt_expense_price.grid_forget()
            self.var_expense_active = False
            '''
            Add vars to be empty
            '''



if __name__ == "__main__":
    root = CTk()
    obj = InventoryPage_ServiceAdd(root)
    root.mainloop()