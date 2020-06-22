#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/10 20:38
# @File    : radiobutton.py
# @Software: PyCharm

import tkinter as tk
from tkinter.ttk import Radiobutton, Label


def show_selection():
    num = var.get()     # get的值就是value的值，所以必须设置variable属性

    if num == 1:
        lb.config(text="我是男生")
    else:
        lb.config(text="我是女生")


root = tk.Tk()
root.title("radiobutton的用法")

# anchor用来控制文本的显示位置，默认是居左
lb = Label(root, text='这是预设， 你还没有选择', background='lightyellow', width=30, anchor='center')
lb.pack(pady=5)

var = tk.IntVar()
var.set(0)

rb1 = Radiobutton(root, text='我是男生', variable=var, value=1, command=show_selection)
rb2 = Radiobutton(root, text='我是女生', variable=var, value=2, command=show_selection)

rb1.pack()
rb2.pack(pady=5)

root.mainloop()