import tkinter as tk;

root = tk.Tk();

root.title('Menu example')

menubar = tkinter = tk.Menu(root);
root.config(menu=menubar)


## claback functions

def do_new():
	print("do new")

def do_open():
	print("do open")
    

#File menu
file_menu = tk.Menu(menubar, tearoff=0)

file_menu.add_command(
	    label='new',
	    command= do_new
	)

file_menu.add_command(
	    label='Open',
	    command= do_open
	)

menubar.add_cascade(label="File", menu=file_menu)



#Edit menu
edit_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=edit_menu)

#Help menu
help_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=help_menu)

root.mainloop();