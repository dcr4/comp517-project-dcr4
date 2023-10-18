import tkinter as tk

from render import HTML_Renderer
from constants import RWIDTH, RHEIGHT
from url import URL

class Vagabond:
    """
    The main web browser class.
    """

    def __init__(self):
        """
        Instantiates a new instance of Vagabond.
        """
        self.window = tk.Tk()
        self.canvas = tk.Canvas(self.window, width=RWIDTH, height=RHEIGHT)
        self.canvas.pack()
        self.input_url = ""
        self.html_renderer = HTML_Renderer()

    def run(self):
        """
        Creates, configures, and organizes widgets.
        """
        # Set title
        self.window.winfo_toplevel().title("Vagabond")

        # Create and configure widgets
        self.url_lbl = tk.Label(self.window, text="Enter URL:")
        self.url_entry = tk.Entry(self.window, textvariable=self.input_url)  # Link the Entry to the input_url variable
        self.save_btn = tk.Button(self.window, text="Save URL", command=self.save_text)
        self.load_btn = tk.Button(self.window, text="Load HTML", command = self.load)
        self.show_btn = tk.Button(self.window, text="Show HTML", command = self.show)
        self.body_lbl = tk.Label(self.window, text="")

        # Add the button and label to the canvas using create_window
        url_lbl_window = self.canvas.create_window(300, 200, window=self.url_lbl)
        url_entry_window = self.canvas.create_window(300, 200, window=self.url_entry)
        save_btn_window = self.canvas.create_window(100, 100, window=self.save_btn)
        load_btn_window = self.canvas.create_window(100, 200, window=self.load_btn)
        show_btn_window = self.canvas.create_window(100, 300, window=self.show_btn)

        # Organize widgets using grid layout manager
        # self.url_lbl.grid(row=0, column=0)
        # self.url_entry.grid(row=0, column=1)
        # self.save_btn.grid(row=1, columnspan=2)
        # self.load_btn.grid(row=2, columnspan=2)
        # self.show_btn.grid(row=3, columnspan=2)
        # self.body_lbl.grid(row=4, column=0, rowspan=10, columnspan=10)


    def save_text(self):
        """
        Responds to click event on "Save Text" button1.
        """
        self.input_url = self.url_entry.get()  # Get the text from the Entry widget
        self.url_lbl.config(text=f"URL: {self.input_url}")
        self.url_entry.delete(0, "end")
        self.url = URL(self.input_url)

    def show(self):
        """
        Draws a web page to the screen.
        """
        text = self.html_renderer.get_body_text(self.body)
        display_list = self.html_renderer.layout_text(text)
        for x, y, c in display_list:
            self.canvas.create_text(x, y, text=c)

        # self.body_lbl.config(text=self.body)
        # self.body_lbl.config(text=text)
    
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