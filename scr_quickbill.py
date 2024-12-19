import pyautogui as pg
from customtkinter import *
from PIL import Image

from style_global import COLOR, fn_grid

SCREEN_WIDTH = pg.size()[0]
SCREEN_HEIGHT = pg.size()[1]

WINDOW_WIDTH = int(SCREEN_WIDTH * 0.4)
WINDOW_HEIGHT = int(SCREEN_HEIGHT * 0.42)+10
WINDOW_X = int(SCREEN_WIDTH * 0.2)
WINDOW_Y = int(SCREEN_HEIGHT * 0.2)

class StyleQuickBillPage:
    def __init__(self) -> None:
        self._lbl_title = {
            'text_color' : COLOR[4], 
            'fg_color' : COLOR[1], 
            'font' : ('Arial', 20, 'bold'),
            'corner_radius': 1,
            'width' : int(WINDOW_WIDTH),
            'height' : 50,
        }
        self._opt_stakeholder = {
            'fg_color' : '#343638',
            'width' : int(WINDOW_WIDTH/2)-40, 
            'anchor' : CENTER,
        }
        self._txt_customer_form = {
            'width' : int(WINDOW_WIDTH/4)-40,
        }
        self._btn_add_items = {
            'height': 30,
            'width': int(WINDOW_WIDTH/2)-40,
        }
        self._btn_discount_type = {
            'width' : 40,
            'fg_color' : '#144870',
        }
        self._btn_bill = {
            'width' : 85,
            'height' : 40,
        }
        self._btn_bill_generate = {
            'fg_color' : 'green',
        }
        self._btn_bill_save = {}
        self._btn_bill_print = {
            'fg_color' : 'orange',
        }
        self._btn_bill_clear = {
            'fg_color' : 'grey',
        }
        self._txt_bill = {
            'fg_color' : 'lightgrey'
        }

style = StyleQuickBillPage()

class QuickBillPage:
    def __init__(self, root:CTk):
        self._root = root
        self._root.title('Quick Bill')
        self._root.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{WINDOW_X}+{WINDOW_Y}')

        # === Widgets ===
        # === Title ===
        lbl_title = CTkLabel(self._root, text='Quick Bill', **style._lbl_title)
        lbl_title.place(x=0, y=0)

        # === Left Side Of Info ===
        frm_details = CTkFrame(self._root, width=int(WINDOW_WIDTH/2), fg_color='transparent')
        frm_details.place(x=5, y=50)

        # === Date ===
        lbl_date = CTkLabel(frm_details, text='DATE: DD-MM-YYYY', width=int(WINDOW_WIDTH/2))
        lbl_date.grid(**fn_grid(0, 0), columnspan=2)

        # === Customer Details ===
        # Select stakeholder
        opt_stakeholder = CTkOptionMenu(frm_details, values=['Stakeholder 1', 'Stakeholder 2', 'Stakeholder 3'], **style._opt_stakeholder)
        opt_stakeholder.grid(**fn_grid(1, 0), columnspan=2)

        # Enter Details Manually
        self.txt_customer_name = CTkEntry(frm_details, placeholder_text='Customer Name', width=int(WINDOW_WIDTH/2)-40)
        self.txt_customer_name.grid(**fn_grid(2, 0), columnspan=2, pady=(20, 0))

        self.txt_customer_contact1 = CTkEntry(frm_details, placeholder_text='Contact 1', **style._txt_customer_form)
        self.txt_customer_contact1.grid(**fn_grid(3, 0), pady=(10, 0))

        self.txt_customer_contact2 = CTkEntry(frm_details, placeholder_text='Contact 2', **style._txt_customer_form)
        self.txt_customer_contact2.grid(**fn_grid(3, 1), pady=(10, 0))

        # Add Items Button
        icon_add = CTkImage(dark_image=Image.open('AppData/icons/png/add.png'), size=(25, 25))
        btn_add_items = CTkButton(frm_details, text='Add Items', image=icon_add, command=self.win_transfer_to_billing, **style._btn_add_items)
        btn_add_items.grid(**fn_grid(4, 0), columnspan=2, pady=(20, 0))

        # Amount Details
        frm_amount = CTkFrame(self._root, width=int(WINDOW_WIDTH/2), fg_color='transparent')
        frm_amount.place(x=5, y=260)
        lbl_frm_amount_width = CTkLabel(frm_amount, text='', width=int(WINDOW_WIDTH/2), height=10).grid(**fn_grid(0, 0), columnspan=5)

        # Row 1
        lbl_total_amount = CTkLabel(frm_amount, text='Total Amount', width=int(WINDOW_WIDTH/9))
        lbl_total_amount.grid(**fn_grid(1, 0), sticky=W, pady=(0, 10))

        self.txt_total_amount = CTkEntry(frm_amount, placeholder_text='0.0', width=int(WINDOW_WIDTH/4.5))
        self.txt_total_amount.grid(**fn_grid(1, 1), columnspan=2, sticky=W, pady=(0, 10))

        self.opt_pay_type = CTkOptionMenu(frm_amount, values=['Cash', 'Cheque', 'Debit Card', 'Credit Card', 'Other'], width=int(WINDOW_WIDTH/7.8))
        self.opt_pay_type.grid(**fn_grid(1, 3), sticky=W, pady=(0, 10))

        # Row 2
        lbl_discount = CTkLabel(frm_amount, text='Discount', width=int(WINDOW_WIDTH/9))
        lbl_discount.grid(**fn_grid(2, 0), sticky=W, pady=(0, 10))

        self.txt_discount = CTkEntry(frm_amount, placeholder_text='0.0', width=int(WINDOW_WIDTH/4.5))
        self.txt_discount.grid(**fn_grid(2, 1), columnspan=2, sticky=W, pady=(0, 10))

        self.btn_discount_type = CTkButton(frm_amount, text='%', command=self.fn_change_discount_type, **style._btn_discount_type)
        self.btn_discount_type.grid(**fn_grid(2, 3), sticky=W, padx=5, pady=(0, 10))

        # Row 3
        lbl_paid_amount = CTkLabel(frm_amount, text='Paid', width=int(WINDOW_WIDTH/9))
        lbl_paid_amount.grid(**fn_grid(3, 0), sticky=W, pady=(0, 10))

        self.txt_total_amount = CTkEntry(frm_amount, placeholder_text='0.0', width=int(WINDOW_WIDTH/4.5))
        self.txt_total_amount.grid(**fn_grid(3, 1), sticky=W, pady=(0, 10))

        lbl_change_amount = CTkLabel(frm_amount, text='Change 0.0')
        lbl_change_amount.grid(**fn_grid(3, 2), columnspan=3, sticky=W, padx=2, pady=(0, 10))

        # Bill Actions
        frm_bill_actions = CTkFrame(self._root, fg_color='transparent')
        frm_bill_actions.place(x=5, y=410)

        btn_bill_generate = CTkButton(frm_bill_actions, text='Generate', **style._btn_bill, **style._btn_bill_generate)
        btn_bill_generate.grid(**fn_grid(0, 0), padx=(2, 5))

        btn_bill_save = CTkButton(frm_bill_actions, text='Save', **style._btn_bill, **style._btn_bill_save)
        btn_bill_save.grid(**fn_grid(0, 1), padx=5)

        btn_bill_print = CTkButton(frm_bill_actions, text='Print', **style._btn_bill, **style._btn_bill_print)
        btn_bill_print.grid(**fn_grid(0, 2), padx=5)

        btn_bill_clear = CTkButton(frm_bill_actions, text='Clear', **style._btn_bill, **style._btn_bill_clear)
        btn_bill_clear.grid(**fn_grid(0, 3), padx=5)

        # ==== Bill ====
        frm_bill = CTkFrame(self._root, height=WINDOW_HEIGHT-60, width=int(WINDOW_WIDTH/2)-5)
        frm_bill.place(x=int(WINDOW_WIDTH/2), y=55)

        txt_bill = CTkTextbox(frm_bill, height=WINDOW_HEIGHT-60, width=int(WINDOW_WIDTH/2)-5, state=DISABLED, **style._txt_bill)
        txt_bill.pack()

    
    def fn_change_discount_type(self):
        if self.btn_discount_type.cget('text') == 'INR': 
            self.btn_discount_type.configure(text='%')
        else:
            self.btn_discount_type.configure(text='INR')
        
        self.btn_discount_type.configure(width=40)

    def win_transfer_to_billing(self):
        data_to_billing = []



if __name__ == "__main__":
    root = CTk()
    obj = QuickBillPage(root)
    root.mainloop()