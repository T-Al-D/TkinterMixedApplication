import tkinter as tk


# This Class is for the Menubar and for the contents within it!

class MenuGUI:

    def __init__(self, gui):
        self.gui = gui
        self.menu = tk.Menu(gui)
        gui.configure(menu=self.menu)                   # Menu is bound in GUI

    # creates 1 menu_bar_item with one under_item and 1 command
    def create_menu_item(self, menu_name, second_name, com=None):
        new_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label=menu_name, menu=new_menu)
        new_menu.add_command(label=second_name, command=com)
        return new_menu

    # all are added and can be changed dynamically during running program
    def add_themes(self):
        themes_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Change Themes", menu=themes_menu)
        for theme in sorted(self.gui.get_themes()):
            themes_menu.add_radiobutton(label=theme, command=lambda name=theme: self.gui.set_theme(theme_name=name))
        return themes_menu
