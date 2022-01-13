import tkinter as ttk
from tkinter.constants import COMMAND

window = ttk.Tk() #crea la ventana
# window2 =ttk.Tk()

window.title("Calculator") # titulo de la ventana principal
window.geometry("750x600") # tamaño de la ventana principal

def button_click(button_content):
    current_value = display_text.get()
    next_value = current_value + button_content
    display_text.set(next_value)

def solve():
    current_value = display_text.get()
    result = str(eval(current_value))
    display_text.set(result)


def clear_display():
    display_text.set("")

display_text = ttk.StringVar()

# button1= ttk.Button(window, text="Hola mundo" )
# button1.grid(row = 0, column=0)

# button2 = ttk.Button(window, text="Botton 2")
# button2.grid(row = 1, column=1)

display_frame = ttk.Frame(window, width= 500, height=100, bg = "Black")  # Crea un frame el cual colocamos dentro de la ventana 1
display_frame.pack(side=ttk.TOP)

#Crea un epacio vacio, aqui colocaremos nuestro espacio, este se encuenta dentro del frame anterior 
input_field = ttk.Entry(display_frame, width = 83, bg="#eee", justify= ttk.RIGHT,textvariable= display_text) 
input_field.grid(row=0, column=0)
input_field.pack(padx= 2, pady= 2)


#creamos el Frame para los botones
buttons_frame = ttk.Frame(window, width= 500, height=1000, bg="red")
# buttons_frame.pack(side=ttk.BOTTOM)
buttons_frame.pack()

erase_button = ttk.Button(buttons_frame, text="C", bg= "blue", cursor="hand2", width= 35, height= 5, command= clear_display)
erase_button.grid(row=0, column=0, columnspan= 3, padx= 5, pady=5)

divide_button = ttk.Button(buttons_frame, text="/", bg= "blue", cursor="hand2", width= 10, height= 5, command= lambda:button_click("/"))
divide_button.grid(row=0, column=3, columnspan= 1, padx=5, pady=5)

seven_button = ttk.Button(buttons_frame, text="7", bg= "blue", cursor="hand2", width= 10, height= 5, command= lambda:button_click("7"))
seven_button.grid(row=1, column=0, columnspan= 1, padx=5, pady=5)
eigth_button = ttk.Button(buttons_frame, text="8", bg= "blue", cursor="hand2", width= 10, height= 5, command= lambda:button_click("8"))
eigth_button.grid(row=1, column=1, columnspan= 1, padx=5, pady=5)
nine_button = ttk.Button(buttons_frame, text="9", bg= "blue", cursor="hand2", width= 10, height= 5, command= lambda:button_click("9"))
nine_button.grid(row=1, column=2, columnspan= 1, padx=5, pady=5)
multiplication_button = ttk.Button(buttons_frame, text="*", bg= "blue", cursor="hand2", width= 10, height= 5, command= lambda:button_click("*"))
multiplication_button.grid(row=1, column=3, columnspan= 1, padx=5, pady=5)

four_button = ttk.Button(buttons_frame, text="4", bg= "blue", cursor="hand2", width= 10, height= 5, command= lambda:button_click("4"))
four_button.grid(row=2, column=0, columnspan= 1, padx=5, pady=5)
five_button = ttk.Button(buttons_frame, text="5", bg= "blue", cursor="hand2", width= 10, height= 5, command= lambda:button_click("5"))
five_button.grid(row=2, column=1, columnspan= 1, padx=5, pady=5)
six_button = ttk.Button(buttons_frame, text="6", bg= "blue", cursor="hand2", width= 10, height= 5, command= lambda:button_click("6"))
six_button.grid(row=2, column=2, columnspan= 1, padx=5, pady=5)
minus_button = ttk.Button(buttons_frame, text="-", bg= "blue", cursor="hand2", width= 10, height= 5, command= lambda:button_click("-"))
minus_button.grid(row=2, column=3, columnspan= 1, padx=5, pady=5)

one_button = ttk.Button(buttons_frame, text="1", bg= "blue", cursor="hand2", width= 10, height= 5, command= lambda:button_click("1"))
one_button.grid(row=3, column=0, columnspan= 1, padx=5, pady=5)
two_button = ttk.Button(buttons_frame, text="2", bg= "blue", cursor="hand2", width= 10, height= 5, command= lambda:button_click("2"))
two_button.grid(row=3, column=1, columnspan= 1, padx=5, pady=5)
three_button = ttk.Button(buttons_frame, text="3", bg= "blue", cursor="hand2", width= 10, height= 5, command= lambda:button_click("3"))
three_button.grid(row=3, column=2, columnspan= 1, padx=5, pady=5)
plus_button = ttk.Button(buttons_frame, text="+", bg= "blue", cursor="hand2", width= 10, height= 5, command= lambda:button_click("+"))
plus_button.grid(row=3, column=3, columnspan= 1, padx=5, pady=5)

zero_button = ttk.Button(buttons_frame, text="0", bg= "blue", cursor="hand2", width= 25, height= 5, command= lambda:button_click("0"))
zero_button.grid(row=4, column=0, columnspan= 2, padx=5, ipady=5)
dot_button = ttk.Button(buttons_frame, text=".", bg= "blue", cursor="hand2", width= 10, height= 5, command= lambda:button_click("."))
dot_button.grid(row=4, column=2, columnspan= 1, padx=5, ipady=5)
equal_button = ttk.Button(buttons_frame, text="=", bg= "blue", cursor="hand2", width= 10, height= 5, command= solve)
equal_button.grid(row=4, column=3, columnspan= 1, padx=5, ipady=5)

window.mainloop()