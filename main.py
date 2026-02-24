import tkinter as tk
from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk
import json
import xml.etree.ElementTree as ET
from lxml import etree

from sklearn import tree

# Tkinter configuration
root = tk.Tk()

root.title("Lego Universe AlphaDB Editor")
root.configure(background="#AFAFAF")
root.minsize(500, 500)
root.maxsize(700, 700)
root.geometry("650x650+50+50")

OBJECT_TYPES = ["Select object type", "Environmental", "Smashables"]

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
    
    db_path_entry.delete(0, END)
    db_path_entry.insert(0, db_filename)

def select_obj_path():
    obj_filename = fd.askopenfilename()
    print(obj_filename)

    obj_path_entry.delete(0, END)
    obj_path_entry.insert(0, obj_filename)


def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def display_object():
    clear_frame(display_frame)

    #testing XML parsing
    parser = etree.XMLParser(recover=True)
    tree = ET.parse(db_path_entry.get(), parser=parser)
    tree_root = tree.getroot()
    for child in tree_root:
        print(child.tag, child.attrib)

    print("made it here")
    pass


def aggregate_row():
    pass




# GUI Elements
main_frame = tk.Frame(root, width=600, height=600, bg="grey")
main_frame.pack(padx=30)
center_frame = tk.Frame(main_frame, width=600, height=600, bg="grey")
center_frame.pack(padx=20, pady=30)

db_frame = tk.Frame(center_frame, width=600, height=100, bg="grey")
db_frame.pack(pady=20)

db_path_button = tk.Button(db_frame, text="Select path to ivantest.xml", command=select_db_path)
db_path_button.pack(side=BOTTOM, pady=10)

db_path_label = Label(db_frame, text="Database Path:", bg="grey", fg="white")
db_path_label.pack(side=LEFT)
db_path_entry = Entry(db_frame, bd =2, width=200)
db_path_entry.pack(side = RIGHT)
db_path_entry.insert(0, db_filename)
db_path_entry.bind("<Leave>", lambda event: save_json("db_path", db_path_entry.get()))


obj_frame = tk.Frame(center_frame, width=600, height=100, bg="grey")
obj_frame.pack(pady=10)

obj_path_button = tk.Button(obj_frame, text="Select path to .nif object file", command=select_obj_path)
obj_path_button.pack(side=BOTTOM, pady=10)
obj_path_label = Label(obj_frame, text=".nif Object Path:", bg="grey", fg="white")
obj_path_label.pack(side=LEFT)
obj_path_entry = Entry(obj_frame, bd =2, width=200)
obj_path_entry.pack(side = RIGHT)

obj_type_var = tk.StringVar(root)
obj_type_var.set(OBJECT_TYPES[0])

obj_menu = ttk.OptionMenu(center_frame, obj_type_var, *OBJECT_TYPES, command=lambda _: display_object())
obj_menu.pack(pady=20,)


display_frame = tk.Frame(center_frame, width=600, height=100, bg="grey")
display_frame.pack(pady=20)




root.mainloop()