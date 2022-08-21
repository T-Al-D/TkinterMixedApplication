import tkinter as tk
from tkinter import ttk



class MenuGUI:

    def __init__(self, gui):
        self.menu = tk.Menu(gui)
        gui.configure(menu=self.menu)       # Menu is bound in GUI
        self.style_menu = tk.Menu(self.menu)

        # self.selected_theme = None
        self.styles = ttk.Style()

    def create_menu_item(self, menu_name, second_name, com=None):
        new_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label=menu_name, menu=new_menu)
        new_menu.add_command(label=second_name, command=com)
        return new_menu


    def change_theme(self, gui):
        # self.styles.theme_use(self.selected_theme.get())
        gui.add_label("Hello", None, 1, 0, 0)
        gui.quit()
        pass


