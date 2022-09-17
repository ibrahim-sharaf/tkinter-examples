import tkinter as tk
from tkinter import ttk

root = tk.Tk();
root.title("MyTitle")

root.geometry('500x300')

def submit_programing_language():
	result.configure(text="You chose "+ programing_language.get())

#Adding Label
tk.Label(root, text="Choose a programing language: ").grid(column=0,  row=0)

#Add textbox
programing_language = tk.StringVar()

programing_language_combobox = ttk.Combobox(root, width=30, state='readonly',textvariable= programing_language)

programing_language_combobox["values"] = ["c", "c++", "Java", "Python", "PHP", "Go", "Javascript"]

programing_language_combobox.grid(column=1, row=0)

programing_language_combobox.current(0)

tk.Button(root, text="Submit", command=submit_programing_language).grid(column=3,  row=0)

result = tk.Label(root, text=" ")
result.grid(column=0,  row=2)

root.mainloop()