import tkinter
from tkinter import filedialog
import os, sys, subprocess
from view.file_creator import Creator

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
def delete_file():
    chosen_file = filedialog.askopenfilename(initialdir=files_dir,
            title="Archivo a eliminar",
            filetypes = ( ("Archivos de texto", "*.txt*") , ("Todos los archivos", "*.*")) )
    if chosen_file != '':
        #print("Deleted: %s" % chosen_file)
        subprocess.run(["rm", chosen_file])
def open_file():
    chosen_file = filedialog.askopenfilename(initialdir=files_dir,
         title="Archivo a eliminar",
         filetypes = ( ("Archivos de texto", "*.txt*") , ("Todos los archivos", "*.*")) )
    if chosen_file != '':
        #print("Opening: %s" % chosen_file)
        subprocess.run(["gedit",chosen_file] )

#main window
main_window = tkinter.Tk()
main_window.title("Proyecto unidad 5")
main_window.geometry("700x400")
main_window.resizable(False, False)

#Create button
create_file = tkinter.Button(main_window, text="Crear archivo", command= create_file)
#Delete button
delete_button = tkinter.Button(main_window, text="Borrar archivo", command= delete_file )
#Show file explorer
file_explorer = tkinter.Button(main_window, text="Mostrar archivos", command= browse_files ) 
#Show file
show_file = tkinter.Button(main_window, text="Abrir archivo", command = open_file )

create_file.pack()
delete_button.pack()
file_explorer.pack()
show_file.pack()

main_window.mainloop()
