import tkinter as tk
from tkinter.filedialog import askopenfilename

def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Text Editor Application - {filepath}")

def cut():
    txt_edit.event_generate("<<Cut>>")
def copy():
    txt_edit.event_generate("<<Copy>>")
def paste():
    txt_edit.event_generate("<<Paste>>")

window = tk.Tk()
window.title("Suhas Text Editor")
window.rowconfigure(0, minsize=600, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

#buttons name and function connection
txt_edit = tk.Text(window)
fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
btn_cut  = tk.Button(fr_buttons, text="Cut", command=cut)
btn_copy = tk.Button(fr_buttons, text="Copy", command=copy)
btn_paste= tk.Button(fr_buttons, text="Paste", command=paste)

#buttons display grid
btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_cut.grid(row=2,column=0,sticky="ew",padx=5, pady=5)
btn_copy.grid(row=3,column=0,sticky="ew",padx=5, pady=5)
btn_paste.grid(row=4,column=0,sticky="ew",padx=5, pady=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()