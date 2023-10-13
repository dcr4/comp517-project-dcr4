import tkinter as tk
from url import URL


WIDTH = 1280
HEIGHT = 720

class Vagabond:
    """
    The main web browser class.
    """
    def __init__(self):
        self.window = tk.Tk()
        self.canvas = tk.Canvas(self.window, width=WIDTH, height=HEIGHT)
        # self.canvas.pack()
        self.input_url = ""

    def run(self):
        """
        Creates, configures, and organizes widgets.
        """
       # Create and configure widgets
        self.label = tk.Label(self.window, text="Enter URL:")
        self.entry = tk.Entry(self.window, textvariable=self.input_url)  # Link the Entry to the input_url variable
        self.save_btn = tk.Button(self.window, text="Save URL", command=self.save_text)
        self.load_btn = tk.Button(self.window, text="Load HTML", command = self.load)
        self.show_btn = tk.Button(self.window, text="Show HTML", command = self.show)
        self.body_lbl = tk.Label(self.window, text="")

        # Organize widgets using grid layout manager
        self.label.grid(row=0, column=0)
        self.entry.grid(row=0, column=1)
        self.save_btn.grid(row=1, columnspan=2)
        self.load_btn.grid(row=2, columnspan=2)
        self.show_btn.grid(row=3, columnspan=2)
        self.body_lbl.grid(row=4, column=0, rowspan=10, columnspan=10)


    def save_text(self):
        """
        Responds to click event on "Save Text" button1.
        """
        self.input_url = self.entry.get()  # Get the text from the Entry widget
        self.label.config(text=f"URL: {self.input_url}")
        self.entry.delete(0, "end")
        self.url = URL(self.input_url)

    def show(self):
        """
        Draws a web page to the screen.
        """
        # in_angle = False
        # for c in body:
        #     if c == "<":
        #         in_angle = True
        #     elif c == ">":
        #         in_angle = False
        #     elif not in_angle:
        #         print(c, end="")
        self.body_lbl.config(text=self.body)
    
    def load(self):
        """
        Loads a web page.
        """
        self.url.parse_url()
        self.headers, self.body = self.url.req()

"""
Main
"""
if __name__ == "__main__":
    Vagabond().run()
    tk.mainloop()