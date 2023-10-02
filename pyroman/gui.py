# File: pyroman/gui.py
import tkinter as tk
from tkinter import messagebox


class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("PyRoman GUI")
        self.create_widgets()

    def create_widgets(self):
        # Aggiungi qui i widget e la logica della GUI
        pass


def run_gui():
    root = tk.Tk()
    app = GUI(root)
    root.mainloop()
