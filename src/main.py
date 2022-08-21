from Calculation.Calc import *
from GUI.BasicTkGUI import *
from GUI.MenuBarGUI import *


# this method is used to give other classes a gui to build on
def get_gui():
    return gui


if __name__ == "__main__":
    calc = Calc(100)

    ################ WINDOW ################
    # initialize
    gui = GUI("Experimental AI ! kArIn", "800x600", True, "#1f073b", "resources/Icon/slightlyCreepy.png", True)

    # build the surface (add widgets)
    gui.display_date(2, 0, 20)
    gui.display_time(2, 1, 20)

    menu_bar = MenuGUI(gui)
    menu_bar.create_menu_item("Change Style", "Null", lambda: menu_bar.change_theme(gui))
    menu_bar.create_menu_item("Exit", "Goodbye!", gui.quit)



    # keep the window going
    gui.mainloop()
    ########################################
