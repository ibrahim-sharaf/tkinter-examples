import tkinter as tk;

root = tk.Tk();
root.title("MyTitle")

farme = tk.Frame(root)
farme.pack()

button = tk.Button(farme, text="Hello")
button.pack()

root.mainloop()