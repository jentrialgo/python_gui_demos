import sys
from threading import Thread
import tkinter as tk

import customtkinter

sys.path.insert(0, "../../..")
import demos_res.rest_mock.rest_mock as rest_mock

# We need a thread for updating the progress bar without halting the GUI thread
class UserDownload(Thread):
    def __init__(self):
        super().__init__()
        self.response = ""

    def run(self):
        self.response = rest_mock.get_users()


def monitor(thread):
    if thread.is_alive():
        root.after(100, lambda: monitor(thread))
    else:
        for user in thread.response["users"]:
            text = user["firstName"] + " " + user["lastName"]
            list_box.insert(0, text)

        progress_bar.stop()
        progress_bar.grid_forget()


def get_users_clicked():
    progress_bar.grid(row=3, column=0, columnspan=2)
    progress_bar.start()

    download_thread = UserDownload()
    download_thread.start()

    monitor(download_thread)


root = customtkinter.CTk()
title = customtkinter.CTkLabel(root, text="Rest consumer").grid(row=0, column=0)

customtkinter.CTkButton(root, text="Get users", command=get_users_clicked).grid(
    row=1, column=0
)

# Notice that CustomTkinter doesn't have a custom list box and tk's one has to
# be used
list_box = tk.Listbox(root)
list_box.grid(row=2, column=0)

progress_bar = customtkinter.CTkProgressBar(
    root, orientation="horizontal", mode="indeterminate", width=100
)
progress_bar.grid(row=3, column=0, columnspan=2)
progress_bar.grid_forget()

root.mainloop()
