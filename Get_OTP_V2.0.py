# -*- coding: utf-8 -*-
import tkinter as tk
import hmac, base64, struct, hashlib, time

# 堡垒机和vpn密钥串（时间步长为30和120的)
jump_str = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
vpn_str = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

# 根据VPN的secret，生成固定key
def hotp(counter, secret):
    basedSecret = base64.b32decode(secret)
    structSecret = struct.pack(">Q", counter)
    hmacSecret = hmac.new(basedSecret, structSecret, hashlib.sha1).digest()
    ordSecret = hmacSecret[19] & 15
    tokenSecret = (struct.unpack(">I", hmacSecret[ordSecret:ordSecret+4])[0] & 0x7fffffff) % 1000000
    return tokenSecret

# 根据VPN的secret，生成时间步长为timeset的key
def totp(secret, timeset):
    counter = int(time.time()) // timeset
    return str(hotp(counter, secret))

# 每隔500毫秒，刷新key
def refreshOTP():
    textotp.configure(text=r'堡垒机    ' + totp(jump_str, 30) + '\nVPN       ' + totp(vpn_str, 120), font=("Microsoft YaHei", 16))
    windows.after(500, refreshOTP)

# 设置tk窗口参数
windows = tk.Tk()
windows.title('OTP')
windows.geometry('200x50')
textotp = tk.Label(windows, text=r'堡垒机    ' + totp(jump_str, 30) + '\nVPN       ' + totp(vpn_str, 120), font=("Microsoft YaHei", 16))
textotp.pack()
windows.after(500, refreshOTP)
windows.mainloop()