import tkinter as tk
from tkinter import ttk


class UpAndDownApp:

    def __init__(self, master, stand_proportion):
        self.master = master
        self.master.withdraw()  # start with the window hidden

        minutes_seconds_ms = 60 * 60*1000
        self.ms_standing = int(stand_proportion * minutes_seconds_ms)
        self.ms_sitting =  int(minutes_seconds_ms - self.ms_standing)

        self.label = tk.Label(self.master, text="-", font=("Helvetica", 48))
        self.label.pack(expand=True)

        self.stop_button = ttk.Button(self.master, text="Got it", command=self.hide_window)
        self.stop_button.pack(pady=10)

        self.stop_button = ttk.Button(self.master, text="Stop", command=self.stop)
        self.stop_button.pack(pady=10)

        self.start_timer()  # Start the timer loop
        # (start_timer -> ms_sitting elapsed -> fullscreen -> ms_standing elapsed -> fullscreen)

    def start_timer(self):
        self.master.after(self.ms_sitting, self.show_stand_up_message)

    def show_stand_up_message(self):
        self.label.text = "Stand Up"
        self.label.config(text="Stand Up")
        self.master.deiconify()
        self.master.attributes("-fullscreen", True)

        self.master.after(self.ms_standing, self.show_sit_down_message)

    def show_sit_down_message(self):
        self.label.text = "Sit Down"
        self.label.config(text="Sit Down")
        self.master.deiconify()
        self.master.attributes("-fullscreen", True)

        self.master.after(self.ms_sitting, self.show_stand_up_message)

    def hide_window(self):
        self.master.withdraw()

    def stop(self):
        self.master.attributes("-fullscreen", False)
        self.master.destroy()


def main():
    root = tk.Tk()
    # about 30 % standing, 60 % sitting,  10 % moving
    app = UpAndDownApp(root, stand_proportion=1/3)
    root.mainloop()


if __name__ == "__main__":
    main()
