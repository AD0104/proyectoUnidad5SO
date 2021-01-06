import tkinter
from tkinter import filedialog
from view.file_creator import Creator
import os, sys

root_dir = os.getcwd()
files_dir = root_dir+"/files"
def create_file():
    popup = Creator(main_window, root_dir)
    popup.mainloop()
def browse_files():
    chosen_file = filedialog.askopenfilename(initialdir=files_dir,
            title="Archivos...",
            filetypes = ( ("Archivos de texto","*.txt*"), ("Todos","*.*")) )
    print(chosen_file)


#main window
main_window = tkinter.Tk()
main_window.title("Proyecto unidad 5")
main_window.geometry("700x400")
main_window.resizable(False, False)

#Create button
create_file = tkinter.Button(main_window, text="Crear archivo", command= create_file)
#Delete button
delete_button = tkinter.Button(main_window, text="Borrar archivo", command= lambda:print("delete") )
#Show file explorer
file_explorer = tkinter.Button(main_window, text="Mostrar archivos", command= browse_files ) 
#Show file
show_file = tkinter.Button(main_window, text="Abrir archivo", command = lambda:print("show 1 file") )

create_file.pack()
delete_button.pack()
file_explorer.pack()
show_file.pack()

main_window.mainloop()
