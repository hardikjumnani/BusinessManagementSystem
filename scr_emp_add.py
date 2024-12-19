import pyautogui as pg
from customtkinter import *
from PIL import Image

from style_global import COLOR

SCREEN_WIDTH = pg.size()[0]
SCREEN_HEIGHT = pg.size()[1]

WINDOW_WIDTH = int(SCREEN_WIDTH * 0.32)
WINDOW_HEIGHT = int(SCREEN_HEIGHT * 0.53)
WINDOW_X = int(SCREEN_WIDTH * 0.29)
WINDOW_Y = int(SCREEN_HEIGHT * 0.1)

class StyleEmployeesPage_Add:
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

style = StyleEmployeesPage_Add()


class EmployeesPage_Add:
    def __init__(self, root:CTk):
        self._root = root
        self._root.title('Add Employee')
        self._root.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{WINDOW_X}+{WINDOW_Y}')

        # === Vars ====
        self.var_first_name = StringVar()

        # === Widgets ===

        # === title ===
        lbl_title = CTkLabel(self._root, text='New Employee', **style._lbl_title)
        lbl_title.place(x=0, y=0)

        # === profile image ===
        frm_profile_img = CTkFrame(self._root)
        frm_profile_img.place(x=int(WINDOW_WIDTH/1.85), y=70)

        jpg_default_image = CTkImage(dark_image=Image.open('AppData/icons/jpg/stakeholder_default.jpg'), size=(260, 260))
        lbl_profile_img = CTkLabel(frm_profile_img, image=jpg_default_image, text='')
        lbl_profile_img.pack(fill=BOTH)

        # === stakeholders details ===
        frm_details_1 = CTkFrame(self._root, width=int(WINDOW_WIDTH/2), height=int(WINDOW_HEIGHT/2), fg_color='transparent')
        frm_details_1.place(x=20, y=70)

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
        lbl_company = CTkLabel(frm_details_1, text='Company')
        lbl_company.grid(row=5, column=0, sticky=W, padx=8)

        txt_designation = CTkEntry(frm_details_1, placeholder_text='Designation', **style._txt_form)
        txt_designation.grid(row=6, column=0, padx=5, pady=(0, 10))

        txt_department = CTkEntry(frm_details_1, placeholder_text='Department', **style._txt_form)
        txt_department.grid(row=6, column=1, padx=5, pady=(0, 10))

        # Row 4
        lbl_id = CTkLabel(frm_details_1, text='Employee ID')
        lbl_id.grid(row=7, column=0, sticky=W, padx=8)

        txt_id = CTkEntry(frm_details_1, placeholder_text='ABC123', **style._txt_form)
        txt_id.grid(row=8, column=0)

        lbl_date_of_hire = CTkLabel(frm_details_1, text='Date Of Hire')
        lbl_date_of_hire.grid(row=7, column=1, sticky=W, padx=8)

        txt_date_of_hire = CTkEntry(frm_details_1, placeholder_text='DD-MM-YYYY', **style._txt_form)
        txt_date_of_hire.grid(row=8, column=1)

        # Row 6
        frm_details_3 = CTkFrame(self._root, width=WINDOW_WIDTH-30, height=int(WINDOW_HEIGHT/3), fg_color='transparent')
        frm_details_3.place(x=15, y=340)

        lbl_address = CTkLabel(frm_details_3, text='Address')
        lbl_address.grid(row=0, column=0, sticky=W, padx=8)

        txt_address = CTkTextbox(frm_details_3, width=WINDOW_WIDTH-30, height=70, **style._txt_form)
        txt_address.grid(row=1, column=0, pady=(0, 5))

        # Row 7
        lbl_email = CTkLabel(frm_details_3, text='Email')
        lbl_email.grid(row=2, column=0, sticky=W, padx=8)

        txt_email = CTkEntry(frm_details_3, placeholder_text='Email', width=WINDOW_WIDTH-30, **style._txt_form)
        txt_email.grid(row=3, column=0, pady=(0, 10))

        # Row 8
        frm_details_4 = CTkFrame(self._root, width=int(WINDOW_WIDTH/2), height=int(WINDOW_HEIGHT/9), fg_color='transparent')
        frm_details_4.place(x=int(WINDOW_WIDTH/4), y=520)

        btn_save = CTkButton(frm_details_4, text='Save', command=self.fn_save, **style._btn_save)
        btn_save.grid(row=0, column=0, padx=10)

        btn_clear = CTkButton(frm_details_4, text='Clear', command=self.fn_clear, **style._btn_clear)
        btn_clear.grid(row=0, column=1, padx=10)
        

    def fn_save(self): ...
    def fn_clear(self): ...


if __name__ == "__main__":
    root = CTk()
    obj = EmployeesPage_Add(root)
    root.mainloop()