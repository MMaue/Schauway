import tkinter as tk
from tkinter import ttk


class LookAwayApp:

    def __init__(self, master):
        self.master = master
        self.master.withdraw()  # start with the window hidden
        self.is_running = False  # flag to control the loop

        self.label = tk.Label(self.master, text="Look Away", font=("Helvetica", 48))
        self.label.pack(expand=True)

        self.smaller_label = tk.Label(self.master, text="20 feet (6m)", font=("Helvetica", 24))
        self.smaller_label.pack()

        self.stop_button = ttk.Button(self.master, text="Stop", command=self.stop)
        self.stop_button.pack(pady=10)

        self.start_timer()  # Start the timer loop
        # (20min -> show_message -> 20s -> hide_window -> start_timer)

    def start_timer(self):
        if self.is_running:
            return

        self.is_running = True
        self.master.after(1200000, self.show_message)  # 20 minutes in ms

    def show_message(self):
        if not self.is_running:
            return

        self.master.deiconify()
        self.master.attributes("-fullscreen", True)

        self.master.after(20000, self.hide_window)  # 20 seconds in ms

    def hide_window(self):
        if not self.is_running:
            return

        self.master.withdraw()
        self.is_running = False
        self.start_timer()  # Restart the loop

    def stop(self):
        self.is_running = False
        self.master.attributes("-fullscreen", False)
        self.master.destroy()


def main():
    root = tk.Tk()
    app = LookAwayApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
