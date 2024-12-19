'''
Greater than less than, and shows total products and count after filter
'''
'''
How to make new prod and service, Min Stock Vali Sorting
'''
import pyautogui as pg
from customtkinter import *
from PIL import Image
from tkinter import Frame
from tkinter.ttk import Treeview, Scrollbar, Style

from style_global import COLOR
from scr_inv_service_add import InventoryPage_ServiceAdd
from scr_inv_product_add import InventoryPage_ProductAdd

SCREEN_WIDTH = pg.size()[0]
SCREEN_HEIGHT = pg.size()[1]

WINDOW_WIDTH = int(SCREEN_WIDTH * 0.65)
WINDOW_HEIGHT = int(SCREEN_HEIGHT * 0.6)
WINDOW_X = int(SCREEN_WIDTH * 0.1)
WINDOW_Y = int(SCREEN_HEIGHT * 0.05)

class StyleInventoryPage:
    def __init__(self):
        self._lbl_title = {
            'text_color' : COLOR[4], 
            'fg_color' : COLOR[1], 
            'font' : ('Arial', 20, 'bold'),
            'corner_radius': 1,
            'width' : int(WINDOW_WIDTH/2.5),
            'height' : 40,
        }
        self._txt_form = {
            'border_width' : 0,
            'height' : 30,
        }
        self._btn_search = {
            'width' : 20,
            'fg_color' : COLOR[1],
            'hover_color' : 'blue',
        }
        self._rad_sort = {
            'font' : ('Calibra', 14),
            'width' : 5,
            'height' : 10,
            'radiobutton_width' : 10,
            'radiobutton_height' : 10,
            'border_width_unchecked' : 2,
        }
        self._chk_sort = {
            'width' : 10,
            'height' : 10,
            'corner_radius' : 5,
            'checkbox_width' : 15,
            'checkbox_height' : 15,
        }
        self._btn_clear = {
            'fg_color' : 'grey',
        }
        self._btn_add = {
            'anchor' : W,
            'text_color' : 'black',
            'fg_color' : 'lightgreen',
            'hover_color' : 'green',
            'height' : 10, # To set it to min
        }
        self._lbl_sort = {
            'font' : ('Calibra', 14, 'bold')
        }
style = StyleInventoryPage()


class InventoryPage:
    def __init__(self, root:CTk):
        self._root = root
        self._root.title('Inventory')
        self._root.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{WINDOW_X}+{WINDOW_Y}')

        # Styling Table
        style2 = Style()
        style2.theme_use('clam')
        style2.configure(
            'Treeview',
            background='', # row original color
            foreground='', # selected color
            rowheight=30,
            fieldbackground='#242424', # no row vali space ka color
        )
        style2.map('Treeview', background=[('selected', COLOR[2])])

        # === All Vars ===
        self.var_sort_product_alphabetical = StringVar(value='other')
        self.var_sort_product_retail = StringVar(value='other')
        self.var_sort_product_stock = StringVar(value='other')
        self.var_sort_product_category = StringVar(value='other')

        self.var_sort_service_alphabetical = StringVar(value='other')
        self.var_sort_service_price = StringVar(value='other')
        self.var_sort_service_expense = StringVar(value='other')


        # === Widgets ===
        # === Products Table ===
        frm_product_table = Frame(self._root)
        frm_product_table.place(x=10, y=10, width=int(WINDOW_WIDTH/1.4), height=int(WINDOW_HEIGHT/1.6)-10)

        scrollx = Scrollbar(frm_product_table, orient=HORIZONTAL) # making scroll bar
        scrolly = Scrollbar(frm_product_table, orient=VERTICAL) # making scroll bar

        tbl_services= Treeview(frm_product_table, columns=('Code', 'Name', 'Retail', 'Unit1', 'Stock', 'Category', 'Wholesale', 'Unit2', 'Purchase'), xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)

        scrollx.pack(side=BOTTOM, fill=X) #packing
        scrollx.config(command=tbl_services.xview)

        scrolly.pack(side=RIGHT, fill=Y) #packing
        scrolly.config(command=tbl_services.yview)

        # ('Code', 'Name', 'Retail', 'Unit1', 'Stock', 'Category', 'Wholesale', 'Unit2', 'Purchase')
        tbl_services.heading("Code", text="Code")
        tbl_services.heading("Name", text="Name")
        tbl_services.heading("Retail", text="Retail P")
        tbl_services.heading("Unit1", text="Unit M")
        tbl_services.heading("Stock", text="Stock")
        tbl_services.heading("Category", text="Category")
        tbl_services.heading("Wholesale", text="Wholesale P")
        tbl_services.heading("Unit2", text="Unit B")
        tbl_services.heading("Purchase", text="Purchase P")
        
        tbl_services["show"] = "headings"

        tbl_services.column("Code", width=90, anchor=CENTER)
        tbl_services.column("Name", width=280, anchor=CENTER)
        tbl_services.column("Retail", width=100, anchor=CENTER)
        tbl_services.column("Unit1", width=100, anchor=CENTER)
        tbl_services.column("Stock", width=100, anchor=CENTER)
        tbl_services.column("Category", width=170, anchor=CENTER)
        tbl_services.column("Wholesale", width=100, anchor=CENTER)
        tbl_services.column("Unit2", width=100, anchor=CENTER)
        tbl_services.column("Purchase", width=100, anchor=CENTER)

        tbl_services.pack(fill=BOTH, expand=1)

        # === Services Table ===
        frm_service_table = Frame(self._root)
        frm_service_table.place(x=10, y=int(WINDOW_HEIGHT/2)+110, width=int(WINDOW_WIDTH/1.4), height=int(WINDOW_HEIGHT/1.7)-10)

        scrollx = Scrollbar(frm_service_table, orient=HORIZONTAL) # making scroll bar
        scrolly = Scrollbar(frm_service_table, orient=VERTICAL) # making scroll bar

        tbl_services= Treeview(frm_service_table, columns=('Code', 'Name', 'Price', 'Expense'), xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)

        scrollx.pack(side=BOTTOM, fill=X) #packing
        scrollx.config(command=tbl_services.xview)

        scrolly.pack(side=RIGHT, fill=Y) #packing
        scrolly.config(command=tbl_services.yview)

        # ('Code', 'Name', 'Retail', 'Unit1', 'Stock', 'Category', 'Wholesale', 'Unit2', 'Purchase')
        tbl_services.heading("Code", text="Code")
        tbl_services.heading("Name", text="Name")
        tbl_services.heading("Price", text="Price")
        tbl_services.heading("Expense", text="Expense")
        
        tbl_services["show"] = "headings"

        tbl_services.column("Code", width=90, anchor=CENTER)
        tbl_services.column("Name", width=280, anchor=CENTER)
        tbl_services.column("Price", width=100, anchor=CENTER)
        tbl_services.column("Expense", width=100, anchor=CENTER)

        tbl_services.pack(fill=BOTH, expand=1)



        # === Search & Sort ===
        # lbl_title = CTkLabel(self._root, text='Search & Sort', **style._lbl_title)
        # lbl_title.place(x=int(WINDOW_WIDTH/1.7), y=10)

        # === Product ====
        frm_product = CTkFrame(self._root, fg_color='transparent')
        frm_product.place(x=int(WINDOW_WIDTH/1.7), y=10)
        
        frm_product_options = CTkFrame(frm_product, width=int(WINDOW_WIDTH/2.5), height=int(WINDOW_HEIGHT/2), fg_color='transparent')
        frm_product_options.pack()

        # Row 1
        txt_product_search = CTkEntry(frm_product_options, placeholder_text='Search Product', width=int(WINDOW_WIDTH/3), **style._txt_form)
        txt_product_search.grid(row=0, column=0, columnspan=5)

        icon_search = CTkImage(dark_image=Image.open('AppData/icons/png/search.png'), size=(25, 25))
        btn_product_search = CTkButton(frm_product_options, image=icon_search, text='', **style._btn_search)
        btn_product_search.grid(row=0, column=5, padx=10)

        frm_sort_and_filter = CTkFrame(frm_product, fg_color='transparent')
        frm_sort_and_filter.pack(fill=X)

        # Row 2
        frm_sort = CTkFrame(frm_sort_and_filter, fg_color='transparent')
        frm_sort.pack(anchor=W, side=LEFT)

        lbl_sort = CTkLabel(frm_sort, text='Sort', font=('Calibra', 20, 'bold'))
        lbl_sort.grid(row=0, column=0, padx=10)
        
        # ::: Column 1
        # lbl_sort_alphabetical = CTkLabel(frm_sort, text='Alphabetical', **style._lbl_sort)
        # lbl_sort_alphabetical.grid(row=1, column=0, columnspan=2, padx=(0, 20))

        rad_sort_AZ = CTkRadioButton(frm_sort, text='A-Z', value='az', variable=self.var_sort_product_alphabetical, **style._rad_sort)
        rad_sort_AZ.grid(row=1, column=0, padx=20, pady=(10, 3))
        rad_sort_ZA = CTkRadioButton(frm_sort, text='Z-A', value='za', variable=self.var_sort_product_alphabetical, **style._rad_sort)
        rad_sort_ZA.grid(row=2, column=0, padx=20, pady=(3, 10))

        # ::: Column 2
        # lbl_sort_retail = CTkLabel(frm_sort, text='Retail Price', **style._lbl_sort)
        # lbl_sort_retail.grid(row=3, column=0, columnspan=2, padx=(0, 20))

        rad_sort_retail_LH = CTkRadioButton(frm_sort, text='Retail:Low To High', value='lh', variable=self.var_sort_product_retail, **style._rad_sort)
        rad_sort_retail_LH.grid(row=3, column=0, padx=20, pady=(10, 3))
        rad_sort_retail_HL = CTkRadioButton(frm_sort, text='Retail:High To Low', value='hl', variable=self.var_sort_product_retail, **style._rad_sort)
        rad_sort_retail_HL.grid(row=4, column=0, padx=20, pady=(3, 10))

        # ::: Column 3
        # lbl_sort_stock = CTkLabel(frm_sort, text='Stock', **style._lbl_sort)
        # lbl_sort_stock.grid(row=1, column=2, columnspan=2, padx=(0, 20))

        rad_sort_stock_LH = CTkRadioButton(frm_sort, text='Stock:Low To High', value='lh', variable=self.var_sort_product_stock, **style._rad_sort)
        rad_sort_stock_LH.grid(row=5, column=0, padx=20, pady=(10, 3))
        rad_sort_stock_HL = CTkRadioButton(frm_sort, text='Stock:High To Low', value='hl', variable=self.var_sort_product_stock, **style._rad_sort)
        rad_sort_stock_HL.grid(row=6, column=0, padx=20, pady=(3, 10))

        # ::: Column 4
        # lbl_sort_category = CTkLabel(frm_sort, text='Category', **style._lbl_sort)
        # lbl_sort_category.grid(row=3, column=2, columnspan=2, padx=(0, 20))

        chk_sort_category = CTkCheckBox(frm_sort, text='Sort By Category', onvalue='on', offvalue='off', variable=self.var_sort_product_category, **style._chk_sort)
        chk_sort_category.grid(row=7, column=0, pady=10)
        

        # Filter Part
        frm_filter = CTkFrame(frm_sort_and_filter, fg_color='transparent')
        frm_filter.pack(anchor=E)

        lbl_filter = CTkLabel(frm_filter, text='Filter', font=('Calibra', 20, 'bold'))
        lbl_filter.grid(row=0, column=0, columnspan=3, padx=20)

        # Row 1
        lbl_retail_price = CTkLabel(frm_filter, text='Retail Price')
        lbl_retail_price.grid(row=1, column=0, pady=8)

        opt_comparison = CTkOptionMenu(frm_filter, values=['<', '≤', '≥', '=', '≠'], width=50)
        opt_comparison.grid(row=1, column=1, pady=8)

        txt_retail_price = CTkEntry(frm_filter, width=80)
        txt_retail_price.grid(row=1, column=2, pady=8)

        # Row 2
        lbl_wholesale_price = CTkLabel(frm_filter, text='Wholesale Price')
        lbl_wholesale_price.grid(row=2, column=0, pady=8)

        opt_comparison = CTkOptionMenu(frm_filter, values=['<', '≤', '≥', '=', '≠'], width=50)
        opt_comparison.grid(row=2, column=1, pady=8)

        txt_wholesale_price = CTkEntry(frm_filter, width=80)
        txt_wholesale_price.grid(row=2, column=2, pady=8)

        # Row 3
        lbl_purchase_price = CTkLabel(frm_filter, text='Purchase Price')
        lbl_purchase_price.grid(row=3, column=0, pady=8)

        opt_comparison = CTkOptionMenu(frm_filter, values=['<', '≤', '≥', '=', '≠'], width=50)
        opt_comparison.grid(row=3, column=1, pady=8)

        txt_purchase_price = CTkEntry(frm_filter, width=80)
        txt_purchase_price.grid(row=3, column=2, pady=8)

        # Row 3
        lbl_stock = CTkLabel(frm_filter, text='Stock')
        lbl_stock.grid(row=4, column=0, pady=8)

        opt_comparison = CTkOptionMenu(frm_filter, values=['<', '≤', '≥', '=', '≠', '≤ Min Stock', '≥ Min Stock'], width=110)
        opt_comparison.grid(row=4, column=1, pady=8)

        txt_stock = CTkEntry(frm_filter, width=80)
        txt_stock.grid(row=4, column=2, pady=8)

        # Row 4
        frm_actions = CTkFrame(frm_filter, width=int(WINDOW_WIDTH/2.7), height=50, fg_color='transparent')
        frm_actions.grid(row=5, column=0, columnspan=3)

        btn_apply_sort = CTkButton(frm_actions, text='Apply All')
        btn_apply_sort.grid(row=0, column=0, padx=10, pady=10)

        btn_clear = CTkButton(frm_actions, text='Clear All', **style._btn_clear)
        btn_clear.grid(row=0, column=1, padx=10, pady=10)

        icon_add = CTkImage(dark_image=Image.open('AppData/icons/png/add.png'), size=(22, 22))
        btn_product_add = CTkButton(frm_product, image=icon_add, text='New Product', command=self.win_product_add, **style._btn_add)
        btn_product_add.pack()



        # === Service ====
        frm_service = CTkFrame(self._root, fg_color='transparent')
        frm_service.place(x=int(WINDOW_WIDTH/1.7), y=360)

        frm_service_options = CTkFrame(frm_service, width=int(WINDOW_WIDTH/2.5), height=int(WINDOW_HEIGHT/2), fg_color='transparent')
        frm_service_options.pack()

        # Row 1
        txt_service_search = CTkEntry(frm_service_options, placeholder_text='Search Service', width=int(WINDOW_WIDTH/3), **style._txt_form)
        txt_service_search.grid(row=2, column=0, columnspan=5)

        icon_search = CTkImage(dark_image=Image.open('AppData/icons/png/search.png'), size=(25, 25))
        btn_service_search = CTkButton(frm_service_options, image=icon_search, text='', **style._btn_search)
        btn_service_search.grid(row=2, column=5, padx=10)


        frm_sort_and_filter = CTkFrame(frm_service, fg_color='transparent')
        frm_sort_and_filter.pack(fill=X)

        # Row 2
        frm_sort = CTkFrame(frm_sort_and_filter, fg_color='transparent')
        frm_sort.pack(side=LEFT)

        lbl_sort = CTkLabel(frm_sort, text='Sort', font=('Calibra', 20, 'bold'))
        lbl_sort.grid(row=0, column=0, padx=10)
        
        # ::: Column 1
        # lbl_sort_alphabetical = CTkLabel(frm_sort, text='Alphabetical')
        # lbl_sort_alphabetical.grid(row=1, column=1, padx=(50, 100))

        rad_sort_AZ = CTkRadioButton(frm_sort, text='A-Z', value='az', variable=self.var_sort_service_alphabetical, **style._rad_sort)
        rad_sort_AZ.grid(row=1, column=0, padx=20, pady=(10, 3))
        rad_sort_ZA = CTkRadioButton(frm_sort, text='Z-A', value='za', variable=self.var_sort_service_alphabetical, **style._rad_sort)
        rad_sort_ZA.grid(row=2, column=0, padx=20, pady=(3, 10))

        # ::: Column 2
        # lbl_sort_retail = CTkLabel(frm_sort, text='Price')
        # lbl_sort_retail.grid(row=1, column=2, padx=(0, 20))

        rad_sort_price_LH = CTkRadioButton(frm_sort, text='Price:Low To High', value='lh', variable=self.var_sort_service_price, **style._rad_sort)
        rad_sort_price_LH.grid(row=3, column=0, padx=20, pady=(10, 3))
        rad_sort_price_HL = CTkRadioButton(frm_sort, text='Price:High To Low', value='hl', variable=self.var_sort_service_price, **style._rad_sort)
        rad_sort_price_HL.grid(row=4, column=0, padx=20, pady=(3, 10))

        # ::: Column 3
        rad_sort_expense_LH = CTkRadioButton(frm_sort, text='Expense:Low To High', value='lh', variable=self.var_sort_service_expense, **style._rad_sort)
        rad_sort_expense_LH.grid(row=5, column=0, padx=20, pady=(10, 3))
        rad_sort_expense_HL = CTkRadioButton(frm_sort, text='Expense:High To Low', value='hl', variable=self.var_sort_service_expense, **style._rad_sort)
        rad_sort_expense_HL.grid(row=6, column=0, padx=20, pady=(3, 10))

        # Filter Part
        frm_filter = CTkFrame(frm_sort_and_filter, fg_color='transparent')
        frm_filter.pack(side=RIGHT)

        lbl_filter = CTkLabel(frm_filter, text='Filter', font=('Calibra', 20, 'bold'))
        lbl_filter.grid(row=0, column=0, columnspan=3, padx=20)

        # Row 1
        lbl_price = CTkLabel(frm_filter, text='Price')
        lbl_price.grid(row=1, column=0, pady=8)

        opt_comparison = CTkOptionMenu(frm_filter, values=['<', '≤', '≥', '=', '≠'], width=50)
        opt_comparison.grid(row=1, column=1, pady=8)

        txt_price = CTkEntry(frm_filter, width=80)
        txt_price.grid(row=1, column=2, pady=8)

        # Row 2
        lbl_expense = CTkLabel(frm_filter, text='Expense')
        lbl_expense.grid(row=2, column=0, pady=8)

        opt_comparison = CTkOptionMenu(frm_filter, values=['<', '≤', '≥', '=', '≠'], width=50)
        opt_comparison.grid(row=2, column=1, pady=8)

        txt_expense = CTkEntry(frm_filter, width=80)
        txt_expense.grid(row=2, column=2, pady=8)
        
        # Row 3
        frm_actions = CTkFrame(frm_filter, width=int(WINDOW_WIDTH/2.7), height=50, fg_color='transparent')
        frm_actions.grid(row=3, column=0, columnspan=3)

        btn_apply_sort = CTkButton(frm_actions, text='Apply All', width=135)
        btn_apply_sort.grid(row=0, column=0, padx=10, pady=10)

        btn_clear = CTkButton(frm_actions, text='Clear All', width=135, **style._btn_clear)
        btn_clear.grid(row=0, column=1, padx=10, pady=10)

        # Row 4
        icon_add = CTkImage(dark_image=Image.open('AppData/icons/png/add.png'), size=(25, 25))
        btn_service_add = CTkButton(frm_service, image=icon_add, text='New Service', command=self.win_service_add, **style._btn_add)
        btn_service_add.pack()

    
    def win_product_add(self):
        new_win = CTkToplevel(self._root)
        new_obj = InventoryPage_ProductAdd(new_win)
        new_win.transient(self._root)
    
    def win_service_add(self):
        new_win = CTkToplevel(self._root)
        new_obj = InventoryPage_ServiceAdd(new_win)
        new_win.transient(self._root)


if __name__ == "__main__":
    root = CTk()
    obj = InventoryPage(root)
    root.mainloop()