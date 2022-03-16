from tkinter import *
from math import *
convert_constant = 1
inverse_convert_constant = 1

def go():
    root= Tk()
    btn_params1 = {
        'padx': 16,
        'pady': 1,
        'bd': 4,
        'fg': 'white',
        'bg': '#003040',
        'font': ('arial', 18),
        'width': 2,
        'height': 2,
        'relief': 'raise',
        'activebackground': "#aadd1d"
    }
    btn_params2 = {
        'padx': 16,
        'pady': 1,
        'bd': 4,
        'fg': 'black',
        'bg': '#9d9d9d',
        'font': ('arial', 18),
        'width': 2,
        'height': 2,
        'relief': 'ridge',
        'activebackground': "#9d9d9d"
    }
    #class 
    class Calculator:
        def __init__(self, master):
            self.exp=""
            self.expression=""
            self.sum_up =""
            self.master=master
    b = Calculator(root)

    #top frame
    top_frame = Frame(root, width=650, height=20, bd=4, relief='flat', bg='#666666')
    top_frame.pack(side=TOP)
    my_item = Label(top_frame, text="SCI CALCULATOR" ,font=('arial', 14), fg='white', width=650, bg='#000000')
    my_item.pack()
    txt_display = Entry(top_frame, font=('arial', 36),bg='#002030', fg='white', width=650,bd=15, justify='right')
    txt_display.pack()

   #functions to be used
    
    def btn_equal():

        def fsin(arg):
            return sin(arg * convert_constant)


        def fcos(arg):
            return cos(arg * convert_constant)


        def ftan(arg):
            return tan(arg * convert_constant)


        def arcsin(arg):
            return inverse_convert_constant * (asin(arg))


        def arccos(arg):
            return inverse_convert_constant * (acos(arg))


        def arctan(arg):
            return inverse_convert_constant * (atan(arg))
        
        
        def fsinh(arg):
            return sinh(arg * convert_constant)


        def fcosh(arg):
            return cosh(arg * convert_constant)


        def ftanh(arg):
            return tanh(arg * convert_constant)
        
        b.total = str(eval(b.expression))
        txt_display.delete(0, END)
        txt_display.insert(0, b.total)
        b.expression = b.total 

    
    def btn_click(expression_val):
        if len(b.expression) >= 23:
            b.expression = b.expression
            txt_display.delete(0, END)
            txt_display.insert(0, b.expression)
        else:
            b.expression = b.expression + str(expression_val)
            txt_display.delete(0, END)
            txt_display.insert(0, b.expression)

    def btn_clear():
        b.expression=""
        txt_display.delete(0,END)
        txt_display.insert(0,b.expression)
    
    def btn_delete():
        b.expression= b.expression[:-1]
        txt_display.delete(0,END)
        txt_display.insert(0,b.expression)

    def convert_deg():
        global convert_constant
        global inverse_convert_constant
        convert_constant = pi / 180
        inverse_convert_constant = 180 / pi
        btn_Rad["foreground"] = 'white'
        btn_Deg["foreground"] = '#aadd1d'

    def convert_rad():
        global convert_constant
        global inverse_convert_constant
        convert_constant = 1
        inverse_convert_constant = 1
        btn_Rad["foreground"] = '#aadd1d'
        btn_Deg["foreground"] = 'white'

    # set frame showing all buttons
    bottom_frame = Frame(root, width=650, height=500, bd=4, relief='flat', bg='#eeeedd')
    bottom_frame.pack(side=BOTTOM)

#row 0
    #factorial
    btn_factorial = Button(bottom_frame, **btn_params1, text="n!", command=lambda: btn_click('factorial('))
    btn_factorial.grid(row=0, column=0)
    #left brackets
    btn_lb = Button(bottom_frame, **btn_params1, text="(", command=lambda: btn_click('('))
    btn_lb.grid(row=0, column=1)
    #right bracket
    btn_rb = Button(bottom_frame, **btn_params1, text=")", command=lambda: btn_click(')'))
    btn_rb.grid(row=0, column=2)
    #clear
    btn_clear = Button(bottom_frame, **btn_params2, text="C", command=btn_clear)
    btn_clear.configure(bg='#ff9900', activebackground='#ffaa00', relief ='raise')
    btn_clear.grid(row=0, column=3)
    #pi
    btn_pi = Button(bottom_frame, **btn_params1, text="pi", command=lambda: btn_click('pi'))
    btn_pi.grid(row=0, column=4)
    #delete last
    btn_delete = Button(bottom_frame, **btn_params2, text="Del", command=btn_delete)
    btn_delete.configure(bg='#ff9900', activebackground='#ffaa00', relief ='raise')
    btn_delete.grid(row=0, column=5)
    #sqrt
    btn_sqrt = Button(bottom_frame, **btn_params1, text="sqrt", command=lambda: btn_click('sqrt('))
    btn_sqrt.grid(row=0, column=6)
    #e
    btn_e = Button(bottom_frame, **btn_params1, text="e", command=lambda:btn_click('e'))
    btn_e.grid(row=0, column=7)
    #tau
    btn_tau = Button(bottom_frame, **btn_params1, text="Tau", command=lambda:btn_click('tau'))
    btn_tau.grid(row=0, column=8)

#row 1
    #sine
    btn_sine = Button(bottom_frame, **btn_params1, text="sin", command=lambda: btn_click('fsin('))
    btn_sine.grid(row=1, column=0)
    #cosine
    btn_cosine = Button(bottom_frame, **btn_params1, text="cos", command=lambda: btn_click('fcos('))
    btn_cosine.grid(row=1, column=1)
    #tan
    btn_tan = Button(bottom_frame, **btn_params1, text="tan", command=lambda: btn_click('ftan('))
    btn_tan.grid(row=1, column=2)
    # one
    btn_1 = Button(bottom_frame, **btn_params2, text="1", command=lambda: btn_click(1))
    btn_1.grid(row=1, column=3)
    # two
    btn_2 = Button(bottom_frame, **btn_params2, text="2",command=lambda: btn_click(2) )
    btn_2.grid(row=1, column=4)
    # three
    btn_3 = Button(bottom_frame, **btn_params2, text="3", command=lambda: btn_click(3))
    btn_3.grid(row=1, column=5)
    #cube
    btn_cube = Button(bottom_frame, **btn_params1, text="cube", command=lambda: btn_click('**3'))
    btn_cube.grid(row=1, column=6)
    # multiplicaton
    btn_mult = Button(bottom_frame, **btn_params1, text="x", command=lambda: btn_click('*'))
    btn_mult.grid(row=1, column=7)
    #square
    btn_sq = Button(bottom_frame, **btn_params1, text="sq", command=lambda: btn_click('**2'))
    btn_sq.grid(row=1, column=8)

#row 2
    #sin_inverse
    btn_asine = Button(bottom_frame, **btn_params1, text="asin", command=lambda: btn_click('arcsin('))
    btn_asine.grid(row=2, column=0)
    #cos_inverse
    btn_acos = Button(bottom_frame, **btn_params1, text="acos", command=lambda: btn_click('arccos('))
    btn_acos.grid(row=2, column=1)
    #atan
    btn_atan = Button(bottom_frame, **btn_params1, text="atan", command=lambda: btn_click('arctan('))
    btn_atan.grid(row=2, column=2)
    #four
    btn_4 = Button(bottom_frame, **btn_params2, text="4", command=lambda: btn_click(4))
    btn_4.grid(row=2, column=3)
    #five
    btn_5 = Button(bottom_frame, **btn_params2, text="5", command=lambda: btn_click(5))
    btn_5.grid(row=2, column=4)
    #six
    btn_6 = Button(bottom_frame, **btn_params2, text="6", command=lambda: btn_click(6))
    btn_6.grid(row=2, column=5)
    #mod
    btn_mod = Button(bottom_frame, **btn_params1, text="mod", command=lambda: btn_click('abs('))
    btn_mod.grid(row=2, column=6)
    #divide
    btn_divide = Button(bottom_frame, **btn_params1, text="/", command=lambda: btn_click('/'))
    btn_divide.grid(row=2, column=7)
    #power
    btn_power = Button(bottom_frame, **btn_params1, text="x^y", command=lambda: btn_click('**'))
    btn_power.grid(row=2, column=8)
    

#row 3
#sin_hyperbolic
    btn_sinh= Button(bottom_frame, **btn_params1, text="sinh", command=lambda: btn_click('fsinh('))
    btn_sinh.grid(row=3, column=0)
    #cos_hyperbolic
    btn_cosh= Button(bottom_frame, **btn_params1, text="cosh", command=lambda: btn_click('fcosh('))
    btn_cosh.grid(row=3, column=1)
    #tan_hyperbolic
    btn_tanh= Button(bottom_frame, **btn_params1, text="tanh", command=lambda: btn_click('ftanh('))
    btn_tanh.grid(row=3, column=2)
    #seven
    btn_7 = Button(bottom_frame, **btn_params2, text="7", command=lambda: btn_click(7))
    btn_7.grid(row=3, column=3)
    #eight
    btn_8 = Button(bottom_frame, **btn_params2, text="8", command=lambda: btn_click(8))
    btn_8.grid(row=3, column=4)
    #nine
    btn_9 = Button(bottom_frame, **btn_params2, text="9", command=lambda: btn_click(9))
    btn_9.grid(row=3, column=5)
    #log
    btn_ln = Button(bottom_frame, **btn_params1, text="ln", command=lambda: btn_click('log('))
    btn_ln.grid(row=3, column=6)
    #subtract
    btn_subtract = Button(bottom_frame, **btn_params1, text="-", command=lambda: btn_click('-'))
    btn_subtract.grid(row=3, column=7)
    #exp
    btn_exp= Button(bottom_frame, **btn_params1, text="exp", command=lambda: btn_click('exp('))
    btn_exp.grid(row=3, column=8)
    
 #row 4 
    # changes trig function outputs to degrees
    btn_Deg = Button(bottom_frame, **btn_params1, text="Deg",command= convert_deg)
    btn_Deg.grid(row=4, column=0)
    # changes trig function outputs to default back to radians
    btn_Rad = Button(bottom_frame, **btn_params1, foreground='#aadd1d', text="Rad",command= convert_rad)
    btn_Rad.grid(row=4, column=1)
    #avogadro_const
    btn_avo = Button(bottom_frame, **btn_params1, text="Na", command=lambda: btn_click('6.0221409*(10**23)'))
    btn_avo.grid(row=4, column=2)
    # '.' Button
    btn_dot= Button(bottom_frame, **btn_params2, text=".", command=lambda: btn_click('.'))
    btn_dot.configure(bg='#ff9900', activebackground='#ffaa00', relief ='raise')
    btn_dot.grid(row=4, column=3)
    #zero
    btn_0 = Button(bottom_frame, **btn_params2, text="0", command=lambda: btn_click(0))
    btn_0.grid(row=4, column=4)
    # equals button
    btn_eq = Button(bottom_frame, **btn_params2, text="=", command=btn_equal)
    btn_eq.configure(bg='#ff9900', activebackground='#ffaa00', relief ='raise')
    btn_eq.grid(row=4, column=5)
    #ln
    btn_log = Button(bottom_frame, **btn_params1, text="log", command=lambda: btn_click('log10('))
    btn_log.grid(row=4, column=6)
    #addititon
    btn_add = Button(bottom_frame, **btn_params1, text="+", command=lambda: btn_click('+'))
    btn_add.grid(row=4, column=7)
    #expo_10
    btn_pow_10 = Button(bottom_frame, **btn_params1, text="10^", command=lambda: btn_click('10**'))
    btn_pow_10.grid(row=4, column=8)
    
    
 
    
    root.title("Scientific Calculator")
    root.geometry("655x520+150+100")
    root.resizable(False, False)
    root.mainloop()

if __name__=="__main__":
    go()