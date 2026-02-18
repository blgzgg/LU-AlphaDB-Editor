import tkinter as tk
from tkinter import filedialog as fd
import json

# Tkinter configuration
root = tk.Tk()

root.title("Lego Universe AlphaDB Editor")
root.configure(background="yellow")
root.minsize(200, 200)
root.maxsize(500, 500)
root.geometry("500x500+50+50")


# Functions
def select_db_path():
    db_filename = fd.askopenfilename()
    print(db_filename)


# GUI Elements
db_path_button = tk.Button(root, text="Select path to ivantest.xml", command=select_db_path)
db_path_button.pack()

tk.Label(root, text="Select path to ").pack()
tk.Label(root, text="- Maya Angelou").pack()



root.mainloop()


