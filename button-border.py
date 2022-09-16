import tkinter as tk;

root = tk.Tk();
root.title("MyTitle")

frame = tk.Frame(root)
frame.pack()

def getStyle(widget, style):
	for key in style:
		widget[key] = style[key]


style = {
	'background': '#224499',
	'fg': 'red',
	'justify': 'left',
	'relief': 'flat',
	'cursor': "hand2",
	'font': 'Century 16 bold',
	'bd': 0
	
}

buttonPressedStyle = {
	'activebackground': 'green',
	'activeforeground': 'red',
	'bd': 0
}

def buttonPressed(e):
	getStyle(e.widget, buttonPressedStyle)


button_border = tk.Frame(frame, highlightbackground='red', highlightthickness=1)
button_border.pack()

button = tk.Button(button_border, text="Exit")
getStyle(button, style)

#onhover effect
button.bind('<ButtonPress-1>', buttonPressed)

button.pack()

root.mainloop()