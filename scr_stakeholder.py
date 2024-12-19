import pyautogui as pg
from PIL import Image
from customtkinter import *
from tkinter import Frame
from tkinter.ttk import Treeview, Scrollbar, Style

from style_global import COLOR
from scr_sta_add import StakeHoldersPage_Add

SCREEN_WIDTH = pg.size()[0]
SCREEN_HEIGHT = pg.size()[1]

WINDOW_WIDTH = int(SCREEN_WIDTH * 0.6)
WINDOW_HEIGHT = int(SCREEN_HEIGHT * 0.55)
WINDOW_X = int(SCREEN_WIDTH * 0.1)
WINDOW_Y = int(SCREEN_HEIGHT * 0.1)

class StyleStakeholder:
    def __init__(self):
        # self.ss_lbl_title = {
        #     'text_color' : COLOR[4], 
        #     'fg_color' : COLOR[1], 
        #     'font' : ('Arial', 30, 'bold'),
        #     'corner_radius': 1,
        #     'width' : WINDOW_WIDTH-20,
        #     'height' : 60,
        # }
        self.ss_lbl_total_stakeholders = {
            'font' : ('Arial', 20),
            'width' : 120,
            'height' : 60,
        }
        self.ss_frm_search = {
            'fg_color' : '#4A4A4A',
            'width' : 600,
            'height' : 60
        }
        self.ss_txt_search = {
            'font' : ('Arial', 18),
            'width' : 460,
            'height' : 40,
        }
        self.ss_btn_search = {
            'width' : 50,
            'fg_color' : COLOR[1],
            'hover_color' : 'blue',
        }
        self.ss_drp_sort = {
            'width' : 150,
            'height' : 40,
            'font' : ('Calibra', 18),
            'fg_color' : COLOR[1],
            'button_color' : COLOR[1],
            'button_hover_color' : 'blue',
        }
        self.ss_btn_add = {
            'anchor' : W,
            'width' : 100,
            'height' : 60,
            'font' : ('Calibra', 18),
            'fg_color' : 'green',
            'hover_color' : 'darkgreen',
        }
        self.ss_btn_delete = {
            'anchor' : W,
            'width' : 100,
            'height' : 60,
            'font' : ('Calibra', 18),
            'fg_color' : '#ff4a4d',
            'hover_color' : '#c4393b',
        }

style = StyleStakeholder()

class StakeholdersPage:
    def __init__(self, root:CTk):
        self._root = root
        self._root.title('Stakeholders')
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

        # ==== All VARS ====
        self.var_total_stakeholders = StringVar(value='Total\n[]')
        self.var_search = StringVar()

        # === Title ===
        # lbl_title = CTkLabel(self._root, text='Stakeholders', **style.ss_lbl_title)
        # lbl_title.place(x=10, y=10)

        # === Total Stakeholders ===
        lbl_total_stakeholders = CTkLabel(self._root, text='Total\n[]', **style.ss_lbl_total_stakeholders)
        lbl_total_stakeholders.place(x=10, y=20)

        # === Search Stakeholders ===
        frm_search = CTkFrame(self._root, **style.ss_frm_search)
        frm_search.place(x=150, y=20)

        txt_search = CTkEntry(frm_search, textvariable=self.var_search, **style.ss_txt_search)
        txt_search.grid(row=0, column=0, padx=10, pady=10)

        icon_search = CTkImage(dark_image=Image.open('AppData/icons/png/search.png'), size=(32, 32))
        btn_search = CTkButton(frm_search, image=icon_search, text='', **style.ss_btn_search)
        btn_search.grid(row=0, column=1, padx=10, pady=10)

        drp_sort = CTkOptionMenu(frm_search, values=['Sort', 'A-Z', 'Z-A', 'To Give Max', 'To Receive Max'],**style.ss_drp_sort)
        drp_sort.grid(row=0, column=2, padx=10, pady=10)

        # === Manage Stakeholders ===
        icon_add = CTkImage(dark_image=Image.open('AppData/icons/png/add.png'), size=(32, 32))
        btn_add = CTkButton(self._root, image=icon_add, text='New  ', command=self.win_sta_add, **style.ss_btn_add)
        btn_add.place(relx=0.79, y=20)

        icon_delete = CTkImage(dark_image=Image.open('AppData/icons/png/delete.png'), size=(32, 32))
        btn_delete = CTkButton(self._root, image=icon_delete, text='Delete', command=self.fn_sta_delete, **style.ss_btn_delete)
        btn_delete.place(relx=0.89, y=20)

        # === Stakeholders Table ===
        frm_table = Frame(self._root)
        frm_table.place(rely=0.2, x=20, height=580)

        scrolly = Scrollbar(frm_table, orient=VERTICAL) # making scroll bar

        tbl_stakeholders= Treeview(frm_table, columns=('SrNo', 'Pronouns', 'Name', 'Contact1', 'Contact2', 'Email', 'Type', 'Balance', 'BalanceType'), yscrollcommand=scrolly.set)

        scrolly.pack(side=RIGHT, fill=Y) #packing
        scrolly.config(command=tbl_stakeholders.yview)

        # ('SrNo', 'Pronouns', 'Name', 'Contact1', 'Contact2', 'Email', 'Type', 'Balance', 'BalanceType')
        tbl_stakeholders.heading("SrNo", text="SrNo")
        tbl_stakeholders.heading("Pronouns", text="Pronouns")
        tbl_stakeholders.heading("Name", text="Name")
        tbl_stakeholders.heading("Contact1", text="Contact 1")
        tbl_stakeholders.heading("Contact2", text="Contact 2")
        tbl_stakeholders.heading("Email", text="Email")
        tbl_stakeholders.heading("Type", text="Type")
        tbl_stakeholders.heading("Balance", text="Balance")
        tbl_stakeholders.heading("BalanceType", text="BalanceType")
        
        tbl_stakeholders["show"] = "headings"

        tbl_stakeholders.column("SrNo", width=100, anchor=CENTER)
        tbl_stakeholders.column("Pronouns", width=100, anchor=CENTER)
        tbl_stakeholders.column("Name", width=280, anchor=CENTER)
        tbl_stakeholders.column("Contact1", width=160, anchor=CENTER)
        tbl_stakeholders.column("Contact2", width=160, anchor=CENTER)
        tbl_stakeholders.column("Email", width=170, anchor=CENTER)
        tbl_stakeholders.column("Type", width=100, anchor=CENTER)
        tbl_stakeholders.column("Balance", width=200, anchor=CENTER)
        tbl_stakeholders.column("BalanceType", width=110, anchor=CENTER)

        tbl_stakeholders.pack(fill=BOTH, expand=1)

    def win_sta_add(self):
        new_win = CTkToplevel(self._root)
        new_obj = StakeHoldersPage_Add(new_win)
        new_win.transient(self._root)
    
    def fn_sta_delete(self): ...


if __name__ == "__main__":
    root = CTk()
    obj = StakeholdersPage(root)
    root.mainloop()