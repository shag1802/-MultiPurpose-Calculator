from tkinter import *
from math import *

STEP_SIZE = 0.001
ASYMPTOTE = 2.0
formula = "x+sin(x)"
def graph():
    btn_params1 = {
            'padx': 18,
            'pady': 1,
            'bd': 4,
            'fg': 'white',
            'bg': '#003040',
            'font': ('arial', 18),
            'width': 2,
            'height': 1,
            'relief': 'raise',
            'activebackground': "#aadd1d"
        }
    btn_params2 = {
            'padx': 18,
            'pady': 1,
            'bd': 4,
            'fg': 'black',
            'bg': '#9d9d9d',
            'font': ('arial', 18),
            'width': 2,
            'height': 1,
            'relief': 'ridge',
            'activebackground': "#9d9d9d"
        }
    def print_formula(pre_text):
        Label(root, text=pre_text + " f(x) = " + formula, relief=SUNKEN,bg="#addd1d",
            width=1,font="18").grid(row=1, column=0, columnspan=5, sticky=W + E)


    def translate(x_current, y_current):
        tc = [0, 0]
        x_mul = int(canvas["width"]) / (8 * 2)
        y_mul = (int(canvas["height"]) / (8 * -2))
        x_current = (x_current + 8) * x_mul
        y_current = (y_current + 8) * y_mul + int(canvas["height"])
        tc[0] = x_current
        tc[1] = y_current
        return tc


    def draw_line(x1, y1, x2, y2, colour):
        from_coord = translate(x1, y1)
        to_coord = translate(x2, y2)
        if ((y2 - y1 > 8 * ASYMPTOTE) or (y1 - y2 > 8 * ASYMPTOTE)):
            from_coord = to_coord
        canvas.create_line(from_coord[0], from_coord[1], to_coord[0], to_coord[1], fill=colour)


    def draw_grid():
        draw_line(8 * -1, 0, 8, 0, "darkgray")
        draw_line(0, 8 * -1, 0, 8, "darkgray")


    def draw_graph(event):
        canvas.delete("all")
        draw_grid()
        y_previous = 0.0
        x = 8 * -1
        while x <= 8:
            try:
                y = eval(formula)
            except ValueError:
                y = 1000000000
                x = STEP_SIZE * 8
                if eval(formula) < 0:
                    y *= -1
            except:
                print_formula("SYNTAX ERROR   ")
                break
            draw_line(x - STEP_SIZE * 8, y_previous, x, y, "#003040")
            y_previous = y
            x += STEP_SIZE * 8


    def append_formula(thing):
        global formula
        formula += thing
        print_formula("")


    def clear_formula():
        global formula
        while formula != "":
            delete_formula()
        print_formula("")


    def delete_formula():
        global formula
        formula = formula[:-1]
        print_formula("")


    def correct_ending_no_number(name):
        return name.endswith('x') or name.endswith('e') or name.endswith(')')


    def correct_ending(thing):
        return thing[-1:].isdigit() or correct_ending_no_number(thing)


    def append_asterisk(thing):
        global formula
        if correct_ending(formula):
            if thing == "**":
                formula += thing
            else:
                formula += "*" + thing
        else:
            formula += thing
        print_formula("")

    def append_number_formula(thing):
        global formula
        if correct_ending_no_number(formula) and thing.isdigit():
            formula += "*"
        formula += thing
        print_formula("")

    root = Tk()

    root.wm_title("Graphing Calculator")
    root.resizable(width=False, height=False)
    root['bg'] = '#eeeedd'
    root.geometry("388x653")

    canvas = Canvas(root)

    print_formula("")

    #row2
    Button(root, text="sin", command=lambda: append_asterisk("sin("),**btn_params1).grid(row=2, column=0)
    Button(root, text="e", command=lambda: append_asterisk("e",),**btn_params1).grid(row=2, column=1)
    Button(root, text="(", command=lambda: append_asterisk("("),**btn_params1).grid(row=2, column=2)
    Button(root, text=")", command=lambda: append_formula(")"),**btn_params1).grid(row=2, column=3)
    Button(root, text="log", command=lambda: append_asterisk("log10("),**btn_params1).grid(row=2, column=4)
    
    #row3
    Button(root, text="cos", command=lambda: append_asterisk("cos("),**btn_params1).grid(row=3, column=0)
    btn_x=Button(root, text="x", command=lambda: append_asterisk("x"),**btn_params2)
    btn_x.grid(row=3, column=1)
    btn_x.configure(bg='#ff9900', activebackground='#ffaa00', relief ='raise')
    Button(root, text="ln", command=lambda: append_asterisk("log("),**btn_params1).grid(row=3, column=2)
    btn_enter = Button(root, text="Enter",**btn_params2)
    btn_enter.bind('<Button-1>', draw_graph)
    btn_enter.grid(row=3, column=3)
    btn_enter.configure(bg='#ff9900', activebackground='#ffaa00', relief ='raise')
    Button(root, text=".", command=lambda: append_formula("."),**btn_params1).grid(row=3, column=4)
    
    #row4
    Button(root, text="tan", command=lambda: append_asterisk("tan("),**btn_params1).grid(row=4, column=0)
    Button(root, text="1", command=lambda: append_number_formula("1"),**btn_params2).grid(row=4, column=1)
    Button(root, text="2", command=lambda: append_number_formula("2"),**btn_params2).grid(row=4, column=2)
    Button(root, text="3", command=lambda: append_number_formula("3"),**btn_params2).grid(row=4, column=3)
    Button(root, text="+", command=lambda: append_asterisk("+"),**btn_params1).grid(row=4, column=4)

    #row5
    Button(root, text="sinh", command=lambda: append_asterisk("sinh("),**btn_params1).grid(row=5, column=0)
    Button(root, text="4", command=lambda: append_number_formula("4"),**btn_params2).grid(row=5, column=1)
    Button(root, text="5", command=lambda: append_number_formula("5"),**btn_params2).grid(row=5, column=2)
    Button(root, text="6", command=lambda: append_number_formula("6"),**btn_params2).grid(row=5, column=3)
    Button(root, text="-", command=lambda: append_asterisk("-"),**btn_params1).grid(row=5, column=4)

    #row6
    Button(root, text="cosh", command=lambda: append_asterisk("cosh("),**btn_params1).grid(row=6, column=0)
    Button(root, text="7", command=lambda: append_number_formula("7"),**btn_params2).grid(row=6, column=1)
    Button(root, text="8", command=lambda: append_number_formula("8"),**btn_params2).grid(row=6, column=2)
    Button(root, text="9", command=lambda: append_number_formula("9"),**btn_params2).grid(row=6, column=3)
    Button(root, text="*", command=lambda: append_formula("*"),**btn_params1).grid(row=6, column=4)

    #row7
    Button(root, text="tanh", command=lambda: append_asterisk("tanh("),**btn_params1).grid(row=7, column=0)
    btn_delete = Button(root, text="Delete", command=lambda: delete_formula(),**btn_params2)
    btn_delete.grid(row=7, column=1)
    btn_delete.configure(bg='#ff9900', activebackground='#ffaa00', relief ='raise')
    Button(root, text="0", command=lambda: append_number_formula("0"),**btn_params2).grid(row=7, column=2)
    btn_clear=Button(root, text="Clear", command=lambda: clear_formula(),**btn_params2)
    btn_clear.grid(row=7, column=3)
    btn_clear.configure(bg='#ff9900', activebackground='#ffaa00', relief ='raise')
    Button(root, text="/", command=lambda: append_formula("/"),**btn_params1).grid(row=7, column=4)
    
    #row8
    Button(root, text="^", command=lambda: append_asterisk("**"),**btn_params1).grid(row=8, column=4)
    Button(root, text="π", command=lambda: append_asterisk("pi"),**btn_params1).grid(row=8, column=0)

    Label(root,text="Graphing Calculator",bd=4,relief="sunken",bg="#aadd1d",fg='black',font="18,arial",padx=18,pady=5,width=21,height=2).grid(row=8,column=1,columnspan=3)

    canvas.grid(row=0, column=0, columnspan=5)
    draw_grid()
    draw_graph("event")
    root.mainloop()

if __name__=="__main__":
    graph()