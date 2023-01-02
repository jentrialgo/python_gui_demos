from tkinter import Tk
import ttkbootstrap as ttk


def convert_clicked():
    result["text"] = str(bin(int(entry.get())))


def clear_clicked():
    result["text"] = ""
    entry.delete(first=0, last=ttk.END)


root = Tk()
title = ttk.Label(root, text="Convert decimal to binary").grid(row=0, column=0)

entry = ttk.Entry(root)
entry.grid(row=1, column=0)

ttk.Button(root, text="Convert", command=convert_clicked).grid(row=1, column=1)
ttk.Button(root, text="Clear", command=clear_clicked).grid(row=1, column=2)

result = ttk.Label(root)
result.grid(row=2, column=0)

root.mainloop()
