#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/10 18:47
# @File    : label控件.py
# @Software: PyCharm

import tkinter as tk

root = tk.Tk()
root.title("第一个窗口实体")       # 修改窗体的名字
root.geometry("300x160")        # 修改窗体的大小和位置

lb = tk.Label(root, text='i am a label', bg='pink', fg='black', width=15, relief='raised', pady=5)
lb.pack(pady=5)   # 之后会讲，这个是布局函数

root.mainloop()     # 进入窗体循环，等待事件
