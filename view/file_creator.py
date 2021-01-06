import tkinter as tk
from tkinter import ttk
import subprocess, os, sys

class Creator(ttk.Frame):
    def create(self, dir_path, name, extension):
        os.chdir(dir_path+"/files")
        subprocess.run(["touch", name+"."+extension] )
        self.application_window.destroy()

    def __init__(self, main_window, dir_path):
        ttk.Frame.__init__(self, main_window)
        self.application_window = tk.Toplevel()
        self.application_window.wm_title("Crear archivo")
        self.application_window.geometry("300x100")
        self.application_window.resizable(False, False)

        file_name = tk.Label(self.application_window, text="Nombre del archivo")
        file_extension = tk.Label(self.application_window, text="Extensión")

        file_name.grid(row=0, column=0)
        file_extension.grid(row=1, column=0)

        entry_file_name = tk.Entry(self.application_window)
        entry_file_extension = tk.Entry(self.application_window)

        entry_file_name.grid(row=0, column=1)
        entry_file_extension.grid(row=1, column=1)
        submit = tk.Button(self.application_window, text="Aceptar", command = lambda: self.create(dir_path, entry_file_name.get(), entry_file_extension.get()) ) 
        submit.grid(row=2, column=0, columnspan=2)
