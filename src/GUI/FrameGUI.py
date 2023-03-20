import tkinter as tk
from datetime import datetime
from tkinter import ttk
from tkinter.constants import *

from PIL.ImageTk import PhotoImage


# if frames are used on the GUI, these methods create objects and paste them on the frame instead of the GUI directly
# therefore we can create more Order and structure in a GUI-Project

class Frame:
    # default variables/parameter
    black = "#000000"
    grey = "#8a8a8a"
    white = "#8a8a8a"
    default_font = ("Cambria", 12, "bold")
    default_cur = "left_ptr"

    def __init__(self, frame):
        self.drop_down_menu_option = None
        self.add_drop_menu_label = None
        self.entry = None
        self.frame = frame

    # add a frame on another (already existing frame)
    @staticmethod
    def add_label_frame_on_frame(frame, text, row, column, b_width=5, pad_x=0, pad_y=0, stick="ew"):
        frame = ttk.LabelFrame(frame, borderwidth=b_width, text=text)
        frame.grid(row=row, column=column, padx=pad_x, pady=pad_y, sticky=stick)
        return frame

    def add_label_on_frame(self, text, text_var, c_span, row, column, bg=grey, fg=black, pad_x=0, pad_y=0,
                           stick="ew", font=default_font):
        label = ttk.Label(self.frame, text=str(text), textvariable=text_var, font=font, foreground=fg, background=bg)
        label.grid(row=row, column=column, columnspan=c_span, padx=pad_x, pady=pad_y, sticky=stick)
        return label

    def add_entry_on_frame(self, width, c_span, row, column, cur=default_cur, bg=white, fg=black, pad_x=0, pad_y=0,
                           stick="ew", font=default_font):
        self.entry = ttk.Entry(self.frame, width=width, foreground=fg, background=bg, cursor=cur, font=font)
        self.entry.grid(columnspan=c_span, row=row, column=column, padx=pad_x, pady=pad_y, sticky=stick)
        return self.entry

    def add_button_on_frame(self, string, com, row, column, cur=default_cur, pad_x=0, pad_y=0, stick="ew"):
        button = ttk.Button(self.frame, text=string, command=com, cursor=cur)
        button.grid(row=row, column=column, padx=pad_x, pady=pad_y, sticky=stick)
        return button

    def add_radio_button_on_frame(self, text, var, val, com, row, column, cur=default_cur, pad_x=0, pad_y=0,
                                  stick="ew"):
        radio_button = ttk.Radiobutton(self.frame, text=text, variable=var, value=val, command=com, cursor=cur)
        radio_button.grid(row=row, column=column, padx=pad_x, pady=pad_y, sticky=stick)
        return radio_button

    def add_checkbox_on_frame(self, string, var, row, column, on="YES", off="NO", cur=default_cur, pad_x=0, pad_y=0,
                              stick="ew"):
        check_box = ttk.Checkbutton(self.frame, text=string, cursor=cur, variable=var, onvalue=on, offvalue=off)
        check_box.grid(row=row, column=column, padx=pad_x, pady=pad_y, sticky=stick)
        return check_box

    # *args for multiple arguments that are written after each other (NOT IN LIST!)
    def add_drop_menu_on_frame(self, var, row, column, pad_x=0, pad_y=0, stick="ew", *args):
        option_menu = ttk.OptionMenu(self.frame, var, *args, command=self.add_drop_menu_label)
        option_menu.grid(row=row, column=column, padx=pad_x, pady=pad_y, sticky=stick)
        return option_menu

    # label that changes with drop menu, value is needed for the global variable to change
    def add_drop_menu_label_on_frame(self, value):
        self.add_label_on_frame(self.drop_down_menu_option.get(), None, 0, 0, 0)

        # scrollbar is created and a listbox is bound in it

    def add_scroll_list_on_frame(self, width, row_span, c_span, row, column, cur=default_cur, pad_x=0, pad_y=0,
                                 stick="ew"):
        scrollbar = ttk.Scrollbar(self.frame, orient=VERTICAL, cursor=cur)
        scrollbar.grid(rowspan=row_span, columnspan=c_span, row=row, column=column + 1, padx=0, pady=pad_y, sticky="ns")
        listbox = tk.Listbox(self.frame, width=width, selectmode=SINGLE, yscrollcommand=scrollbar.set)
        listbox.grid(rowspan=row_span, columnspan=c_span, row=row, column=column, padx=pad_x, pady=pad_y, sticky=stick)
        scrollbar.config(command=listbox.yview)
        return listbox

        # scrollbar is created and a textbox is bound in it

    def add_text_box_on_frame(self, width, height, row_span, col_span, row, column, cur=default_cur, pad_x=0, pad_y=0,
                              stick="ew"):
        scrollbar = ttk.Scrollbar(self.frame, orient=VERTICAL, cursor=cur)
        scrollbar.grid(rowspan=row_span, columnspan=col_span, row=row, column=column + 3, padx=0, pady=pad_y,
                       sticky="ns")
        textbox = tk.Text(self.frame, width=width, height=height, yscrollcommand=scrollbar.set)
        textbox.grid(rowspan=row_span, columnspan=col_span, row=row, column=column, padx=pad_x, pady=pad_y,
                     sticky=stick)
        scrollbar.config(command=textbox.yview)
        return textbox

    # display an image on label
    def display_img_on_frame(self, file_name, r_span, col_span, row, column, pad_x=0, pad_y=0, stick="ew"):
        img = PhotoImage(file=file_name)
        panel = ttk.Label(self.frame, image=img)
        panel.image = img
        panel.grid(rowspan=r_span, columnspan=col_span, row=row, column=column, padx=pad_x, pady=pad_y, sticky=stick)
        return panel

    # display date on label
    def display_date_on_frame(self, col_span, row, column, bg=grey, fg=black, pad_x=0, pad_y=0, stick="ew",
                              font=default_font):
        now_str = datetime.now().strftime(str("%d.%m.%y"))
        self.add_label_on_frame(now_str, None, col_span, row, column, bg, fg, pad_x, pad_y, stick, font)

    # display time on label and update it
    def display_time_on_frame(self, col_span, row, column, bg=grey, fg=black, pad_x=0, pad_y=0, stick="ew",
                              font=default_font):
        now_str = datetime.now().strftime(str("%H:%M:%S"))
        time_label = self.add_label_on_frame(now_str, None, col_span, row, column, bg, fg, pad_x, pad_y, stick, font)
        time_label.after(1000,
                         lambda: self.display_time_on_frame(col_span, row, column, bg, fg, pad_x, pad_y, stick, font))
