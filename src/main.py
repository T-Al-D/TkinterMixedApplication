#
from GUI.BasicThemedTkGUI import *
from GUI.MenuBarGUI import *
from src.Calculation.Calc import Calc
from src.GUI.FrameGUI import *
from src.SubFrames.DateTime import DateTime
from src.SubFrames.TextNote import *
from src.SubFrames.ToDoList import ToDoList

if __name__ == "__main__":
    ################ WINDOW ################
    # initialize
    gui = GUI("Tkinter MixedPrograms", "800x800", True, "#1f073b", "resources/Icon/slightlyCreepy.png", True)

    # add items to menubar
    menu_bar = MenuGUI(gui)
    menu_bar.add_themes()

    # variables
    # switch_frame parameters (for all switch_frames the same)
    sf_row_span = 2
    sf_column_span = 2
    sf_row = 2
    sf_column = 2
    sf_border_width = 8
    sf_pad_x = 4
    sf_pad_y = 4
    sf_expand = "nsew"

    nav_button_cur = "arrow"

    # frames in the main GUI
    datetime_label_in_frame = Frame(gui.add_label_frame("DateTime", 1, 1, 1, 0, 8, 3, 3))
    DateTime(datetime_label_in_frame)

    text_note_frame = Frame(gui.add_label_frame("TextNote", 1, 1, 2, 0, 10, 2, 2))
    TextNote(text_note_frame)

    to_do_list_frame = Frame(gui.add_label_frame("ToDoList", 1, 1, 3, 0, 10, 2, 2))
    ToDoList(to_do_list_frame)


    # switched frames (through buttons)
    neutral_switch_frame = Frame(gui.add_label_frame("Pick a Mini-Program", sf_row_span, sf_column_span, sf_row,
                                                     sf_column, sf_border_width, sf_pad_x, sf_pad_y, sf_expand))
    neutral_label = Frame.add_label_on_frame(neutral_switch_frame, "Neutral", None, 1, 0, 0)

    calc_switch_frame = Frame(gui.add_label_frame("Calculation", sf_row_span, sf_column_span, sf_row, sf_column,
                                                  sf_border_width, sf_pad_x, sf_pad_y, sf_expand))
    Calc(calc_switch_frame)


    # "navigation" with buttons
    all_switch_frames = [calc_switch_frame, neutral_switch_frame]
    nav_button_frame = Frame(gui.add_label_frame("Navigation", 1, 2, 1, 2, 7, 2, 2))
    chatbot_button = Frame.add_button_on_frame(nav_button_frame, "Calculation",
                                               lambda: GUI.switch_frame(calc_switch_frame, all_switch_frames), 0, 1,
                                               nav_button_cur, 4, 4)
    neutral_button = Frame.add_button_on_frame(nav_button_frame, "Neutral",
                                               lambda: GUI.switch_frame(neutral_switch_frame, all_switch_frames), 0, 0,
                                               nav_button_cur, 4, 4)

    # keep the window going
    gui.mainloop()
    ########################################
