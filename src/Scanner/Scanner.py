import platform

import psutil as psutil


class Scanner:

    def __init__(self, frame):
        self.frame = frame
        self.scanner_label = self.frame.add_label_on_frame("Scanner", None, 1, 0, 0)
        self.host_info_button = self.frame.add_button_on_frame("Scan host for info!",
                                                               lambda: self.show_host_info(), 1, 0)
        self.host_name_label = self.frame.add_label_on_frame("...", None, 2, 1, 1)
        self.host_os_label = self.frame.add_label_on_frame("...", None, 2, 2, 1)
        self.host_core_label = self.frame.add_label_on_frame("...", None, 2, 3, 1)

    def show_host_info(self):
        self.host_name_label.config(text="Host Name: " + platform.node())
        self.host_os_label.config(text="Host OS: " + platform.system())
        self.host_core_label.config(text="Host Cores: " + str(psutil.cpu_count()))
