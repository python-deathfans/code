#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/10 18:58
# @File    : entry控件.py
# @Software: PyCharm

import tkinter as tk
from tkinter.ttk import Entry, Label

root = tk.Tk()
root.title("entry控件")
root.geometry("300x160")

Label(root, text='Name:').grid(row=0)
Label(root, text='Pwd:').grid(row=1)

var1 = tk.StringVar()
var2 = tk.StringVar()

entry1 = Entry(root, textvariable=var1, show="$")
entry2 = Entry(root, textvariable=var2, show="$")

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)
entry1.focus_set()

root.mainloop()