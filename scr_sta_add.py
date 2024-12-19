import pyautogui as pg
from customtkinter import *
from PIL import Image

from style_global import COLOR

SCREEN_WIDTH = pg.size()[0]
SCREEN_HEIGHT = pg.size()[1]

WINDOW_WIDTH = int(SCREEN_WIDTH * 0.35)
WINDOW_HEIGHT = int(SCREEN_HEIGHT * 0.55)
WINDOW_X = int(SCREEN_WIDTH * 0.27)
WINDOW_Y = int(SCREEN_HEIGHT * 0.1)

class StyleStakeHoldersPage_Add:
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

style = StyleStakeHoldersPage_Add()


class StakeHoldersPage_Add:
    def __init__(self, root:CTk):
        self._root = root
        self._root.title('Add Stakeholders')
        self._root.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{WINDOW_X}+{WINDOW_Y}')

        # === Vars ====
        self.var_first_name = StringVar()

        # === Widgets ===

        # === title ===
        lbl_title = CTkLabel(self._root, text='Stakeholder', **style._lbl_title)
        lbl_title.place(x=0, y=0)

        # === profile image ===
        frm_profile_img = CTkFrame(self._root)
        frm_profile_img.place(x=20, y=70)

        jpg_default_image = CTkImage(dark_image=Image.open('AppData/icons/jpg/stakeholder_default.jpg'), size=(300, 300))
        lbl_profile_img = CTkLabel(frm_profile_img, image=jpg_default_image, text='')
        lbl_profile_img.pack(fill=BOTH)

        # === stakeholders details ===
        frm_details_1 = CTkFrame(self._root, width=int(WINDOW_WIDTH/2), height=int(WINDOW_HEIGHT/2), fg_color='transparent')
        frm_details_1.place(x=int(WINDOW_WIDTH/2), y=70)

        # Row 1
        lbl_name = CTkLabel(frm_details_1, text='Name')
        lbl_name.grid(row=0, column=0, sticky=W, padx=8)

        txt_first_name = CTkEntry(frm_details_1, placeholder_text='First Name', **style._txt_form)
        txt_first_name.grid(row=1, column=0, padx=5, pady=(0, 10))

        txt_last_name = CTkEntry(frm_details_1, placeholder_text='Last Name', **style._txt_form)
        txt_last_name.grid(row=1, column=1, padx=5, pady=(0, 10))

        # CTkLabel(frm_details_1, text='', width=5).grid(row=2, column=0, columnspan=2) # gap

        # Row 2
        lbl_contact_no = CTkLabel(frm_details_1, text='Contact Number')
        lbl_contact_no.grid(row=3, column=0, sticky=W, padx=8)

        txt_contact_1 = CTkEntry(frm_details_1, placeholder_text='Contact 1', **style._txt_form)
        txt_contact_1.grid(row=4, column=0, padx=5, pady=(0, 10))

        txt_contact_2 = CTkEntry(frm_details_1, placeholder_text='Contact 2', **style._txt_form)
        txt_contact_2.grid(row=4, column=1, padx=5, pady=(0, 10))

        # CTkLabel(frm_details_1, text='', width=5).grid(row=5, column=0, columnspan=2) # gap
        
        # Row 3
        frm_details_2 = CTkFrame(self._root, width=int(WINDOW_WIDTH/2), height=int(WINDOW_HEIGHT/2), fg_color='transparent')
        frm_details_2.place(x=int(WINDOW_WIDTH/2), y=200)

        lbl_company = CTkLabel(frm_details_2, text='Company')
        lbl_company.grid(row=0, column=0, sticky=W, padx=8)

        txt_company_title = CTkEntry(frm_details_2, placeholder_text='Title', width=90, **style._txt_form)
        txt_company_title.grid(row=1, column=0, padx=5, pady=(0, 10))

        txt_company_name = CTkEntry(frm_details_2, placeholder_text='Company Name', width=190, **style._txt_form)
        txt_company_name.grid(row=1, column=1, padx=5, pady=(0, 10))

        # Row 4
        lbl_balance = CTkLabel(frm_details_2, text='Balance')
        lbl_balance.grid(row=2, column=0, sticky=W, padx=8)

        opt_balance = CTkOptionMenu(frm_details_2, width=90, values=['Give', 'Receive'], **style._opt_balance)
        opt_balance.grid(row=3, column=0)

        txt_balance = CTkEntry(frm_details_2, placeholder_text='Amount', width=190, **style._txt_form)
        txt_balance.grid(row=3, column=1)

        # Row 5
        opt_type = CTkOptionMenu(frm_details_2, width=150, values=['Client', 'Supplier'], **style._opt_balance)
        opt_type.grid(row=4, column=0, columnspan=2, sticky=N, pady=(20, 0))

        # Row 6
        frm_details_3 = CTkFrame(self._root, width=WINDOW_WIDTH-30, height=int(WINDOW_HEIGHT/3), fg_color='transparent')
        frm_details_3.place(x=15, y=390)

        lbl_address = CTkLabel(frm_details_3, text='Address')
        lbl_address.grid(row=0, column=0, sticky=W, padx=8)

        txt_address = CTkEntry(frm_details_3, placeholder_text='Address', width=WINDOW_WIDTH-30, **style._txt_form)
        txt_address.grid(row=1, column=0, pady=(0, 10))

        # Row 7
        lbl_email = CTkLabel(frm_details_3, text='Email')
        lbl_email.grid(row=2, column=0, sticky=W, padx=8)

        txt_email = CTkEntry(frm_details_3, placeholder_text='Email', width=WINDOW_WIDTH-30, **style._txt_form)
        txt_email.grid(row=3, column=0, pady=(0, 10))

        # Row 8
        frm_details_4 = CTkFrame(self._root, width=int(WINDOW_WIDTH/2), height=int(WINDOW_HEIGHT/9), fg_color='transparent')
        frm_details_4.place(x=int(WINDOW_WIDTH/4), y=530)

        btn_save = CTkButton(frm_details_4, text='Save', command=self.fn_save, **style._btn_save)
        btn_save.grid(row=0, column=0, padx=10)

        btn_clear = CTkButton(frm_details_4, text='Clear', command=self.fn_clear, **style._btn_clear)
        btn_clear.grid(row=0, column=1, padx=10)
        

    def fn_save(self): ...
    def fn_clear(self): ...


if __name__ == "__main__":
    root = CTk()
    obj = StakeHoldersPage_Add(root)
    root.mainloop()