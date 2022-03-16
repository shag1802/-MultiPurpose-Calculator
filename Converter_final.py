from tkinter import *
def uc():
    # Conversion factors
    unit_dict = {
        "cm" : 0.01,
        "m" : 1.0,
        "km": 1000.0,
        "feet": 0.3048,
        "miles": 1609.344,
        "inches": 0.0254,
        "yards":0.9144,
        "sq. m" : 1.0,
        "sq. km": 1000000.0,
        "acre": 4046.856,
        "sq. foot" : 0.0929,
        "cu. cm" : 0.001,
        "Litre" : 1.0,
        "degrees" : 0.0174,
        "radians" : 1,
        "ml" : 0.001,
        "gallons": 3.785,
        "US Dollar":72.60,
        "Euro":86.37,
        "Japanese Yen":0.66,
        "British Pound":100.96,
        "INR":1,
        "AU Dollar":56.03,
        "Russian Ruble":0.99

    }
        
    lengths = ["cm", "m", "km", "feet", "miles", "inches","yards"]
    temps = ["Celsius", "Fahrenheit","Kelvin"]
    areas = ["sq. m", "sq. km","acre", "sq. foot"]
    volumes = ["cu. cm", "Litre", "ml", "gallon"]
    angles=["degrees", "radians"]
    currencies = ["US Dollar","Euro","Japanese Yen","British Pound","INR","AU Dollar","Russian Ruble"]

    # Options for drop-down menu
    OPTIONS = ["select units",
                ["cm",
                "m",
                "km",
                "feet",
                "miles",
                "inches",
                "yards"],
                ["Celsius",
                "Fahrenheit",
                "Kelvin"],
                ["degrees",
                 "radians"],
                ["sq. m",
                "sq. km",
                "acre",
                "sq. foot"],
                ["cu. cm",
                "Litre",
                "ml",
                "gallons"],
                ["US Dollar",
                "Euro",
                "Japanese Yen",
                "British Pound",
                "INR",
                "AU Dollar",
                "Russian Ruble"]]

    # Main window
    root = Tk()
    root.geometry("420x350")
    root.title("Unit Converter")
    root.resizable("False", "False")
    root['bg'] = 'black'

    my_menu = Menu(root)
    root.config(menu=my_menu)

    file_menu = Menu(my_menu)
    my_menu.add_cascade(label="All", menu=file_menu)
    file_menu.add_command(label="Length", command=lambda: convert(1))
    file_menu.add_command(label="Temp", command=lambda: convert(2))
    file_menu.add_command(label="Angles", command=lambda: convert(3))
    file_menu.add_command(label="Area", command=lambda: convert(4))
    file_menu.add_command(label="Volume", command=lambda: convert(5))
    file_menu.add_command(label="Currency", command=lambda: convert(6))
    


    def ok():
        inp = float(inputentry.get())
        inp_unit = inputopt.get()
        out_unit = outputopt.get()

        cons = [inp_unit in lengths and out_unit in lengths,
        inp_unit in temps and out_unit in temps,
        inp_unit in angles and out_unit in angles,       
        inp_unit in areas and out_unit in areas,
        inp_unit in volumes and out_unit in volumes,
        inp_unit in currencies and out_unit in currencies]

        if any(cons): # If both the units are of same type, do the conversion
            if inp_unit == "Celsius" and out_unit == "Fahrenheit":
                outputentry.delete(0, END)
                outputentry.insert(0, (inp * 1.8) + 32)
            elif inp_unit == "Fahrenheit" and out_unit == "Celsius":
                outputentry.delete(0, END)
                outputentry.insert(0, (inp - 32) * (5/9))
            elif inp_unit == "Kelvin" and out_unit == "Celsius":
                outputentry.delete(0, END)
                outputentry.insert(0, (inp - 273.150))
            elif inp_unit == "Celsius" and out_unit == "Kelvin":
                outputentry.delete(0, END)
                outputentry.insert(0, (inp +273.15))
            elif inp_unit == "Kelvin" and out_unit == "Fahrenheit":
                outputentry.delete(0, END)
                outputentry.insert(0, (inp - 273.15)*((9/5)+32))
            elif inp_unit == "Fahrenheit" and out_unit == "Kelvin":
                outputentry.delete(0, END)
                outputentry.insert(0, (inp - 32) * (5/9)+273.15)
            else:
                outputentry.delete(0, END)
                outputentry.insert(0, round(inp * unit_dict[inp_unit]/unit_dict[out_unit], 5))

        else: # Display error if units are of different types
            outputentry.delete(0, END)
            outputentry.insert(0, "ERROR")

    inputopt = StringVar()
    inputopt.set(OPTIONS[0])

    outputopt = StringVar()
    outputopt.set(OPTIONS[0])

    # Widgets
    def convert(i):
        inputlabel = Label(root, text = "Input",font ="bold",background="black",foreground="orange")
        inputlabel.grid(row = 0, column = 0, pady = 20)
        
        global inputentry
        inputentry = Entry(root, justify = "center", font = "bold")
        inputentry.grid(row = 1, column = 0, padx = 35, ipady = 5)

        inputmenu = OptionMenu(root, inputopt, *OPTIONS[i])
        inputmenu.grid(row = 1, column = 1)
        inputmenu.config(font = "Arial 10")

        outputlabel = Label(root, text = "Output",font="bold",background="black",foreground="orange")
        outputlabel.grid(row = 2, column = 0, pady = 20)
        
        global outputentry
        outputentry = Entry(root, justify = "center", font = "bold")
        outputentry.grid(row = 3, column = 0, padx = 35, ipady = 5)

        outputmenu = OptionMenu(root, outputopt, *OPTIONS[i])
        outputmenu.grid(row = 3, column = 1)
        outputmenu.config(font = "Arial 10")

        okbtn = Button(root, text = "Convert", command = ok, padx = 80, pady = 2,background="black",foreground="orange")
        okbtn.grid(row = 4, column = 0, columnspan = 2, pady = 50)

   
    root.mainloop()
    
if __name__=="__main__":
    uc()