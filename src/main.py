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
    gui.display_date(2, 0, 20)
    gui.display_time(2, 1, 20)
    frame = Frame(gui.add_frame(7, 7))
    frame2 = Frame(gui.add_label_frame("labelFrame1",9, 9))

    frame.add_label_on_frame("FrameLabel", None, 1, 0, 0)
    frame.display_time_on_frame(2,1,0)
    frame2.add_label_on_frame("FrameLabel2", None, 1, 0, 0)
    frame2.display_date_on_frame(2,1,0)
    frame2.add_button_on_frame("But", None, 3, 5)
    frame2.add_checkbox_on_frame("Check", None, 3, 0)
    frame2.add_entry_on_frame(20, 1, 1, 1)
    frame2.add_radio_button_on_frame("What", None, None, None, 2, 3)
    frame2.add_scroll_list_on_frame(20, 1,2, 3, 3)
    frame2.add_text_box_on_frame(70, 70, 2, 2 , 5 ,0)

    gui.add_label_frame( "labelFrram2",6, 6)
    gui.add_radio_button("Hello", None, None, None, 2, 2)

    menu_bar = MenuGUI(gui)
    menu_bar.add_themes()




    # keep the window going
    gui.mainloop()
    ########################################
