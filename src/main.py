from Calculation.Calc import *
from GUI.BasicThemedTkGUI import *
from GUI.MenuBarGUI import *


if __name__ == "__main__":
    calc = Calc(100)

    ################ WINDOW ################
    # initialize
    gui = GUI("Experimental AI ! KAREN", "800x600", True, "#1f073b", "resources/Icon/slightlyCreepy.png", True)

    # build the surface (add widgets)
    gui.display_date(2, 0, 20)
    gui.display_time(2, 1, 20)
    gui.add_frame(7,7,"Frame")
    gui.add_label_frame(6,6,"LabelFrame")
    gui.add_radio_button("Hello",None ,None, None, 2, 2)
    gui.add_entry(10,3,5,5)

    menu_bar = MenuGUI(gui)
    menu_bar.add_themes()




    # keep the window going
    gui.mainloop()
    ########################################
