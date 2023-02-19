from Calculation.Calc import *
from GUI.BasicThemedTkGUI import *
from GUI.MenuBarGUI import *
from src.GUI.FrameGUI import *

if __name__ == "__main__":
    calc = Calc(100)

    ################ WINDOW ################
    # initialize
    gui = GUI("Experimental AI ! KAREN", "800x600", True, "#1f073b", "resources/Icon/slightlyCreepy.png", True)

    # build the surface (add widgets)
    gui.display_date(1, 0, 2)
    gui.display_time(1, 0, 3, "#e3e6e4")
    label_frame_1 = Frame(gui.add_label_frame("Test AI", 1, 0))


    menu_bar = MenuGUI(gui)
    menu_bar.add_themes()




    # keep the window going
    gui.mainloop()
    ########################################
