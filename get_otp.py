# -*- coding: utf-8 -*-
import tkinter as tk
import pyotp


def getOTP(secretstr):
    return pyotp.TOTP(secretstr).now()


def refreshOTP():
    textotp.delete(0.0, tk.END)
    textotp.insert(tk.INSERT, r'堡垒机OTP  ' + getOTP('B4T6KFBJHKX3AR5EDV5KABBFHK2UAZKZ'))
    textotp.update()
    windows.after(500, refreshOTP)


windows = tk.Tk()
windows.geometry('200x70')
textotp = tk.Text(windows, width=200, height=100)
textotp.configure(font=("Microsoft YaHei", 15))
textotp.pack()
windows.after(500, refreshOTP)
windows.mainloop()
