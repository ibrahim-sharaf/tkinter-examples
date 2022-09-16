import tkinter as tk;

root = tk.Tk();
root.title("MyTitle")

farme = tk.Frame(root)
farme.pack()

def button_action():
	root.destroy();

button = tk.Button(farme, text="Exit", command=button_action)
button.pack()

root.mainloop()