import tkinter as tk;

root = tk.Tk();

root.title('Menu example')

menubar = tkinter = tk.Menu(root);
root.config(menu=menubar)

#File menu
file_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)

#Edit menu
edit_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=edit_menu)

#Help menu
help_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=help_menu)

root.mainloop();