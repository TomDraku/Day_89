import tkinter as tk
import time


def delate_if_notwritten():
    global last_text
    current_text = editor.get('1.0', 'end-1c')
    if current_text == last_text:
        editor.delete('1.0', 'end')
    else:
        last_text = current_text
    editor.after(5000, delate_if_notwritten)

top = tk.Tk()
top.geometry("400x450")

empty_label = tk.Label(top, text="")
empty_label.grid(row=0,column=0)

empty_label2 = tk.Label(top, text="")
empty_label2.grid(row=0,column=2)

title = tk.Label(top, text="Write your text below, but do not stop becouse your text will disappear")
title.grid(row=0, column=1)

editor = tk.Text(top, font=('Arial', 12), width=30, height=15)
editor.grid(row=1, column=1)

last_text = ""
editor.after(5000, delate_if_notwritten)


top.mainloop()