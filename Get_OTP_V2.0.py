# -*- coding: utf-8 -*-
import tkinter as tk
import pyotp

sec_str = 'XXXX'

def getOTP(sec_str):
    return pyotp.TOTP(sec_str).now()

def refreshOTP():
    textotp.configure(text=r'堡垒机    ' + getOTP(sec_str), font=("Microsoft YaHei", 16))
    windows.after(500, refreshOTP)

windows = tk.Tk()
windows.title('OTP')
windows.geometry('200x50')
textotp = tk.Label(windows, text=r'堡垒机    ' + getOTP(sec_str), font=("Microsoft YaHei", 16))
textotp.pack()
windows.after(500, refreshOTP)
windows.mainloop()