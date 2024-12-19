from main import WINDOW_WIDTH, WINDOW_HEIGHT

COLOR = {
    1: '#0C359E', # blue
    2: '#EE99C2', # pink
    3: '#FFE3CA', # peach
    4: '#F6F5F5', # white
}
# ==== main.py ===========================
s_lbl_main_title = {
    'text_color' : COLOR[4], 
    'fg_color' : COLOR[1], 
    'font' : ('Arial', 50, 'bold'),
    'corner_radius': 1,
    'width' : WINDOW_WIDTH,
    'height' : 80,
}

s_btn_cart = {
    'width' : 50,
    'height' : 50,
    'bg_color': COLOR[1],
    'fg_color' : COLOR[4],
    'corner_radius' : 10,
}

s_btn_settings = {
    'width' : 50,
    'height' : 50,
    'bg_color': COLOR[1],
    'fg_color' : COLOR[4],
    'hover_color' : '#b3b3b3',
}

s_lbl_menu = {
    'width' : 250,
    'height': 30,
    'text_color' : 'black',
    'font' : ('Arial', 20, 'bold'),
    'corner_radius' : 1,
}

s_btn_menu = {
    'width' : 260,
    'height': 40,
    'text_color' : 'black',
    'font' : ('Arial', 20),
    'fg_color' : COLOR[3],
    'corner_radius' : 1,
    'hover_color': '#D1BBA7',
}

