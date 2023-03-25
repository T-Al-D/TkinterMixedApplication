
from tkinter import messagebox, END
from matplotlib import pyplot


class Calc:

    def __init__(self, frame):
        self.frame = frame
        self.calculation_label = self.frame.add_label_on_frame("Calculation", None, 1, 0, 0)
        self.explanation_label = self.frame.add_label_on_frame(
            "Matplotlib Graph: Add SAME AMOUNT of X and Y values separated with comma ! Coordinates drawn in order.",
            None, 1, 1, 0, "white", "black", 2, 2, "ew", ("Cambria", 8, "bold"))
        self.graph_entry_x = self.frame.add_entry_on_frame(20, 2, 2, 0)
        self.graph_entry_y = self.frame.add_entry_on_frame(20, 2, 3, 0)
        self.x_label = self.frame.add_label_on_frame("X-Axis", None, 1, 2, 3)
        self.y_label = self.frame.add_label_on_frame("Y-Axis", None, 1, 3, 3)
        self.show_button = self.frame.add_button_on_frame("Show math-graph", lambda: self.show_graph(), 4, 3)

        self.x_axis = []
        self.y_axis = []

    @staticmethod
    def assign_values(axis_entry, axis):

        for value in axis_entry:
            try:
                int_value = int(value)
                axis.append(int_value)
            except Exception:
                axis.append(value)

    def show_graph(self):
        x_axis_entry = self.graph_entry_x.get().split(",")
        y_axis_entry = self.graph_entry_y.get().split(",")

        if len(x_axis_entry) == len(y_axis_entry):
            self.assign_values(x_axis_entry, self.x_axis)
            self.assign_values(y_axis_entry, self.y_axis)

            print(self.x_axis)
            print(self.y_axis)

            figure = pyplot.figure(num="math graph", figsize=(6, 5), dpi=100)
            pyplot.plot(self.x_axis, self.y_axis)
            figure.show()

            self.graph_entry_x.delete(0, END)
            self.graph_entry_y.delete(0, END)

            self.x_axis = []
            self.y_axis = []
        else:
            messagebox.showwarning("Faulty Entry", "Entries need same amount of values!")
