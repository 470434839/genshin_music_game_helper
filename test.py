from ctypes import *
from pykeyboard import *
import time
dict ={}
dict["w"]=(993,765)
dict["a"] = (890,862)
dict["s"] = (992,962)
dict["d"] = (1091,863)
dict["i"] = (2445,765)
dict["j"] = (2352,862)
dict["k"] = (2447,962)
dict["l"] = (2544,864)
kb=PyKeyboard()
user= windll.LoadLibrary("c:\\windows\\system32\\user32.dll")   # 旧版windows系统如果找不到文件请将路径中的windows替换成winnt
h = user.GetDC(0)
gdi= windll.LoadLibrary("c:\\windows\\system32\\gdi32.dll") # 旧版windows系统如果找不到文件请将路径中的windows替换成winnt
front ={}
for k in dict.keys():
    front[k]=0
while True:
    time.sleep(0.01)
    for k,v in dict.items():
        rgb = gdi.GetPixel(h, v[0], v[1])
        if front[k] > 14000000 and rgb>5800000 and rgb< 9500000:
            print(k,front[k],rgb)
            kb.tap_key(k)
        front[k]=rgb
