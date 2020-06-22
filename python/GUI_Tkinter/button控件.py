#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/10 19:15
# @File    : button控件.py
# @Software: PyCharm

import tkinter as tk
from tkinter.ttk import Button, Label


def print_sth():
    lb.config(text="i love python")


root = tk.Tk()
root.title("button控件")
root.geometry("300x160")

lb = Label(root, background='pink', width=15, justify='center')
lb.pack(pady=5)

btn = Button(root, text='打印信息', command=print_sth)
btn.pack()

root.mainloop()