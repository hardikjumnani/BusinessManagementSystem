'''
Images to style global
'''
import pyautogui as pg
from customtkinter import *
from PIL import Image

from style_global import COLOR, fn_grid

SCREEN_WIDTH = pg.size()[0]
SCREEN_HEIGHT = pg.size()[1]

WINDOW_WIDTH = int(SCREEN_WIDTH * 0.3)
WINDOW_HEIGHT = int(SCREEN_HEIGHT * 0.41)
WINDOW_X = int(SCREEN_WIDTH * 0.27)
WINDOW_Y = int(SCREEN_HEIGHT * 0.15)

class StyleInventoryPage_ProductAdd:
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
style = StyleInventoryPage_ProductAdd()


class InventoryPage_ProductAdd:
    def __init__(self, root:CTk):
        self._root = root
        self._root.title('Add Product')
        self._root.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{WINDOW_X}+{WINDOW_Y}')

        # === Vars ====
        self.var_first_name = StringVar()


        # === Widgets ===
        # === title ===
        lbl_title = CTkLabel(self._root, text='New Product', **style._lbl_title)
        lbl_title.place(x=0, y=0)

        # === product image ===
        frm_product_img = CTkFrame(self._root)
        frm_product_img.place(x=20, y=70)

        jpg_default_image = CTkImage(dark_image=Image.open('AppData/icons/png/product_default.png'), size=(250, 250))
        lbl_product_img = CTkLabel(frm_product_img, image=jpg_default_image, text='')
        lbl_product_img.pack(fill=BOTH)

        # ===== Product Details =====
        # Frame 1 (Right)
        frm_details1 = CTkFrame(self._root, fg_color='transparent')
        frm_details1.place(x=int(WINDOW_WIDTH/2), y=70)

        # Row 1
        lbl_description = CTkLabel(frm_details1, text='Description')
        lbl_description.grid(**fn_grid(2, 0), sticky=W, padx=5)

        txt_description = CTkTextbox(frm_details1, width=int(WINDOW_WIDTH/2)-10, height=70, **style._txt_form)
        txt_description.grid(**fn_grid(3, 0), sticky=W, columnspan=4)

        # Row 2
        lbl_stock = CTkLabel(frm_details1, text='Stock')
        lbl_stock.grid(**fn_grid(4, 0), sticky=W, padx=5)

        txt_stock_current = CTkEntry(frm_details1, placeholder_text='Current Stock', width=int(WINDOW_WIDTH/4)-10, **style._txt_form)
        txt_stock_current.grid(**fn_grid(5, 0), sticky=W, columnspan=2, padx=(0, 2), pady=(0, 10))

        txt_stock_min = CTkEntry(frm_details1, placeholder_text='Min Stock', width=int(WINDOW_WIDTH/4)-10, **style._txt_form)
        txt_stock_min.grid(**fn_grid(5, 2), sticky=W, columnspan=2, padx=(2, 0), pady=(0, 10))

        # Row 3
        lbl_retail = CTkLabel(frm_details1, text='Retail*')
        lbl_retail.grid(**fn_grid(6, 0), sticky=W, padx=5)

        txt_retail_price = CTkEntry(frm_details1, placeholder_text='Retail Price', width=int(WINDOW_WIDTH/4)-10, **style._txt_form)
        txt_retail_price.grid(**fn_grid(7, 0), columnspan=2, sticky=W, padx=(0, 2), pady=(0, 10))

        txt_unit_1 = CTkEntry(frm_details1, placeholder_text='Retail Unit', width=int(WINDOW_WIDTH/4)-10, **style._txt_form)
        txt_unit_1.grid(**fn_grid(7, 2), columnspan=2, sticky=W, padx=(2, 0), pady=(0, 10))

        # Row 4
        lbl_wholesale = CTkLabel(frm_details1, text='Wholesale')
        lbl_wholesale.grid(**fn_grid(8, 0), sticky=W, padx=5)

        self.icon_add = CTkImage(dark_image=Image.open('AppData/icons/png/add.png'), size=(15, 15))
        self.icon_subtract = CTkImage(dark_image=Image.open('AppData/icons/png/subtract.png'), size=(15, 15))
        self.btn_wholesale = CTkButton(frm_details1, text='', image=self.icon_add, command=self.fn_wholesale_toggle, fg_color='lightgreen', hover_color='green', **style._btn_add)
        self.btn_wholesale.grid(**fn_grid(8, 1), sticky=W)
        self.var_wholesale_active = False

        self.txt_wholesale_price = CTkEntry(frm_details1, placeholder_text='Wholesale Price', width=int(WINDOW_WIDTH/4)-10, **style._txt_form)
        # self.txt_wholesale_price.grid(**fn_grid(9, 0), columnspan=2, sticky=W, padx=(0, 2), pady=(0, 10))

        self.txt_unit_2 = CTkEntry(frm_details1, placeholder_text='Wholesale Unit', width=int(WINDOW_WIDTH/4)-10, **style._txt_form)
        # self.txt_unit_2.grid(**fn_grid(9, 2), columnspan=2, sticky=W, padx=(2, 0), pady=(0, 10))

        # Row 5
        lbl_purchase = CTkLabel(frm_details1, text='Purchase')
        lbl_purchase.grid(**fn_grid(10, 0), sticky=W, padx=5)

        self.btn_purchase = CTkButton(frm_details1, text='', image=self.icon_add, command=self.fn_purchase_toggle, fg_color='lightgreen', hover_color='green', **style._btn_add)
        self.btn_purchase.grid(**fn_grid(10, 1), sticky=W)
        self.var_purchase_active = False

        self.txt_purchase_price = CTkEntry(frm_details1, placeholder_text='Purchase Price', width=int(WINDOW_WIDTH/4)-10, **style._txt_form)
        # self.txt_purchase_price.grid(**fn_grid(11, 0), columnspan=2, sticky=W, padx=(0, 2), pady=(0, 10))

        self.txt_unit_3 = CTkEntry(frm_details1, placeholder_text='Purchase Unit', width=int(WINDOW_WIDTH/4)-10, **style._txt_form)
        # self.txt_unit_3.grid(**fn_grid(11, 2), columnspan=2, sticky=W, padx=(2, 0), pady=(0, 10))


        # Frame 2 (Left)
        frm_details2 = CTkFrame(self._root, fg_color='transparent')
        frm_details2.place(x=15, y=330)

        # Row 1
        txt_code = CTkEntry(frm_details2, placeholder_text='Code', **style._txt_form)
        txt_code.grid(**fn_grid(0, 1), sticky=W, columnspan=2, padx=5, pady=(0, 4))

        # Row 2
        txt_name = CTkEntry(frm_details2, placeholder_text='Product Name*', width=int(WINDOW_WIDTH/2.2), **style._txt_form)
        txt_name.grid(**fn_grid(1, 0), columnspan=4)

        # Row 3
        btn_save = CTkButton(frm_details2, text='Save', **style._btn_save)
        btn_save.grid(**fn_grid(2, 0), columnspan=2, pady=(10, 5))

        btn_clear = CTkButton(frm_details2, text='Clear', **style._btn_clear)
        btn_clear.grid(**fn_grid(2, 2), columnspan=2, pady=(10, 5))

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 

    def fn_save(self): ...
    def fn_clear(self): ...

    def fn_wholesale_toggle(self):
        if not self.var_wholesale_active:
            self.btn_wholesale.configure(image=self.icon_subtract, fg_color='tomato', hover_color='red')
            self.txt_wholesale_price.grid(**fn_grid(9, 0), columnspan=2, sticky=W, padx=(0, 2), pady=(0, 10))
            self.txt_unit_2.grid(**fn_grid(9, 2), columnspan=2, sticky=W, padx=(2, 0), pady=(0, 10))
            self.var_wholesale_active = True
        else:
            self.btn_wholesale.configure(image=self.icon_add, fg_color='lightgreen', hover_color='green')
            self.txt_wholesale_price.grid_forget()
            self.txt_unit_2.grid_forget()
            self.var_wholesale_active = False
            '''
            Add vars to be empty
            '''
    
    def fn_purchase_toggle(self):
        if not self.var_purchase_active:
            self.btn_purchase.configure(image=self.icon_subtract, fg_color='tomato', hover_color='red')

            self.txt_purchase_price.grid(**fn_grid(11, 0), columnspan=2, sticky=W, padx=(0, 2), pady=(0, 10))
            self.txt_unit_3.grid(**fn_grid(11, 2), columnspan=2, sticky=W, padx=(2, 0), pady=(0, 10))

            self.var_purchase_active = True
        else:
            self.btn_purchase.configure(image=self.icon_add, fg_color='lightgreen', hover_color='green')
            self.txt_purchase_price.grid_forget()
            self.txt_unit_3.grid_forget()
            self.var_purchase_active = False
            '''
            Add vars to be empty
            '''




if __name__ == "__main__":
    root = CTk()
    obj = InventoryPage_ProductAdd(root)
    root.mainloop()