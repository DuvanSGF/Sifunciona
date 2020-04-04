# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 22:03:18 2018

@author: Mr Mejia
"""
from tkinter import *
import random
import time

tk = Tk()
tk.title("Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()
