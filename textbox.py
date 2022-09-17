import tkinter as tk

root = tk.Tk();
root.title("MyTitle")

root.geometry('500x300')

def submit_name():
	result.configure(text="hello "+ name_var.get())

#Adding Label
tk.Label(root, text="Write your name: ").grid(column=0,  row=0)

#Add textbox
name_var = tk.StringVar()

name_textbox = tk.Entry(root, width=30, textvariable= name_var)

name_textbox.grid(column=1, row=0)

name_textbox.focus()

tk.Button(root, text="Submit", command=submit_name).grid(column=3,  row=0)

result = tk.Label(root, text=" ")
result.grid(column=0,  row=2)

root.mainloop()