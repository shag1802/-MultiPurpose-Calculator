from tkinter import *
from tkinter import ttk
import time

import Scientific_final
import Graphing_final
import Converter_final

splash_root = Tk()
splash_root.title("Start")
splash_root.geometry("400x500")
splash_root['bg']='black'

splash_label = Label(splash_root, text="Hello",bg="black" ,font=("Helvetica", 14), fg="orange")
splash_label.pack(pady=20)

splash_label = Label(splash_root,bg='black', text="Created by Yugaan, Dhanvi, Shaurya, Anmol", font=("Helvetica", 11),fg="orange")
splash_label.pack(pady=20)

canvas1 = Canvas(splash_root, width = 180, height = 300)
canvas1.pack()      
img1 = PhotoImage(file='c.png')      
canvas1.create_image(0,0, anchor=NW, image=img1)

my_progress = ttk.Progressbar(splash_root, orient=HORIZONTAL, length=300, mode='determinate')
my_progress.pack(pady=10)


prog_button = Button(splash_root, text="Start", command= lambda: step())
prog_button.pack()


def step():
   for x in range(5):
       my_progress['value']+= 20
       splash_root.update_idletasks()
       time.sleep(1)
       
   #Splash Screen Timer
   splash_root.after(500, main_window)
   
def main_window():
    splash_root.destroy()
    root = Tk()
    root.title("Main")
    root.geometry("180x300")
    root.resizable("False", "False")

    canvas = Canvas(root, width = 400, height = 370)
    canvas.pack()      
    img = PhotoImage(file='c.png')      
    canvas.create_image(0,0, anchor=NW, image=img)      


    my_menu = Menu(root)
    root.config(menu=my_menu)


    def grapher():
        Graphing_final.graph() 
    def calc():
        Scientific_final.go()
    def unit_convert():
        Converter_final.uc()
        

    file_menu = Menu(my_menu)
    my_menu.add_cascade(label="All", menu=file_menu)
    file_menu.add_command(label="Scientific Calculator", command= lambda:calc())
    file_menu.add_command(label="Grapher", command=lambda: grapher())
    file_menu.add_command(label="Converter", command=lambda: unit_convert())
    file_menu.add_command(label="Exit", command=root.destroy)
    root.mainloop()
splash_root.mainloop()