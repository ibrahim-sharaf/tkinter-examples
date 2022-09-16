import tkinter as tk;
from tkinter import filedialog

root = tk.Tk();

root.title('Menu example')

menubar = tkinter = tk.Menu(root);
root.config(menu=menubar)


## claback functions
def browseFiles():
    path = filedialog.askopenfilename(initialdir ="./",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.txt*"),
                                                       ("all files",
                                                        "*.*")))
      
    print(path)
    

#File menu
file_menu = tk.Menu(menubar, tearoff=0)

file_menu.add_command(
	    label='Open',
	    command= browseFiles
	)

file_menu.add_command(
	    label='Exit',
	    command= root.destroy
	)

menubar.add_cascade(label="File", menu=file_menu)

root.mainloop();