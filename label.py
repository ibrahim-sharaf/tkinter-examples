import tkinter as tk

root = tk.Tk();
root.title("MyTitle")

#Adding Label
tk.Label(root, text="Hello Wrold").grid(column=0,  row=0)

tk.Label(root, text="Hello Wrold").grid(column=1,  row=0)

tk.Label(root, text="Hello Wrold").grid(column=1,  row=1)



root.mainloop()