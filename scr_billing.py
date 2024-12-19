import pyautogui as pg
from customtkinter import *
from PIL import Image
from tkinter import Frame
from tkinter.ttk import Treeview, Scrollbar, Style

from style_global import COLOR, fn_grid

SCREEN_WIDTH = pg.size()[0]
SCREEN_HEIGHT = pg.size()[1]

WINDOW_WIDTH = int(SCREEN_WIDTH * 0.7)
WINDOW_HEIGHT = int(SCREEN_HEIGHT * 0.65)
WINDOW_X = int(SCREEN_WIDTH * 0.05)
WINDOW_Y = int(SCREEN_HEIGHT * 0.05)

class StyleBillingPage:
    def __init__(self) -> None:
        self._lbl_title = {
            'text_color' : COLOR[4], 
            'fg_color' : COLOR[1], 
            'font' : ('Arial', 25, 'bold'),
            'corner_radius': 1,
            'width' : WINDOW_WIDTH,
            'height' : 50,
        }
        self._btn_search = {
            'width' : 20,
            'height' : 10,
            'fg_color' : COLOR[1],
            'hover_color' : 'blue',
        }
        self._lbl_customer_details = {
            'fg_color' : 'gray17',
            'width' : int(WINDOW_WIDTH/3.1),
            'font' : ('Arial', 20, 'bold'),
            'height' : 40,
        }
        self._opt_stakeholder = {
            'fg_color' : '#343638',
            'width' : int(WINDOW_WIDTH/3.1)-20, 
            'anchor' : CENTER,
        }
        self._lbl_cart = {
            'bg_color' : 'grey',
            'width' : int(WINDOW_WIDTH/6.2),
        }
        self._btn_discount_type = {
            'width' : 40,
            'fg_color' : '#144870',
        }
style = StyleBillingPage()

class BillingPage:
    def __init__(self, root:CTk):
        self._root = root
        self._root.title('Billing')
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

        # ====== All Vars =======
        self.var_bill = StringVar()

        # === Widgets ===
        # === Title ===
        lbl_title = CTkLabel(self._root, text='Billing', **style._lbl_title)
        lbl_title.place(x=0, y=0)

        # =============Inventory Mini ==========
        # === Products Table ===
        frm_product_table = Frame(self._root, bg='gray14')
        frm_product_table.place(x=5, y=80, width=int(WINDOW_WIDTH/2.45), height=int(WINDOW_HEIGHT/1.8))

        # Search Product
        frm_product_search = CTkFrame(frm_product_table, fg_color='gray14')
        frm_product_search.pack(side=TOP, fill=X)

        txt_product_search = CTkEntry(frm_product_search, placeholder_text='Search Product', width=int(WINDOW_WIDTH/3.9))
        txt_product_search.pack(side=LEFT, padx=15, pady=(0, 10))

        icon_search = CTkImage(dark_image=Image.open('AppData/icons/png/search.png'), size=(22, 22))
        btn_search = CTkButton(frm_product_search, image=icon_search, text='', **style._btn_search)
        btn_search.pack(side=LEFT, padx=5, pady=(0, 10))

        # Product Table
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
        frm_service_table = Frame(self._root, bg='gray14')
        frm_service_table.place(x=5, y=int(WINDOW_HEIGHT/1.42), width=int(WINDOW_WIDTH/2.45), height=int(WINDOW_HEIGHT/1.9))

        # Search Service
        frm_service_search = CTkFrame(frm_service_table, fg_color='gray14')
        frm_service_search.pack(side=TOP, fill=X)

        txt_service_search = CTkEntry(frm_service_search, placeholder_text='Search Service', width=int(WINDOW_WIDTH/3.9))
        txt_service_search.pack(side=LEFT, padx=15, pady=(0, 10))

        icon_search = CTkImage(dark_image=Image.open('AppData/icons/png/search.png'), size=(22, 22))
        btn_search = CTkButton(frm_service_search, image=icon_search, text='', **style._btn_search)
        btn_search.pack(side=LEFT, padx=5, pady=(0, 10))

        # Service Table
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


        # ==== Customer Details & Billing Items ====
        frm_middle = CTkFrame(self._root, fg_color='transparent')
        frm_middle.place(x=int(WINDOW_WIDTH/3)+10, y=60)
        # == Customer Details ==
        frm_customer_details = CTkFrame(frm_middle)
        frm_customer_details.pack()

        lbl_customer_details = CTkLabel(frm_customer_details, text='Customer Details', **style._lbl_customer_details)
        lbl_customer_details.grid(**fn_grid(0, 0), columnspan=5)

        opt_stakeholder = CTkOptionMenu(frm_customer_details, values=['Stakeholder 1', 'Stakeholder 2', 'Stakeholder 3'], **style._opt_stakeholder)
        opt_stakeholder.grid(**fn_grid(1, 0), columnspan=5, pady=10)

        # Row 1
        lbl_customer_name = CTkLabel(frm_customer_details, text='Name')
        lbl_customer_name.grid(**fn_grid(2, 0), pady=10)

        txt_customer_name = CTkEntry(frm_customer_details, width=int(WINDOW_WIDTH/4.55))
        txt_customer_name.grid(**fn_grid(2, 1), columnspan=4, pady=10)

        # Row 2
        lbl_customer_contact = CTkLabel(frm_customer_details, text='Contact')
        lbl_customer_contact.grid(**fn_grid(3, 0))

        txt_customer_contact1 = CTkEntry(frm_customer_details, placeholder_text='Contact 1')
        txt_customer_contact1.grid(**fn_grid(3, 1), columnspan=2)

        txt_customer_contact2 = CTkEntry(frm_customer_details, placeholder_text='Contact 2')
        txt_customer_contact2.grid(**fn_grid(3, 3), columnspan=2)

        # == CART ==
        frm_cart = CTkFrame(frm_middle)
        frm_cart.pack(pady=10)

        # Cart Label
        frm_cart_label = CTkFrame(frm_cart)
        frm_cart_label.pack()
        
        lbl_cart = CTkLabel(frm_cart_label, text='Cart', **style._lbl_cart)
        lbl_cart.pack(side=LEFT)
        
        lbl_total_items = CTkLabel(frm_cart_label, text='Total Items [00]', **style._lbl_cart)
        lbl_total_items.pack(side=RIGHT)

        # Cart List
        scrollx = Scrollbar(frm_cart, orient=HORIZONTAL) # making scroll bar
        scrolly = Scrollbar(frm_cart, orient=VERTICAL) # making scroll bar

        tbl_cart = Treeview(frm_cart, columns=('Name', 'Unit1', 'Quantity', 'UnitPrice', 'Total'), xscrollcommand=scrollx.set, yscrollcommand=scrolly.set, height=11)

        scrollx.pack(side=BOTTOM, fill=X) #packing
        scrollx.config(command=tbl_cart.xview)

        scrolly.pack(side=RIGHT, fill=Y) #packing
        scrolly.config(command=tbl_cart.yview)

        # ('Name', 'Unit1', 'Quantity', 'UnitPrice', 'Total')
        tbl_cart.heading("Name", text="Name")
        tbl_cart.heading("Unit1", text="Unit M")
        tbl_cart.heading("Quantity", text="Quantity")
        tbl_cart.heading("UnitPrice", text="Unit Price")
        tbl_cart.heading("Total", text="Total")
        
        tbl_cart["show"] = "headings"

        tbl_cart.column("Name", width=150, anchor=CENTER)
        tbl_cart.column("Unit1", width=80, anchor=CENTER)
        tbl_cart.column("Quantity", width=80, anchor=CENTER)
        tbl_cart.column("UnitPrice", width=80, anchor=CENTER)
        tbl_cart.column("Total", width=100, anchor=CENTER)

        tbl_cart.pack(fill=BOTH, expand=1)


        # == Cart Entry ==
        frm_cart_entry = CTkFrame(frm_middle, width=int(WINDOW_WIDTH/3.1))
        frm_cart_entry.pack()

        # Row 1
        lbl_item_name = CTkLabel(frm_cart_entry, text='Name', width=int(WINDOW_WIDTH/17))
        lbl_item_name.grid(**fn_grid(0, 0), pady=5)

        txt_item_name = CTkEntry(frm_cart_entry, width=int(WINDOW_WIDTH/7.75))
        txt_item_name.grid(**fn_grid(0, 1), columnspan=2, pady=5)

        lbl_item_unit = CTkLabel(frm_cart_entry, text='Unit', width=int(WINDOW_WIDTH/17))
        lbl_item_unit.grid(**fn_grid(0, 3), pady=5)

        opt_item_unit = CTkOptionMenu(frm_cart_entry, values=['Unit', 'PCS', 'BAGS', 'L', '...'], width=int(WINDOW_WIDTH/17))
        opt_item_unit.grid(**fn_grid(0, 4), pady=5)


        # Row 2
        lbl_item_quantity = CTkLabel(frm_cart_entry, text='Quantity', width=int(WINDOW_WIDTH/17))
        lbl_item_quantity.grid(**fn_grid(1, 0), padx=5, pady=5)

        txt_item_quantity = CTkEntry(frm_cart_entry, width=int(WINDOW_WIDTH/17))
        txt_item_quantity.grid(**fn_grid(1, 1), pady=5)

        lbl_item_unit_price = CTkLabel(frm_cart_entry, text='Unit Price', width=int(WINDOW_WIDTH/17))
        lbl_item_unit_price.grid(**fn_grid(1, 2), pady=5)

        txt_item_unit_price = CTkEntry(frm_cart_entry, width=int(WINDOW_WIDTH/17))
        txt_item_unit_price.grid(**fn_grid(1, 3), pady=5)

        lbl_item_in_stock = CTkLabel(frm_cart_entry, text='In Stock []', width=int(WINDOW_WIDTH/17))
        lbl_item_in_stock.grid(**fn_grid(1, 4), pady=5)


        # Row 3
        btn_cart_add = CTkButton(frm_cart_entry, text='Add To Cart', fg_color='orange', width=int(WINDOW_WIDTH/9))
        btn_cart_add.grid(**fn_grid(2, 0), columnspan=2, padx=(15, 5), pady=5)

        btn_cart_add = CTkButton(frm_cart_entry, text='Delete', fg_color='red', width=int(WINDOW_WIDTH/17))
        btn_cart_add.grid(**fn_grid(2, 2), padx=10, pady=5)

        btn_cart_add = CTkButton(frm_cart_entry, text='Clear Cart', fg_color='grey', width=int(WINDOW_WIDTH/11))
        btn_cart_add.grid(**fn_grid(2, 3), columnspan=2, sticky=W, padx=10, pady=5)


        # ===== Bill =====
        frm_right = CTkFrame(self._root, width=int(WINDOW_WIDTH/3.1), fg_color='transparent')
        frm_right.place(x=int(WINDOW_WIDTH/1.48), y=60)     

        # Bill
        frm_bill_preview = CTkFrame(frm_right)
        frm_bill_preview.pack()

        lbl_bill = CTkLabel(frm_bill_preview, text='Bill', width=int(WINDOW_WIDTH/3.13))
        lbl_bill.pack(fill=X)

        txt_bill = CTkTextbox(frm_bill_preview, state=DISABLED, fg_color='lightgrey', height=int(WINDOW_HEIGHT/1.58))
        txt_bill.pack(fill=BOTH)

        # Bill Details & Controls
        frm_bill_details = CTkFrame(frm_right)
        frm_bill_details.pack(fill=X)

        # Row 1
        lbl_amount_paid = CTkLabel(frm_bill_details, text='Paid')
        lbl_amount_paid.grid(**fn_grid(0, 0), padx=8, pady=5)

        txt_amount_paid = CTkEntry(frm_bill_details, width=int(WINDOW_WIDTH/9))
        txt_amount_paid.grid(**fn_grid(0, 1), columnspan=2, padx=5, pady=5)

        lbl_amount_change = CTkLabel(frm_bill_details, text='Change [0.0]')
        lbl_amount_change.grid(**fn_grid(0, 3), padx=8, pady=5)

        opt_pay_type = CTkOptionMenu(frm_bill_details, values=['Cash', 'Cheque', 'Debit Card', 'Credit Card', 'Other'], width=int(WINDOW_WIDTH/13))
        opt_pay_type.grid(**fn_grid(0, 4), sticky=E, pady=5)

        # Row 2 ======
        lbl_discount = CTkLabel(frm_bill_details, text='Discount')
        lbl_discount.grid(**fn_grid(1, 0), sticky=W,padx=5, pady=(0, 10))

        self.txt_discount = CTkEntry(frm_bill_details, placeholder_text='0.0', width=int(WINDOW_WIDTH/9))
        self.txt_discount.grid(**fn_grid(1, 1), columnspan=2, sticky=W, padx=5, pady=(0, 10))

        self.btn_discount_type = CTkButton(frm_bill_details, text='%', command=self.fn_change_discount_type, **style._btn_discount_type)
        self.btn_discount_type.grid(**fn_grid(1, 3), sticky=W, padx=5, pady=(0, 10))
        # =======

        # Row 3
        lbl_amount_payable = CTkLabel(frm_bill_details, text='Bill Amount\n[00.00]', width=int(WINDOW_WIDTH/11), fg_color='green')
        lbl_amount_payable.grid(**fn_grid(2, 0), columnspan=2, padx=5, ipady=5)

        # Row 4
        lbl_bill_items_total = CTkLabel(frm_bill_details, text='Total Items\n[00]', width=int(WINDOW_WIDTH/11), fg_color='blue')
        lbl_bill_items_total.grid(**fn_grid(3, 0), columnspan=2, padx=5, ipady=5)

        # Frame Bill Controls
        frm_bill_controls = CTkFrame(frm_bill_details, fg_color='transparent')
        frm_bill_controls.grid(**fn_grid(2, 2), rowspan=2, columnspan=3, padx=(10, 0))

        btn_bill_generate = CTkButton(frm_bill_controls, text='Generate', fg_color='green', width=150)
        btn_bill_generate.grid(**fn_grid(0, 0), columnspan=2, padx=6, pady=6)

        btn_bill_save = CTkButton(frm_bill_controls, text='Save', fg_color='blue', width=100)
        btn_bill_save.grid(**fn_grid(0, 2), padx=6, pady=6)

        btn_bill_print = CTkButton(frm_bill_controls, text='Print', fg_color='tomato', width=100)
        btn_bill_print.grid(**fn_grid(1, 0), padx=6, pady=6)
    
        btn_bill_clear = CTkButton(frm_bill_controls, text='Clear Bill', fg_color='grey', width=150)
        btn_bill_clear.grid(**fn_grid(1, 1), columnspan=2, padx=6, pady=6)

    def fn_change_discount_type(self):
        if self.btn_discount_type.cget('text') == 'INR': 
            self.btn_discount_type.configure(text='%')
        else:
            self.btn_discount_type.configure(text='INR')
        
        self.btn_discount_type.configure(width=40)

if __name__ == "__main__":
    root = CTk()
    obj = BillingPage(root)
    root.mainloop()