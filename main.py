from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import *
from turtle import onclick
from login import LoginFrame
from tk_models import *
from experiment_pages.experiment_menu_ui import ExperimentMenuUI

from accounts import AccountsFrame
from experiment_pages.select_experiment_ui import ExperimentsUI

#command for 'open' option in menu bar
def open_file():
    file_path = askopenfilename(filetypes=[("Database files","*.db")]);
    page = ExperimentMenuUI(root, file_path, experiments_frame)
    page.tkraise()


root = Tk()
root.title("Mouser")
root.geometry('600x600')
root.minsize(600,600)

#Adds menu bar to root and binds the function to file_menu
menu_bar = Menu(root)
file_menu = Menu(menu_bar, tearoff= 0)
file_menu.add_command(label = "Open", command = open_file)
menu_bar.add_cascade(label = "File", menu=file_menu)
root.config(menu=menu_bar)

main_frame = MouserPage(root, "Mouser")
login_frame = LoginFrame(root, main_frame)

experiments_frame = ExperimentsUI(root, main_frame)

raise_frame(experiments_frame)

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

root.mainloop()


