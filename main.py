'''
Paid :- Invoice Maker, Employee MS
GST on each product, 
Collection of Images in products like collection on top and uske neeche image uske neeche name and side mein code and all
'''
import pyautogui as pg
from customtkinter import *
from CTkMessagebox import CTkMessagebox # https://github.com/Akascape/CTkMessagebox
from PIL import Image
import subprocess
from numpy import nan as NaN

# import from files
from style import *
from scr_settings import SettingsPage
from scr_stakeholder import StakeholdersPage
from scr_inventory import InventoryPage
from scr_quickbill import QuickBillPage
from scr_billing import BillingPage
from scr_employees import EmployeesPage
from Packages.Matplotlib.matplotlib_in_tk import plot
from Packages.ListManager.list_manager import ListOfFrame

SCREEN_WIDTH = pg.size()[0]
SCREEN_HEIGHT = pg.size()[1]

WINDOW_WIDTH = int(SCREEN_WIDTH * 0.78)
WINDOW_HEIGHT = int(SCREEN_HEIGHT * 0.70)
WINDOW_X = int(SCREEN_WIDTH * 0.01)
WINDOW_Y = int(SCREEN_HEIGHT * 0.01)

class HomePage:
    def __init__(self, root:CTk):
        self._root = root
        self._root.title('Business Management System | by Jacob')
        self._root.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{WINDOW_X}+{WINDOW_Y}')

        self.days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        self.days_three = [i[:3] for i in self.days]

        # === Top Label ===
        lbl_main_title = CTkLabel(self._root, text='Business Management System', **s_lbl_main_title)
        lbl_main_title.place(x=0, y=0)

        # === Cart ===
        icon_cart = CTkImage(dark_image=Image.open('AppData/icons/png/cart.png'), size=(32, 32))
        lbl_cart = CTkLabel(self._root, image=icon_cart, text='', **s_btn_cart)
        lbl_cart.place(x=40, y=15)

        # === Settings ===
        icon_settings = CTkImage(dark_image=Image.open('AppData/icons/png/settings.png'), size=(30, 30))
        btn_settings = CTkButton(self._root, image=icon_settings, text='', command=self.win_settings, **s_btn_settings)
        btn_settings.place(x=WINDOW_WIDTH-90, y=15)

        # === Menu ===
        frm_menu = CTkFrame(self._root, width=250, height=500, fg_color='transparent')
        frm_menu.place(x=int(SCREEN_WIDTH*0.02), y=200)

        img_menu_top = CTkImage(dark_image=Image.open('AppData/page/img_menu_top.png'), size=(300, 60))
        lbl_menu = CTkLabel(frm_menu, image=img_menu_top, text='MENU', **s_lbl_menu)
        lbl_menu.pack(fill=X)

        btn_stakeholders = CTkButton(frm_menu, text='STAKEHOLDERS', command=self.win_stakeholders, **s_btn_menu).pack(fill=X, ipady=10)
        btn_inventory = CTkButton(frm_menu, text='INVENTORY', command=self.win_inventory, **s_btn_menu).pack(fill=X, ipady=10)
        btn_quickbill = CTkButton(frm_menu, text='QUICK BILL', command=self.win_quickbill, **s_btn_menu).pack(fill=X, ipady=10)
        btn_billing = CTkButton(frm_menu, text='BILLING', command=self.win_billing, **s_btn_menu).pack(fill=X, ipady=10)
        btn_calculator = CTkButton(frm_menu, text='CALCULATOR', command=lambda : subprocess.Popen('C:\\Windows\\System32\\calc.exe'), **s_btn_menu).pack(fill=X, ipady=10)
        btn_employees = CTkButton(frm_menu, text='EMPLOYEES', command=self.win_employees, **s_btn_menu).pack(fill=X, ipady=10)

        img_menu_bottom = CTkImage(dark_image=Image.open('AppData/page/img_menu_bottom.png'), size=(300, 30))
        lbl_menu_bottom = CTkLabel(frm_menu, image=img_menu_bottom, text='', **s_lbl_menu)
        lbl_menu_bottom.pack(fill=X)

        # === Main Page ===
        # sales (graph), expenses (list), transactions(list), employees online (list), notifications (high prior, lows)
        # === Sales ===
        frm_sales = CTkFrame(self._root)
        frm_sales.place(x=int(SCREEN_WIDTH/4.6), y=100)

        plot(frm_sales, self.days_three, [200, 400, 10000, 500, 800, 900, 100], width_inch=3.2, height_inch=3.2, color='green', graph_title='Sales')

        # === Expenses ===
        frm_expenses = CTkFrame(self._root)
        frm_expenses.place(x=int(SCREEN_WIDTH/2.6), y=100)

        plot(frm_expenses, self.days_three, [200, 400, 90, 500, 899, 900, 100], width_inch=3.2, height_inch=3.2, color='red', graph_title='Expenses')

        # === Transactions ===
        frm_transactions = CTkFrame(self._root, fg_color='transparent')
        frm_transactions.place(x=int(SCREEN_WIDTH*0.22), y=440)

        lbl = CTkLabel(frm_transactions, text='Hi')
        # lbl.pack()

        lis_transactions = ListOfFrame(frm_transactions, max_width=600, max_height=100)

        lis_transactions.title_draw('Transactions', font=('DejaVu Sans', 20), fill=X)

        lis_transactions.headings(['ID', 'To', 'From', 'Amount', 'Date'])
        lis_transactions.draw_headings(headings_width=[50, 180, 180, 120, 80])

        lis_transactions.enable_alt_style(1, 'darkblue')

        lis_transactions.add_item('AB12345', 'Jacob', 'Our Business', 90000, '18-Mar-2024')
        lis_transactions.add_item('AB12346', 'Jacob', 'Our Business', 9000000, '19-Mar-2024')
        lis_transactions.add_item('AB12346', 'Jacob', 'Our Business', 9000000, '19-Mar-2024')
        lis_transactions.add_item('AB12346', 'Jacob', 'Our Business', 9000000, '19-Mar-2024')

        # print(frm_transactions.children)
        # print(frm_transactions.slaves()) # Pack order mein list
        # print(frm_transactions.winfo_children()) # place order mein list

        # === Employees ===
        frm_employees = CTkFrame(self._root)
        frm_employees.place(x=int(SCREEN_WIDTH*0.58), y=150)

        # === Notifications ===
        frm_notifications = CTkFrame(self._root)
        frm_notifications.place(x=int(SCREEN_WIDTH*0.58), y=400)

        lis_notifications = ListOfFrame(frm_notifications, max_width=200, max_height=100)
        
        lis_notifications.title_draw('Notifications', font=('DejaVu Sans', 20), fill=X)

        lis_notifications.headings([''])
        lis_notifications.draw_headings()

        lis_notifications.add_item('PS4 Controllers Low Stock')
        lis_notifications.add_item('PS3 Controllers Low Stock')
        lis_notifications.add_item('PS5 Controllers Low Stock')
        lis_notifications.add_item('PS2 Controllers Low Stock')
        lis_notifications.add_item('PS1 Controllers Low Stock')

    def win_stakeholders(self):
        new_win = CTkToplevel(self._root)
        new_obj = StakeholdersPage(new_win)
        new_win.transient(self._root)
            

    def win_inventory(self):
        new_win = CTkToplevel(self._root)
        new_obj = InventoryPage(new_win)
        new_win.transient(self._root)

    def win_quickbill(self):
        new_win = CTkToplevel(self._root)
        new_obj = QuickBillPage(new_win)
        new_win.transient(self._root)

    def win_billing(self):
        new_win = CTkToplevel(self._root)
        new_obj = BillingPage(new_win)
        new_win.transient(self._root)

    def win_employees(self):
        new_win = CTkToplevel(self._root)
        new_obj = EmployeesPage(new_win)
        new_win.transient(self._root)

    def win_settings(self):
        new_win = CTkToplevel(self._root)
        new_obj = SettingsPage(new_win)
        new_win.transient(self._root)
        


if __name__ == '__main__':
    root = CTk()
    obj = HomePage(root)
    root.mainloop()

'''
Graphs
Sales Graph - It takes Transaction database ke paid amounts and add those values daily, then it is ploted every day.
    - mode can be changed to daily, weekly(if enough data available) +
    - On X axis are particular dates
'''

'''
Notifications
- Of Stock <= Min Stock ⭐
- Of Employee on leave for more than 2 days
- of filling govt papers ⭐
- Of pending balance

open the tab to set priorities
LATER - create notifications
'''