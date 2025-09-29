from model.entity import *
from tools.logging import Logger
from view.main_view import MainView
import tkinter as tk
Logger.info("application started")
if __name__ =="__main__":
    root = tk.Tk()
    app = MainView(root)
    root.mainloop()