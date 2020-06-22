#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/10 19:15
# @File    : button控件.py
# @Software: PyCharm

import tkinter as tk
from tkinter.ttk import Button


def change_color(color):
    root.config(bg=color)


root = tk.Tk()
root.title("button控件")
root.geometry("300x160")

btn1 = Button(root, text='blue', command=lambda: change_color('blue'))
btn1.pack(pady=5)

btn2 = Button(root, text='green', command=lambda: change_color('green'))
btn2.pack()

btn3 = Button(root, text='red', command=lambda: change_color('red'))
btn3.pack(pady=5)

root.mainloop()