import tkinter as tk

root = tk.Tk()
root.title("Hello World")
root.geometry("300x200")
label = tk.Label(root, text="Hello World")
label.pack()
root.mainloop()