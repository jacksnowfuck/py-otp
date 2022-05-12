# -*- coding: utf-8 -*-
import tkinter as tk
import pyotp

sec_str = 'XXXXX'

def getOTP(sec_str):
    return pyotp.TOTP(sec_str).now()


def refreshOTP():
    textotp.delete(0.0, tk.END)
    textotp.insert(tk.INSERT, r'堡垒机OTP  ' + getOTP(sec_str))
    textotp.update()
    windows.after(500, refreshOTP)


windows = tk.Tk()
windows.geometry('200x70')
textotp = tk.Text(windows, width=200, height=100)
textotp.configure(font=("Microsoft YaHei", 15))
textotp.pack()
windows.after(500, refreshOTP)
windows.mainloop()
