import tkinter as tk
from tkinter import messagebox
from controller.user_controller import UserController
from model.entity.user import User

class UserView:
    def __init__(self, master):
        self.controller = UserController()
        self.window = tk.Toplevel(master)
        self.window.title("User Management")
        self.window.geometry("350x300")

        tk.Label(self.window, text="Name").pack()
        self.name_entry = tk.Entry(self.window)
        self.name_entry.pack()

        tk.Label(self.window, text="Email").pack()
        self.email_entry = tk.Entry(self.window)
        self.email_entry.pack()

        tk.Label(self.window, text="Password").pack()
        self.password_entry = tk.Entry(self.window, show="*")
        self.password_entry.pack()

        tk.Button(self.window, text="Add User", command=self.add_user).pack(pady=5)
        tk.Button(self.window, text="Show Users", command=self.show_users).pack(pady=5)

        self.users_listbox = tk.Listbox(self.window, width=50)
        self.users_listbox.pack(pady=10)

    def add_user(self):
        try:
            name = self.name_entry.get()
            email = self.email_entry.get()
            password = self.password_entry.get()
            user = User(None, name, email, password)
            self.controller.add_user(user)
            messagebox.showinfo("Success", "User added!")
            self.show_users()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def show_users(self):
        self.users_listbox.delete(0, tk.END)
        users = self.controller.get_all_users()
        for u in users:
            self.users_listbox.insert(tk.END, f"{u[0]} | {u[1]} | {u[2]}")

            self.reset_form()
            self.window.mainloop()
