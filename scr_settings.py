'''
Light Mode, ( Side )
Business Name, Contact1,2, Address, Logo, Email, Tax Info, Regestration Details ( Main )
Date Format - 12 24 hour || Currency ( Side )
Business Links (Google Maps) as QR Code
Backup DB Location, Time, Often?
Specify Business Hours
Button to start Guide Mode

MastHead, Contact Support
'''
'''
https://pypi.org/project/tkTimePicker/
'''
import pyautogui as pg
from customtkinter import *
from tkinter.ttk import Separator
from PIL import Image

from style_global import COLOR, fn_grid
from scr_set_change_time import ChangeTimePage

SCREEN_WIDTH = pg.size()[0]
SCREEN_HEIGHT = pg.size()[1]

WINDOW_WIDTH = int(SCREEN_WIDTH * 0.4)
WINDOW_HEIGHT = int(SCREEN_HEIGHT * 0.62)
WINDOW_X = int(SCREEN_WIDTH * 0.25)
WINDOW_Y = int(SCREEN_HEIGHT * 0.08)

class StyleSettingsPage:
    def __init__(self):
        self._lbl_title = {
            'text_color' : COLOR[4], 
            'fg_color' : COLOR[1], 
            'font' : ('Arial', 30, 'bold'),
            'corner_radius': 1,
            'width' : WINDOW_WIDTH,
            'height' : 60,
        }
        self._btn_side = {
            'text_color' : COLOR[4],
            'fg_color' : 'grey14',
            'bg_color' : 'transparent',
            'corner_radius' : 100,
            'height' : 50,
            'width' : int(WINDOW_WIDTH/4),
            'font' : ('Calibra', 18, 'bold'),
            'hover_color' : 'grey',
        }
        self._btn_side_active = {
            'text_color' : 'black',
            'fg_color' : COLOR[4],
            'bg_color' : 'transparent',
            'corner_radius' : 100,
            'height' : 50,
            'width' : int(WINDOW_WIDTH/5),
            'font' : ('Calibra', 18, 'bold'),
            'hover_color' : 'grey'
        }
        self._lbl_left = {
            'font' : ('Calibra', 18, 'bold'),
        }
        self._lbl_left_2 = {
            'font' : ('Calibra', 16),
        }
        self._btn_shift1 = {
            'text_color' : '#242424',
            'fg_color' : 'yellow',
            'hover_color' : '#7d7b1b',
        }
        self._btn_shift2 = {
            'fg_color' : COLOR[1],
        }
style = StyleSettingsPage()

class SettingsPage:
    def __init__(self, root:CTk):
        self._root = root
        self._root.title('Settings')
        self._root.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{WINDOW_X}+{WINDOW_Y}')

        # Vars
        self.days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        self.currencies = ['₹ INR', '$ USD', '€ EUR', '¥ JPY', '£ GBP', 'A$ AUD', 'C$ CAD', 'Fr. CHF', '¥ CNY', 'kr SEK', 'NZ$ NZD', '₩ KRW', 'S$ SGD', 'kr NOK', 'Mex$ MXN', '₽ RUB', 'R ZAR', 'R$ BRL', '₺ TRY', 'HK$ HKD']
        self.dict_tab_var = {}
        self.dict_tab_btn = {}


        # ====== Widgets ======
        lbl_title = CTkLabel(self._root, text='Settings', **style._lbl_title)
        lbl_title.place(x=0, y=0)

        # ======== Side FRAME ========
        self.frm_side = CTkFrame(self._root, fg_color='transparent')
        self.frm_side.place(x=-30, y=90)

        self.tab_draw_btns(first_time=True)

        # ======== Main FRAME =========
        self.frm_main = CTkScrollableFrame(self._root, fg_color='transparent', width=int(3*WINDOW_WIDTH/4), height=WINDOW_HEIGHT-80)
        self.frm_main.place(x=int(WINDOW_WIDTH/3), y=90)

        # ===== Business Details =====
        self.fn_toggle_tab(self.tab_business_details, 'business_details')


        # Finance Details
        # self.fn_toggle_tab(self.tab_financials, 'financials')


        # ==== Miscellaneous ====
        # self.fn_toggle_tab(self.tab_miscellaneous, 'miscellaneous')
        

# =======================================================================

    def tab_draw_btns(self, first_time=False, activate_key:str=''):
        for widget in self.frm_side.winfo_children():
            widget.destroy()

        if activate_key == 'business_details': self.dict_tab_btn['business_details'] = CTkButton(self.frm_side, text='Business Details', command=lambda: self.fn_toggle_tab(self.tab_business_details, 'business_details'), **style._btn_side_active)
        else: self.dict_tab_btn['business_details'] = CTkButton(self.frm_side, text='Business Details', command=lambda: self.fn_toggle_tab(self.tab_business_details, 'business_details'), **style._btn_side)

        if activate_key == 'financials': self.dict_tab_btn['financials'] = CTkButton(self.frm_side, text='Financials', command=lambda: self.fn_toggle_tab(self.tab_financials, 'financials'), **style._btn_side_active)
        else: self.dict_tab_btn['financials'] = CTkButton(self.frm_side, text='Financials', command=lambda: self.fn_toggle_tab(self.tab_financials, 'financials'), **style._btn_side)

        if activate_key == 'miscellaneous': self.dict_tab_btn['miscellaneous'] = CTkButton(self.frm_side, text='Miscellaneous', command=lambda: self.fn_toggle_tab(self.tab_miscellaneous, 'miscellaneous'), **style._btn_side_active)
        else: self.dict_tab_btn['miscellaneous'] = CTkButton(self.frm_side, text='Miscellaneous', command=lambda: self.fn_toggle_tab(self.tab_miscellaneous, 'miscellaneous'), **style._btn_side)

        # init vars
        if first_time:
            self.dict_tab_var['business_details'] = False
            self.dict_tab_var['financials'] = False
            self.dict_tab_var['miscellaneous'] = False
        
        # Pack Btns
        self.dict_tab_btn['business_details'].pack(anchor=W, pady=10, ipadx=50)
        self.dict_tab_btn['financials'].pack(anchor=W, pady=10, ipadx=50)
        self.dict_tab_btn['miscellaneous'].pack(anchor=W, pady=10, ipadx=50)


    def fn_toggle_tab(self, tab_fn, tab_key: str):
        if not self.dict_tab_var[tab_key]: # Not Active
            self.dict_tab_var[tab_key] = True

            # Set Others False
            for key, val in self.dict_tab_var.items():
                if self.dict_tab_var[tab_key] != val: self.dict_tab_var[key] = False

            for widget in self.frm_main.winfo_children():
                widget.destroy()

            tab_fn() # Draw on Main frame
            
            # Style Btn
            self.tab_draw_btns(activate_key=tab_key)
        else: # Active
            self.dict_tab_var[tab_key] = False



    def tab_business_details(self):
        for widget in self.frm_main.winfo_children():
            widget.destroy()

        frm_business_details = CTkFrame(self.frm_main, fg_color='transparent', width=int(WINDOW_WIDTH/2))
        frm_business_details.pack(anchor=W)

        # lbl_bd_title = CTkLabel(frm_business_details, text='Business Details', **style._lbl_left)
        # lbl_bd_title.pack(anchor=W, padx=10, pady=(10, 5))

        # Row 1
        txt_bd_name = CTkEntry(frm_business_details, placeholder_text='Business Name*', width=int(WINDOW_WIDTH/2))
        txt_bd_name.pack(fill=X, padx=(15, 0), pady=5)

        # Row 2
        frm_bd_contact = CTkFrame(frm_business_details, fg_color='transparent')
        frm_bd_contact.pack(fill=X)

        txt_bd_contact1 = CTkEntry(frm_bd_contact, placeholder_text='Phone Number 1*', width=int(WINDOW_WIDTH/6)+5)
        txt_bd_contact1.grid(**fn_grid(2, 0), columnspan=2, sticky=W, padx=(15, 5), pady=5)

        txt_bd_contact2 = CTkEntry(frm_bd_contact, placeholder_text='Phone Number 2', width=int(WINDOW_WIDTH/6)+5)
        txt_bd_contact2.grid(**fn_grid(2, 2), columnspan=2, sticky=W, padx=5, pady=5)

        txt_bd_contact3 = CTkEntry(frm_bd_contact, placeholder_text='Landline Number', width=int(WINDOW_WIDTH/6)+5)
        txt_bd_contact3.grid(**fn_grid(2, 4), columnspan=2, sticky=W, padx=5, pady=5)

        txt_bd_email1 = CTkEntry(frm_bd_contact, placeholder_text='Email 1', width=int(WINDOW_WIDTH/4)+10)
        txt_bd_email1.grid(**fn_grid(3, 0), columnspan=3, sticky=W, padx=(15, 5), pady=5)

        txt_bd_email2 = CTkEntry(frm_bd_contact, placeholder_text='Email 2', width=int(WINDOW_WIDTH/4)+10)
        txt_bd_email2.grid(**fn_grid(3, 3), columnspan=3, sticky=W, padx=5, pady=5)
        

        # Row 3
        lbl_bd_address = CTkLabel(frm_business_details, text='Address', **style._lbl_left_2)
        lbl_bd_address.pack(anchor=W, padx=10, pady=(10, 0))

        txt_bd_address1 = CTkEntry(frm_business_details, placeholder_text='Line 1*', width=int(WINDOW_WIDTH/2))
        txt_bd_address1.pack(fill=X, padx=(15, 0), pady=5)

        txt_bd_address1 = CTkEntry(frm_business_details, placeholder_text='Line 2', width=int(WINDOW_WIDTH/2))
        txt_bd_address1.pack(fill=X, padx=(15, 0), pady=5)

        txt_bd_address1 = CTkEntry(frm_business_details, placeholder_text='Line 3', width=int(WINDOW_WIDTH/2))
        txt_bd_address1.pack(fill=X, padx=(15, 0), pady=5)

        # Row 4
        lbl_bd_business_title = CTkLabel(frm_business_details, text='Business Hours', **style._lbl_left_2)
        lbl_bd_business_title.pack(anchor=W, padx=10, pady=(10, 0))

        self.frm_bd_business_hours = CTkFrame(frm_business_details, fg_color='transparent')
        self.frm_bd_business_hours.pack(anchor=W, padx=20, pady=(10, 0))

        lbl_bd_shift1 = CTkLabel(self.frm_bd_business_hours, text='Shift 1')
        lbl_bd_shift1.grid(**fn_grid(1, 1), columnspan=3, sticky=NSEW)

        self.var_shift2_active = False
        self.btn_bd_shift2 = CTkButton(self.frm_bd_business_hours, text='Shift 2', command=self.fn_toggle_shift2, width=80, fg_color='green', hover_color='darkgreen')
        self.btn_bd_shift2.grid(**fn_grid(1, 4), columnspan=3, padx=20)

        lbl_bd_from1 = CTkLabel(self.frm_bd_business_hours, text='From', width=1).grid(**fn_grid(2, 1), padx=20)
        lbl_bd_to1 = CTkLabel(self.frm_bd_business_hours, text='To').grid(**fn_grid(2, 3), padx=20)

        self.lbl_bd_from2 = CTkLabel(self.frm_bd_business_hours, text='From')
        self.lbl_bd_to2 = CTkLabel(self.frm_bd_business_hours, text='To') # .grid(**fn_grid(1, 4), padx=20)

        # CTkLabel(frm_bd_business_hours, text='Sunday').grid(**fn_grid(2, 0))
        # CTkLabel(frm_bd_business_hours, text='Monday').grid(**fn_grid(3, 0))
        # CTkLabel(frm_bd_business_hours, text='Tuesday').grid(**fn_grid(4, 0))
        # CTkLabel(frm_bd_business_hours, text='Wednesday').grid(**fn_grid(5, 0))
        # CTkLabel(frm_bd_business_hours, text='Thursday').grid(**fn_grid(6, 0))
        # CTkLabel(frm_bd_business_hours, text='Friday').grid(**fn_grid(7, 0))
        # CTkLabel(frm_bd_business_hours, text='Saturday').grid(**fn_grid(8, 0))

        # Loop To print all days as label
        for i in range(3, 10):
            CTkLabel(self.frm_bd_business_hours, text=self.days[i-3]).grid(**fn_grid(i, 0))

        self.dict_shift2_btn : dict[str, CTkButton]= {}

        # width=1 to set it to min and responsive
        btn_bd_bh_0_f1 = CTkButton(self.frm_bd_business_hours, text='09:00 AM', width=1, **style._btn_shift1).grid(**fn_grid(3, 1), padx=2, pady=2)
        btn_bd_bh_0_t1 = CTkButton(self.frm_bd_business_hours, text='05:00 PM', width=1, **style._btn_shift1).grid(**fn_grid(3, 3), padx=2, pady=2)
        self.dict_shift2_btn['0_f2'] = CTkButton(self.frm_bd_business_hours, text='09:00 AM', width=1, **style._btn_shift2)
        self.dict_shift2_btn['0_t2'] = CTkButton(self.frm_bd_business_hours, text='05:00 PM', width=1, **style._btn_shift2)

        btn_bd_bh_1_f1 = CTkButton(self.frm_bd_business_hours, text='09:00 AM', width=1, **style._btn_shift1).grid(**fn_grid(4, 1), padx=2, pady=2)
        btn_bd_bh_1_t1 = CTkButton(self.frm_bd_business_hours, text='05:00 PM', width=1, **style._btn_shift1).grid(**fn_grid(4, 3), padx=2, pady=2)
        self.dict_shift2_btn['1_f2'] = CTkButton(self.frm_bd_business_hours, text='09:00 AM', width=1, **style._btn_shift2)
        self.dict_shift2_btn['1_t2'] = CTkButton(self.frm_bd_business_hours, text='05:00 PM', width=1, **style._btn_shift2)
        
        btn_bd_bh_2_f1 = CTkButton(self.frm_bd_business_hours, text='09:00 AM', width=1, **style._btn_shift1).grid(**fn_grid(5, 1), padx=2, pady=2)
        btn_bd_bh_4_t1 = CTkButton(self.frm_bd_business_hours, text='05:00 PM', width=1, **style._btn_shift1).grid(**fn_grid(5, 3), padx=2, pady=2)
        self.dict_shift2_btn['2_f2'] = CTkButton(self.frm_bd_business_hours, text='09:00 AM', width=1, **style._btn_shift2)
        self.dict_shift2_btn['2_t2'] = CTkButton(self.frm_bd_business_hours, text='05:00 PM', width=1, **style._btn_shift2)
        
        btn_bd_bh_3_f1 = CTkButton(self.frm_bd_business_hours, text='09:00 AM', width=1, **style._btn_shift1).grid(**fn_grid(6, 1), padx=2, pady=2)
        btn_bd_bh_3_t1 = CTkButton(self.frm_bd_business_hours, text='05:00 PM', width=1, **style._btn_shift1).grid(**fn_grid(6, 3), padx=2, pady=2)
        self.dict_shift2_btn['3_f2'] = CTkButton(self.frm_bd_business_hours, text='09:00 AM', width=1, **style._btn_shift2)
        self.dict_shift2_btn['3_t2'] = CTkButton(self.frm_bd_business_hours, text='05:00 PM', width=1, **style._btn_shift2)
        
        btn_bd_bh_4_f1 = CTkButton(self.frm_bd_business_hours, text='09:00 AM', width=1, **style._btn_shift1).grid(**fn_grid(7, 1), padx=2, pady=2)
        btn_bd_bh_4_t1 = CTkButton(self.frm_bd_business_hours, text='05:00 PM', width=1, **style._btn_shift1).grid(**fn_grid(7, 3), padx=2, pady=2)
        self.dict_shift2_btn['4_f2'] = CTkButton(self.frm_bd_business_hours, text='09:00 AM', width=1, **style._btn_shift2)
        self.dict_shift2_btn['4_t2'] = CTkButton(self.frm_bd_business_hours, text='05:00 PM', width=1, **style._btn_shift2)
        
        btn_bd_bh_5_f1 = CTkButton(self.frm_bd_business_hours, text='09:00 AM', width=1, **style._btn_shift1).grid(**fn_grid(8, 1), padx=2, pady=2)
        btn_bd_bh_5_t1 = CTkButton(self.frm_bd_business_hours, text='05:00 PM', width=1, **style._btn_shift1).grid(**fn_grid(8, 3), padx=2, pady=2)
        self.dict_shift2_btn['5_f2'] = CTkButton(self.frm_bd_business_hours, text='09:00 AM', width=1, **style._btn_shift2)
        self.dict_shift2_btn['5_t2'] = CTkButton(self.frm_bd_business_hours, text='05:00 PM', width=1, **style._btn_shift2)
        
        btn_bd_bh_6_f1 = CTkButton(self.frm_bd_business_hours, text='09:00 AM', width=1, **style._btn_shift1).grid(**fn_grid(9, 1), padx=2, pady=2)
        btn_bd_bh_6_t1 = CTkButton(self.frm_bd_business_hours, text='05:00 PM', width=1, **style._btn_shift1).grid(**fn_grid(9, 3), padx=2, pady=2)
        self.dict_shift2_btn['6_f2'] = CTkButton(self.frm_bd_business_hours, text='09:00 AM', width=1, **style._btn_shift2)
        self.dict_shift2_btn['6_t2'] = CTkButton(self.frm_bd_business_hours, text='05:00 PM', width=1, **style._btn_shift2)

        # Loop to print (-)
        for i in range(3, 10):
            CTkLabel(self.frm_bd_business_hours, text='-', width=1, font=('Calibra', 20, 'bold')).grid(**fn_grid(i, 2))        

    def tab_financials(self):
        for widget in self.frm_main.winfo_children():
            widget.destroy()
        frm_finance_details = CTkFrame(self.frm_main, fg_color='transparent', width=int(WINDOW_WIDTH/2))
        frm_finance_details.pack(anchor=W)

        # lbl_fd_title = CTkLabel(frm_finance_details, text='Finance Details', **style._lbl_left)
        # lbl_fd_title.pack(anchor=W, padx=10, pady=(10, 5))

        txt_gstin = CTkEntry(frm_finance_details, placeholder_text='GST Identification Number', width=int(WINDOW_WIDTH/2))
        txt_gstin.pack(fill=X, padx=(15, 0), pady=5)

        lbl_reg_details = CTkLabel(frm_finance_details, text='Registration Details')
        lbl_reg_details.pack(anchor=W, padx=(15, 0), pady=5)
        
        txt_reg_details = CTkTextbox(frm_finance_details, width=int(WINDOW_WIDTH/2))
        txt_reg_details.pack(fill=X, padx=(15, 0), pady=5)

        fil_reg_details_1 = ...
        fil_reg_details_2 = ...
        fil_reg_details_3 = ...
        '''doc_regdoc'''
    
    def tab_miscellaneous(self):
        for widget in self.frm_main.winfo_children():
            widget.destroy()

        frm_right = CTkFrame(self.frm_main, fg_color='transparent', width=int(WINDOW_WIDTH/2))
        frm_right.pack(anchor=W)

        # lbl_miscellaneous = CTkLabel(frm_right, text='Miscellaneous', font=('Calibra', 20, 'bold'))
        # lbl_miscellaneous.grid(**fn_grid(0, 0), columnspan=2, sticky=NSEW, pady=10)

        lbl_light_dark_mode = CTkLabel(frm_right, text='Light Mode').grid(**fn_grid(1, 0), sticky=E, padx=5)
        swi_light_dark_mode = CTkSwitch(frm_right, onvalue='dark', offvalue='light', text='Dark Mode', width=int(WINDOW_WIDTH/3))
        swi_light_dark_mode.grid(**fn_grid(1, 1), columnspan=2, sticky=NSEW)
        swi_light_dark_mode.select()

        lbl_hour_format = CTkLabel(frm_right, text='12-Hour Format').grid(**fn_grid(2, 0), sticky=E, padx=5)
        swi_hour_format = CTkSwitch(frm_right, onvalue='24', offvalue='12', text='24-Hour Format', width=int(WINDOW_WIDTH/3))
        swi_hour_format.grid(**fn_grid(2, 1), columnspan=2, sticky=NSEW)
        swi_hour_format.select()

        lbl_currency = CTkLabel(frm_right, text='Currency')
        lbl_currency.grid(**fn_grid(3, 0), pady=10)
        opt_currency = CTkOptionMenu(frm_right, values=self.currencies)
        opt_currency.grid(**fn_grid(3, 1), pady=10)

        lbl_backup_freq = CTkLabel(frm_right, text='Backup Frequency').grid(**fn_grid(4, 0))
        opt_backup_freq = CTkOptionMenu(frm_right, values=['Daily', 'Weekly', 'Fortnightly', 'Monthly', 'Quarterly'])

    def win_change_time(self, time_data):
        new_win = CTkToplevel(self._root)
        new_obj = ChangeTimePage(new_win)
        new_win.transient(self._root)
    
    def fn_toggle_shift2(self):
        if not self.var_shift2_active:
            self.btn_bd_shift2.configure(fg_color='red', hover_color='darkred')

            self.lbl_bd_from2.grid(**fn_grid(2, 4), padx=20)
            self.lbl_bd_to2.grid(**fn_grid(2, 6), padx=20)

            # Loop to print (-)
            for i in range(3, 10):
                CTkLabel(self.frm_bd_business_hours, text='-', width=1, font=('Calibra', 20, 'bold')).grid(**fn_grid(i, 5))
                
            # Buttons for shift 2
            for i in range(7):
                self.dict_shift2_btn[f'{i}_f2'].grid(**fn_grid(i+3, 4), padx=2, pady=2)
                self.dict_shift2_btn[f'{i}_t2'].grid(**fn_grid(i+3, 6), padx=2, pady=2)
            
            self.var_shift2_active = True
        else:
            self.btn_bd_shift2.configure(fg_color='green', hover_color='darkgreen')
            clearing_row = list(range(3, 10))
            clearing_column = [4, 5, 6]
            self.lbl_bd_from2.grid_forget()
            self.lbl_bd_to2.grid_forget()

            # To forget all elements of Shift 2
            for child in self.frm_bd_business_hours.grid_slaves():
                if int(child.grid_info()['row']) in clearing_row and int(child.grid_info()['column']) in clearing_column:
                    child.grid_forget()
            
            self.var_shift2_active = False

        

if __name__ == "__main__":
    root = CTk()
    obj = SettingsPage(root)
    root.mainloop()