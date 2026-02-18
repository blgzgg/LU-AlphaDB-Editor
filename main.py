import tkinter as tk
from tkinter import *
from tkinter import filedialog as fd
import json

# Tkinter configuration
root = tk.Tk()

root.title("Lego Universe AlphaDB Editor")
root.configure(background="#AFAFAF")
root.minsize(500, 500)
root.maxsize(700, 700)
root.geometry("650x650+50+50")

# Load paths from JSON
with open("data/paths.json", "r") as f:
    paths = json.load(f)

db_filename = paths.get("db_path", "")


# Functions
def save_json(json_data, filename):
    paths[json_data] = filename
    with open("data/paths.json", "w") as f:
        json.dump(paths, f, indent=4)

def select_db_path():
    db_filename = fd.askopenfilename()
    print(db_filename)

    #save path to JSON
    save_json("db_path", db_filename)
    
    E1.delete(0, END)
    E1.insert(0, db_filename)




# GUI Elements
main_frame = tk.Frame(root, width=600, height=600, bg="grey")
main_frame.pack(padx=30)
center_frame = tk.Frame(main_frame, width=600, height=600, bg="grey")
center_frame.pack(padx=20, pady=30)

db_path_button = tk.Button(center_frame, text="Select path to ivantest.xml", command=select_db_path)
db_path_button.pack()

L1 = Label(center_frame, text="Database Path:", bg="grey", fg="white")
L1.pack( side = LEFT)
E1 = Entry(center_frame, bd =2, width=200)
E1.pack(side = RIGHT)
E1.insert(0, db_filename)
E1.bind("<Leave>", lambda event: save_json("db_path", E1.get()))




root.mainloop()


