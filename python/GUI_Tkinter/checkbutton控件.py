#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/10 20:52
# @File    : checkbutton控件.py
# @Software: PyCharm

import tkinter as tk
from tkinter.ttk import Checkbutton, Label, Button


def show_selection():
    selection="喜欢的城市是:"
    for i in check_boxes:
        if check_boxes[i].get():
            selection += country[i] + " "
    lb.config(text=selection)


root = tk.Tk()
root.title("checkbutton控件")
root.geometry("300x200")

lb = Label(root, text='这是预设，您还没有选择', background='lightyellow', width=30, anchor='center')
lb.pack(pady=5)

country = {0: "兰州", 1: "宁波", 2: "商丘", 3: "郑州"}
check_boxes = {}

for c in country:
    check_boxes[c] = tk.BooleanVar()
    Checkbutton(root, text=country[c], variable=check_boxes[c]).pack(pady=5)

btn = Button(root, text="确定", width=10, command=show_selection)
btn.pack()

root.mainloop()