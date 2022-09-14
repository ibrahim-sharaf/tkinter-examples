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

onEnterStye = {
	'bg': 'blue'
}

onLeaveStye = {
	'bg': '#224499'
}

def onEnter(e):
	getStyle(e.widget, onEnterStye)

def onLeave(e):
	getStyle(e.widget, onLeaveStye)

button = tk.Button(farme, text="Exit")
getStyle(button, style)

#onhover effect
button.bind("<Enter>", onEnter)
button.bind("<Leave>", onLeave)

button.pack()

root.mainloop()