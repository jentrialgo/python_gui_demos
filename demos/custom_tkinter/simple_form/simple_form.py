import tkinter as tk
import customtkinter


def convert_clicked():
    result.configure(text=str(bin(int(entry.get()))))


def clear_clicked():
    result.configure(text="")
    entry.delete(first_index=0, last_index=tk.END)


root = customtkinter.CTk()
title = customtkinter.CTkLabel(root, text="Convert decimal to binary").grid(
    row=0, column=0
)

entry = customtkinter.CTkEntry(root)
entry.grid(row=1, column=0)

customtkinter.CTkButton(root, text="Convert", command=convert_clicked).grid(
    row=1, column=1
)
customtkinter.CTkButton(root, text="Clear", command=clear_clicked).grid(row=1, column=2)

result = customtkinter.CTkLabel(root, text="")
result.grid(row=2, column=0)

root.mainloop()
