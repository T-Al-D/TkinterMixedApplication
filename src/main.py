#
from GUI.BasicThemedTkGUI import *
from GUI.MenuBarGUI import *
from src.GUI.FrameGUI import *
from src.SubFrames.Notepad import *

if __name__ == "__main__":
    ################ WINDOW ################
    # initialize
    gui = GUI("Experimental AI ! KAREN", "800x600", True, "#1f073b", "resources/Icon/slightlyCreepy.png", True)

    # frames in the main GUI
    # datetime
    datetime_label_in_frame = Frame(gui.add_label_frame("DateTime", 1, 0, 5, 2, 2))
    time_label_in_frame = Frame.display_time_on_frame(datetime_label_in_frame, 1, 0, 0)
    date_label_in_frame = Frame.display_date_on_frame(datetime_label_in_frame, 1, 1, 0)

    notepad_frame = Frame(gui.add_label_frame("Notepad", 3, 0, 10, 2, 2))
    Notepad(notepad_frame)


    # switched frames (through buttons)
    chatbot_switch_frame = Frame(gui.add_label_frame("Mini-ChatBot", 1, 2, 8, 4, 4, "nsew"))
    chatbot_label = Frame.add_label_on_frame(chatbot_switch_frame, "Chatbot", None, 1, 0, 0)

    neutral_switch_frame = Frame(gui.add_label_frame("Pick a Mini-Program", 1, 2, 8, 4, 4, "nsew"))
    neutral_label = Frame.add_label_on_frame(neutral_switch_frame, "Neutral", None, 1, 0, 0)

    all_switch_frames = [chatbot_switch_frame, neutral_switch_frame]



    # "navigation" with buttons
    nav_button_frame = Frame(gui.add_label_frame("Navigation", 2, 0, 5, 2, 2))
    neutral_button = Frame.add_button_on_frame(nav_button_frame, "Neutral",
                                               lambda: GUI.switch_frame(neutral_switch_frame, all_switch_frames), 0, 0)
    chatbot_button = Frame.add_button_on_frame(nav_button_frame, "Mini-Chatbot",
                                               lambda: GUI.switch_frame(chatbot_switch_frame, all_switch_frames), 1, 0)


    # add items to menubar
    menu_bar = MenuGUI(gui)
    menu_bar.add_themes()


    # keep the window going
    gui.mainloop()
    ########################################
