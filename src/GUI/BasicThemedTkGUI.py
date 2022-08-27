from datetime import datetime
from tkinter import ttk
from tkinter.constants import *
from PIL.ImageTk import PhotoImage
import tkinter as tk
from ttkthemes import *

# initialization with tk.Tk__init__(self) all Methods are being inherited
# this class contains all methods needed to create Objects on the GUI DIRECTLY!


class GUI(ThemedTk):
    # default variables/parameter
    black = "#000000"
    grey = "#8a8a8a"
    white = "#8a8a8a"
    default_font = ("Cambria", 12, "bold")
    default_cur = "left_ptr"

    # the class itself becomes the ROOT
    def __init__(self, title, size="360x360", resizable=True, bg_color=None, icon_path=None, icon_is_used=False):
        super().__init__()
        self.set_theme("default")
        self.drop_down_menu_option = None
        self.entry = None
        self.title(title)                                                # window title
        self.geometry(size)                                              # window size
        self.resizable(width=resizable, height=resizable)                # resizable window
        self.config(bg=bg_color)

        if icon_is_used:
            self.iconphoto(icon_is_used, tk.PhotoImage(file=icon_path))  # Icon from .png


    # a frame can contain other items and objects, but needs functions from other class
    def add_frame(self, row, column, text=None, b_width=5,  side="top", pad_x=0, pad_y=0, stick="ew"):
        frame = ttk.Frame(self, borderwidth=b_width)
        # (text=text, side=side)
        frame.grid(row=row, column=column, padx=pad_x, pady=pad_y, sticky=stick)
        return frame

    def add_label_frame(self, row, column, text=None, b_width=5, pad_x=0, pad_y=0, stick="ew"):
        label_frame = ttk.LabelFrame(self, borderwidth=b_width)
        # text=text, side="top",
        label_frame.grid(row=row, column=column, padx=pad_x, pady=pad_y, sticky=stick)
        return label_frame

    def add_label(self, text, text_var, c_span, row, column, bg=grey, fg=black, pad_x=0, pad_y=0, stick="ew",
                  font=default_font):
        label = ttk.Label(self, text=str(text), textvariable=text_var, font=font, foreground=fg, background=bg)
        label.grid(row=row, column=column, columnspan=c_span, padx=pad_x, pady=pad_y, sticky=stick)
        return label

    # a string Input which has to handled carefully
    def add_entry(self, width, c_span, row, column, cur=default_cur, bg=white, fg=black, pad_x=0, pad_y=0,
                  stick="ew", font=default_font):
        self.entry = ttk.Entry(self, width=width, foreground=fg, background=bg, cursor=cur, font=font)
        self.entry.grid(columnspan=c_span, row=row, column=column, padx=pad_x, pady=pad_y, sticky=stick)
        return self.entry

    def add_button(self, string, com, row, column, cur=default_cur, pad_x=0, pad_y=0, stick="ew"):
        button = ttk.Button(self, text=string, command=com, cursor=cur)
        button.grid(row=row, column=column, padx=pad_x, pady=pad_y, sticky=stick)
        return button

    def add_radio_button(self, text, var, val, com, row, column, cur=default_cur, pad_x=0, pad_y=0, stick="ew"):
        radio_button = ttk.Radiobutton(self, text=text, variable=var, value=val, command=com, cursor=cur)
        radio_button.grid(row=row, column=column, padx=pad_x, pady=pad_y, sticky=stick)
        return radio_button

    def add_checkbox(self, string, var, row, column, on="YES", off="NO", cur=default_cur, pad_x=0, pad_y=0, stick="ew"):
        check_box = ttk.Checkbutton(self, text=string, cursor=cur, variable=var, onvalue=on, offvalue=off)
        check_box.grid(row=row, column=column, padx=pad_x, pady=pad_y, sticky=stick)
        return check_box

    # *args for multiple arguments that are written after each other (NOT IN LIST!)
    def add_drop_menu(self, var, row, column, pad_x=0, pad_y=0, stick="ew", *args):
        option_menu = ttk.OptionMenu(self, var, *args, command=self.add_drop_menu_label)
        option_menu.grid(row=row, column=column, padx=pad_x, pady=pad_y, sticky=stick)
        return option_menu

    # label that changes with drop menu, value is needed for the global variable to change
    def add_drop_menu_label(self, value):
        self.add_label(self.drop_down_menu_option.get(), None, 0, 0, 0)

    # scrollbar is created and a listbox is bound in it
    def add_scroll_list(self, width, row_span, c_span, row, column, cur=default_cur, pad_x=0, pad_y=0, stick="ew"):
        scrollbar = ttk.Scrollbar(self, orient=VERTICAL, cursor=cur)
        scrollbar.grid(rowspan=row_span, columnspan=c_span, row=row, column=column + 1, padx=0, pady=pad_y, sticky="ns")
        listbox = tk.Listbox(self, width=width, selectmode=SINGLE, yscrollcommand=scrollbar.set)
        listbox.grid(rowspan=row_span, columnspan=c_span, row=row, column=column, padx=pad_x, pady=pad_y, sticky=stick)
        scrollbar.config(command=listbox.yview)
        return listbox

    # scrollbar is created and a textbox is bound in it
    def add_text_box(self, width, height, row_span, col_span, row, column, cur=default_cur, pad_x=0, pad_y=0,
                     stick="ew"):
        scrollbar = ttk.Scrollbar(self, orient=VERTICAL, cursor=cur)
        scrollbar.grid(rowspan=row_span, columnspan=col_span, row=row, column=column + 3, padx=0, pady=pad_y,
                       sticky="ns")
        textbox = tk.Text(self, width=width, height=height, yscrollcommand=scrollbar.set)
        textbox.grid(rowspan=row_span, columnspan=col_span, row=row, column=column, padx=pad_x, pady=pad_y,
                     sticky=stick)
        scrollbar.config(command=textbox.yview)
        return textbox

    # display an image on label
    def display_img(self, file_name, r_span, col_span, row, column, pad_x=0, pad_y=0, stick="ew"):
        img = PhotoImage(file=file_name)
        panel = ttk.Label(self, image=img)
        panel.image = img
        panel.grid(rowspan=r_span, columnspan=col_span, row=row, column=column, padx=pad_x, pady=pad_y, sticky=stick)
        return panel

    # display date on label
    def display_date(self, col_span, row, column, bg=grey, fg=black, pad_x=0, pad_y=0, stick="ew", font=default_font):
        now_str = datetime.now().strftime(str("%d.%m.%y"))
        self.add_label(now_str, None, col_span, row, column, bg, fg, pad_x, pad_y, stick, font)

    # display time on label and update it
    def display_time(self, col_span, row, column, bg=grey, fg=black, pad_x=0, pad_y=0, stick="ew", font=default_font):
        now_str = datetime.now().strftime(str("%H:%M:%S"))
        time_label = self.add_label(now_str, None, col_span, row, column, bg, fg, pad_x, pad_y, stick, font)
        time_label.after(1000, lambda: self.display_time(col_span, row, column, bg, fg, pad_x, pad_y, stick, font))
