
class DateTime:

    def __init__(self, frame):
        self.frame = frame
        self.time_label_in_frame = self.frame.display_time_on_frame(1, 0, 0)
        self.empty_label_in_frame = self.frame.add_label_on_frame(" / ", None, 1, 0, 1)
        self.date_label_in_frame = self.frame.display_date_on_frame(1, 0, 2)
