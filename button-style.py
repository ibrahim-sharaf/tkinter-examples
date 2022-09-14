import tkinter as tk;

root = tk.Tk();
root.title("MyTitle")

farme = tk.Frame(root)
farme.pack()

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

button = tk.Button(farme, text="Exit")
getStyle(button, style)
button.pack()

root.mainloop()