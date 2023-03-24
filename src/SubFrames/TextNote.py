from tkinter import filedialog, END


class TextNote:

    def __init__(self, frame):
        self.frame = frame
        self.textbox = self.frame.add_text_box_on_frame(21, 20, 3, 3, 0, 0)
        self.open_button = self.frame.add_button_on_frame("OPEN", lambda: self.open_text(), 4, 0)
        self.save_button = self.frame.add_button_on_frame("SAVE", lambda: self.save_text(), 4, 1)
        self.clear_button = self.frame.add_button_on_frame("CLEAR", lambda: self.clear_text(), 4, 2)

    # clear the entire text
    def clear_text(self):
        self.textbox.delete(1.0, END)

    # save a .txt
    def save_text(self):
        text_file = filedialog.asksaveasfilename(title="Select place to save file.",
                                                 filetypes=[("Text Files", "*.txt")])
        if text_file != "":
            text_file = open(text_file, "w")
            contents = self.textbox.get(1.0, END)
            text_file.write(contents)
            text_file.close()

    # open a .txt
    def open_text(self):
        self.clear_text()
        text_file = filedialog.askopenfilename(title="Select file to open.", filetypes=[("Text Files", "*.txt")])
        if text_file != "":
            text_file = open(text_file, "r+")
            contents = text_file.read()
            self.textbox.insert(END, contents)
            text_file.close()
