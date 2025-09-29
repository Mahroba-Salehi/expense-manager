from model.entity import *
from tools.logging import Logger
from view.main_view import Logger
from view.main_view import MainView
import tkinter as tk
Logger.info("application started")
if name =="main":
    root = tk.Tk()
    app = MainView(root)
    root.mainloop()